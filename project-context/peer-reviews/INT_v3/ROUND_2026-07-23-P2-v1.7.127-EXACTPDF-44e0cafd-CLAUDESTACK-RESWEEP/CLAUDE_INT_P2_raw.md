# CLAUDE INT — P2 raw referee report (routine re-sweep 2026-07-23)

- **Paper:** P2 — "The Exact Matter-Contraction Non-Gaussian Amplitude: Four-Vertex Derivation and Conditional Large-Scale-Structure Mapping"
- **Bound PDF:** `research/focused_paper_source_integration/02_full_draft.pdf`
- **Declared version:** v1.7.127, 11pp, PRD (revtex4-2)
- **Binding SHA-256 (expected):** `44e0cafd6fd92b6df7e0fbb8c06ecf696e97620aa0e16de4c7c9cc7105d22866`
- **Computed SHA-256:** `44e0cafd6fd92b6df7e0fbb8c06ecf696e97620aa0e16de4c7c9cc7105d22866`
- **Binding:** VERIFIED (exact match). Reviewed all 11 pages of the exact bound bytes.
- **Referee stance:** standard high journal-referee bar, no steering. Scope: confirm the five 2026-07-22 numeric-transparency closures landed with no physics regression and no new contradiction; recompute every touched number; flag anything genuinely new.

## Closure verification (five 2026-07-22 numeric-transparency rewrites)

**C1 — 30% prior labeled illustrative benchmark.** LANDED.
Table III caption (p7): "The 30% row is explicitly theory-prior conditional (an illustrative benchmark, not a first-principles bound)." Body p5: "a declared 30% Gaussian bracketing typical assembly-bias departures from the universal-mass-function b_φ, not a first-principles bound." Abstract carries "an explicit 30% theory prior." Consistent; the illustrative/benchmark framing is now explicit at every occurrence. No regression.

**C2 — r_eff clause.** LANDED.
p5: "r_eff = 0.9929 and 0.9986 ... (a covariance-weighted information cosine, *not* the bare σ ratio, e.g. 0.626/0.631 = 0.992)"; Sec VII closes with "no uncertainty band is invented for r_eff." The clause correctly distinguishes the information-cosine recovery statistic from a bare σ ratio and declines an invented band. No regression.

**C3 — 0.36σ.** LANDED and recomputed correct.
Sec VIII (p6/8): Planck PR4/NPIPE f_NL = −0.1 ± 5.0; CMB-weighted r = 0.876 → f_NL^bounce = −0.11 ± 5.71.
  - Recompute f_NL^bounce: −0.1/0.876 = −0.1142 ≈ −0.11 ✓ ; 5.0/0.876 = 5.708 ≈ 5.71 ✓
  - Recompute σ-distance from −35/16 = −2.1875: (2.1875 − 0.11)/5.71 = 2.0775/5.71 = 0.364σ ≈ 0.36σ ✓
  - Consistency-with-zero cross-check: 0.11/5.71 = 0.019σ, matching "consistent with both the matter-bounce amplitude and zero." ✓

**C4 — 34.7% baseline 0.688 → 0.449.** LANDED and recomputed correct.
p5: "The approximately 34.7% bias-marginalized gain over the real-space calculation (0.688 → 0.449, the bounce-template bias-marginalized baseline)."
  - Recompute: (0.688 − 0.449)/0.688 = 0.239/0.688 = 0.3474 = 34.7% ✓
  - The rewrite now names the specific baseline pair (real-space bounce-template bias-marginalized 0.688 → redshift-space bounce-template bias-marginalized 0.449), removing the prior ambiguity. No regression.

**C5 — 2.63σ recompute wording.** LANDED and recomputed correct.
p4/5: "direct substitution gives |f_NL|·r/0.7 = 2.61σ; recomputing with the adopted r = 0.84 convention gives 2.63σ ... reduced from the naive ratio 3.13σ. (the rounding is in r: 0.8354 → 0.84, not a rounding of 2.61σ)."
  - r = 0.8354: 2.1875·0.8354/0.7 = 2.611σ ≈ 2.61σ ✓
  - r = 0.84: 2.1875·0.84/0.7 = 2.625σ ≈ 2.63σ ✓
  - naive ratio: 2.1875/0.7 = 3.125 ≈ 3.13σ ✓
  - The parenthetical correctly attributes the 2.61→2.63 shift to the r-convention rounding, not a σ rounding. No regression.

## Full recompute battery (all seven task-listed touched numbers)

- 0.626 — real-space local-template, bias fixed (p5). Present, consistent. ✓
- 0.687 — real-space local-template, bias marginalized (p5). ✓
- 0.688 — real-space bounce-template, bias marginalized (p5). ✓
- 0.449 — redshift-space bounce-template, bias marginalized (p5). ✓
- 34.7% — (0.688−0.449)/0.688 = 34.74% ✓
- 0.36σ — (2.1875−0.11)/5.71 = 0.364σ ✓
- 2.63σ — 2.1875·0.84/0.7 = 2.625σ ✓

## Independent cross-checks (physics untouched, spot-verified)

- Headline coefficient −35/16 = −2.1875, consistent in abstract, Eq (2), Table I, Sec IX, X, App B. ✓
- Ordered-basis coefficient vector (3, 1, −9, 5, −33, 9), Eq (4); consistent throughout. ✓
- Equilateral −255/128 = −1.9922 (Table I) ✓ ; folded −9/8 = −1.125 ✓.
- Template-normalization benchmark 146: 2.1875/0.015 = 145.83 ≈ 146 ✓.
- Torsion bound endpoints (Eq 5): γ=1 → (35/16)(3/16)(0.5) = 0.205 ≈ 0.21 ✓ ; γ=0.2375 → 0.0219 ≈ 0.022 ✓.
- Channel-native ladder Table III (3.47/3.14/2.32/0.42σ) matches abstract/Sec IV/Sec IX rounded (3.5/3.1/2.3/0.4σ). ✓
- Flat-grid recovery r = 0.83542294, r_cos = 0.98167825 (p2) ↔ abstract 0.8354/0.9817. ✓

All physics, derivations, and the four-vertex re-summation are unchanged and internally consistent. No physics regression from the numeric-transparency wave.

## Genuinely-new finding

**N1 (MINOR, presentation / internal inconsistency) — stale in-body version self-reference.**
Data Availability (p7) states: "the present manuscript is **v1.7.126**, and this and subsequent versions are added to the same Zenodo record." The title-page version tag (p1) and the binding are **v1.7.127**. The Data-Availability self-reference is stale by one patch relative to the actual document version. This is a factual internal inconsistency a reader can catch; it is not a science, claims, or data problem. Appears to be version-stamp drift: the directive-G bump updated the header/date/tag but not the manual Data-Availability prose string. Closeable by syncing that one string ("v1.7.126" → "v1.7.127"; verify the "reviewed v1.7.125" Zenodo reference is likewise current).

No other new contradictions surfaced across the 11 pages. The five targeted closures each landed correctly and all recomputes pass.

## Verdict rationale

Every 2026-07-22 numeric-transparency closure landed correctly; all seven touched numbers recompute exactly; no physics regression. One genuinely-new, low-severity internal inconsistency (N1: version self-reference v1.7.126 vs v1.7.127) prevents a clean ACCEPT under the high referee bar. Severity is copy-edit tier, single string.

VERDICT: MINOR-REVISIONS
