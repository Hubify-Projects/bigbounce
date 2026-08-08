# EXTDB P2 — Gemini MAJOR Truth Audit

- **Round:** EXTDB (DE-BIASED, R57 PDFs)
- **Paper:** P2 — `research/focused_paper_source_integration/02_full_draft.tex` (v1.7.75)
- **Subject:** Gemini 3.5 Flash returned **MAJOR REVISIONS** (2 BLOCKERs + 1 MAJOR); ChatGPT (Instant) and Grok (Expert) both returned **MINOR**.
- **Auditor verdict:** **FALSE-POSITIVE.** All three load-bearing Gemini items are FALSIFIED or ALREADY-DISCLOSED against source. Zero require a `.tex` edit. P2 holds.
- **Calibration (patterns 061/063/064):** Gemini Flash is the FAST tier (1.5-page-ahead rasterization misreads + caveat-skipping). Prior P2 vendor MAJORs across R52–R57 were ALL false-positives (recast misreads, Eq-extraction artifacts). The de-biased prompt is meant to catch real issues, so each item was checked verdict-first against the source line, not reflexively dismissed.

---

## BLOCKER 1 — "r > 1 null-space samples shrink σ_eff below the optimal baseline"

**Gemini claim (precise):** σ_eff = σ(fNL)/r is used throughout; the untruncated 10,000-sample null-space scan yields r up to 1.14; retaining r > 1 lets the effective uncertainty artificially shrink below the local-template baseline, which is mathematically impossible for a local estimator. Resolution: truncate to r ≤ 1 or re-derive variance under a joint cross-Fisher matrix.

**Verdict: FALSIFIED (extraction/caveat-skip artifact; recast misread).**

Source explicitly excludes the exact scenario Gemini posits:

- **Abstract (L664):** "*Only the noise-weighted r ≈ 0.83 enters the SPHEREx significance; r is applied as a shape-weighted degradation to the Heinrich et al. baseline...*"
- **Body L727:** "*these tails are not propagated into the headline significance (which uses the noise-weighted central value r = 0.84 ± 0.02 of Eq. r_noise)...*"
- **Eq:projection footnote (L794):** dedicates a full footnote to the r > 1 reconciliation: r ≲ 1.14 arises only because "*the squeezed-limit value is not the global maximum of |B_NL| for these coefficient choices, not a violation of any physical condition... We retain the full null-space distribution ... without truncation; restricting to r ≤ 1 would amount to imposing an artificial single-field-like monotonicity that the matter-bounce shape does not satisfy. The headline noise-weighted central value r = 0.84 ± 0.02 ... is well below unity and is unaffected by this reconciliation.*"
- **Table IV caption (L1060):** "*Significance = |fNL| × r / σ_eff with r = 0.84 (noise-weighted central value).*"

The r = 0.85 ± 0.13 (range 0.55–1.14) is an explicitly-labeled **distributional scatter band** under uniform Euclidean measure in the monomial null space; it never enters σ_eff. Gemini's premise ("if a null-space sample yields r = 1.14, the effective uncertainty would artificially shrink") is precisely the case the paper rules out in three separate places. No edit. (Mirrors prior STALE/FALSIFIED triage of this same item at R53/R54/EXT18.)

---

## BLOCKER 2 — "Headline 2.6–5σ rests on quadrature-additive systematics, not joint marginalization"

**Gemini claim (precise):** The realistic significance adds individual systematic budgets in quadrature — a heuristic, not a self-consistent forecast. b1 and bϕ are degenerate with fNL; joint marginalization could warp constraints. Resolution: temper the headline in Abstract + Conclusion to state it relies on a quadrature-stacking heuristic, not a full joint covariance.

**Verdict: ALREADY-DISCLOSED → OPINION (not BLOCKER-tier). No defect.**

This is the one genuine methodological soft spot in the paper — and the paper already discloses it in the exact words Gemini's "resolution" demands:

- **Abstract (L666):** "*these systematics are combined additively in quadrature, a transparent scoping choice whose conservatism a full joint Fisher would need to confirm (correlations between systematics can tighten or loosen the combined budget depending on the sign of the covariance...).*"
- **Abstract (L666):** "*...are a sensitivity recast rather than an independent cross-Fisher forecast.*"
- **Table IV caption (L1060):** "*Combination rule '⊕' denotes addition in quadrature ... a transparent scoping choice ... (additive-quadrature rather than joint-marginalized Fisher).*"
- **bϕ degeneracy (L984):** the bϕ marginalization degradation (O(20–50%)) is explicitly carried into the headline range as the bϕ-30%/50% Table IV scenarios.

The requested fix is already in the abstract and conclusion. ChatGPT raised the identical point as its **MAJOR-1** and Grok as **MINOR M2** — the cross-vendor consensus tier is MINOR/already-caveated, not BLOCKER. Gemini over-escalated a disclosed limitation to BLOCKER. No edit required; optional strengthening only.

---

## M1 — "Scale-dependent-bias redshift bins (z=0.1–1.5) disconnect from Heinrich bispectrum (z≈0.5–2)"

**Gemini claim (precise):** The joint (fNL, n_fNL) Fisher uses six bins z=0.1–1.5 while Heinrich's SPHEREx bispectrum baseline targets ELGs at z≈0.5–2. The paper "combines two completely different tracer distributions and redshift ranges for a singular unified complementary mapping." Resolution: harmonize, or add a note on coordinating tracer boundaries without double-counting cross-correlations over z=0.5–1.5.

**Verdict: FALSIFIED / STALE — premise is factually wrong; the disconnect is explicitly disclosed and the channels are NOT combined.**

- **L1122 (verbatim, parenthetical on the six-bin forecast):** "*z = 0.1–1.5, f_sky = 0.75; this is the low-redshift bin subset of the SPHEREx public-products sample structure used in the committed SDB Fisher computation, **a different tracer selection from the z ≈ 0.5–2 emission-line sample underlying the Heinrich et al. bispectrum forecast of Sec. spherex — the two channels quote different redshift ranges by construction.***"
- **L1122 / L1125:** "*Two distinct Fisher analyses are reported ... we distinguish them explicitly here to avoid confusion.*" The SDB joint channel is "*a subordinate cross-check on the running, not a competitor to the bispectrum-only headline.*"
- **Channel-hierarchy note (L1130):** "*The two channels use distinct Fisher matrices, distinct survey samples, and distinct sufficient statistics; they are complementary rather than competing.*"

Gemini's core premise — that the paper merges the two into "a singular unified complementary mapping" with double-counted cross-correlations — is false: the paper explicitly keeps them as separate Fisher matrices, never sums them, and flags the z-range difference "by construction." There is no double-counting because there is no combination. This is a fast-tier misread of the two-channel framing. No edit.

---

## Bottom line

| Item | Gemini tier | Audit verdict | Fix needed |
|------|-------------|---------------|------------|
| BLOCKER 1 (r>1 / σ_eff) | BLOCKER | FALSIFIED | None |
| BLOCKER 2 (quadrature systematics) | BLOCKER | ALREADY-DISCLOSED / OPINION | None |
| M1 (z-bin disconnect) | MAJOR | FALSIFIED / STALE | None |

The Gemini MAJOR is a **FALSE-POSITIVE**, consistent with the R52–R57 pattern of P2 fast-tier recast misreads. The cross-vendor signal agrees: ChatGPT and Grok, reading the same de-biased PDF, found **zero BLOCKERs** and only presentational MINORs. The single genuinely real methodological limitation (additive-quadrature systematics) is already disclosed verbatim in the abstract, conclusion, and Table IV caption. **P2 holds at current readiness; no source edit triggered by this round.**

(Per CLAUDE.md standing rule, this round still warrants a `reviewTimeline.ts` entry of kind external-review-round when the EXTDB round is bundled.)
