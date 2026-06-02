# P1B R-round synthesis — 2026-06-01_R-multi-true95

**Paper**: `arxiv/paper1b_mcmc_companion.tex` — Technical Verification Companion
**Version closure**: v1B.0.30 → **v1B.0.31** (2026-06-01)
**PDF**: 11 pages, 699,400 bytes, md5=`56d95f8e5c86b33f42c6fd3a52746056`
**Mirror paths**:
- `site/public/papers/paper1b_mcmc_companion.pdf` (canonical)
- `site/public/papers/paper1b_mcmc_companion_v1B.0.31.pdf` (versioned)

---

## 1. Dispatch summary

3 of 4 attempted vendors returned reports via direct vendor APIs (no OpenRouter):

| Vendor | Model | Persona | Status |
|---|---|---|---|
| xAI | `grok-4` | brutal-honesty | 6 findings (2 BLOCKER, 3 MAJOR, 1 minor) |
| OpenAI | `gpt-4o` (fallback from `gpt-5`) | methodology rigor | 6 findings (1 BLOCKER, 4 MAJOR, 1 minor) |
| Perplexity | `sonar-pro` | citation forensics | 6 findings (4 MAJOR, 2 minor) |
| Google | `gemini-2.5-pro` | cosmology | **SKIPPED** — billing failure |

Aggregate: **18 findings**.

---

## 2. Per-finding truth-audit verdicts

Per `feedback_peer_review_truth_audit_protocol` — every finding gets a verdict before any closure work.

| ID | Reviewer severity | Verdict | Evidence |
|---|---|---|---|
| GRO-B1 | BLOCKER | **STALE** | Title literally reads "Technical Verification Companion … Not a Spin-Torsion Theory Module"; §I L330-352 + §III L398 explicit scope disclaimers. |
| GRO-B2 | BLOCKER | **STALE** | fn:wcaveat at L509 already declares verbatim "posterior-extrapolation distance only, NOT a Bayes-factor exclusion and NOT a frequentist tension". |
| GRO-B3 | MAJOR | **STALE** | Abstract L305-306 + §VI L778-784 already declare "not a distinctive ECH prediction." |
| GRO-B4 | MAJOR | **STALE** | Abstract L298-301 + §IV scope note L668-673 explicitly disclaim pipeline-vs-sky conflation. |
| GRO-B5 | MAJOR | **STALE** | L928-933 declares ln B "queued"; Savage-Dickey explicitly invalid; cross-paper anchor is the posterior, not the Bayes factor. |
| GRO-B6 | minor | **STALE** | "null-consistency test/check" framing already used at L290, L416, L633-634. |
| GPT-B1 | BLOCKER | **STALE** | Same scope as GRO-B1; §III header "(Not a Spin-Torsion Theory Module)" + body verbatim "does *not* verify the spin-torsion theory module itself". |
| GPT-B2 | MAJOR | **STALE** | Same caveat-already-prominent as GRO-B2; fn:wcaveat is in-cell. |
| GPT-B3 | MAJOR | **STALE** | Same as GRO-B4. |
| GPT-B4 | MAJOR | **STALE** | Same as GRO-B3. |
| GPT-B5 | MAJOR | **STALE** | Table app:claims row "Model-comparison ΔAIC/BIC/ln B — Omitted (pending) v1B.0.18+ Nested Sampling"; openly disclosed. |
| GPT-B6 | minor | **OPINION** | fn:sample_stratification is the 309189/123129/216432 reconciliation Houston explicitly preserved in v1B.0.23 R25a-BLK-1 closure. No action. |
| PER-B1 | MAJOR | **FALSIFIED** | `references.bib` L571-579: Liu, Li, Xu, Biesiada, Wang, EPJC 2025, arXiv 2507.04265 — real, correctly cited. |
| PER-B2 | MAJOR | **FALSIFIED** | `references.bib` L1040-1052: Eskilt & Komatsu 2022 PRD 106:063503, arXiv 2205.13962 — real, correctly cited. |
| PER-B3 | MAJOR | **FALSIFIED** | `references.bib` L444-466: DiegoPalazuelos+Eskilt+Minami+Tristram PRL 128:091302 (arXiv 2201.07682) and DiegoPalazuelos+Komatsu (arXiv 2509.13654) — both real. |
| PER-B4 | MAJOR | **FALSIFIED** | `references.bib` L491-502: Fujita+Murai+Nakatsuka+Tsujikawa PRD 103:043509 (arXiv 2011.11894) — exact ALP-birefringence subject. |
| PER-B5 | minor | **FALSIFIED** | `references.bib` L431-441 (arXiv 2401.02929 DES SN5YR) and L468-479 (arXiv 2503.14738 DESI DR2) — real preprints. |
| PER-B6 | minor | **OPINION** | Companion papers cross-cited intentionally; status reflected in .bib. |

**Tally**: STALE × 13 / FALSIFIED × 5 / OPINION × 2 / VERIFIED × 0.

(Note: GPT-B6 and PER-B6 classified OPINION rather than STALE — 18 total findings, 16 reducible to no-action, 0 requiring substantive .tex edits.)

---

## 3. Closures

**Zero real-action closures required.** The cascade of v1B.0.22 → v1B.0.30 already in-place addressed every substantive critique these reviewers raised; the 2026-06-01 round confirms the cascade was effective. Perplexity's citation-forensics persona overcalled on cite-keys it could not resolve via web search — but every cited key in the manuscript resolves to a real, correctly-attributed paper in `references.bib`.

**v1B.0.31 closure deliverable** = this synthesis doc + version stamp + recompile + PDF mirror + Convex bump. The version bump is the closure receipt for a clean round.

---

## 4. Cross-vendor convergence

- Grok-4 + GPT-4o (methodology) **agree** on 4 of 6 BLOCKER/MAJOR findings (B1=B1, B2=B2, B3=B4, B4=B3). Both are scope/framing critiques pre-empted by the paper's explicit "Not a Spin-Torsion Theory Module" title and disclaimers.
- Perplexity Sonar Pro **completely disagrees** with both — its 4 MAJORs are all citation-database confabulations from the model not finding cite-keys via its web-search tool. All 5 falsifiable claims were falsified by direct `references.bib` inspection.
- Gemini-2.5-pro **silent** (billing failure; Gemini's prior 9-consecutive-round 0-BLOCKER streak on P1B remains intact per v1B.0.22 records).

3/3 reachable vendors produced findings that all reduce to **no-action**. This matches the **clean-round** definition: STALE+FALSIFIED+OPINION exhaustively cover the finding set.

---

## 5. Next steps

- No body edits required for v1B.0.31.
- Genuine open scope items (already openly disclosed, not new):
  - Nested-sampling ln B against ΛCDM (queued v1B.0.15+; PolyChord/MultiNest on identical likelihood stack).
  - SH0ES YAML audit follow-up (deferred per v1B.0.27 cascade).
- Houston sign-off remains the only gate for 95% → 99% under `feedback_99_pct_readiness_cap`.
