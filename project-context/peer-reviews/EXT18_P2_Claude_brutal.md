# EXT18 Cross-Vendor Peer Review — P2 (Claude_brutal leg)

- **Reviewer:** Claude_brutal (Claude Code sub-agent, Anthropic) — replaces the
  failed API leg (API call returned 400 "credit balance too low"; this read was
  performed natively by the Claude Code sub-agent with full PDF + tool access).
- **Paper:** P2 — "Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook"
- **Round:** EXT18
- **Version:** v1.7.69 (dated June 14, 2026)
- **Pages reviewed:** 1–29 (full PDF, both ranges, all equations + 5 tables + 6 figures + Appendix A)
- **Read type:** Confirmation read of 3 EXT18 fixes + fresh brutal review of Fisher/Bayes logic, every equation, recomputed table arithmetic.

---

## EXT18 fix confirmation (the 3 items)

**(a) 16th-percentile "comfortably above" → fixed.** Page 5 now reads: "the
16th-percentile 4.4σ draw sits ∼0.8σ below the pre-systematic 5.2–5.5σ band
but remains well above the post-systematic floor." Internally consistent:
4.4σ at σ=0.7 ⇒ r≈0.70, which IS below the band (r∈[0.83,0.88]); pushed
through σ_GR=1.0 it maps to 4.4×(0.7/√(0.7²+1²)) = 2.52σ, consistent with the
~2.6–2.8σ all-combined endpoint. **The "4.4σ" is now described as below, not
above, the band. CONSISTENT.**

**(b) "r ≲ 1.2" → "r ≲ 1.14" → fixed.** Pages 4 and 8 both read "up to
r ≲ 1.14 in our 10,000-sample null-space scan," matching the stated scan range
0.55–1.14. **CONSISTENT.**

**(c) abstract "84%–88%" → "83%–88%" → fixed.** Abstract (p1): "a local
estimator recovers 83%–88% ... (r ∈ [0.829, 0.876])." 0.829→83%, 0.876→88%.
**CONSISTENT.**

All three EXT18 corrections now read consistently across abstract and body.

---

## Recomputed arithmetic (independent verification)

| Claim | Location | Recompute | Status |
|---|---|---|---|
| naive 6.25σ | abstract, Fig 2, Table IV | 4.375/0.7 = 6.250 | ✓ |
| CMB-Fisher 5.5σ (r=0.876) | abstract, §IV | 4.375×0.876/0.7 = 5.475 | ✓ |
| LSS-weighted 5.25σ (r=0.84) | §IV | 4.375×0.84/0.7 = 5.250 | ✓ |
| lower 5.2σ (r=0.829) | §IV | 4.375×0.829/0.7 = 5.181 | ✓ |
| 16th-pctile pre-sys 4.7σ (r=0.75) | p4 | 4.375×0.75/0.7 = 4.688 | ✓ |
| GR σ_GR=0.5 → ~4.3σ | Table IV | 4.375×0.84/√(0.49+0.25)=4.27 | ✓ |
| GR σ_GR=1.0 → ~3.0σ | Table IV | 4.375×0.84/1.221 = 3.011 | ✓ |
| all-combined 30%+GR → ~2.7σ | Table IV | 4.375×0.84/1.345 = 2.73 | ✓ |
| all-combined 50%+GR → ~2.6σ | Table IV | 4.375×0.84/1.414 = 2.60 | ✓ |
| BF delta broad ~17 | Table II/III | 30/(√2π·0.7) = 17.10 | ✓ |
| BF delta rebooked ~14 | p12 | 30/(√2π·0.833) = 14.37 | ✓ |
| Planck recast 0.75σ | §VIII | |−4.375+0.1|/5.71 = 0.749 | ✓ |
| Planck recast central −0.11 | §VIII | −0.1/0.876 = −0.114 | ✓ |
| n_s = 1+12w = 0.964 | §VIII | w=−0.003 ⇒ 0.964 | ✓ |
| 8ε−11 = 1 at ε=3/2 | §VIII | 8(1.5)−11 = 1.0 | ✓ |
| folded B_NL −2.250 = −9/4 | Table I, Fig 1 | −9/4 = −2.25 | ✓ |
| equilateral −3.984 = −255/64 | Table I | −255/64 = −3.984 | ✓ |
| Li −35/16 → 3.13σ pre-sys | Table V, §X | (35/16)/0.7 = 3.125 | ✓ |
| τ_NL local-analog 27.56 | §IX.D | (36/25)(4.375²) = 27.56 = (6·4.375/5)² | ✓ |
| QSFI Δ=3/2 at m²=9H²/4 | §IX.D | 1.5−√(9/4−9/4) = 1.5 | ✓ |

Every recomputed number matches the manuscript. No arithmetic errors found.

---

## ESSENTIAL findings

None.

## MAJOR findings

None. The −35/8 result is honestly framed as **adopted from Cai et al. and
cross-checked**, NOT independently re-derived — the paper states this
explicitly and repeatedly (p7: "A complete independent re-derivation of the
in-in bispectrum integral from the vertex-level Maldacena action is not
undertaken here"; Appendix A.1 derives the −2Im **operator-algebra identity**
symbolically but explicitly does not evaluate the conformal-time integrals).
This is the honest disposition: the factor-of-2 vs Li et al. is resolved as a
convention + operator-ordering distinction (App A, A.1, A.2, Table V), and the
single-time-ordering −35/16 stress-test is correctly labeled "not an
alternative physical bispectrum branch." The σ forecasts are earned: all derive
from the published Heinrich et al. σ(f_NL)=0.7 baseline degraded by a
template-overlap r and systematic budget, never inflated beyond that input.
Abstract matches body throughout.

## MINOR findings

- **M1 (cosmetic, optional).** Abstract is extremely dense (~1.5 pages of small
  text spanning two front-matter columns before §I). PRD will accept it, but an
  editor may request tightening; the closing "Robustness to the single- vs
  full-ordering Li/Cai factor of two" paragraph reads more like a footnote than
  abstract content. *Suggested:* consider moving that paragraph into §II C where
  it is already covered. Not a correctness issue.

- **M2 (consistency, very minor).** §VII and §IX.D both describe the joint
  (f_NL, n_f_NL) SDB Fisher as "subordinate"/"a cross-check"; the
  σ_marg(f_NL)=3.08–7.06 vs fixed-bias 1.53/3.08 numbers are interleaved across
  §VII, Fig 6 caption discussion, and §IX.D. The text does disambiguate ("Two
  distinct Fisher analyses... we distinguish them explicitly"), so this is
  correct — but a single parenthetical pointer table would reduce a momentary
  reader confusion. Optional.

- **M3 (leftover-tag scan).** NO leftover audit tags, TODO/FIXME/XXX markers, or
  placeholder σ values found in the rendered PDF. Artifact JSON filenames
  (c9h_*, c9i_*, c9j_*, c9k_*, c9l_*, null_space_analysis.py, etc.) are
  intentional Data-and-Code-Availability references, not stray tags. Clean.

- **M4 (duplicate-phrase scan).** "UV-completion-independent within the
  Wilson-Ewing class" and "conditional on faithful cubic-order transfer" recur
  (p1, p2, p6, p7) — deliberate hedging consistency, appropriate given the
  no-go-relevant scope claim, not accidental duplication. No problematic
  verbatim repetition found.

---

## Honesty assessment (the brutal part)

- **Is −35/8 honest?** Yes. The paper does not overclaim derivation. It is
  transparent that the value is Cai et al.'s, validated through exact benchmark
  matching (Table I), convention audit (App A), the −2Im commutator identity
  (App A.1, symbolic only), and null-space stability (r_cos=0.985±0.007). The
  "we instead validate... rather than through a fully independent derivation"
  sentence (p7) is exactly the right disclosure.

- **Are the σ forecasts earned?** Yes. Every significance traces to the
  published Heinrich σ=0.7 input × template-overlap r ∈ [0.829,0.876] ×
  systematic budget. The headline is the *noise-weighted* r=0.84 path; the
  CMB-Fisher r=0.876 5.5σ endpoint is correctly quoted as optimistic, and the
  2.6–5σ realistic range correctly carries the GR + b_φ + photo-z budget. The
  "sensitivity recast not an independent forecast" framing (abstract, §IV, §X)
  is repeated honestly.

- **Overclaim check.** The paper caps its own claims: "should be read as
  illustrative of the discriminating power... not as definitive model-selection
  evidence" (abstract, Table II caption, §VI, conclusion). N3-ceiling discipline
  respected — no "proof"/Nobel-tier language. The exclusion-arithmetic-is-
  symmetric statement (a null disfavors the bounce at the same significance) is
  the honest dual framing.

The Bayes-factor logic (closed-form Eq. 9, with the delta-prior vs
Gaussian-prior equation-assignment caveat spelled out exhaustively on p12–14),
the Fisher degradation chain, and the in-in operator algebra are all internally
consistent and conservatively framed.

---

## FINAL VERDICT

**ACCEPT.**

The three EXT18 fixes now read consistently. Every table number and inline
forecast recomputes exactly. The −35/8 result and its in-in treatment are
honestly scoped (adopted + cross-checked, not falsely re-derived). The σ
forecasts are earned from the published Heinrich baseline with transparent
degradation bookkeeping. Abstract matches body. No ESSENTIAL or MAJOR findings;
the MINOR items are cosmetic/optional and do not block submission to Physical
Review D.
