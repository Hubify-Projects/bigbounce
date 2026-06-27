# R56 P4 — Truth Audit (HARDENED / de-biased re-review)

**Paper:** P4 — Survey-Scale Galaxy Chirality with Equivariant TTA (catalog-class)
**Source:** `pipelines/p2_chirality/chirality_catalog_paper.tex` (\paperVersion v1.0.190)
**PDF:** `/tmp/R56_P4/chirality_catalog_paper.pdf` (23 pp, 0 undef refs/citations, 0 overfull boxes)
**Standard:** uniform PRD/MNRAS bar; self-favoring reporting / unstated assumption / internal
inconsistency treated as a real finding (MINOR min, not OPINION). Calibration filter
(patterns 061–064) applied to exclude already-adjudicated / disclosed items.
**Method:** verdict-first per claim vs. source + own Opus full read; native-PDF vendor leg
(Anthropic Opus / OpenAI o3 / Grok 4) + Perplexity (quota-failed).

---

## Verdict-first summary

**Net: ACCEPT-class. No NEW verified findings. No fresh closeable self-favoring item under
the hardened bar.** The paper is internally consistent, numerically self-tying, and
exhaustively caveated across ~50 prior rounds. All prior-round + integrity fixes verified
intact and NOT re-opened.

---

## Integrity fixes — verified intact (not re-opened)

| Fix | Location | Status |
|-----|----------|--------|
| z=0.58 same-generator primary; z=0.70 independent re-impl disclosed | abstract L349; Sec.IV L606 | INTACT (2 sites) |
| +3.29σ [0.5,0.6) bin → −0.03σ at p_eq>0.6 (sample-purity ladder) | L702, L901 | INTACT |
| 37.77 % spiral sum-to-one (CW 18.78+CCW 18.99+NS 62.23=100.00; exact 37.774 %) | L521 | INTACT, arithmetic checks |
| Shamir factor ~5–12× (1.7 %–4.0 % / 0.32 %) | L366, L755; 0.46–0.56 % disclosed L711 | INTACT |
| +3.64σ moment-z / ≈1.9σ Gaussian-eq / +7.93σ 10⁴-perm / +7.28σ apodized | abstract, Table III, Sec.IV | INTACT, all cross-tied |
| 2√3 Fisher floor (σ(A)=√(3/N)=9.7e-4) | Eq.(fisher_floor) L730 | INTACT, reproduces |

Numeric self-consistency spot-checks (all pass): CW 1,592,107 + CCW 1,609,053 =
3,201,160 = N_spiral; f_CW = 1,592,107/3,201,160 = 0.49735 = Table cw_frac C row
0.497353(279); Dev. −9.47σ = text "−9.5σ" monopole; WLS mask-equiv 24,087 px both
branches; block-boot z=−18.1 (nside8) within disclosed −16.9/−18.4/−19.4 sweep.

---

## Hardened self-favoring sweep (the assigned focus)

Systematic search for OTHER "headline-the-more-favorable-number" choices beyond the
already-fixed z=0.58/0.70 item. For a NULL paper, "favorable" = lower significance /
larger exclusion factor / smaller residual.

| Candidate | Finding | Verdict |
|-----------|---------|---------|
| Real-space dipole headline +0.41σ (lowest of 0.41/0.55/0.58/0.70 family) | +0.41σ is the **declared** primary estimator (pixel-perm null, hierarchy row i, Sec.III.B); the full 0.55/0.58/0.70 range is disclosed in the same abstract/Sec.IV sentence with an explicit "not directly comparable" caveat | NOT self-favoring — declared + fully disclosed |
| WLS exclusion headline z≈−18 | =nside8 value (−18.4), the **middle** of the −16.9/−18.4/−19.4 sweep (could have headlined −19.4) | NOT self-favoring |
| Fisher floor 0.29 % (full N) vs 0.53 % (HC-broad N) | both disclosed; text explicitly directs reader to 0.53 % as "the appropriate Fisher reference for the A₅₀ comparison" | NOT self-favoring |
| 99.32 % monopole-mask reproduction | emphatically scoped "applies exclusively to pre-MASTER"; post-MASTER only ~12 % disclosed | NOT self-favoring |
| Harmonic completeness P(≥3σ)=0.92 @ A_p=0.5 % | labeled channel-specific, different null, "not interchangeable with real-space boundary" | NOT self-favoring |
| **Shamir ~5–12× factor uses 0.32 % (cleanest-partition) when global WLS best-fit=0.455 % A_p and slab maxima 0.46–0.56 %** | The headline factor in intro (L366) and parity (L755) is computed from the single most-favorable amplitude (0.32 %); 0.455 %/0.56 % give the less-favorable ~3–9×. **BORDERLINE self-favoring.** BUT already adjudicated at R35conf (R35-P4-O17), which required + added the 0.46–0.56 % disclosure at L711; reader can reconstruct the less-favorable factor; the comparison is heavily hedged ("we do *not* claim a frequentist exclusion; matched Ganalyzer reanalysis required") | **Already-disclosed + already-adjudicated → not a fresh MINOR; not re-opened** (re-raising would itself trip the calibration filter on adjudicated items) |

**Conclusion of sweep:** the integrity audit's z=0.58/0.70 catch was the substantive
self-favoring item; it is fixed. The one remaining borderline framing (0.32 % Shamir factor)
is already disclosed in-body and was adjudicated in a prior round — reported here for
transparency, not re-opened.

---

## Deferred / future-work items (all TRULY-BLOCKED, honestly disclosed — none closeable in a text review)

- 1000-MC cross-spectrum rerun (currently 200-MC, ℓ=2 r=−0.65) — compute, disclosed L697.
- Matched-footprint Ganalyzer reanalysis — needs Shamir's pipeline; correctly stated as
  required for a likelihood-level exclusion, no exclusion over-claimed.
- Zenodo DOI — at submission (skipped per mandate).
- Axis-ratio cross-match for edge-on quantitative penalty — needs external catalog.
- Finer-grid A₉₅ recovery curve — A₉₅∈(1.0 %,1.5 %] bracketed, correctly labeled "not measured".

No fabrication, no hidden estimator, no undisclosed assumption found. The 3.05σ hemisphere
max (p_LEE≤1e-4) is honestly disclosed as significant-but-systematics-attributed, not buried.

---

## Legs

1. **Compile:** pdflatex ×4 (embedded thebibliography, no bibtex), 0 undef refs/citations,
   23 pp; only warning is cosmetic font-shape `OT1/cmr/bx/sc`.
2. **Own Opus read:** full 1232-line source, verdict-first per major claim — above.
3. **Vendor native-PDF leg:** Anthropic Opus / OpenAI o3 / Grok 4 dispatched on the 33 MB PDF;
   Perplexity quota-failed (401 insufficient_quota). See `R56_P4_<vendor>.md`.
4. **Overflow audit:** 0 overfull hboxes on recompile ×3.

## Vendor-leg adjudication (hardened, verdict-first)

3 native-PDF reviewers returned (Anthropic file not emitted; Perplexity quota-failed).
All three headline "MAJOR REVISIONS" verdicts dissolve under audit:

| Vendor finding | Verdict |
|----------------|---------|
| Gemini P4-E1 "June 26 2026 / commit 53b41d12 are future-date placeholders → reproducibility MAJOR" | **FALSE POSITIVE** — 2026-06-26 is the actual current date; hash is real. Vendor lacks date context. |
| OpenAI + Gemini "Zenodo DOI not minted → MAJOR" | **TRULY-BLOCKED (DOI)** — excluded per mandate; paper correctly states DOI at submission + interim release tag. Not closeable now. |
| Grok E1/E2 "σ-mixing caveat appears only once; later juxtapositions omit it" | **FALSIFIED** — the "distinct null procedures, not directly comparable" caveat is repeated in abstract (×2), Results intro L516, Table I & III captions, and Figs sky_map/confidence_dist/raw_vs_eq/multipoles (Pattern2 closures, v1.0.185→186). Claim is factually wrong. |
| Grok M1 / Gemini M1 / OpenAI "condense further" | **OPINION** — already cut 54pp→23pp per external mandate. |
| OpenAI P4-M7 "rank-8 vs condition-number 4.5e16 inconsistency" | **FALSE POSITIVE** — a rank-8 (singular) 9-template design has ~infinite condition number; 4.5e16 is its float manifestation; text explains it + gives leg-drop cond=1.2e4. Consistent. |
| OpenAI "pLEE ≤ 1e-4 → < 1e-4 (resolution-limited); avoid 'rejection'" | polish-tier MINOR; resolution floor 1/(N+1)≈1e-4 already disclosed in Table III caption. Not self-favoring, not numerical error. |
| OpenAI "Catalog-B N / slab-σ baseline / edge-on basis" | polish-tier clarity nits on a non-cosmological tier; already largely disclosed. |

**Key cross-check for the assigned focus:** the most adversarial reviewer (Grok) flagged
σ-*presentation*, NOT a hidden favorable-number choice — and its specific claim is false.
No vendor surfaced a second self-favoring number-choice. This corroborates the Opus finding:
z=0.58/0.70 was the self-favoring item, it is fixed, and no other exists. No source edit
made this round (editing for the false-date / false σ-caveat findings would itself be a
false-positive closure, forbidden by mandate).

## Convergence statement

P4 has converged under the hardened de-biased standard: integrity fixes intact, no NEW
verified findings, no fresh self-favoring item beyond the one already-disclosed/adjudicated
0.32 % framing. Remaining open items are genuinely compute/data-blocked and honestly
labeled. Recommend P4 remains at its prior readiness; no source change warranted this round.
