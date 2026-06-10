# P4 R25conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/chirality_catalog_paper_v169.pdf` md5=ad396d7d pages=20
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (8737 chars)
**Wall time**: 432.3s

---

Referee report on P4 (PRD Methods), 20 pages

Scope and contribution:
The paper presents a very large chirality-labeled galaxy catalog (8.47M DESI Legacy DR8 images; 3.20M spirals) and a cosmological “no dipole” result based primarily on a real-space monopole+dipole fit using an explicitly pre-declared estimator hierarchy. The analysis emphasizes flip-equivariant test-time averaging (TTA), bias audits, and extensive null/permutation, injection–recovery, and MASTER pseudo-Cℓ diagnostics. The work is ambitious and methodologically oriented.

Overall assessment (methodology rigor):
- The main numerical claims in the abstract and conclusions are, in general, traceable and (where recomputable from reported numbers) internally consistent.
- The authors do keep “σ” values from different null procedures mostly segregated and explicitly non-comparable; good practice.
- However, there are several essential issues before this is suitable for PRD:
  • The manuscript contains extensive version-history language, withdrawn-result narrative, audit-path file references, and internal repository bookkeeping throughout the body text. PRD does not accept this in the main text; it must be removed or placed in a succinct erratum/provenance note and/or Supplemental Material.
  • Amplitude units and the symbol “A” are used in two different conventions (Ap units vs. fCW units) in multiple places; while the paper often states the mapping Ap = 2(fCW − 1/2), the usage remains inconsistent and occasionally ambiguous (e.g., “0.57% dipole” without stating the unit convention). This must be fully harmonized.
  • The “95% upper limit” defined as the 95th percentile of the null (with no signal model) is not a conventional confidence interval on the physical amplitude. If kept, it must be labeled as an estimator-level rank bound; alternatively, provide a proper confidence interval on the dipole amplitude using a likelihood or injection-calibrated frequentist construction.

Below I itemize findings with required fixes.

ESSENTIAL

P4-E1
- Location: Throughout; concrete instances on pp. 3, 6–9, 13–15, 17–18 (e.g., “Artifact: outputs/dipole/catalog c summary.json.”; “earlier version of this paper reported … withdrawn …”; “a misquote … traced to the withdrawn synthetic-catalog artifact”).
- Problem: Version-history/audit-log prose and internal file-path artifacts are embedded in the main text. PRD does not accept run-log style narrative in the article body.
- Required fix: Remove all internal file paths, run logs, commit hashes, “earlier version” verbiage, and withdrawn-result narrative from the main text. If provenance disclosure is essential, move a concise, single-paragraph note to an Appendix or Supplemental Material, and cite a stable Zenodo DOI with the full reproducibility bundle.

P4-E2
- Location: Abstract (p. 1), Sec. IV C (pp. 6–8), Sec. VI A (p. 11–12), Appendix D (pp. 16–17).
- Problem: Inconsistent and sometimes ambiguous amplitude units and symbol A (Ap vs fCW “percent”). Examples:
  • Abstract: “A95 between 1.0% and 1.5% (A50 ≈ 0.75%)” – these are in fCW units, but elsewhere A denotes Ap units (e.g., AUL95 = 6.8 × 10−3 in Ap units).
  • Sec. IV C: “0.57% dipole at z ≈ 4.2–4.4” – unit not specified (Ap or fCW?).
  • Appendix D/Table IX: Aref = 0.034 “in Ap units” corresponds to 1.7% in fCW units; good here, but this mapping must be uniform everywhere.
- Required fix: Introduce a single amplitude symbol convention section early (Sec. III A or IV C). Provide one conversion table or a concise boxed note:
  • Define explicitly: A_fCW (full-amplitude in fCW units) and A_Ap (Ap units) with A_Ap = 2 × A_fCW.
  • Label every quoted amplitude with the unit convention in text, tables, and figure captions.
  • Replace all ambiguous occurrences (“0.57% dipole”, “A = 0.75%”) with explicit unit-labeled amplitudes.

P4-E3
- Location: Sec. IV C (p. 7), Abstract (p. 1).
- Problem: “AUL95 = 6.8 × 10−3” is defined as the 95th percentile of the null amplitude distribution (rank construction), not a standard 95% upper confidence bound on the physical dipole amplitude. Calling it “upper limit” risks misinterpretation.
- Required fix: Either (a) relabel this quantity as an “estimator-level 95th-percentile rank bound under the null (no-signal) distribution,” and do not call it an “upper limit,” or (b) provide a conventional CI on the dipole amplitude (e.g., via maximum-likelihood with permutation-calibrated sampling distribution or via injection-calibrated frequentist coverage). State clearly which estimator and null this CI pertains to.

P4-E4
- Location: Abstract (p. 1), Table I (p. 4), Sec. IV C–D (pp. 6–11).
- Problem: Multiple σ values from different estimators and nulls are unavoidably shown side-by-side. While the manuscript often cautions that these are not directly comparable, some presentations (e.g., Abstract listing +3.64σ and +7.28σ) lack immediate and explicit “not directly comparable” caveat at that juxtaposition.
- Required fix: At every place where two or more σ values from different estimators/nulls are juxtaposed (Abstract; Conclusions §VII), add a parenthetical “(different estimators/nulls; not directly comparable).” Table I already has a good column noting “Null”; ensure all text mentions mirror that clarity.

P4-E5
- Location: Data availability (p. 18).
- Problem: No persistent DOI for the exact released catalog/code version; links include spaced/broken URLs (likely PDF line breaks).
- Required fix: Mint stable DOIs (e.g., Zenodo) for the exact versions of: catalog (all tiers), model weights, and code that reproduce the submitted results; give clean, copyable URLs/DOIs in the manuscript (PRD style). If a DOI cannot be minted pre-acceptance, state that it will be minted and provided in the revised manuscript and provide a temporary tag; remove line-break/space artifacts in URLs.

MAJOR

P4-M1
- Location: Sec. IV C (p. 8; “dropping the confidence threshold entirely … yields a 0.57% dipole at z ≈ 4.2–4.4”).
- Problem: The amplitude unit for “0.57% dipole” is not specified; also, the null type underpinning the reported z-range is not explicitly repeated in this sentence (though null types are discussed elsewhere).
- Required fix: State explicitly “0.57% in fCW (A_Ap ≈ 1.14%)” or equivalent, and specify the null used (pixel-permutation or label-shuffle) right there.

P4-M2
- Location: Multiple (e.g., Fig. 8 caption p. 9; Appendix D intro p. 16).
- Problem: Use of low NMC (e.g., 200 permutations) for some pseudo-Cℓ diagnostics while quoting σ to two decimals and assigning interpretation weight. For heavy-tailed permutation distributions, small NMC inflates uncertainty on p and σ.
- Required fix: Either increase NMC (≥2000) for all quoted per-ℓ diagnostic σ values that are later used as formal discriminants (e.g., the +3.63, +4.73 findings), or explicitly caveat the sampling noise on σ (and, if kept at 200, reduce precision to one significant digit).

P4-M3
- Location: Sec. VII “Conclusions” (pp. 13–14; item a).
- Problem: The harmonic-channel completeness claim “injected Ap = 1.7% yields median recovered significance z ≈ 68–218” is striking and axis-dependent; no table/figure references are given beyond “artifact c9b.”
- Required fix: Include a concise, citable quantitative summary in the paper body or Supplemental (e.g., a small table or figure showing z vs. axis for 1.7% and 3.0%), with the null definition, mask, weight, and NMC stated. Remove the “artifact c9b” reference from main text.

P4-M4
- Location: Sec. III C (p. 4–5) and Appendix B (p. 15).
- Problem: The flip-equivariance/TTA protocol is clear, but the residual rotation non-equivariance discussion relies on small hold-outs. Given the centrality of equivariance to bias control, the rotational stability validation could be documented more compactly and precisely (e.g., population-level, not only argmax flip rate).
- Required fix: Add one quantitative summary statistic for D4 vs Z2 at catalog scale (e.g., distribution of ΔpCW over a larger random sample with confidence intervals), or explicitly state the size limits and that catalog-scale D4 was not computationally feasible.

P4-M5
- Location: Sec. VI A (pp. 11–12) and Abstract/Conclusions (pp. 1, 13).
- Problem: The “falsification criterion” (“≥5σ detection at A ≳ A95”) is not tied explicitly to a specific estimator and null procedure. As written, it is ambiguous.
- Required fix: Specify: “≥5σ with the real-space monopole+dipole estimator under the per-pixel label-shuffle null on the HC-broad (peq > 0.6) selection.” If you intend a different estimator (e.g., harmonic-channel), state so unambiguously.

P4-M6
- Location: Sec. IV B (p. 6).
- Problem: The generative test demonstrating a constant monopole does not bias the real-space dipole estimator is sound, but the text should emphasize more clearly that depth/morphology-modulated monopoles can bias harmonic-space diagnostics and potentially affect the real-space estimator if the modulation correlates with the footprint geometry (later discussed).
- Required fix: Add one clarifying sentence in Sec. IV B acknowledging that while a uniform monopole is absorbed, a depth/morphology-modulated monopole can leak into low-ℓ modes on a cut/weighted sky and motivate the subsequent diagnostics.

MINOR

P4-m1
- Location: Table II (p. 6).
- Problem: For Catalog C, dev = −9.47σ; recomputed using f = 0.497353 and σbin ≈ 0.000279 yields ≈ −9.49. OK within rounding, but the table mixes rounded and unrounded inputs.
- Required fix: State explicitly that Dev. is computed from unrounded fractions. Optionally add more digits to fCW to avoid round-off confusion.

P4-m2
- Location: Sec. A (Appendix A, pp. 13–14).
- Problem: Notational oddities “C 2 2◦” for apodization appear (spacing/format).
- Required fix: Standardize to “C2 apodization with 2° length” consistently.

P4-m3
- Location: Appendix B (p. 15), Table VII.
- Problem: T7 criterion description (“>30% at max p > 0.9”) is a heuristic; the earlier misprint note is again version-history flavor.
- Required fix: Remove the misprint history; keep only the implemented criterion.

P4-m4
- Location: Sec. V A (p. 11).
- Problem: “a ≳25× sample extension” computed as 3.2×10^6 / 1.27×10^5 ≈ 25.2 is fine, but “≳” is unnecessary.
- Required fix: Give the exact factor or round to “~25×” without the inequality.

P4-m5
- Location: Appendix E (p. 18).
- Problem: Footnote “3” references the “monopole-preserving” estimator, with a long explanatory note repeating earlier content.
- Required fix: Shorten and refer to the main definition once; move the rest to Supplemental.

NITS

P4-n1
- Location: Various captions (Figs. 4, 7).
- Problem: Some captions restate text at length.
- Required fix: Trim captions to figure-relevant content; put methodology details in the main text.

P4-n2
- Location: Bibliography.
- Problem: Minor style inconsistencies (e.g., arXiv IDs not consistently included; capitalization).
- Required fix: Bring references to PRD style uniformly (journal info, DOIs where appropriate).

Arithmetic/dimensional checks (spot-audit):
- Catalog C fCW = 1,592,107 / 3,201,160 = 0.497353; σbin ≈ 0.000279; dev ≈ −9.49. Matches claims within rounding.
- Catalog A fCW = 0.507879; σbin ≈ 0.000274; dev ≈ +28.7. OK.
- MASTER C1 apodized: z = (2.348e−5 − 1.71e−6) / 2.99e−6 ≈ 7.28; rank p = (5+1)/(10,000+1) ≈ 6.0e−4. OK.
- Monopole+mask leakage: (1.6961 − 1.6846)/0.0068 ≈ 1.69σ. OK.
- Injection mapping g = 2a − 1 = 0.398 for a = 0.6991; Atrue ≈ 0.75%/0.398 ≈ 1.88%. OK.
- Fisher floor σ(A) = √(3/N) for N = 3.20116e6 ≈ 9.68e−4 (0.097%); 3σ ≈ 0.29%. OK.
- WLS bootstrap exclusion: (0.00455 − 0.034)/0.00163 ≈ −18.1. OK.

Length:
The paper is long (20 pages) for the core findings given. Much of the length comes from internal audit narrative and artifact references. Recommended maximum: 12–14 pages main text, with technical diagnostics moved to a comprehensive Supplemental Material (with DOIs).

## Summary recommendation
MAJOR REVISIONS

Justification: The core methodological result (real-space dipole null with rigorously pre-declared estimator and robust null checks) is valuable and generally well-supported. However, the manuscript in its current form contains extensive version-history/audit-log text and internal file-path references inappropriate for a PRD article; amplitude-unit conventions are inconsistent and must be harmonized; the “upper limit” definition must be corrected or rephrased; and several presentation issues (explicit estimator/null for the falsification criterion, NMC sizes for quoted diagnostic σ values) need revision. Addressing the ESSENTIAL and MAJOR items above should bring the manuscript to PRD methodological standards.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eyes audit)

ESSENTIAL

P4-E6
- Location: Sec. IV C (p. 8), Table I (p. 4), Sec. IV A (p. 5–6).
- Problem: Inconsistent spiral counts for the “full, unthresholded” in-mask sample. Sec. IV C states “all 3,200,420 in-mask equivariant spirals,” whereas the catalog-wide spiral count is 3,201,160 and Table I uses Ncatalog spiral = 3,201,160 for the canonical mask. A 740-object discrepancy is unexplained.
- Required fix: Harmonize the counts and explicitly state why the in-mask spiral count differs (if it truly does) from 3,201,160 under the canonical Nspiral(p) ≥ 10 mask. If it is a stale number, correct it. If the real-space estimator uses a slightly different mask, say so and quantify the difference.

P4-E7
- Location: Sec. III A (p. 3–4), Sec. IV C (pp. 6–8), Table I (p. 4), captions (e.g., Fig. 8).
- Problem: Null-procedure nomenclature is inconsistent and potentially confusing. The text uses multiple labels for related but distinct nulls (“isotropic-bootstrap,” “pixel-permutation,” “per-galaxy label-shuffle,” “depth-stratified,” etc.) sometimes interchangeably, and not all σ/p values are immediately tied to one precise null name at their point of use.
- Required fix: Add a Null Taxonomy box early in Methods that defines each null precisely (inputs held fixed, what is permuted, what spatial/marginal distributions are preserved), assigns a unique short label, and then use those labels consistently everywhere each σ or p-value appears. Replace vague labels like “isotropic-bootstrap” with the precise taxonomy term.

P4-E8
- Location: Sec. IV C b (p. 8) vs. Appendix A (pp. 13–14).
- Problem: The main-text MASTER ℓ = 1 result (C1 = 2.348×10−5, +7.28σ) does not explicitly state in-line that it uses a monopole-subtracted field, whereas Appendix A declares that choice. This can mislead readers about what field normalization the main-text number applies to.
- Required fix: In Sec. IV C b, add a single explicit sentence clarifying that the reported MASTER ℓ = 1 value is computed on the monopole-subtracted Ap field (galaxy-weighted mask-mean removed) under the stated mask/weight/apodization, matching Appendix A.

MAJOR

P4-M7
- Location: Sec. IV C (pp. 6–8).
- Problem: The real-space “isotropic” permutation null is constructed by permuting Ap across in-mask pixels; while this preserves the one-point distribution on the realized footprint, it is not strictly an “isotropic” sky null (it inherits the mask geometry). The paper partially addresses null dependence by also using per-galaxy label-shuffles, but a rotation-based diagnostic null (where feasible) would test robustness to geometry assumptions.
- Required fix: Add one additional null/robustness test for the real-space estimator that preserves the aperture/mask geometry while scrambling large-scale modes, e.g., (i) ring-wise (iso-latitude) permutations; or (ii) sky rotations followed by intersection with the mask (if practicable); or (iii) a block-permutation preserving local coherence. Report whether the headline +0.41σ conclusion is unchanged.

P4-M8
- Location: Appendix A, item a (p. 13–14).
- Problem: Counterintuitive change: “Monopole subtraction reduces decoupled C1 from 2.30×10−5 to 1.51×10−5 (∼34%) and increases σ from +1.85 to +3.64.” Readers may wonder how σ increases as the measured power decreases.
- Required fix: Add a brief quantitative explanation that the null mean and/or variance change more than the data value after monopole subtraction, hence the σ increase. Ideally show the pre-/post-subtraction null means and σnull so readers can verify the effect.

P4-M9
- Location: Appendix C, item c (p. 16).
- Problem: Hemisphere look-elsewhere grid is specified as “36 × 18 = 648 directions (10° grid).” It is unclear how latitudes are sampled (e.g., are poles included? what is the latitude range and step?), which affects reproducibility and the trials-factor geometry.
- Required fix: Specify the exact directional grid (longitude sampling; latitude range and step; whether poles/edge latitudes are included) so the max-statistic null can be reproduced exactly.

P4-M10
- Location: Sec. II B (p. 2), Appendix B e (p. 15–16), Sec. IV C (p. 6–8), Sec. VI A (pp. 11–12).
- Problem: The paper rightly warns that max-class probabilities are overconfident, yet key selections and sensitivity floors hinge on peq thresholds (0.6, 0.8). A concise empirical calibration of precision/recall vs peq using the GZ1 cross-match would strengthen the choice of the HC-broad cut used for the headline estimator.
- Required fix: Add a small summary (table or figure, possibly in Supplemental) showing chirality accuracy and retained-sample fraction as a function of peq threshold on the disjoint GZ1 cross-match, to justify peq > 0.6 as the operational choice for the HC-broad estimator.

P4-M11
- Location: Appendix D d (p. 16–17).
- Problem: The statement that imaging-leg fraction templates account for “∼25% of the observed canonical-mask ℓ = 1 amplitude” is qualitative.
- Required fix: Quantify this partial closure numerically: report the leg-only model’s predicted C1 (or dipole vector magnitude) relative to the data, with uncertainties. If it’s 25% ± X%, state X%.

P4-M12
- Location: Sec. IV C (p. 7).
- Problem: The term “conservative companion max(Aobs, AUL95)” is introduced without definition and could confuse readers, especially since AUL95 is a null-rank statistic (not a physical CI).
- Required fix: Either define this construction precisely (what inference task it addresses), or remove the phrase. If kept, state clearly that it is a descriptive estimator-level bound with no coverage guarantee.

MINOR

P4-m6
- Location: Sec. VII a (p. 13).
- Problem: Unit confusion specific to this sentence: “injected Ap = 1.7% yields median recovered significance z ≈ 68–218.” Elsewhere, 1.7% refers to fCW units with AAp = 0.034. Writing “Ap = 1.7%” here contradicts the paper’s own Ap↔fCW mapping.
- Required fix: Replace with “injected full-amplitude 1.7% in fCW units (AAp = 0.034)” or with a unified symbol per your amplitude-convention fix.

P4-m7
- Location: Sec. IV B (p. 6).
- Problem: The constant-monopole generative test reports the null means (1.957×10−3 vs 1.935×10−3) and then says this is a “0.39σ shift in the standard error of the difference,” which is a nonstandard phrasing.
- Required fix: Provide a clearer statistical comparison (e.g., difference-of-means in units of the pooled standard error with a p-value), or simply state the numeric difference and its practical irrelevance for the dipole estimator.

P4-m8
- Location: Appendix A c (p. 14).
- Problem: “Nmap,weighted = … reported in Table I” could be misread as if all rows carry this number; but Table I lists Nmap weighted only for the apodized footprint row.
- Required fix: Clarify in text that this Nmap,weighted applies to the apodized Wp = Nall configuration and not to the canonical unweighted rows.

P4-m9
- Location: Sec. IV D footnote 1 (p. 9–10).
- Problem: The per-pixel trial-count inflation factor ⟨Nall/Nspiral⟩ = 2.83 is quoted; readers may wish to see how widely this ratio varies across pixels since it affects binomial variance.
- Required fix: Provide a supplemental histogram or summary stats (median, IQR) of Nall/Nspiral across in-mask pixels.

P4-m10
- Location: Appendix B c (p. 15).
- Problem: The D4 vs Z2 stability summary gives |Δ⟨pCW⟩| < 0.0016 and a 21.4% argmax flip rate on two small hold-outs. A confidence interval on |Δ⟨pCW⟩| would make this more interpretable.
- Required fix: Add a 95% CI on Δ⟨pCW⟩ for the reported subsamples or explicitly note the sampling uncertainty expected at those N.

NITS

P4-n3
- Location: Sec. IV C (p. 8), Appendix E b (p. 18).
- Problem: Multiple closely related ℓ = 1 pseudo-Cℓ statistics appear (+3.64σ canonical; +4.31σ monopole-preserving variant on Catalog C-full; +7.28σ apodized MASTER), which may confuse readers even with caveats.
- Required fix: Add a one-line “navigation” note where the second variant is introduced (Appendix E b), cross-referencing the canonical +3.64σ and the apodized +7.28σ, to help readers map the three estimators.

Rationale
I re-ran arithmetic spot-checks, scanned all figure captions against body text, checked equation units/normalizations, and traced cross-references between main text and appendices. The items above are new relative to the initial review: they address stale or inconsistent counts, clarify null nomenclature, ensure harmonic-field definitions are explicit in the main text, request a small number of additional or clearer robustness summaries, and clean up residual unit/wording ambiguities. These changes improve reproducibility and reader clarity without altering the scientific conclusions.