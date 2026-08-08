# P1B RB-INT — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/arxiv/paper1b_mcmc_companion.pdf` md5=1cb9ff66 pages=22
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7679 chars)
**Wall time**: 377.4s

---

Referee report (PRD methodology review)

Overall assessment
The manuscript presents three technical-verification exercises that are explicitly framed as compatibility checks rather than model-evidence results: (i) a stock-CAMB ΛCDM+ΔNeff MCMC proxy; (ii) a NaMaster pseudo-Cl pipeline sanity check on synthetic CMB polarization skies; and (iii) a spectator-ALP consistency check against a Gaussian summary likelihood for cosmic birefringence. The authors include substantial caveats distinguishing internal pipeline SNR from sky-measurement significance and clearly state where their chains are overlap-uncorrected or where they mix Planck release pairings.

The submission contains a large amount of process-level detail (file paths, seeds, pod identifiers) that is unusual for PRD and belongs in a code repository or Supplement. Two issues are methodologically central and must be fixed before publication: (1) the birefringence estimator is explicitly unweighted (no inverse-variance/covariance weighting), yet the observed bias is repeatedly labeled a “NaMaster pipeline bias,” which generalizes beyond the actual cause (estimator choice plus template mismatch); and (2) core reproducibility artifacts are “pending DOI,” and the main text includes live commit hashes and warning notes that are not appropriate for the archival record.

Findings

ESSENTIAL

P1B-E1
- Location: Sec. IV, p. 10, Eq. (1) and surrounding text; Fig. 3 caption, p. 9; Sec. IV “Robustness battery,” p. 11
- Problem: The birefringence estimator is an unweighted χ^2 template fit (no σ_b^2 divisor; no bandpower covariance), yet the manuscript repeatedly promotes the observed under-recovery as a general “NaMaster pipeline bias (deconvolution-algebra bias).” The robustness study itself shows the dominant contribution to the ~12% multiplicative bias is the equal weighting of noise-dominated high-ℓ bins, and that inverse-variance weighting removes ~80% of the bias (β̂ = 0.264°, bias −0.006°). Labeling this as an intrinsic pseudo-Cl/MASTER “pipeline bias” is misleading and overgeneralized.
- Required fix:
  1) Either adopt the inverse-variance–weighted (or full-covariance–weighted) estimator as the primary result and demote the unweighted numbers to a historical-control appendix, or
  2) If the unweighted fit is retained as the baseline, revise all instances of “NaMaster pipeline bias” to “unweighted-estimator bias (plus BB-template mismatch),” and move the 0.040° “bias floor” out of headlines/captions; state plainly that the bias is not intrinsic to NaMaster/MASTER deconvolution but to the chosen unweighted estimator. In either path, report the weighted-estimator recovery (point estimate and uncertainty) prominently and quantify residual bias under the statistically appropriate weighting.
  3) Provide an explicit reference (or short derivation) for the weighted-likelihood estimator under Gaussian bandpower covariance, and state whether bin–bin covariances are neglected or included in practice.

P1B-E2
- Location: Data and Code Availability (p. 18) and Appendix A (pp. 18–20)
- Problem: The paper relies on external artifacts with “DOI assignment is pending,” points to moving targets (HuggingFace datasets unnamed by DOI), and includes internal commit identifiers (e.g., b22f8cc9), “CHANGELOG.md,” a “parameter_summary_CORRECTED.json” vs. “legacy parameter_summary.json” warning, and other process notes. PRD requires a citable, immutable archival record. The current state is not stable for publication.
- Required fix:
  - Deposit all committed artifacts that substantiate Tables I–III, Fig. 1–4, and the ALP posteriors (chains and code) to a permanent repository with DOIs (e.g., Zenodo/Long-term archive). Replace “pending” language by fixed DOIs. Remove internal commit/CHANGELOG warnings from the paper proper; include a concise, stable “Data Availability” paragraph with final DOIs and exact version tags. The “column-permutation warning” and similar repository process notes should be removed from the manuscript and retained in the repository only.

MAJOR

P1B-M1
- Location: Throughout Sec. IV (pp. 9–12), Appendix A (pp. 18–20)
- Problem: Excessive operational detail (file paths, driver script names, pod run directories, seeds) in the main text dilutes the scientific narrative and is not PRD style. It also risks breaking the archival record if directories change.
- Required fix: Move all file-path-level detail (script names, repository subpaths, pod job folders) to a short “Reproduction guide” in Supplementary Material or keep it solely within the public repository. Retain in the paper only the essential methodological description (masks, Nside, ℓmax, binning, estimator specification, noise model) and final numerical results with uncertainties.

P1B-M2
- Location: Fig. 3 caption (p. 9); Sec. IV, “Production 500-realization run,” “Sky-fraction sweep,” and “Robustness battery” (pp. 10–11)
- Problem: The manuscript “carries forward” a 0.040° “NaMaster pipeline bias” as a “systematic floor,” but subsequently demonstrates that inverse-variance weighting eliminates ~80% of the bias. Presenting the 0.040° as a floor is inconsistent with the robustness finding and risks misinterpretation by readers.
- Required fix: Replace “observed NaMaster pipeline bias”/“systematic floor” phrasing with a precise, conditional statement: “Under the unweighted estimator and EE-only template the bias is −0.032° to −0.040°; under inverse-variance weighting the bias is −0.006°.” Do not frame 0.040° as a pipeline/systematic “floor.”

P1B-M3
- Location: Sec. V A, B; Table III (p. 13); “Release-pairing note” (p. 12)
- Problem: Mixed Planck pairings (PR4/NPIPE high-ℓ with 2018 low-ℓ and lensing) are used in headline frozen chains. Although an auxiliary rerun with PR4-consistent low-ℓ/lensing shows a 0.04σ agreement in ΔNeff, the paper treats this as a “known limitation” but still relies on the mixed pairing for headline results.
- Required fix: Either (a) rerun the headline ΛCDM+ΔNeff chains with a fully consistent PR4 pairing and move the mixed-pairing results to a diagnostic appendix, or (b) add a quantitative robustness table for all headline parameters (ΔNeff, H0, σ8, S8, Ωm) comparing mixed vs. consistent PR4 pairings with uncertainties, so readers can assess any residual bias beyond ΔNeff.

P1B-M4
- Location: Table II caption and Sec. III “Caveats (e)” (pp. 6–7, 12)
- Problem: While the text warns that the DES-Y5×Pantheon+ SN product likelihood double-counts ~20% shared events and narrows uncertainties, Table II still presents w0/wa uncertainties in a standard table. Casual readers may miss the caveat despite the footnote.
- Required fix: Place a boldface warning in the Table II caption header (e.g., “Overlap-uncorrected SN combination; quoted ± widths are not valid uncertainties for model selection or σ-distances”) and add a watermark or superscript “overlap-uncorrected” marker next to the four dark-energy rows.

MINOR

P1B-m1
- Location: Sec. IV, “Simulated skies,” (p. 9–10)
- Problem: The template used in the canonical fit omits the −CBB term, although later you note the general expression is ½ sin(4β)(CEE − CBB). The text mentions a “−CBB template mismatch” as a bias source without first writing the full expression.
- Required fix: Write the general small-rotation prediction explicitly (C′EB ≈ ½ sin(4β)(CEE − CBB)) before stating that the canonical fit drops CBB, and then quantify the shift when including CBB in the template (you have the number; surface it clearly once).

P1B-m2
- Location: Sec. VI, Eq. (4) (p. 14)
- Problem: Convention note is correct, but the text buries the logic. Some readers will look for a quick check of the β–gaγ relation.
- Required fix: Add one sentence: “Under L ⊃ −(gaγ/4)φ Fμν F̃μν, uniform rotation gives β = (gaγ/2)Δφ, hence β = [αEM/(4π)] Caγ Δφ/fa.”

P1B-m3
- Location: Sec. III “MB–H0 joint-posterior offset check,” (p. 7–8)
- Problem: The 3.2σ “offset” is normalized by σMB only, which you acknowledge is not a properly conditioned statistic.
- Required fix: Add the conditional counterpart using the covariance along the SN degeneracy direction (or remove the σ language entirely and give only the 0.156 mag offset with a clear statement that significance is not defined in this projection).

P1B-m4
- Location: Data and Code Availability (p. 18)
- Problem: The acknowledgments mention use of an AI assistant. PRD policy generally requires that all analyses and text are author-controlled; the language is acceptable but should be streamlined.
- Required fix: Keep a short statement that all analyses and conclusions are the author’s and that no AI-generated text is included in the scientific content; or remove the tool mention if it contributed only to non-scientific drafting.

NITS

P1B-n1
- Location: Sec. IV, Fig. 3 caption (p. 9)
- Problem: “template-fit SNR” is used; although you define it in a footnote, the label “SNR” risks confusion with sky-measurement significance.
- Required fix: Rename to “template-matched SNR (MC injection)” in the caption wherever the number appears.

P1B-n2
- Location: Multiple places (pp. 10–12)
- Problem: Binning to ℓ = 1536 with Nside = 512 (ℓmax=1024) is fine, but state once in the main text (not just robustness notes) that bins >1024 are β-independent and enter χ^2 as constants.
- Required fix: Add a single clarifying sentence in Sec. IV next to Eq. (1).

P1B-n3
- Location: General
- Problem: Units are consistently given, but occasionally crowded (e.g., “km s−1 Mpc−1” without thin spaces).
- Required fix: Apply consistent formatting with thin spaces in units.

Dimensional and arithmetic checks (selected)

- H0 tension: (73.04−67.68)/sqrt(1.04^2+1.06^2)=3.61σ. Matches “~3.6σ”.
- S8 two-Gaussian difference: (0.827−0.776)/sqrt(0.010^2+0.017^2)=2.59σ. Matches text “2.6σ”.
- CPL pivot: ap=0.790, zp=1/ap−1=0.27; σwpivot computed from reported covariances gives 0.019. Correct.
- H(z=0.5) fractional shift ≈ +1.7% from reported (w0,wa,Ωm): matches recomputation.
- β formula: β = [α/(4π)] Caγ Δφ/fa = 0.28° for Caγ=8, Δφ/fa=1.06. Correct.
- Caγ(Δφ/fa) from βobs: 0.342° = 5.97×10−3 rad; divide by 5.81×10−4 gives 10.27. Correct.
- ρcrit,0 ≈ 3H0^2 MPl^2 ≈ 3.7×10−11 eV^4: consistent.

Scope/claims

- Abstract-last drift: The abstract’s three quantitative bullets (ΔNeff posteriors; NaMaster bias magnitudes; ALP m/H0 shift and spectator caveat) are traceable in the body and carry appropriate caveats that they are compatibility checks, not evidence. Good.
- Sigma-procedure juxtaposition: Where different null procedures are shown side-by-side (e.g., “2.7–2.9σ” sky detection vs “template SNR”), the text does flag non-comparability. Keep this everywhere any σ appears; after edits to Fig. 3 caption per P1B-n1, ensure the non-comparability warning remains local.

Length
- The manuscript is long for a “technical companion” (22 pages). After moving process-level detail to Supplement/repository and condensing footnote 1 (burn-in/sample-count reconciliation) into a short methods line, the paper could be reduced to ~15–16 pages without loss.

## Summary recommendation
MAJOR REVISIONS

The core numerical results appear arithmetically consistent and appropriately caveated, but two methodological issues must be corrected before publication: (1) the unweighted EB template-fit should not be presented as a general “NaMaster pipeline bias”; either adopt the statistically appropriate weighted estimator as primary or rephrase and demote the unweighted result, and (2) finalize archival availability with fixed DOIs and remove repository-process notes from the paper. Additional presentation fixes (mixed Planck pairing robustness, stronger table-level caveats for overlap-uncorrected SN, and moving file-path details to Supplement) are required to meet PRD standards.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eyes pass)

ESSENTIAL

P1B-E3
- Location: Sec. IV, p. 10, Eq. (1) and surrounding text; Fig. 3 caption; “Production 500-realization run”
- Problem: The objective minimized is labeled χ^2(β) but is not a statistical χ^2 (no variance or covariance weighting; dimensions are Cℓ^2). Calling it “χ^2” strongly suggests a likelihood with known per-bin variances and dof, which is not what is minimized here.
- Required fix: Rename the objective to “unweighted least-squares objective” or similar throughout; if a χ^2 is intended, supply the full definition with the diagonal (or full) covariance and use it in the baseline. Report both unweighted and variance-weighted results side-by-side, with residual bias for each.

MAJOR

P1B-M5
- Location: Sec. IV, estimator description; “Robustness battery” (pp. 10–11)
- Problem: The treatment appears to neglect inter-bin covariance entirely (no MASTER-coupling–induced bandpower covariance is included), even in the “inverse-variance” variant. This can bias both point estimates and reported uncertainties for pseudo-Cℓ estimators on a cut sky.
- Required fix: Quantify the impact of including a realistic bandpower covariance (from MC) in a generalized least squares fit (full-covariance weighting) on the recovered β and its uncertainty, and report the residual bias. If you choose to retain diagonal-only weighting, justify it with a quantitative comparison (e.g., show that off-diagonal terms change β̂ by < X×10−3 deg and the error bar by < Y%).

P1B-M6
- Location: Sec. IV, “Simulated skies,” “Robustness battery”
- Problem: The EB template uses an external semi-analytic CEE, and you attribute part of the bias to a “−CBB template mismatch.” A straightforward control—building a self-calibrated template from the realization’s own decoupled CEE (and optional CBB) under the identical mask—was not presented. This test directly isolates template-mismatch systematics from the pseudo-Cℓ deconvolution.
- Required fix: Add a control where the template uses the realization’s decoupled CEE (and optionally CBB) and report β̂ and bias. If this removes most of the residual, state that the remaining bias is estimator-weighting–dominated, not NaMaster/MASTER deconvolution.

P1B-M7
- Location: Sec. VI, “ALP dark-energy fraction Ωa: definition and computation” (pp. 16–17)
- Problem: Ωa is computed with the potential-dominated approximation at zosc and an (1+zosc)−3 dilution, and you state it was “verified against full EOM integration,” but no quantitative validation (scatter, max fractional error) is shown. Since Ωa is used to define the “spectator-safe” subsets, the approximation accuracy matters.
- Required fix: Provide a quantitative validation figure/table comparing Ωa from the approximation vs. full EOM for a representative posterior sample (e.g., 200 points spanning the support), quoting mean and max fractional deviation, and confirm that the Ωa<0.01 classification is unaffected at the quoted precision.

P1B-M8
- Location: Table III; Sec. V C; Conclusions p. 17–18
- Problem: The iter2 w0wa chain uses planck 2018 lensing.native, not the .clik variant used elsewhere, and no robustness test is provided for this choice. Given the sensitivity of w0–wa posteriors to lensing likelihood details, this should be checked.
- Required fix: Rerun the iter2 stack with the alternative lensing likelihood (or the PR4-consistent pair used in your c15 test) and provide a small robustness table for (w0, wa, wpivot, H0, S8), with shifts and uncertainties.

MINOR

P1B-m5
- Location: Sec. IV, Eq. (1) and surrounding text; Fig. axes labeling
- Problem: β appears in degrees in figures but must be in radians inside sin/cos. You note conversion “when evaluating sin and cos” once, but this is easy to miss and not stated near Eq. (1).
- Required fix: Add a one-line explicit note at Eq. (1): “β is scanned in degrees for convenience; all trigonometric functions are evaluated in radians.” Ensure all figure axes explicitly state “β [deg].”

P1B-m6
- Location: Sec. V A (Datasets); Table I notes
- Problem: The “full-tension” chain includes a DES-Y3 S8 Gaussian prior alongside Planck CMB+lensing. While commonly treated as independent, there is potential shared-sky cosmic-variance correlation between Planck lensing and DES-Y3 shear that is neglected.
- Required fix: Add a one-sentence disclaimer that the DES-Y3 Gaussian prior is treated as independent of Planck, with expected impact small at current errors, or cite a study justifying the independence at the current precision.

P1B-m7
- Location: Sec. III, “MB–H0 joint-posterior offset check” (pp. 7–8)
- Problem: Small numerical mismatch from rounding: the constant MB − 5 log10 h recomputation differs by ~0.003 mag from your printed values. Not scientifically important, but distracting in a section focused on arithmetic consistency.
- Required fix: Recompute with consistent rounding or report one additional decimal to remove the apparent discrepancy.

NITS

P1B-n4
- Location: Sec. IV, SNR discussion (footnote 4), Fig. 3 caption
- Problem: Two different weightings coexist: the baseline β estimator is unweighted, while SNRtmpl uses per-bin σb from MC. This is correct for an MC “template-matched SNR,” but readers may conflate it with the estimator weighting.
- Required fix: Add a short parenthetical in the caption: “Estimator is unweighted; SNR uses per-bin MC variances and is not the sky-measurement significance.”

ARITHMETIC/CONSISTENCY SPOT CHECKS (new items only)
- No new arithmetic inconsistencies were found beyond the rounding note in P1B-m7. Recomputed values for all σ, ratios, and combined constraints checked in this pass (S8 combination, LiteBIRD σ to significance, CaγΔφ/fa from βobs, wpivot and zp, fsky scaling of σβ) match the manuscript within rounding.

FIGURE-CAPTION VS BODY
- No new mismatches found: Fig. 3 panel (b) σβ values (0.029° at fsky=0.85; 0.033° at 0.65) and the absence of an error bar at fsky=0.32 (mean only) are consistent with the body text; Fig. 4 priors and medians match Sec. VI text.

EQUATION DIMENSIONAL CONSISTENCY
- All checked equations (EOM, birefringence β relation, Ωa scaling) are dimensionally consistent under natural units; no new issues found.

INTERNAL CROSS-REFERENCES
- No new broken or incorrect cross-references detected in this pass.

NULL PROCEDURE COMPARABILITY
- No new juxtapositions lacking caveats were found beyond those already flagged in the initial review; the manuscript consistently distinguishes MC template SNR from sky-measurement significance.

ABSTRACT FAITHFULNESS
- One phrasing to revisit after addressing P1B-M2 from the initial review: the abstract’s “observed pipeline bias floor” wording should be aligned with the weighted-estimator result (−0.006°) and relabeled as “unweighted-estimator bias” per P1B-E1/P1B-M2.

UNSUPPORTED NOVELTY CLAIMS
- None newly detected.

APPENDIX VS MAIN-TEXT MISMATCH
- None newly detected. Appendixed priors/chains match main-text descriptions.

STALE NUMBERS
- None newly detected. Where two different medians appear for m/H0 (36 vs. 40.5), they refer to different subsets (fixed Caγ vs. Ωa≤0.01), as stated.

Summary
The most important additional issues are: (i) relabel the EB objective to avoid implying a true χ^2 and add a covariance-weighted result; (ii) quantify the impact of including full bandpower covariance; (iii) add a self-calibrated EE-template control to isolate template-mismatch effects; (iv) validate the Ωa approximation against full EOM quantitatively; and (v) provide a lensing-likelihood robustness check for the iter2 chain. All other additions are clarifications and minor presentation fixes.