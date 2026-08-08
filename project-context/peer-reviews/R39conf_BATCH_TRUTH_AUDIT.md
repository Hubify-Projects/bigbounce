# R39conf Batch Truth-Audit (all 6 papers, one Opus pass)

**Date:** 2026-06-13 PDT
**Round:** R39conf (v3 native-PDF cross-vendor)
**Vendors landed:** Perplexity_citations, Grok_brutal, Gemini_cosmology, OpenAI_methodology (4/5)
**Claude_brutal:** FAILED all 6 (Anthropic credit). Round flagged DEGRADED per pattern-009 — does NOT count toward clean-round counter, but 4-vendor findings are admissible.
**Auditor:** Opus 4.7 (judgment); Sonnet sub-agents will close on the per-paper edit list.

## Verdict schema

- **VERIFIED** — finding maps to real text in the .tex; closure required
- **PARTIAL** — partially correct (e.g., reviewer caught one of two instances)
- **OPINION** — stylistic / journal-policy preference, no factual error
- **STALE** — reviewer cites a number/text already changed in current source
- **FALSIFIED** — auto-rule (HD-*, F0 Fisher, P5 k=20, 2√3, June 2026 date, pattern-052 OCR re-raises)
- **HOUSTON-DECISION** — auto-rules to DO-NOW per Houston standing 2026-06-12

Standing auto-falsify (no closure work): June 2026 date is correct (not future); `(in preparation)` companion phrasing under audit (see cross-paper resolution); pattern-052 re-raises are STALE-OCR; F₀ Fisher form already 8×-verified; P5 k=20 6×-falsified; 2√3 P4 rederived-correct.

---

## THREE cross-paper pattern resolutions (load-bearing)

### Pattern 1 — `companion` (P1A, P1B, P2, P5)

**Resolution policy (auto-applied across all 6 .tex):**

For every `\cite{Golden2026P{1b,2,3,4}}` instance, classify by what the citation supports:

| Use class | Action | Wording template |
|-----------|--------|------------------|
| (a) Number is load-bearing for a numerical claim in THIS paper | INLINE the fact + acknowledge non-public companion | "MCMC chains (Cobaya configs in supplementary, results to be detailed separately) give $H_0 = …$" — number stays, "companion" framing dropped from the sentence |
| (b) Number is contextual / not load-bearing | REPLACE with public-literature anchor or REMOVE the precise quote | "values consistent with Planck 2018 $\Lambda$CDM" (Gemini P1A-m3 pattern) |
| (c) Methodology pointer (NaMaster pipeline, MCMC infrastructure) | KEEP as "(in preparation)" + repo-link via `\artifact{}` macro, drop "companion" honorific | "the NaMaster pipeline validation (in preparation; see \artifact{pipelines/.../p1b\_namaster/})" |

**Canonical edit (P1A line 681–705 region, applies to all instances):**

OLD: `multi-tracer SPHEREx Fisher forecast is presented in a companion work in preparation~\cite{Golden2026P2}`
NEW: `multi-tracer SPHEREx Fisher forecast (in preparation, \cite{Golden2026P2}; methodology and results to be detailed separately)` — drops "companion work" honorific (Perplexity P1A-E2 explicit fix); keep citation for forward-compatibility with arXiv posting order.

**Table IV "Verified Value" column rename** (OpenAI P1A-m5, P1B Table IV): rename column heading to `Reference value` and add per-row footnote citing public source where one exists; remove rows whose only provenance is unpublished companion. This is the largest single closure unlocking ACCEPT verdict shift on P1A from OpenAI + Gemini + Perplexity simultaneously.

### Pattern 2 — `sigma_mixing` (P1A, P2, P4, P5)

**Canonical text for the universal caveat** (insert at every juxtaposition where σ-values from different null procedures appear within ~3 sentences of each other):

> *Note: the σ values quoted in this paragraph (abstract / panel / row) arise from distinct null procedures — see [Section / Table] — and are not directly comparable as detection significances; they are diagnostic indicators only.*

**Per-paper anchor edits:**

- **P4 abstract (line 328 region):** Add the caveat immediately after `…+7.93σ; both are systematics-attributed diagnostics from different null-run sizes, not two independent detection claims.` — extend it to cover the `+0.41σ (moment-z) … robust under per-galaxy label-shuffle null, z = 0.70` juxtaposition that opens the abstract (Grok P4-E1). One sentence: `The +0.41σ (moment-z, isotropic-bootstrap null) and z = 0.70 (label-shuffle null) values use distinct null constructions and are diagnostic-only, not directly comparable.`
- **P4 §VII.c (line ~14 conclusions):** Same caveat at the `+3.64σ / +7.93σ` juxtaposition (OpenAI P4-E4).
- **P4 Fig 4, 6, 7, 9 captions:** Append one-line `(σ values across panels use different null procedures; see text.)` (OpenAI P1A-M11 analog, P4-N5, P4-N8, P4-M9).
- **P1A Fig 4, Fig 6 captions:** Same one-line note (OpenAI P1A-M11).
- **P2 §IV (naive 6.25σ vs template-corrected 5.2–5.5σ):** Add "not directly comparable" tag (OpenAI P2-n2).
- **P5 §V, Fig 5, Table V:** Label `σ_from_half` (counting) vs `σ_vs_monopole` (residual) explicitly at every co-occurrence; one-line caption note (OpenAI P5-M2).

### Pattern 3 — `audit_artifact` (P1A, P1B, P3, P4, P5)

**Grep-and-strip tokens** (apply across all 6 .tex bodies; do NOT touch `%` comments):

```
v1A\.0\.\d+ | v1B\.0\.\d+ | v3\.1\.\d+ | v1\.0\.\d+   # version stamps in body
— v[0-9]+\.[0-9]+\.[0-9]+                              # "— v1A.0.71" dash-version
PDT — v                                                # date-block versioning
\\artifact\{[^}]*\.json\}                              # artifact-JSON paths in body
superseded | Path-C rebuild | gate-PASS | gate-FAIL    # P3 specific
FB103-1 | EXT[0-9]+ | R[0-9]+conf                      # tracker labels in body
"An earlier run reported" | "An earlier rendering"     # P4 process logs
"closure-wave" | "closes the … ask"                    # process language
"in-tex v.*stamp" | "spin_torsion.input.yaml"          # P1B
"pipelines/p[0-9]_.*\.json"                            # P3, P4, P5 paths
quarantined (in main-text figs)                        # P3 Fig 2 (keep in appendix only)
"canonical canonical" | "0/7/8" typos                   # P5, P1A
```

**Title-block fix (applies to P1A, P1B, P3, P4, P5):**
OLD: `(Dated: June 13, 2026 PDT — v1A.0.71)` → NEW: `(Dated: June 13, 2026)`
(Strip everything after the date; the version tag is in `version.json` not the PDF.)

**P3-specific (line 612, 649, 668-676, etc.):** Replace "Path-C rebuild / native re-score / before/after diagnostic" prose in main text with neutral "primary methodology / verification baseline"; keep the operational detail in Appendix B only. Move all `\artifact{…json}` URLs from main-text into a single Data Availability appendix listing.

**P4-specific:** Strip footnote 1 ("An earlier run reported 0.43σ ... selection-filter defect") and Fig 8 caption "earlier rendering" mention (OpenAI P4-M3). These were truth-audit closure notes that should never have left the .tex comment block.

**P5-specific:** Strip the `pipelines/p5_desi_chirality/outputs/17_v0151…` literal paths from §VI prose (OpenAI P5-E6); harmonize "97.8% / 97.9%" stale-number drift (P5-N7).

---

## Per-paper sections

### P1A (51 findings → triage)

**Counts:**
- VERIFIED: 9 (E1 version tag, E2 internal artifacts, E4 Pontryagin notation, E5 Holst theorem citation, E7 appendix cross-ref errors, M3 dim-+1 operator caveat sharpening, M11 caption σ-caveat, M12 derivation line, m4 appendix label)
- PARTIAL: 4 (companion items: E1/E2/M5/M13 all collapse to one cross-paper fix → see Pattern 1)
- OPINION: 18 (most NIT-level typography, AI-acknowledgment, length judgments, KSVZ/DFSZ reference inserts)
- STALE: 6 (M1 ρ_Λ arithmetic — already 8×-FALSIFIED on F₀; m10 LQC "no free parameters" — already softened; M14 Levi-Civita convention — declared in v1A.0.66 audit)
- FALSIFIED: 3 (pattern-052 OCR on "0/7/8", future-date, in-prep-companion-illegitimate)
- HOUSTON-DECISION: 11 (every ESSENTIAL not yet covered → DO-NOW; includes E3 Zenodo DOI, E6 RG running β-function, E8 ϑNY normalization, E9 reduced vs unreduced M_Pl, M8 13-barriers independence)

**Closure plan (concrete edits):**

1. **Title block:** `\date{June 13, 2026}` — strip `— v1A.0.71`. (1 line, P1A-E1 + Perplexity P1A-E1)
2. **Companion citations sweep (Pattern 1):** apply (a)/(b)/(c) policy table; Table IV column rename + 2 unsupported rows removed. (~30 lines)
3. **σ-mixing caption sweep (Pattern 2):** insert one-line note in Fig 4, Fig 6 captions. (2 lines)
4. **Appendix cross-ref audit (E7, m6):** find/replace "Appendix B" → "Appendix A" wherever the parameter summary is meant; sed-driven. (~6 sites)
5. **Notation (E4 Pontryagin, M14 Levi-Civita, m7 γ vs γ_PTA):** add notation table at top of §II.A.2 declaring εμνρσ-as-symbol vs as-tensor convention once. (8-line insertion + 6 site fixes)
6. **Date + Zenodo DOI placeholder (E3):** finalize the "DOI inserted at submission" string with actual Zenodo DOI before submission; not a closure item until mint. Add commit-hash pin in Data Availability NOW (Sonnet can do).
7. **M3 dim-+1 operator framing:** strengthen the existing "on-shell scaling ansatz" caveat to a boxed disclaimer (1 paragraph).
8. **M8 "13 logically-independent constraints":** soften to "13 distinct barriers" in abstract + add 1-paragraph independence sketch in §IX. (4-line abstract change + 1 paragraph)
9. **M9 NJL "cosmologically relevant":** reword to "even at dense ISM-like n_ψ ~ 10^2 cm^-3" (1 sentence).
10. **m11 Fig 3 caption internal path:** strip "see generate_all_figures.py" (1 line).

**Path to ACCEPT (P1A):** Items 1, 2, 3, 4, 5, 8, 10 — minimum 7 edits → all four reviewers' ESSENTIAL/MAJOR move to ACCEPT-with-minor. ~50 lines diff total. The companion sweep (item 2) is the biggest unlock — 3-reviewer consensus collapses immediately.

---

### P1B (38 findings → triage)

**Counts:**
- VERIFIED: 7 (E1 frozen DOI, E2 versioning audit tags, E3/E4 release-pairing apples-to-apples, E5 "systematic floor" terminology, E6 Ωa definition missing, E7 abstract process language, N1 future-date)
- PARTIAL: 3 (M7/m10 Planck likelihood interface — companion truth that the v1B.0.59 patch already partially addressed)
- OPINION: 13 (most "n" findings — axis units, hyphenation, terminology preferences)
- STALE: 4 (M1 ℓ-range, M2 ALP ODE — already documented in v1B.0.68 supplement; n6 floor-vs-bound — partially addressed)
- FALSIFIED: 2 (pattern-052 OCR re-raises on β-conventions; June 2026 date)
- HOUSTON-DECISION: 9 (E8 ALP likelihood-to-Ωa H0 marginalization; M3/M4/M5/M6 coupling benchmarks + estimator comparability + rotation-periodicity + MASTER bin-zero treatment → DO-NOW)

**Closure plan (concrete edits):**

1. **Title block:** strip `— v1B.0.68` from `\date{}`. (1 line)
2. **Strip internal versioning prose (E2):** find "in-tex v1B.0.68 stamp", "entry for the v1B.0.59 closure wave", "Column-permutation warning for JSON artifacts" — replace with neutral data-availability prose. (~10 sites)
3. **Companion citations sweep (Pattern 1):** apply Pattern-1 (a)/(b)/(c) policy. (~8 sites)
4. **Ωa definition (E6) — load-bearing:** Add subsection in §VI or Appendix C giving explicit V(ϕ) = m²f_a²[1 − cos(ϕ/fa)], onset of oscillations criterion (3H = m), and the integration from sampled (m_a, θ_i, f_a) to ρ_a(z=0). (~1 page; Sonnet can draft from Cobaya configs)
5. **Release-pairing transparency (E3/E4):** acknowledge low-ℓ + lensing differences explicitly in §V.B "independent re-run" prose; either re-run (overkill) or add explicit caveat. (Caveat-only: 2 sentences.)
6. **"Systematic floor" → "observed pipeline bias" (E5/n6):** sed across §IV + Conclusions. (~6 sites)
7. **Future-date + commit-hash pin:** already addressed in item 1; add explicit commit hash in Data Availability.
8. **ALP likelihood H0 fix-vs-marginalize (E8):** Add 2-sentence clarification that Ω_a uses the same fixed H0 = 67.7 as the Cobaya posterior mean, and quote the 1σ shift if H0 were marginalized (deferred-acceptable with explicit "fixed at posterior mean" note).

**Path to ACCEPT (P1B):** Items 1, 2, 3, 5, 6, 7 → 6 edits, ~25 lines diff. Item 4 (Ωa derivation) is the biggest single-paper closure — moves Grok's M1 + OpenAI's E6 to ACCEPT. Plan to land item 4 in same commit as items 1–3 for one-bump close.

---

### P2 (24 findings → triage)

**Counts:**
- VERIFIED: 5 (E1 squeezed-limit ratio sign-error, E2 Bayes-factor narrow-prior inconsistency, E5 Eq. (7) "quadrature" mis-citation, M6 k notation, M7 r heterogeneity)
- PARTIAL: 2 (E4 systematic budget, M1 σ_GR calibration — partially addressed in v0.151 prose)
- OPINION: 8 (most "n" findings + length compression)
- STALE: 2 (Table II BF entries — last recomputed but reviewer cites old draft; M9 abstract vs Tables labeling)
- FALSIFIED: 1 (June 2026)
- HOUSTON-DECISION: 6 (E3 Zenodo DOI, E4 systematic-budget-tied-to-covariance, M1 σ_GR survey-calibration, M2 shot-noise reconciliation, M3 Bayes-factor closed-form, M8 KSW noise-cov definition)

**Closure plan (concrete edits):**

1. **E1 squeezed-limit sign:** Fix `x3 ≡ k3/k1 → 0` to `x ≡ k1/k3 → 0` (or redefine ordering) — 1-line correction, no figure change. (P2-E1)
2. **E2 Bayes-factor narrow-prior recompute (Table III):** Recompute B = W/(√(2π)σ_eff) for σ_GR ∈ {0, 0.5, 1.0} with consistent σ_eff; update Table III + Table II footnote. (~6 numbers + 1-paragraph derivation insert)
3. **E5 Eq. (7) "quadrature" mis-citation:** Replace abstract + Table IV caption "Eq. 7's quadrature convention" with "the additive-quadrature systematic budget defined in §VII"; insert one-line definition in §VII. (~3 sites)
4. **M6 k notation:** Define k explicitly at first squeezed-limit statement: `…take k1/k → 0, with k ≡ k2 ≈ k3`. (1 line)
5. **m10 "105 → 10^5":** Find all `105-realization` → `$10^5$-realization`. (~6 sites)
6. **n4 "illustrative only" tag on MegaMapper 3–7σ:** Insert in abstract. (1 phrase)
7. **Title block + Zenodo DOI:** strip version, add commit-hash pin.

**Path to ACCEPT (P2):** Items 1, 2, 3, 4, 5, 7. Item 2 is the biggest unlock (OpenAI E2 ACCEPT shift). ~20 lines diff. P2 is the smallest closure package — likely to be the first ACCEPT-flipping commit.

---

### P3 (47 findings → triage)

**Counts:**
- VERIFIED: 11 (E1 F₀ formula 1/8.98 vs 1/8.98²; E2 Cramér's V missing sqrt; E3 αˆ² typo; E5/E8 Table I Ntotal + 58.8% inconsistency; E6 FB103-1/EXT9 jargon; E7 artifact-path in main text; E9 dust-correlation p-value; E10 quarantined ACT in Fig 2; M9 SDSS classification rules; N1 "canonical canonical" typo)
- PARTIAL: 5 (M3 c=0.0747 derivation — already in artifact log, needs main-text exposure; M4 SIMBAD radius standardization — partially documented; M6 Planck top-200 train-set; M11 DESI training spectra; M12 latitude unit-of-analysis)
- OPINION: 14 (length compression, NIT typesetting)
- STALE: 7 (E2 abstract drift on 17.8% novelty — partially closed; M4 "largest-scale" — already softened; m1 exponent formatting — patched in v3.1.103; pattern-045 ABSTRACT-LAST DRIFT already-closed instances)
- FALSIFIED: 4 (June 2026; F₀ form 8×-verified; HD-* re-raises; pattern-052 OCR on Cramér's V)
- HOUSTON-DECISION: 6 (E4 Zenodo DOI, M1 random-coincidence derivation, M2 Landy-Szalay details, M7 largest-claim quantification, M8 train/test leakage NEOWISE+Gaia, M10 BF prior-robustness)

**Closure plan (concrete edits):**

1. **E1 F₀ formula correction (FALSIFIED on principle — already verified 8x):** Reviewer is reading display string `1/8.98^2 = 0.01239` and stripping the exponent. Add explicit parenthesis: `F₀ = 1/(8.98)² = 0.01239` — typesetting fix only. (1 line, §V.b)
2. **E2 Cramér's V (genuine arithmetic):** Add the square root visibly: `Cramér's V = √[χ²/(N·(k-1))] = √[376,713/(378,280 × 24,047)] ≈ 0.0064` (corrects 0.020 → 0.0064). (1 numeric, 1 formula)
3. **E3 αˆ² display typo:** Replace `max(0, 0.19² − 0.65²) = 0` for clarity. (1 line)
4. **E5/E8 Table I Ntotal & 58.8% disclosure:** Adjust the Total-row footnote to make explicit that the 58.8% is from a separate pooled exercise, NOT from the cross-transfer Total set. Add `^¶ 58.8% from §IV.A pooled top-100 exercise; not the cross-transfer Total denominator.` (1 footnote)
5. **E6/E7 audit_artifact strip (Pattern 3):** Remove "FB103-1 / EXT9", "Path-C rebuild", "before/after diagnostic", "gate-PASS/FAIL", every `\artifact{…json}` from main text → push to Appendix B "Data Availability". (~25 site edits; Sonnet sub-agent task)
6. **E9 dust-correlation p-value (genuine):** Recompute t = r√(n-2) and report consistent p; if per-pixel n=24049, p ≈ 0.35 not 0.21. Quick recompute + 1-line correction. (1 numeric)
7. **E10 quarantined ACT in Fig 2:** Either (a) remove ACT points from Fig 2 main text, OR (b) move Fig 2 to Appendix. Prefer (a). (1 figure regen — Sonnet can edit the matplotlib script.)
8. **M9 SDSS classification rules:** Add deterministic rule set to Appendix (per-arm thresholds, line windows, precedence). (~1/2 page; Houston has the rules in pipeline yaml — Sonnet ports.)
9. **N1 "canonical canonical-mask" duplicate:** sed fix. (1 site)
10. **Title block:** strip `v3.1.105` from `\date{}`. (1 line)

**Path to ACCEPT (P3):** Items 1, 2, 3, 4, 5, 6, 7, 9, 10. Item 5 is the dominant edit (resolves Grok's E1 ESSENTIAL + OpenAI's E6/E7 essentials + many "n" findings about file paths). ~40 lines diff for items 1-4 + 9-10, plus ~25 sed-driven removals for item 5. P3 has the most rote work but is straightforward.

---

### P4 (33 findings → triage)

**Counts:**
- VERIFIED: 8 (E1 version/provenance inconsistency v1.0.185 vs v1.0.180, E2 artifact paths in body, E4 σ-mixing in §VII.c, E5 training-set 80/20 arithmetic, E6 release-tag mismatch, M8 abstract σ-juxtaposition, M3 earlier-run prose, N1 hyphenation glitches)
- PARTIAL: 4 (E3 Zenodo DOI; M7 +6.48σ artifact citation; M9 axis-averaged Fig 9; M10 6-12× factor explicit basis)
- OPINION: 7 (length, AI ack, formatting)
- STALE: 3 (M2 hemisphere LEE double-correction — already addressed in v1.0.183 audit; M5 65.7% edge-on; M6 SHA256 mask audit)
- FALSIFIED: 4 (2√3 P4 rederived-correct; June 2026; HD-* all DO-NOW already-ruled; "+6.48σ" claim — verified in artifact log)
- HOUSTON-DECISION: 7 (E3 Zenodo, E4 abstract σ-mixing, E5 training arithmetic, M1 A_p units, M2 LEE single-correction, M4 Fig 9 single-value, M10 6-12× explicit anchors)

**Closure plan (concrete edits):**

1. **Title-block + version unification (E1, E6):** Strip `— v1.0.185` from `\date{}`; harmonize Data Availability commit-pin to single version (commit `53b41d12` at v1.0.185). (3 sites)
2. **σ-mixing abstract caveat (E4, M8 — Pattern 2 canonical):** Insert canonical-caveat sentence in abstract at the `+3.64σ … +7.28σ` juxtaposition AND at `+0.41σ … z=0.70` juxtaposition. (2 sentences)
3. **σ-mixing §VII.c caveat (E4):** Same one-liner. (1 sentence)
4. **σ-mixing figure caption notes (N5, N8):** Fig 4, 7, 9 — append `(σ values use distinct null procedures; see text.)`. (3 captions)
5. **E2 artifact strip (Pattern 3):** Strip footnote 1 "An earlier run reported 0.43σ...", Fig 8 "earlier rendering" mention, all `artifact pipelines/p2_chirality/...` strings from main-text → Data Availability appendix. (~15 sites)
6. **E5 training arithmetic reconciliation:** Walk the 25,790 → 26,616 augmentation math; either correct narrative (preferred: state 20,467 pre-aug + 5,323 val + 826 flip-augs in train) or restate as approximate. (1 paragraph)
7. **M1 A_p units uniformity:** Replace "0.57% (A_p-unit)" → "A_p = 0.0057 (= 0.57%)" — uniform with §IV.C. (1 site)
8. **M2 LEE single-correction:** Drop the additional Bonferroni/BH layer; report only the direct-MC p_LEE. (1 paragraph)
9. **M4 Fig 9 single observed-σ value:** Use 7.28 throughout; move 7.21 to a footnote `(matched to a different MC-realization count; both within MC stat error)`. (1 caption + 1 footnote)
10. **M10 factor 6–12 anchors:** Add inline citation `(comparing pipeline best-fit 0.32% WLS to Shamir 1.7% upper / 4.0% maximum amplitudes)`. (1 sentence)

**Path to ACCEPT (P4):** Items 1, 2, 3, 4, 5, 7, 8, 9, 10. Items 2-4 (Pattern 2 sigma_mixing canonical fix) move Grok+OpenAI ESSENTIAL → ACCEPT in one pass. Item 5 is the biggest standalone unlock. ~45 lines diff. P4 has the cleanest path because the abstract sigma_mixing fix is a 2-sentence insert.

---

### P5 (43 findings → triage)

**Counts:**
- VERIFIED: 8 (E1 Paper-IV monopole dependency, E2 duplicate-TARGETID χ², E3 LEE only 1000 perms, E4 V-Web vs T-Web naming, E5 RSD correction not propagated, E6 internal paths in prose, E10 Bonferroni one-sided vs two-sided sign-error, E11 χ[Mpc]·h unit error)
- PARTIAL: 5 (E7 Rs=10 below grid — partial: bins flagged but not removed; E8/E9 duplicate-TID propagation through nulls; M1 bright/dark systematic error budget; M4 deduplication systematic)
- OPINION: 11 (length, sigma label preferences, axis units)
- STALE: 7 (k=20 — 6×-FALSIFIED; companion-monopole — partially addressed in v0.151 prose; M6 Table VII arithmetic — already audited and matches CSV in latest commit; M7 wall % typo — already harmonized; N1 σ_from_half units; N2/N3/N7 stale numbers from older draft)
- FALSIFIED: 5 (k=20 6×-falsified; pattern-052 OCR; June 2026; P4-dependency caveat now standard; HD-* pre-ruled)
- HOUSTON-DECISION: 7 (E1 Paper-IV cross-paper coordination, E5 RSD bound, E10 Bonferroni two-sided recompute, E11 unit-fix propagation through all coordinates, M3 contingency-table inclusion, M8 numeric comparison to Ullah+2026 and Zapata+2026)

**Closure plan (concrete edits):**

1. **Title block:** strip version from `\date{}`. (1 line)
2. **Pattern 1 companion fix (E1, E3 — Grok + Gemini consensus + OpenAI E1):** Reproduce the Δf_CW = −0.0026 monopole measurement inside P5 from the now-public P4 catalog (publication coordination: P5 must lag P4 by ≥1 day on arXiv submission OR P5 must internally compute the monopole from the released catalog). Concrete edit: Add §V.A "Monopole self-calibration" inserting the 1-paragraph self-calibration with the CW/CCW classification count → Δf_CW recomputed in-paper. (~1/2 page; not deferred — Sonnet can draft from the public P4 CSV.)
3. **Pattern 3 audit-artifact strip (E6):** Strip `pipelines/p5_desi_chirality/outputs/17_v0151…` style paths from prose → Data Availability. (~12 sites)
4. **E10 Bonferroni two-sided recompute (genuine math error):** All 4 thresholds (3.09, 4.05, 2.58, 2.77) need recompute as `|σ| = √2 erfc⁻¹(α/2K)`: 3.26, 4.15, 2.81, 2.94. Update §V.A + every downstream "Bonferroni-K" reference. (~8 sites; numeric only)
5. **E11 χ unit fix (genuine error):** `χ[h⁻¹ Mpc] = χ[Mpc] / h` not `× h`. The "sanity value χ(0.2) = 570" is wrong — true value ≈ 1246. ALL Cartesian X, Y, Z coordinates downstream may need recompute. THIS IS LOAD-BEARING — flagged for Houston review. If the actual pipeline uses the correct unit and only the .tex footnote is wrong, single-line fix. If the pipeline used the wrong unit, recompute all environment classifications. Action: GREP pipeline code for the h-conversion; if pipeline is correct, fix .tex only.
6. **E2 duplicate-TARGETID χ²:** Replace the headline χ² = 3.55 (N=812,793) with the deduplicated χ² (N=783,820). Recompute p-value. Same fix in abstract. (3 sites)
7. **E3 LEE → ≥10,000 permutations:** Re-run with 10k permutations OR round p to two decimals + report MC SE. Prefer re-run for ACCEPT verdict. (Sonnet can dispatch the perm sweep on existing artifact.)
8. **E4 V-Web → T-Web naming:** Global sed `V-Web → T-Web (density-Hessian)`, with one-sentence disclaimer in §IV. (~15 sites)
9. **σ-mixing label fix (M2 — Pattern 2):** Label `σ_from_half` (counting) vs `σ_vs_monopole` (residual) at every co-occurrence. (~10 sites)

**Path to ACCEPT (P5):** Items 1, 2, 3, 4, 6, 8, 9 are mechanical. Item 5 (χ unit) requires Houston judgment on whether the pipeline used the correct or incorrect convention. Item 7 (10k LEE re-run) is the largest compute item but is a single dispatch. ~70 lines diff + 1 dispatch. P5 has the heaviest closure load — item 5 alone could trigger a major recompute if the pipeline is wrong.

---

## Aggregate Path-to-ACCEPT summary

| Paper | Findings | VERIFIED | Min edits | Biggest unlock | Risk |
|-------|----------|----------|-----------|----------------|------|
| P1A | 51 | 9 | ~10 sites, ~50 lines | Companion sweep (Pattern 1) collapses 3-reviewer consensus | Low |
| P1B | 38 | 7 | ~8 sites, ~25 lines + 1/2-page Ωa | Ωa derivation (E6) | Low |
| P2  | 24 | 5 | ~7 sites, ~20 lines | Bayes-factor recompute (E2) | Low — smallest delta |
| P3  | 47 | 11 | ~25 sites, ~40 lines | audit_artifact strip (Pattern 3, ~25 sed) | Low — rote |
| P4  | 33 | 8 | ~10 sites, ~45 lines | sigma_mixing abstract caveat (Pattern 2, 2 sentences) | Low |
| P5  | 43 | 8 | ~20 sites, ~70 lines + LEE re-run + Houston unit-call | Bonferroni two-sided + χ unit (E10/E11) | **MEDIUM** — E11 may force pipeline recompute |

---

## Pattern-052 OCR re-raises detected

- **P3 E1:** "F₀ = 1/8.982 = 0.01239" — reviewer OCR'd `8.98^2` as `8.982`. Already 8×-FALSIFIED in archive. Closure = typesetting only (add explicit parens).
- **P3 E2:** Cramér's V — reviewer read the formula correctly this time (genuine missing-sqrt typo), NOT pattern-052. Genuine VERIFIED.
- **P5 multiple:** k=20 6×-FALSIFIED auto-rule applies to any "k=20 grid" re-raise (none in R39conf — confirmed).

## Recommendation: fire closures NOW vs wait for EXT10

**FIRE NOW for Pattern 1 + Pattern 2 + Pattern 3 cross-paper sweeps.** These are exactly the items EXT10 will re-raise verbatim (all three patterns hit 3+ reviewers across 3+ papers — vintage external-reviewer ammunition). Closing them before EXT10 lands maximizes ACCEPT-shift probability:

1. **Pattern 3 (audit_artifact) — fire immediately** (Sonnet sub-agent, all 6 papers, ~2hr): mechanical sed sweep, zero judgment, blocks no other work, makes every paper render cleaner for EXT10 readers.
2. **Pattern 1 (companion) — fire immediately on P1A, P1B, P5; coordinate publication order so P4 lands before P5** (Sonnet, ~3hr): three-reviewer consensus collapses on P1A alone.
3. **Pattern 2 (sigma_mixing) — fire immediately on P4, P5, P1A, P2** (Sonnet, ~1hr): 2-sentence inserts; one batch commit.
4. **Per-paper genuine arithmetic/numeric fixes (P2 E2, P3 E1/E2/E3/E9, P5 E10/E11, P1A m1):** fire immediately (Sonnet, ~2hr).
5. **HOUSTON-DECISION items requiring judgment:** P5 E11 χ unit (pipeline-vs-tex), P5 E5 RSD bound, P1B E6 Ωa subsection content, P2 E2 Bayes-factor formula derivation — single Opus pass after Sonnet lands the mechanical sweeps.

**Wait for EXT10 on:** Length-compression items (Grok P3-M1, P4-M1, P5-M1, Gemini P5-M1) — wait to see if EXT10 echoes; otherwise OPINION. AI-tool acknowledgment items — journal policy decision pending. Zenodo DOI minting — done at submission, no closure work now.

## Confidence on 1-more-cycle to 18/18 ACCEPT (5 vendors × 6 papers, Claude_brutal restored)

**HIGH (≥85%) for P1A, P1B, P2, P3, P4** after the closures above land and Claude_brutal credit is restored. The pattern-driven closures resolve the 3-paper-consensus findings; remaining items are OPINION-class or per-paper polish.

**MEDIUM (~60-70%) for P5** because E11 χ unit fix may force a pipeline recompute that changes downstream classifications — if so, P5 lags by ~2-3 days for verification. If E11 is .tex-only (pipeline correct), P5 joins HIGH.

Net: one more cross-vendor round after fire-now closures is high-probability 18/18 ACCEPT (or 17/18 with P5 lagging). Conditional on Claude_brutal returning admissible findings, which historically over-call ESSENTIAL by ~2x — budget 1 more round to absorb its delta.
