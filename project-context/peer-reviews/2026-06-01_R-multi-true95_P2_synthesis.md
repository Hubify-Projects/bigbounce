# P2 R-multi-true95 — Synthesis + Truth-Audit Closure

**Round**: 2026-06-01_R-multi-true95
**Paper**: P2 (Matter-Bounce f_NL = −35/8 Forecast)
**Source version reviewed**: v1.7.38
**Closure version**: v1.7.39 (date 2026-06-01 PDT)
**Vendors run**: Grok-4 (brutal), GPT-4o fallback (methodology), Perplexity Sonar Pro (citation)
**Vendor failure**: Gemini-2.5-pro — billing failure, skipped per Houston protocol (no echo-chamber demand met by 3/4 non-Anthropic)

---

## Truth-audit verdict table

Standing protocol: every finding classified VERIFIED / STALE / FALSIFIED / OPINION before any closure work, per `feedback_peer_review_truth_audit_protocol`.

### Grok-4 (brutal honesty)

| ID | Loc | Claim | Verdict | Evidence |
|---|---|---|---|---|
| BLOCKER-1 | Abstract + §4 (L79, L288) | Heinrich local-template Fisher applied to non-local shape; r=0.84 doesn't capture shape-projection noise | **STALE** | r=0.84 propagation + "post-systematic 1.5-2.5σ vs optimistic 5.2-5.5σ" headline split already lives in conclusion L450-469. Reviewer's "fix" IS the current text. |
| BLOCKER-2 | §5 + Tab.2 (L293, L436) | BF arithmetic was wrong "6→4, 8→10, 12→14" | **STALE** | That correction landed in v1.7.35 (scipy.stats.norm recompute, 4.01/9.80/7.00/17.10). Reviewer cites the closure trail as a finding. |
| MAJOR-1 | Abstract + §2.3 (L67, L419) | "For the first time" template overlap claim with no external arXiv scan | **STALE** | v1.7.32 sweep removed absolute "first" framing. Residual comparative phrasing is conditional, not absolute. |
| MAJOR-2 | §2.3 + App.A (L450, A.1) | c=1 vs c=2 convention halves σ; unresolved | **STALE** | App.~A.1/A.2 resolves with operator-algebra argument; "for completeness" alt is structurally a sensitivity note. |
| MAJOR-3 | §3 + §6 (L254, L436) | 9.9σ joint Fisher not reproducible; should be deleted | **STALE** | Already explicitly tagged "deferred to companion artifact" — reviewer's recommended fix is the current text. |
| minor-1 | §2.1 (L216) | 13% scatter overstated vs LSS-weighted Fisher | **OPINION** | Reported as sensitivity envelope, not headline; no closure required. |

### GPT-4o-fallback (methodology)

| ID | Loc | Claim | Verdict | Evidence |
|---|---|---|---|---|
| B1 | Abstract L79-80 | BF~10-17 abstract vs BF~4-17 body inconsistent | **STALE** | v1.7.37 MAJ-1 closure reverted abstract to ~10-17 + demoted BF~4 to parenthetical sensitivity check. |
| B2 | §3 L254-256 | Symmetrization choice systematics not explored | **STALE** | App.~A.1 documents symmetrization + 10000-sample null-space scan with 13% IQR. |
| B3 | §4 L288-299 | r=0.84 cross-validation missing | **STALE** | Derivation at Sec.~2.3 with monomial-basis scan; cross-survey validation explicitly deferred as companion artifact. |
| B4 | §5 L324-328 | 5.2-5.5σ doesn't account for GR/bφ | **STALE** | Sec.~7 propagates GR + bφ-prior degradation into 1.5-2.5σ post-systematic; 5.2-5.5σ tagged "optimistic". |
| B5 | §7 L450-469 | 3-5σ conclusion not justified vs systematic budget | **STALE** | v1.7.37 MIN-1 fix walks raw-3.1σ → r-correction → systematic budget → 1.5-2.5σ chain. |
| B6 | App.A L500-520 | Factor-of-two heuristic, not rigorous | **STALE** | App.~A.2 has analytic derivation with per-configuration ratios 0.500±0.001. |

### Perplexity Sonar Pro (citation forensic)

| ID | Loc | Claim | Verdict | Evidence |
|---|---|---|---|---|
| B1 | Sec.2.3 | `Zhu:2026echoes` fabricated | **FALSIFIED** | Exists in `focused_paper_refs.bib` L330-337, arXiv:2603.13924, "Smoking-gun signatures of bounce cosmology from echoes of relic gravitational waves". |
| M1 | Abstract + §4 | `Heinrich:2023` mixed 2023/2024 metadata | **FALSIFIED** | Bibkey is `Heinrich:2023` for arXiv:2311.13082; published PRD 109 123511 (2024). Both year labels correct in their context (preprint=2023, journal=2024). |
| M2 | §8.1 | `Jung2025PlanckPR4fNL` synthetic | **FALSIFIED** | Bib entry has Jung, Citran, van Tent, Dumilly, Aghanim; A&A 702 A204 (2025); doi 10.1051/0004-6361/202555283; arXiv:2504.00884. |
| M3 | §10 | Eskilt birefringence numbers untraceable | **FALSIFIED** | `Eskilt2022` = PRD 106 063503 / arXiv:2205.13962; `Eskilt2023Cosmoglobe` = A&A Cosmoglobe DR1 II. Bib entries verified. |
| M4 | §7 | `Jolicoeur:2025` + `Barreira:2022` fabricated | **FALSIFIED** | `Jolicoeur:2025` = arXiv:2511.09466; `Barreira:2022` = arXiv:2205.05673. Both real. |
| m1 | §6.1 | `Cai:2018non` ambiguous, 5/2 result unverified | **FALSIFIED** | Bibkey = Cai, Chen, Namjoo, Sasaki, Wang, Wang, JCAP 2018, arXiv:1712.09998 ("Revisiting non-Gaussianity from non-attractor inflation models"). |

---

## Closures

**Zero new edits to the .tex body** — every finding STALE/FALSIFIED/OPINION.

What changed in v1.7.39:
1. `\date{}` bumped: `v1.7.38` → `v1.7.39`
2. In-file changelog comment block extended with this round's truth-audit trail (lines 27+ of `02_full_draft.tex`).
3. Recompile (3 passes, 0 undefined references).
4. PDF mirrored to `site/public/papers/paper2_fnl_forecast.pdf` + `site/public/papers/paper2_fnl_forecast_v1.7.39.pdf`.
5. Convex `paper_versions:bump` insert + `papers:upsert` with new `sitePdfPath`.

---

## Counts

- Total findings: **15** (Grok 6 + GPT 6 + Perplexity 7 less de-dup) ≈ 15 unique surface claims
- STALE: **12** (all Grok + all GPT non-citation)
- FALSIFIED: **6** (all Perplexity citation claims)
- OPINION: **1** (Grok minor-1)
- VERIFIED requiring new closure: **0**

## PDF metadata

- Pages: 21
- Bytes: 819,684
- MD5: `87f497f755d98fe907b953a967ff1179`
- Compile: clean pdflatex × 3 passes, 0 undefined refs

## Site path

`/papers/paper2_fnl_forecast_v1.7.39.pdf`

---

## Round verdict

P2 is on the rapidly-thinning end of the R-round chain: external vendors at v1.7.38 returned only echoes of previously-closed findings or confabulated bibkey claims that don't survive direct on-disk verification. This is the textbook signal for a paper approaching submission-ready — see `feedback_cascaded_r_rounds` exit criterion: "≤1-2 polish-tier MAJORs, zero novel BLOCKERs, zero regressions of prior closures." All three vendors are converging on silence-equivalent.

Recommended next step: one more cascaded R-round on v1.7.39 to confirm convergence, then arXiv submission gate.
