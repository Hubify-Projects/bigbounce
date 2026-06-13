# P2 R36conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper2_fnl_forecast_v1.7.58.pdf` md5=6b3c9b5e pages=27
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6442 chars)
**Wall time**: 415.0s

---

Referee report (Physical Review D – Methodology and internal-consistency review)

Scope
I audited the full manuscript (27 pp.), equations, figures, tables, and all quoted numbers. My review focuses on statistical/forecast methodology, derivation chains, dimensional and arithmetic consistency, estimator definitions, and traceability of every scalar quoted in the abstract and conclusions to the body of the paper.

Overall impression
The paper is a sensitivity recast: it does not build a new Fisher matrix but degrades a published SPHEREx bispectrum σ(fNL) using a carefully quantified template overlap r and a stated “systematics budget.” The technical narrative is unusually detailed and many caveats are spelled out. However, PRD requires that load-bearing numerical claims and methodological steps be fully reproducible from the text without internal version-history notes or placeholder artifacts. Several essential editorial and methodological fixes are required before this can meet PRD standards.

Findings

ESSENTIAL

P2-E1 — Version-history prose in the body
- Location: p. 14 (Sec. VI.C.b, “Correction note: an earlier version…”), p. 16 (Table III note, “Correction note…”), p. 21 (Sec. VIII.D, “Correction note…”), p. 26 (Table IV note, “earlier version…”), and scattered elsewhere.
- Problem: Version-history and draft-to-draft correction notes appear in the body. PRD requires a self-contained final text without internal revision log comments.
- Required fix: Remove all version-history/correction notes from the main text. If truly needed, move a concise changelog to an arXiv ancillary note, not the PRD manuscript.

P2-E2 — Data/code archival incompleteness
- Location: p. 22–23, Data and Code Availability.
- Problem: “DOI inserted at submission” is a placeholder; only a mutable GitHub branch is cited. No frozen commit hash/tag is specified for the exact version used to generate the reported numbers.
- Required fix: Archive the full code and artifacts in a permanent repository (Zenodo or similar) and provide the DOI; specify the exact Git commit hash/tag used to produce every table/figure/value. Ensure that all named JSON/py artifacts referenced in the text are present in that archive. PRD requires a stable provenance surface.

P2-E3 — Internal-audit artifact names inside the scientific narrative
- Location: p. 4–7 and Appendix A (e.g., “artifact c9i epsilon ratio check.json”, “phase3 fisher overlap.json”, “appendix A1 wick doubling.py”, etc.).
- Problem: These are internal bookkeeping identifiers embedded in the scientific prose, which is not acceptable PRD style and hinders readability.
- Required fix: Move all such file-name callouts to the Data and Code Availability section or to a single Supplementary Materials table listing artifacts and their roles. Remove them from the main scientific narrative.

P2-E4 — Systematics “budget” lacks a consolidated, quantitative summary
- Location: Abstract; p. 8–10 (Sec. IV); p. 15–18 (Sec. VII).
- Problem: The paper states a “realistic ∼2.6–5σ after the systematic budget” and describes the ingredients qualitatively across sections (template mismatch r, ϵ-correction, null-space scatter in r, photo-z degradation, bϕ marginalization, GR projection modeled via σGR). However, there is no single consolidated table that lists, for SPHEREx: (i) the baseline σ(fNL), (ii) each degradation contribution with its numerical value and whether it is applied to the numerator, denominator, or both, (iii) the combination rule (quadrature vs covariance-aware), and (iv) the resulting σeff and significance. As written, a reader must assemble these pieces from multiple paragraphs; that is not sufficiently transparent for PRD.
- Required fix: Add a single table that line-items every systematic entering the “2.6–5σ” window with the exact numbers used (e.g., r = 0.84±0.02, ϵ-correction range mapped to Δ|fNL|, null-space scatter mapped to Δr, photo-z degradation factor, bϕ prior widening: 20/30/50% cases, σGR = 0/0.5/1.0), and shows how they combine to produce the endpoints quoted. If some effects are not applied jointly in the headline, say so explicitly.

P2-E5 — Abstract-to-body alignment must be locked to the same bookkeeping
- Location: Abstract; p. 9–10 (Sec. IV), p. 10–11 (Sec. V), Table II.
- Problem: The abstract quotes Bayes factors “≈ 9–14” under the noise-weighted r ≈ 0.84 bookkeeping, while Table II presents the r → 1 endpoint values. The text later explains the two bookkeepings and gives the rescaled numbers, but the abstract does not say that Table II carries a different bookkeeping. PRD requires that abstract claims match the exact body conventions, or explicitly say when numbers are from a different bookkeeping.
- Required fix: Add one sentence to the abstract noting that Table II reports the r → 1 endpoint values and that the abstract headline adopts the noise-weighted r ≈ 0.84 bookkeeping. Alternatively, unify all Bayes-factor numbers to a single consistent bookkeeping throughout.

P2-E6 — Remove or relocate speculative “stress-test” central values that are not part of the physical model
- Location: Abstract p. 1–2 and Appendix A/Table IV (Li et al. single-time-ordering values).
- Problem: The manuscript repeatedly presents detection significances for the non-physical single-time-ordering intermediate (−35/16), sometimes adjacent to the physical forecast. This risks confusing readers about what is actually forecast.
- Required fix: Keep the operator-identity derivation in Appendix A, but move all single-time-ordering significance numbers out of the main text and tables into a brief Appendix “stress-test” box, clearly labeled as non-physical. Ensure no abstract or conclusion line quotes these as an alternative forecast.

MAJOR

P2-M1 — Mixed use of different shape metrics to argue “projection noise is subdominant”
- Location: p. 7–8 (Sec. III.B).
- Problem: The suppression of projection noise is argued using rcos computed in an unweighted shape metric, while the estimator Fisher metric is survey-noise-weighted. The text acknowledges this is heuristic, but then uses it to support subdominance claims.
- Required fix: Either compute rcos (or an equivalent overlap) in the same Fisher metric used for the estimator, or clearly quarantine this as a qualitative indication and remove any quantitative inference (“subdominant”) based on it. A short supplemental calculation with survey weight would resolve this.

P2-M2 — Inconsistent rcos floor quoted in two places
- Location: p. 4–5 vs p. 6–7.
- Problem: The text states “rcos > 0.97 for all 10,000 samples” and elsewhere “rcos > 0.95 across scan radii 10–500.” These are not strictly inconsistent (different scan setups), but they read as contradictory.
- Required fix: State the precise conditions for each bound (e.g., “for the 10k null-space samples at radius 50 we find rcos > 0.97; across radius 10–500 scans, rcos > 0.95”). Remove any ambiguity.

P2-M3 — Squeezed-cutoff variable x3,min is used without definition
- Location: p. 8 (Sec. III.B).
- Problem: “squeezed cutoffs (x3,min from 0.001 to 0.2)” appears without a prior definition of x3.
- Required fix: Define x3 explicitly (e.g., x3 ≡ k3/k1 in the squeezed configuration with k1 ≥ k2 ≥ k3; or the exact ratio used in your grid).

P2-M4 — Consolidate SPHEREx vs SDB-vs-CMB estimator comparisons to avoid implicit comparability
- Location: p. 5 (injection/recovery), p. 8 (ℓ-space Fisher overlap), p. 19–21 (joint SDB Fisher).
- Problem: Different estimator/weighting contexts are presented adjacently and occasionally on the same page figure/caption without a repeated “not directly comparable” disclaimer at each juxtaposition. While the text often notes the differences, the density and proximity of numbers invites unintentional comparisons.
- Required fix: Add an explicit “not directly comparable” note wherever CMB-inspired 2D KSW, ℓ-space CMB Fisher, and 3D LSS bispectrum/SDB results appear side-by-side. Alternatively, relegate the CMB-style validation to an appendix.

P2-M5 — Bayes-factor presentation would benefit from a single, consistent, closed-form worked example
- Location: p. 11–14 (Sec. VI.C), Table II, Table III.
- Problem: The text mixes delta vs Gaussian bounce priors, narrow vs broad competitor priors, r → 1 vs r ≈ 0.84 bookkeeping, and σGR variations. All of these are legitimate, but the reader needs one canonical worked example in the body that exactly matches the abstract headline.
- Required fix: Add a boxed worked example (one paragraph) reproducing the abstract’s BF ≈ 9–14 from Eq. (8) with the stated priors and σeff, including the r ≈ 0.84 bookkeeping, so the headline is reproducible from one place.

P2-M6 — “Additively in quadrature” combination of heterogeneous systematics needs explicit justification
- Location: Abstract; p. 9–10; p. 15–18.
- Problem: The manuscript adds conceptually different effects (template mismatch, theoretical ϵ-correction, estimator covariance tails, bϕ priors, GR projection nuisance) in quadrature. The text flags this as a “transparent scoping choice,” but PRD readers will expect either a rationale for why cross-covariances are negligible or a sensitivity table showing how correlations could shift the range.
- Required fix: Provide: (i) a sentence that justifies treating these terms as independent for quadrature (or, if not, state that this is an upper-bound heuristic), and (ii) a small 2×2 example showing the effect of positive/negative covariance between two dominant terms on σeff, to demonstrate robustness of the quoted 2.6–5σ window.

MINOR

P2-n1 — Check of key arithmetic/ratios (all OK but document)
- Location: various.
- Verified:
  - |fNL|/σ = 4.375/0.7 = 6.25 (naive).
  - Template-corrected 4.375×0.83–0.876 / 0.7 = 5.19–5.48σ (reported 5.2–5.5σ).
  - GR-only floor: 4.375×0.83/√(0.7^2+1.0^2) ≈ 2.98σ (reported ≈3.0σ).
  - “All-combined conservative endpoint”: 4.375×0.84/√(0.9^2+1.0^2) = 2.73σ, and with σ = 1.0 gives 2.60σ (reported 2.6–2.8σ).
  - MegaMapper intermediate case: 4.375×0.84/√(0.7^2+0.9^2) ≈ 3.22σ (reported ≈3.2σ).
  - Ratio |fbounce|/|finf|: 4.375/0.015 = 291.7 (reported ≈ 290).
  - Planck PR4 recast with r = 0.876: σ = 5.0/0.876 = 5.71; tension |−4.375−(−0.11)|/5.71 = 0.75σ (reported 0.75σ).
  - τNL estimate: (36/25) fNL^2 = 1.44 × 19.14 = 27.6 (matches).
- Required fix: None; note included for the editor that the headline numbers check out.

P2-n2 — Dalal-convention mapping
- Location: p. 7 (Eqs. 3–4).
- Observation: Δb(k,z) = 2 fNL (b1−1) δc / M(k,z) with M = 2k^2 T D /(3ΩmH0^2) is the standard α(k) definition. Dimensions and limiting scaling ∝ 1/k^2 check out.
- Required fix: None.

P2-n3 — Fig. 2 caption clarity
- Location: p. 10 (Fig. 2).
- Problem: The caption mixes “naive”, “template-corrected optimistic”, “realistic post-systematic-budget envelope”, and “all-combined conservative endpoint” in one panel. It is easy to confuse which inputs were used in each bar.
- Required fix: Add the exact numerical inputs under each bar (e.g., “4.375×0.84/0.7”, “4.375×0.84/√(0.9^2+1.0^2)”), or include a small legend table in the caption.

P2-n4 — Minor notational overload and clarity
- Location: p. 7 (Sec. III.B), p. 18–21 (Sec. VIII.D).
- Problem: r is used for template overlap; later rt is defined explicitly to avoid collision with the tensor-to-scalar ratio. Good practice, but reserve a one-time “r is the template-overlap factor throughout” reminder when rt first appears.
- Required fix: Add that reminder once; optional.

NITS

P2-N1 — Hyphenation artifacts and micro-typos
- Location: throughout (PDF extraction soft hyphens, e.g., “en￾ters”).
- Fix: Clean final PDF typesetting.

P2-N2 — Length and focus
- Location: whole paper (27 pages).
- Comment: For a recast (not a full, independent Fisher forecast), 27 pages is long. Consider moving Appendix A and the S3-orbit counting discussion to Supplementary, and compressing the narrative by ~10–20% without losing methodological content.
- Required fix: Optional but recommended.

Specific confirmations requested by the editor (arithmetic check)
- Sec. V, conservative MegaMapper significance with r = 0.84, σ(fNL) = 0.7 and 30% bϕ prior widening to σ = 0.9: 4.375 × 0.84 / √(0.7^2 + 0.9^2) = 3.22σ. The manuscript reports “≈ 3.2σ.” Verified.
- No other regressions were found; all other headline numbers in the abstract and conclusions trace to explicit body formulas and check arithmetically.

Abstract-last drift sweep (pattern-045)
- The abstract’s 5.2–5.5σ and 2.6–5σ ranges, the r ≈ 0.84 overlap, the Bayes-factor ranges (with the bookkeeping caveat in the body), and the “factor-of-two” resolution are all supported somewhere in the body. However, fix P2-E5 to ensure the Bayes-factor bookkeeping is unambiguous already at the abstract.

Provenance surfaces (patterns 046/047)
- See P2-E2: add DOI and frozen commit hash. The current text is not compliant.

Uncomputed quantitative claims (pattern-048)
- Most qualitative claims are accompanied by numbers. The one substantive gap is the consolidated systematics table (P2-E4). Once added, this issue resolves.

Standalone-reader test
- Generally self-contained, with a commendable amount of technical detail. The single exception is the reliance on the Heinrich et al. SPHEREx σ(fNL) = 0.7 Fisher matrix; this is acceptable as an adopted external baseline, but the paper correctly labels itself a recast rather than an independent forecast.

Effect sizes
- The paper consistently converts to σ-level statements. For Bayes factors, effect-size interpretation is less standard; the manuscript could add a Jeffreys-scale qualitative label once (optional).

## Summary recommendation
MAJOR REVISIONS

The core methodology is sound for a sensitivity recast, and the principal numbers check out. However, PRD requires (i) removal of version-history prose from the body, (ii) a complete, permanent code/data archive with DOI and frozen commit hash, (iii) relocation of internal artifact names out of the scientific narrative, and (iv) a single consolidated, quantitative systematics table so the 2.6–5σ “realistic” window is transparently reproducible from one place. Clarifying the Bayes-factor bookkeeping in the abstract vs body and tightening minor consistency/notation issues will further improve clarity. With these fixes, the paper could be suitable for PRD.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eyes pass)

ESSENTIAL

P2-E7 — Dimensional inconsistency in Eq. (2) (numerator/denominator swap)
- Location: p. 3, Eq. (2) and surrounding paragraph.
- Problem: As printed, “BNL = (10/3) P/AT ∑i k_i^3” implies P cancels out (since AT already contains P from Eq. (1)), contradicting the very next sentence (“no cancellation of P occurs… via AT”) and breaking dimensional consistency. The dimensionless construction described in prose (degree-9 P, −6 from the prefactor, −3 from Σk_i^3) requires BNL ∝ AT/(Σ k_i^3), not P/AT.
- Required fix: Correct Eq. (2) to BNL(k1,k2,k3) = (10/3) AT(k1,k2,k3) / (k1^3 + k2^3 + k3^3). This restores units and matches the “no cancellation of P” statement.

P2-E8 — Ambiguous typesetting in Eq. (1) obscures units
- Location: p. 3, Eq. (1).
- Problem: AT is written as “3 256 k1^2 k2^2 k3^2 P”, which reads as a product rather than a quotient. The intended form (needed for the degree counting that follows) is 3/(256 k1^2 k2^2 k3^2) × P.
- Required fix: Typeset explicitly as AT(k1,k2,k3) = [3/(256 k1^2 k2^2 k3^2)] P(k1,k2,k3). This also aligns with the dimensional narrative immediately below Eq. (2).

MAJOR

P2-M7 — Unreproducible orbit-factor mapping in footnote 1 (C3 vs S3 counting)
- Location: p. 3–4, footnote 1 and the paragraph preceding it.
- Problem: The argument that connects Cai et al.’s single-time-ordering coefficients to your symmetrized basis via “orbit-by-orbit Wick-permutation ratios” (e.g., |S3|/|C3| = 2 for (7,2,0)) is plausible but not reproducible from the text: the stabilization subgroups for all six orbits and the full linear transform (including any additional factors from identical-field symmetry) are not shown.
- Required fix: Provide the explicit 6×6 linear transformation (or list the stabilizer sizes and resulting normalization for each orbit) in Supplementary Material so a reader can verify that the printed Cai coefficients cannot be transplanted and that your basis is correctly normalized.

P2-M8 — Quantitative photo-z and anomaly-tracer claims lack derivations
- Location: p. 10 (Shot-noise caveat paragraph) and p. 17 (Photometric redshift outliers).
- Problem: The text states: (i) “a ∼15–30% degradation in σ(fNL)” for anomaly-selected tracers from a “simple Poisson estimate” and (ii) “even with 10% catastrophic outlier fraction, σ(fNL) degrades by only ∼5%” for the bispectrum channel. No calculation, figure, or external citation is provided to substantiate these numbers.
- Required fix: Either (a) include a short back-of-the-envelope calculation (inputs, scaling, and resulting percent changes) or (b) move both numbers to a clearly labeled scoping remark without quantitative claims. If kept, cite a source or provide the Fisher scaling you used.

P2-M9 — Inconsistent rounding for the central overlap r risks confusion
- Location: p. 8–10 (Sec. III.B, Sec. IV).
- Problem: The text alternates between r ≈ 0.83 and r ≈ 0.84 as the “noise-weighted” central value while quoting a ±0.02 spread, and then uses both values in significance arithmetic. This is numerically minor but invites ambiguity.
- Required fix: Pick one canonical central value for the noise-weighted case (e.g., r = 0.84) and use it consistently in all headline computations; keep the alternative values only when explicitly tied to a different weighting or validation channel.

MINOR

P2-m3 — Missing definitions beyond x3
- Location: p. 4–8.
- Problem: In addition to the already-flagged x3,min definition gap, Slocal and Stempl (used in the cosine definition) are not explicitly defined when first introduced.
- Required fix: Add one sentence defining Slocal (the standard local shape kernel) and Stempl (the normalized local-template shape used by the estimator) at first mention in Sec. II or III.B, alongside the explicit definition of x3 ≡ k3/k1 (with the triangle-ordering convention you adopt).

P2-m4 — Possible overstatement in Fig. 4 caption vs body text
- Location: p. 15 (Fig. 4 caption) vs Sec. VII.A–C.
- Problem: The caption says the SPHEREx bispectrum channel “avoids the ultra-large-scale fragility,” while the body acknowledges residual low-k sensitivities (GR projection, window-coupling). “Avoids” may read as too strong given the later caveats.
- Required fix: Soften the caption (“is substantially less sensitive to ultra-large-scale fragility than SDB”) to align with the GR caveats in Sec. VII.

P2-m5 — Minor forward-reference mismatch on DBI aside
- Location: p. 9 (start of Sec. IV).
- Problem: The paragraph flags DBI inflation as deferred to §VI and as irrelevant for the local template here. Later, §VI.D clarifies DBI is a bispectrum-shape discriminator rather than an nfNL discriminator. The logic is fine, but the cross-reference could be tightened for readers skimming only the SPHEREx section.
- Required fix: Add a parenthetical in Sec. IV explicitly saying “DBI has vanishing local squeezed amplitude; a bispectrum-shape comparison (not performed here) is required for DBI and is discussed in §VI.D.”

NITS

P2-N3 — Consistent symbol hygiene for r vs rt reminder
- Location: p. 7 and p. 7–8 (where rt first appears).
- Problem: Although you later clarify rt is the tensor-to-scalar ratio, a one-line reminder at first mention would prevent misinterpretation with the template-overlap r.
- Required fix: Add “We reserve r for the template-overlap factor; rt denotes the tensor-to-scalar ratio” at the first use of rt.

P2-N4 — “Launched March 2025” phrasing
- Location: Abstract and Sec. IX.A.
- Problem: While likely accurate by the manuscript date, PRD copyeditors sometimes prefer “launched in 2025” or “launched March 2025 (nominal)” to avoid time-sensitive phrasing aging poorly.
- Required fix: Optional wording softening.

Explanation for completeness
I performed a fresh equation-by-equation dimensional check, recomputed representative Bayes-factor magnitudes and detection significances, and cross-compared captions with body claims. The most substantive new issue is the dimensional/numerator error in Eq. (2), which contradicts the adjoining text and would force P to cancel if left as written. The other additions tighten reproducibility (orbit-factor mapping), quantify or quarantine heuristic degradation percentages, and improve internal consistency and clarity. All arithmetic spot-checks of headline claims (σ-levels, Bayes factors, ratios) remain consistent with the body once Eq. (2) is corrected.