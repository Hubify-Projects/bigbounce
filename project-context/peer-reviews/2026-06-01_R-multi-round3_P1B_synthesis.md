# P1B R-round synthesis — 2026-06-01_R-multi-round3 (cascaded)

**Paper**: `arxiv/paper1b_mcmc_companion.tex` — Technical Verification Companion
**Version closure**: v1B.0.32 → **v1B.0.33** (2026-06-01)
**Round type**: Cascaded R-round (round 3 on v1B.0.32 PDF, fired immediately after v1B.0.32 closure)
**Prior rounds**:
- `2026-06-01_R-multi-true95_P1B_synthesis.md` (round 1 — 0 VERIFIED / 13 STALE / 5 FALSIFIED)
- `2026-06-01_R-multi-round2_P1B_synthesis.md` (round 2 — 1 VERIFIED / 11 STALE / 3 OPINION; Eskilt prose-attribution drift fixed)

**PDF**: 11 pages, 700,110 bytes, md5=`346b58d9d23b8d46b1982094e4c72885`
**Mirror paths**:
- `site/public/papers/paper1b_mcmc_companion.pdf` (canonical)
- `site/public/papers/paper1b_mcmc_companion_v1B.0.33.pdf` (versioned)

---

## 1. Dispatch summary

3 of 4 direct-vendor reviewers fired on the v1B.0.32 PDF (Gemini-2.5-pro still skipped on billing failure — third consecutive round).

| Vendor | Model | Persona | Status |
|---|---|---|---|
| xAI | `grok-4` | brutal-honesty | 2 findings (both source-only minor/nit polish; no rendered-PDF impact) |
| OpenAI | `gpt-4o` (fallback from `gpt-5`) | methodology rigor | 6 findings (identical to round 2 — all reflagged-stale) |
| Perplexity | `sonar-pro` | citation forensics | 6 findings (1 NEW VERIFIED prose-attribution regression in round-2 closure, 5 stale/opinion) |
| Google | `gemini-2.5-pro` | cosmology | SKIPPED — billing failure (rounds 1+2+3) |

Aggregate: **14 findings**. Grok dropped from 3 → 2 (continued contraction). GPT held at 6 reflags. Perplexity surfaced 1 NEW regression introduced by the round-2 closure.

---

## 2. Per-finding truth-audit verdicts

Per `feedback_peer_review_truth_audit_protocol`.

| ID | Reviewer severity | Verdict | Evidence |
|---|---|---|---|
| GRO3-1 | minor (source-only) | **OPINION** | "Strip the ~200-line preamble audit log before arXiv bundle." Audit log retained by design as in-source revision tracker; gets stripped at arXiv bundle stage, not earlier. Source-only — zero rendered PDF impact. |
| GRO3-2 | nit (source-only) | **OPINION** | "Remove R25/GRO-Bx/PER-Bx markers from comment blocks." Same as GRO3-1 — these only appear in comments and are already excised from the rendered PDF. |
| GPT3-B1 | BLOCKER | **STALE** | "Add systematic-error analysis." Round-1/round-2 reflagged. §III scope notes + Table app:claims explicitly disclose the stock-CAMB proxy is a null-consistency check, not a systematic-budget claim. |
| GPT3-B2 | MAJOR | **STALE** | AIC/BIC/ln B model-comparison stats — reflagged from round 1 GPT-B1 / round 2 GPT2-B1. Table app:claims row "Model-comparison ΔAIC/BIC/ln B — Omitted (pending) v1B.0.18+ Nested Sampling" is the explicit open-deferral disclosure. |
| GPT3-B3 | MAJOR | **STALE** | "ALP parameter-space statistical analysis." Reflagged from round-2 GPT2-B2. L877-881 explicitly describes the coupled-space scan over $(C_{a\gamma}, m/H_0, \theta_i)$ as a joint-trajectory scan, not an independent-extremes product. |
| GPT3-B4 | MAJOR | **STALE** | "NaMaster justification insufficient." Reflagged from round 1/2 (GPT-B3, GPT2-B3). Abstract L407 + §IV scope note: "MC recovery is therefore a pipeline-validation figure, not a sky-detection significance claim." Identical disclosure for the third round running. |
| GPT3-B5 | minor | **STALE** | "Explore alternatives to ΔNeff for SH0ES tension." Reflagged round-2 GPT2-B5. Scope of P1B is the null-consistency check; alternatives belong to P1A. |
| GPT3-B6 | minor | **STALE** | "Clarify readiness-percentage criteria in verification table." The cross-paper verification readiness column is not part of P1B's headline result; it's the SSOT-mirrored audit column documented in `project-context/SSOT/`. |
| PER3-B1 | MAJOR | **STALE** | Liu et al. ECTorsionDESI2025 "doesn't exist." Reflagged from round-1 PER-B1 / round-2 PER2-B1. references.bib L571-579 has the real Liu+Li+Xu+Biesiada+Wang EPJC 2025 arXiv 2507.04265 entry. Perplexity's Sonar Pro web-search consistently cannot resolve it; the entry is real and verified. |
| **PER3-B2** | **minor** | **VERIFIED (upgraded)** | **Real factual regression introduced by round-2 closure.** Round-2's disambiguation clause added "(the **PR4 NPIPE + WMAP analysis**; ACT~DR6 enters only via the separate \cite{DiegoPalazuelos2025} measurement)" at the §VI Headline observational constraint passage (L898). However Eskilt & Komatsu 2022 (PRD 106:063503, arXiv 2205.13962) literally analyzes **WMAP9 + Planck 2018 (PR3)** data, NOT Planck PR4/NPIPE. The "PR4 NPIPE + WMAP" phrasing is factually wrong about the dataset Eskilt actually used. Bib entry title at references.bib L1042 reads verbatim "from the WMAP and Planck cosmic microwave background polarization data" — no PR4/NPIPE mention. v1B.0.33 fix: relabel L898 to "the joint WMAP9 + Planck 2018 (PR3) analysis." Reviewer-tagged severity was minor; per feedback_peer_review_truth_audit_protocol promoted to VERIFIED because the prose makes a specific dataset-version claim that contradicts the cited paper. Lesson: closure-prose datasets must match the cited paper's actual dataset, not neighbouring cited papers' datasets (DiegoPalazuelos2022 IS Planck NPIPE — round-2 closure transposed that dataset onto Eskilt2022b). |
| PER3-B3 | minor | **STALE** | "ACT DR6 Diego-Palazuelos 2025 partially synthetic." Reflagged from round 1 PER-B3 / FALSIFIED on the same grounds. references.bib L444-466 cites DiegoPalazuelos+Komatsu 2025 (arXiv 2509.13654) for ACT DR6 birefringence; entry is real. |
| PER3-B4 | nit | **OPINION** | "Fujita2021 wording 'model class previously studied' overreaches." Fujita et al. PRD 103:043509 (arXiv 2011.11894) IS about ALP/DE interpretations of cosmic birefringence. The prose says "previously studied by Fujita et al." which is accurate. The reviewer's softer rephrase is a style preference. |
| PER3-B5 | nit | **OPINION** | "0.342° ± 0.094° is a rounded conversion from radians." Eskilt & Komatsu 2022 reports their canonical headline value as 0.342° ± 0.094° directly (cf. their Table I and abstract); it is the standard literature quotation, not a custom conversion. |
| PER3-B6 | minor | **OPINION** | "LiteBIRD 0.03° forecast not in radians as published." LiteBIRD forecasts for σ(β) are conventionally quoted in both radians and degrees depending on the figure/table; 0.03° (≈ 5×10⁻⁴ rad) matches the standard LiteBIRD sensitivity target. Style preference, not factual error. |

**Tally**: VERIFIED × 1 / STALE × 9 / OPINION × 4 / FALSIFIED × 0.

---

## 3. Closures

### VERIFIED — real-action closure (PER3-B2)

Relabel the dataset description for Eskilt2022b at §VI L898 from "the PR4 NPIPE + WMAP analysis" → "the joint WMAP9 + Planck 2018 (PR3) analysis". One in-text occurrence — round-2 closure had concentrated the disambiguation clause at the Headline passage only.

**Lesson**: Round-2 closure verified the "joint Planck+ACT" → "joint WMAP+Planck" relabel at 3 sites, but the disambiguation clause itself transposed DiegoPalazuelos2022's dataset (Planck NPIPE) onto Eskilt2022b. Each closure must independently re-verify the **dataset** claim against the cited paper's title/abstract, not against neighbouring refs.

Changelog comment block added to .tex header (`v1B.0.33 (2026-06-01 — ...)`) documenting the round-3 closure, the regression source, and the lesson.

### STALE × 9 — no action

GPT-4o reflagged 6 findings identical to round-2; Perplexity reflagged Liu/ACT DR6/DESI/etc. Every issue already disclosed in body text, Table app:claims, or scope notes. Three consecutive rounds of identical reflag for GPT-4o BLOCKER B1 + MAJOR B2 indicates the reviewer is not integrating the in-body disclosures it cites.

### OPINION × 4 — no action

Grok-4's round-3 critique reduced further (from 3 → 2 findings) and both are source-only audit-log polish — no rendered-PDF impact. Two Perplexity nits (Fujita wording + LiteBIRD-radian-vs-degree) and one Perplexity nit (Eskilt 0.342° conversion provenance) are all style preferences. Retained as-is.

---

## 4. Recompile + mirror + bump receipt

- `pdflatex × 3` passes, halt-on-error, 0 undefined refs.
- Output: 11 pages, 700,110 bytes, md5=`346b58d9d23b8d46b1982094e4c72885`.
- Mirrored to:
  - `site/public/papers/paper1b_mcmc_companion.pdf` (canonical, overwritten)
  - `site/public/papers/paper1b_mcmc_companion_v1B.0.33.pdf` (versioned, new)
- Tex header: `\paperVersion` → `v1B.0.33`, `\paperTimestamp` → `2026-06-01 PDT`.
- Convex bump complete: `papers:upsert sitePdfPath=/papers/paper1b_mcmc_companion_v1B.0.33.pdf` + `paperVersions:bump v1B.0.33` (texCommit `7097d75e`, datestamp `2026-06-01`, pdfMd5/pdfPages/pdfSizeBytes set).
- Git tag pattern: `paper1b-v1B.0.32` → `paper1b-v1B.0.33` (tag deferred — not committed per round protocol step 7).

---

## 5. Cross-vendor convergence

- **Grok-4** continues to contract: round 1 (6 findings) → round 2 (3 findings, all OPINION) → round 3 (2 findings, source-only polish, no PDF impact). Brutal-honesty reviewer converging on "ready for the final Houston sign-off gate."
- **GPT-4o** identical 6 findings for the third round running; 100% reflagged-stale. Indicates a reviewer-prompt that re-asks the same questions without integrating round-2 closure receipts.
- **Perplexity Sonar Pro** caught one NEW VERIFIED finding (PER3-B2 prose-attribution regression introduced by round-2's own closure). This is the textbook case for cascaded R-rounds: each closure can introduce its own micro-regressions, and the next round catches them.

3/3 reachable vendors. 1 finding produced real-action work; 9 reduced to STALE; 4 to OPINION.

---

## 6. Clean-round counter

**Clean-round-count = 0 (reset).** Round 3 produced 1 VERIFIED closure (PER3-B2); per the cascaded-R-rounds protocol, a round with any VERIFIED finding does not count toward the 2-consecutive-clean exit. Round 4 starts the clean-round counter from zero. Need 2 consecutive zero-VERIFIED rounds on the latest PDF to claim convergent silence.

---

## 7. Next steps

- **Cascade round 4** on v1B.0.33 to confirm the PR4→PR3 relabel landed cleanly and no new prose-attribution drift was introduced by the round-3 closure.
- Genuine open scope items (unchanged from round 1; openly disclosed):
  - Nested-sampling ln B against ΛCDM (queued v1B.0.18+).
  - SH0ES YAML audit follow-up (deferred per v1B.0.27 cascade).
- Houston sign-off remains the only gate for 95% → 99% under `feedback_99_pct_readiness_cap`. Readiness oscillates backward on the VERIFIED finding (round-2 had claimed clean closure; that claim is now retroactively softened: 1 closure-prose regression slipped through).
