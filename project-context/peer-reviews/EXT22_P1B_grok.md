# EXT22 P1B grok — chat: https://grok.com/c/5149a033-589a-4e42-8131-a4f07f77d926

Referee Report: MNRAS-style (for MNRAS / PRD / JCAP)
Paper: Technical Verification Companion to the ECH Spin-Torsion Program: ΛCDM+∆Neff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model (Houston Golden, June 20 2026; revised companion to Paper I(a))

Recommendation: MINOR REVISIONS

The manuscript is a carefully scoped technical verification companion. It performs three well-defined compatibility/consistency analyses, repeatedly and explicitly flags what the results do not demonstrate (no evidence for/against bounce cosmology, no direct test of the spin-torsion Boltzmann module, pipeline validation figures are not sky-detection significances, ALP birefringence is not an ECH-specific prediction, model-preference statistics deferred to nested sampling), and supplies unusually complete reproducibility materials (version-stamped GitHub commit, Cobaya YAMLs, driver scripts, frozen chains, independent re-run cross-check, robustness battery). No load-bearing scientific claim is unsupported, no critical control is missing, and non-reproducibility is not an issue. The work meets the standard for a companion verification paper. Minor revisions are requested for presentation polish, a small number of clarifications that would further reduce any residual risk of over-reading, and minor typographic/notation items visible in the extracted PDF.

1. BLOCKERS
None.
The paper contains no unsupported load-bearing claims, missing critical controls, or reproducibility gaps that would require substantial scientific rework. All headline results are framed as compatibility checks with explicit scope limitations stated in the abstract, Sec. I (Scope of this paper; What is NOT in this paper), Sec. III (Scope statement), Sec. IV (Scope note), and Sec. VI (spectator-status caveat and "not a distinctive ECH prediction"). The MCMC convergence diagnostics, pipeline bias attribution, and ALP fine-tuning disclosures are transparent and conservative.

2. MAJORS (none that rise to the threshold of requiring new runs or structural changes; the items below are strong recommendations that can be addressed with text/figure edits)

Sec. I (Introduction) and abstract: Add a compact 3-bullet "Scope summary" box or short paragraph immediately after the three enumerated analyses. Example: "(1) tests whether data prefer an extra radiation-like degree of freedom in stock CAMB (not a torsion-modified module); (2) validates algebraic pseudo-Cℓ deconvolution on synthetic foreground-free skies (not a competitive sky measurement); (3) checks consistency of published β with a spectator ALP in standard GR (not an ECH-derived prediction; requires ∼25× misalignment tuning for spectator status)." This would make the already-excellent scoping impossible to misread on a quick pass.

Sec. VI (ALP consistency check) and Table IV: The spectator-status disclosure (θi ∼ 0.1, ∼25× tuning relative to natural midpoint; Caγ median ∼20–21 outside minimal KSVZ/DFSZ benchmarks) is already present and load-bearing. Elevate the quantitative tuning statement from fn. 6 / main-text note into a short dedicated paragraph or a highlighted sentence in the abstract's final clause and in the Sec. VI headline. This protects readers from inadvertently treating the consistency check as "natural" accommodation.

Fig. 3 and Sec. IV (pipeline bias): The caption and surrounding text correctly distinguish MC-recovery bias from sky systematics. Add one explicit sentence: "The quoted 0.040° worst-case bias is therefore a deconvolution-algebra floor on foreground-free synthetic skies only and is not propagated as a systematic uncertainty on the published Planck/ACT DR6 sky measurements." (Already implied; making it impossible to overlook removes any residual risk of conflation.)

3. MINORS (presentation, notation, and polish items; none affect scientific conclusions)

Abstract, line ~"the worst-case bias across injections, −0.040° at βinj = 0.342°": clarify that this is the MC mean bias (with SE of the mean) rather than a per-realization scatter; the text already does this later but the abstract sentence is slightly compressed.

Sec. III, burn-in reconciliation footnote and Table I caption: the 30 % vs. GetDist-reported 20 % discussion is thorough; a one-sentence "We adopt the more conservative 30 % cut throughout for uniformity across both frozen chains" would help readers who skip the long footnote.

Sec. IV, Eq. (1): the χ² form is correct for the unweighted estimator chosen for comparability with published NaMaster drivers. Add a parenthetical "(no σb² weighting; see robustness battery for inverse-variance variant)" so the equation stands alone.

Sec. VI, LiteBIRD forecast paragraph: the text already notes that 9σ is vs. null and does not separate the spectator-ALP fiducial from the current central value. Make this explicit in one additional clause: "LiteBIRD alone will not discriminate the spectator-ALP benchmark (0.27°) from the present Eskilt–Komatsu central value at high significance."

Minor typographic/notation items visible in the provided extraction:
– "in-tex v1B.0.76" → "in-text".
– Occasional missing thin spaces or minor LaTeX rendering artifacts in subscripts (e.g., ∆Neff, β̂) that do not affect readability but should be checked in the final compile.
– Reference list: ensure all "arXiv 25xx/26xx.xxxxx" placeholders are updated or clearly marked as "submitted / posted concurrently" at submission time (deliberate per calibration note).
– Table IV caption: "post. mass" column header could read "Posterior mass fraction (MC weight)" for immediate clarity.
Fig. 2 / Fig. 3 captions: add a one-line note that error bars in panel (b) of Fig. 3 are per-realization scatter (where measured) vs. SE of the mean, consistent with the text.
Sec. V C (w0wa cross-check): the SN-overlap caveat (e) is already stated; a parenthetical cross-reference "(see also Vincenzi et al. 2026 comparison analysis [16])" in the paragraph would help readers locate the quantitative overlap discussion.

All of the above are addressable with text edits or minor figure-caption expansions; none require new calculations, chains, or re-analysis.

4. Strengths (at least three; the manuscript is strong in several dimensions)

Exceptional scoping discipline and scientific honesty. The paper repeatedly and at multiple levels (abstract, Sec. I bullets, dedicated "Scope statement", "What is NOT in this paper", Sec. IV scope note, Sec. VI spectator caveat, Sec. VII summary) demarcates what each analysis is (compatibility / pipeline validation / consistency check) from what it is not (evidence for bounce, direct test of ECH Boltzmann sector, competitive sky measurement, distinctive ECH prediction, model-selection result). This level of explicit framing is rare and exemplary for a verification companion.

High-standard reproducibility infrastructure. Version-stamped GitHub commit (b22f8cc9 corresponding to v1B.0.76), four verbatim Cobaya YAML configurations, NaMaster driver scripts, 500-MC artifacts, independent re-run cross-validation (0.04σ agreement on ∆Neff under likelihood-pairing swap), robustness battery isolating bias sources, burn-in reconciliation documentation, and planned Hugging Face dataset deposition with pending DOIs. The MCMC convergence metrics (R̂−1 < 0.003, ESS values, worst-row reporting) are reported transparently. This meets or exceeds modern community expectations for cosmological MCMC + pipeline papers.

Careful statistical and methodological hygiene. Distinction between template-fit SNR on injected MC signals vs. published sky-detection significance; explicit carrying-forward of worst-case pipeline bias (0.040°) as a synthetic-sky floor only; proper one-sided 95 % upper limits on ∆Neff after renormalisation on the physical half-line; posterior-tail extrapolation distances clearly labelled "not a Bayes factor or detection significance"; ALP fine-tuning (∼25× misalignment for spectator status; coupling outside minimal benchmarks) quantified and not minimised. The robustness battery (apodization scale, purification, weighting scheme, BB template shape, sky fraction) that pins the dominant bias contributions is particularly commendable.

Balanced cross-checks and external consistency. Independent literature comparison (Liu et al. EC-torsion constraint with torsion parameter consistent with zero and H0/S8 agreement at <1.3σ) and internal consistency (re-run, sign-symmetric negative-β injection, sky-fraction sweep showing multiplicative bias is sky-fraction independent) strengthen confidence without over-claiming.

Overall assessment
This is a solid, conservative, and unusually transparent verification companion. With the minor presentation and emphasis clarifications listed above, the manuscript will be ready for publication and will serve as a useful technical anchor for the broader ECH spin-torsion program. I recommend MINOR REVISIONS.

Date of report: 26 June 2026
Referee identity: External referee (MNRAS / PRD / JCAP pool)
The referee has no conflicts and has evaluated the work solely on the scientific and reproducibility content supplied in the PDF and its referenced artifacts.
