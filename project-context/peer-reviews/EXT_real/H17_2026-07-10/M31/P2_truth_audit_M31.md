# P2 M31-EXT truth audit (2026-07-13, vs byte-unchanged v1.7.116)

Owner: P2 paper-owner (Opus). Strict ledger-first, integrity-first.
Raws read verbatim BEFORE any disposition:
- `EXT_real/H17_2026-07-10/M31/P2_grok_M31.md` — l.1 `VERDICT: MINOR REVISIONS` (0 MAJOR / 6 MINOR)
- `EXT_real/H17_2026-07-10/M31/P2_chatgpt_M31.md` — l.1 `VERDICT: REJECT` (10 MAJOR / 2 MINOR)

Paper: `research/focused_paper_source_integration/02_full_draft.tex` v1.7.116
(headline `f_NL^local = -35/16 = -2.1875`, quadruple-certified DP2-02).
Derivation source re-run this wave: `scripts/p2_vertex_check.py`,
`scripts/caili_certification/cai_vertices.py`.

---

## CRUX — ChatGPT M31 MAJOR #1: the orbit-double-counting claim

**ChatGPT's claim (verbatim substance):** the paper defines every `i≠j≠l` sum as
six ordered permutations, which "double-counts the (5,2,2) orbit because exchanging
the two equal exponents produces the same monomial; the resulting extra copy
generates exactly −99/128 Σkᵢ³" — implying the paper's factor-of-two diagnosis is
mis-derived and the "four-way certification must be redone."

**VERDICT: NON-REAL — source-cited re-flag of DP2-01/-25/-15/-16. NOT genuinely-new. The headline −35/16 is UNAFFECTED, and ChatGPT's own conclusion concedes −35/16 "may nevertheless be correct."**

### Direct verification (re-ran `p2_vertex_check.py` this wave):

The script computes fNL under BOTH orbit conventions explicitly — precisely the
double-counting hypothesis ChatGPT raises:

```
=== 6-perms (ordered-permutation convention, the paper's) ===
  squeezed leading (k1->0): -35/16          ← HEADLINE
  equilateral fNL: -255/128                  ← Table I benchmark
=== distinct-monomial (ChatGPT's "corrected" convention) ===
  squeezed leading (k1->0): -285/128
  equilateral fNL: -65/32
Li at c_s=1: -35/16                           ← independent, convention-FREE
```

**Point 1 — the double-count structure ChatGPT describes is REAL but is exactly
what the paper already documents.** For an orbit with two equal exponents (the two
2's in (5,2,2)), the six-ordered-permutation sum counts each distinct monomial 2!=2
times. Verified: `perms(5,2,2) − distinct(5,2,2) = distinct(5,2,2)` (an exact
extra copy). So switching 6-perms→distinct DOES change the polynomial. This is the
per-orbit Wick-permutation-count structure already stated in the paper
(`02_full_draft.tex` §benchmark footnote L713-714: "linear map from Cai's monomial
normalization to symmetrized basis via per-orbit Wick-permutation count ratios";
App A six-ordered-triple convention L162/L1489). **This is DP2-15's amplitude-
invariant basis/measure question and DP2-01's spurious-term bookkeeping — both
long-standing.**

**Point 2 — ChatGPT gets the physics BACKWARDS: the 6-perms convention is the
CORRECT in-in convention, not the double-count.** The decisive, convention-FREE
arbiter is the independent Li/Quintin/Wang/Cai (2017, arXiv:1612.02036) closed-form
`fNL = −165/16 + 65/(8 c_s²) → −35/16` at c_s=1. This formula never touches the
orbit-counting at all, and it agrees with the **6-perms** result (−35/16), NOT the
distinct-monomial result (−285/128). Independently, the 6-perms equilateral value
(−255/128) matches the paper's Table I benchmark. If ChatGPT's "distinct" convention
were correct, BOTH the squeezed AND equilateral benchmarks would have to move to
−285/128 / −65/32 AND contradict Li — they do not. **ChatGPT's proposed "fix" is the
convention that FAILS the two independent cross-checks; the paper's is the one that
passes. Its premise (6-perms = the double-count) is the inversion of the actual
result.**

**Point 3 — even if the intermediate bookkeeping is re-articulated, the headline
−35/16 is UNAFFECTED.** ChatGPT's "−99/128 Σkᵢ³ extra copy" is a re-description of
the very term the paper already isolates and discloses: the printed-polynomial vs
vertex-sum discrepancy `A_T − Σ(vertices) = −(99/128)Σkᵢ³` (`cai_vertices.py` L31-32;
DP2-01, eq:spurious L1475), which drives the *transcribed printed* polynomial to its
squeezed value −305/64 (NOT −35/8). This term lives in the analysis of *Cai's printed
polynomial* (the erroneous literature value), not in the vertex-sum that produces
−35/16. The −35/16 headline is quadruple-certified by paths that do NOT depend on it
(per-vertex sum, ε-order group, Li c_s=1, collapsed degree-9 polynomial; DP2-02).
ChatGPT itself concedes this ("−35/16 may nevertheless be correct").

**Point 4 — the App-A.1(d) time-ordering sub-claim** ("Cai's ε-grouped terms follow
from the full commutator, not before the −2Im doubling") = DP2-16 (the in-in
operator-algebra identity A7–A12 is convention-fixed in App A since v1.7.104; the
−2Im doubling is stated via Hermiticity). Methodological-interpretation re-flag, not
a numeric error; independently, Li's Eq.(4.13) is written −2×2 Im (both orderings),
refuting the dropped-ordering story (changelog v1.7.89).

**Conclusion on the crux:** the orbit-double-counting claim is a source-cited re-flag
of DP2-01/-15/-16/-25 (Wick-permutation bookkeeping / basis convention / spurious
term / Cai-error trace), NOT a genuinely-new correct finding. The paper's convention
is the one that matches BOTH independent cross-checks (Li c_s=1 and the Table I
equilateral benchmark); ChatGPT's proposed convention fails both. The headline
−35/16 does not move under any orbit convention that is consistent with Li. **0
genuinely-new from this item.** No fabrication used to dismiss it — the dismissal is
carried by re-running the committed script and the convention-free Li formula.

---

## Per-finding disposition table

### EXT-ChatGPT M31 — REJECT (10 MAJOR / 2 MINOR)

| # | Sev | Finding (paraphrase) | D-id | Verdict | Source cite |
|---|-----|----------------------|------|---------|-------------|
| 1 | MAJOR | Orbit double-counts (5,2,2), −99/128 extra copy, redo four-way certification | DP2-01/-15/-16/-25 | NON-REAL re-flag (crux, see above) | `p2_vertex_check.py` (6-perms→−35/16=Li; distinct→−285/128≠Li); L713-714 Wick-perm map; eq:spurious L1475; App A L162 |
| 2 | MAJOR | Eq.(A4) uniquely fixes momentum dep; null-space (r=0.85±0.13) has no physical basis; recompute from single template | DP2-15 | NON-REAL re-flag | reparametrization/basis-measure caveat verbatim L966/L1032; stress-band never enters σ_eff §spherex L987 |
| 3 | MAJOR | Additive local-shape correction ≠ globally halving Cai shape; state one corrected polynomial | DP2-01/-03/-16 | NON-REAL re-flag | amplitude-invariant-shape-ratio disclosed L1025; "not a naive additive shift" L1556 (DP2-03) |
| 4 | MAJOR | Cubic-order transmission through bounce unsupported; δfNL≲10⁻³ an assumption not a bound | DP2-13/-32.6 | RE-FLAG-DISCLOSED (load-bearing caveat ★) | disclosed "verified only at linear order", conditional on dressed-metric quantization; conclusion L1448 / caveats-(ii) |
| 5 | MAJOR | No self-consistent underlying bounce model (Wilson-Ewing prescription/c_s mismatch) | DP2-13/-19/-32.6 | RE-FLAG-DISCLOSED | assumption (a) fixes c_s=1 quasi-dust benchmark §assumptions; deformed-algebra window flagged least-controlled (DP2-32.6) |
| 6 | MAJOR | Quasi-dust κ_ε≃2.8–40 + consistency relation prefactor-only, not from four in-in integrals | DP2-20 | RE-FLAG-DISCLOSED | κ_ε labeled single-prefactor-derivative estimate; fNL–n_s indicative |
| 7 | MAJOR | r=0.84 recast is not a survey projection; own Fisher gives r_eff≈0.99 not 0.84 | DP2-14/-17/-34 | RE-FLAG-DISCLOSED | reconciled §spherex L888/L892 (0.84=flat-weight cosine conservative headline; r_eff≈0.99=validation); channel-native α=0.992 DP2-34 |
| 8 | MAJOR | In-house Fisher (0.42–0.45) does not validate Heinrich (≈0.7); not like-for-like | DP2-22 | RE-FLAG-DISCLOSED | reproduction-vs-Heinrich limitation list disclosed §spherex L1045; labeled validation not independent forecast, abstract Scope L888 |
| 9 | MAJOR | Post-systematic σ not statistically defined; σ_GR added in quadrature; ρ transferred; 0.8/1.3/2.3σ shows prescription-dependence | DP2-04/-07/-26/-34/-35 | RE-FLAG (channel-native COMPUTED) | channel-native surrogate ρ≈−0.42, σ_marg≈0.94/2.32σ (c15, DP2-34/-35); proxy −0.868 retained as conservative cross-check strictly below computed floor |
| 10 | MAJOR | Bayes factors are prior-volume constructions (B≃W/(√2πσ)), not model comparisons; remove from abstract | DP2-18 | RE-FLAG-DISCLOSED | labeled "illustrative … not definitive model-selection evidence"; four-corner prior grid tab:bayes L1236 |
| 11 | MINOR | Observer-frame f_NL≃0.015 "on-sky" vs conformal-Fermi; factor-146 framing | DP2-21 | RE-FLAG-DISCLOSED | gauge-frame template-amplitude comparison disclosed; physical-frame confined to proper role (conclusion L1448) |
| 12 | MINOR | Data/code: mutable repo + future Zenodo; also shorten (birefringence appendix, response-letter register) | DP2-11/-27/-30 (PROCESS-NIT) + DP2-M1 | NON-REAL / PROCESS-NIT (no reset) | Zenodo pending-at-camera-ready disclosed; DAS real GitHub pointer (DP2-31.5); birefringence relegated to `app:birefringence` (DP2-M1.2); c9k/c9g already −35/16 (DP2-11) |

**ChatGPT −35/16 concession recorded verbatim:** "The value −35/16 may nevertheless
be correct—particularly because Li et al.'s independent formula gives it at c_s=1."
Central certification withstands direct challenge; REJECT rests on
survival-through-bounce (DP2-13) + forecast/venue scope (DP2-17/-29), both disclosed.
Structural harsh-referee floor (directive-H). **0 genuinely-new.**

### EXT-Grok M31 — MINOR REVISIONS (0 MAJOR / 6 MINOR)

| # | Finding (paraphrase) | D-id | Verdict | Source cite |
|---|----------------------|------|---------|-------------|
| 1 | Abstract presents 2.6–2.75σ / 1.3–2.75σ / 1.3–1.4σ envelopes as single range; endpoints not directly comparable | DP2-04/-07 | RE-FLAG-DISCLOSED | "scoping sensitivity envelope … not a joint-covariance forecast" abstract L892; "not directly comparable" L888 |
| 2 | Reproduce the corrected vertex-by-vertex monomial coefficients in the appendix (not only in code/json) | DP2-02/-27 | RE-FLAG-DISCLOSED / OPEN-hygiene | four-vertex algebra present tab:vertices L1482 + tab:vertexwalk L1505 + eq:order_grouped L1535; per-vertex print loop = DP2-27 non-blocking |
| 3 | Null-space 16–84 pct → 2.2–3.1σ propagation only in a footnote, not cross-ref'd in abstract/§IV | DP2-15/-14 | RE-FLAG-DISCLOSED | stress-band disclosed §spherex; noise-weighted r=0.84 only enters headline |
| 4 | Quantitative estimate of shift if b_2 marginalized / non-Gaussian covariance included would strengthen | DP2-22/-26 | RE-FLAG-DISCLOSED (OPEN-COMPUTE) | limitation list disclosed §spherex L1045; Cov_B external (DP2-26) |
| 5 | One-sentence abstract note that the lower edge remains a proxy-based floor pending public Cov_B | DP2-07/-33/-26 | RE-FLAG-DISCLOSED | proxy-floor + 0.8σ disclosure landed in abstract v1.7.112 (DP2-32.2/-33) |
| 6 | Presentation: dense internal file references, length; move code lists to Data Availability, condense | DP2-30/-M1 | PROCESS-NIT / presentation OPINION | DP2-M1 restructure actioned the class; residual length = venue/scope floor, Houston-gated |

**Grok central-claim credit recorded verbatim:** "The central claim—that the
corrected matter-bounce f_NL = −35/16 sets a realistic SPHEREx sensitivity target …
is supported by the explicit template-overlap calculation (r=0.84±0.02), independent
Fisher validation, conservative systematic budget, and analytic Bayes-factor formula
cross-checked by Monte Carlo ensembles." **0 genuinely-new.**

---

## Wave summary

- **Verdicts:** Grok = MINOR REVISIONS (0M/6m) · ChatGPT = REJECT (10M/2m), on
  byte-unchanged v1.7.116.
- **ledger_match:** Grok 6/6 → existing D-ids; ChatGPT 12/12 → existing D-ids. The
  crux (ChatGPT #1 orbit-double-counting) is a source-cited re-flag of
  DP2-01/-15/-16/-25, adjudicated by re-running the committed `p2_vertex_check.py`
  (6-perms→−35/16=Li; ChatGPT's "distinct" convention→−285/128≠Li) — the paper's
  convention is the one matching both independent cross-checks; the proposed fix is
  the one that fails them; the headline is unaffected regardless.
- **Genuinely-new count: 0.** No genuinely-new reader-visible editable finding on
  either leg.
- **Clean-wave streak: 12 → 13** (directive-K; thirteenth consecutive 0-genuinely-new
  wave on byte-unchanged v1.7.116).
- **No content bump; v1.7.116 stands; `directive_g.sh` NOT run** (no reader-visible
  edit warranted).
- **Integrity:** both raws read verbatim before any disposition (Grok l.1 `VERDICT:
  MINOR REVISIONS`, ChatGPT l.1 `VERDICT: REJECT`); no ACCEPT faked; every finding
  source-cited to a DP2 D-id + tex line / committed-script output; the crux was
  falsified by re-running the committed derivation + the convention-free Li formula,
  NOT by hand-waving or fabricated math; no version bumped; both reviewers' −35/16
  credit/concession quotes recorded verbatim.
