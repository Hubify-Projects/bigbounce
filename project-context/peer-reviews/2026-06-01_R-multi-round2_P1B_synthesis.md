# P1B R-round synthesis — 2026-06-01_R-multi-round2 (cascaded)

**Paper**: `arxiv/paper1b_mcmc_companion.tex` — Technical Verification Companion
**Version closure**: v1B.0.31 → **v1B.0.32** (2026-06-01)
**Round type**: Cascaded R-round (round 2 on v1B.0.31 PDF, fired immediately after v1B.0.31 closure)
**Prior round**: `2026-06-01_R-multi-true95_P1B_synthesis.md` (clean — 13 STALE / 5 FALSIFIED / 0 VERIFIED)
**PDF**: 11 pages, 700,068 bytes, md5=`7fe91ba2698fbd82995a8290d3df62b3`
**Mirror paths**:
- `site/public/papers/paper1b_mcmc_companion.pdf` (canonical)
- `site/public/papers/paper1b_mcmc_companion_v1B.0.32.pdf` (versioned)

---

## 1. Dispatch summary

3 of 4 attempted direct-vendor reviewers re-fired on the v1B.0.31 PDF (no OpenRouter; Gemini-2.5-pro still skipped on billing failure per round 1).

| Vendor | Model | Persona | Status |
|---|---|---|---|
| xAI | `grok-4` | brutal-honesty | 3 findings (all minor/nit polish, redundancy removal) |
| OpenAI | `gpt-4o` (fallback from `gpt-5`) | methodology rigor | 6 findings (1 BLOCKER reflagged, 2 MAJOR reflagged, 3 minor reflagged) |
| Perplexity | `sonar-pro` | citation forensics | 6 findings (1 BLOCKER, 3 MAJOR, 2 minor) |
| Google | `gemini-2.5-pro` | cosmology | SKIPPED — billing failure (consistent with round 1) |

Aggregate: **15 findings** (Grok shrank from 6 → 3 between rounds, indicating prior round closures landed; GPT and Perplexity held steady at 6).

---

## 2. Per-finding truth-audit verdicts

Per `feedback_peer_review_truth_audit_protocol`.

| ID | Reviewer severity | Verdict | Evidence |
|---|---|---|---|
| GRO2-1 | minor | **OPINION** | Redundant NaMaster scope disclaimer (abstract L298-301 + §IV L668-673). Reviewer requests one-instance condensation. Retained intentionally (in-cell caveat visibility per v1B.0.27 cascade rule). |
| GRO2-2 | nit | **OPINION** | Same as GRO2-1 for fn:wcaveat + Table iter2_posterior caption. Reviewer requests footnote-only cross-ref. Retained for the same in-cell-visibility rule. |
| GRO2-3 | nit | **OPINION** | "ALP not distinctive ECH" stated in abstract L305-306 + §VI L778-784. Reviewer requests abstract-only. Retained for cross-section reader reliability. |
| GPT2-B1 | BLOCKER | **STALE** | Same as round-1 GPT-B1 ("compute Bayes factor or claim is unsupported"). Table app:claims still lists model-comparison ΔAIC/BIC/ln B as `Omitted (pending) v1B.0.18+ Nested Sampling`; explicitly disclosed deferral. |
| GPT2-B2 | MAJOR | **STALE** | ALP β-range methodology (joint-trajectory scan). Body L877-881 already describes the coupled-space scan explicitly: "joint-trajectory scan over the *coupled* $(C_{a\gamma}, m/H_0, \theta_i)$ space and not from an independent-extremes product". |
| GPT2-B3 | MAJOR | **STALE** | Same as round-1 GPT-B3 / GRO-B4 (NaMaster pipeline-validation scope). Abstract + §IV scope note already say verbatim "pipeline-validation figure, not a sky-detection significance claim". |
| GPT2-B4 | minor | **STALE** | Model-comparison stats omission. Already disclosed; Table app:claims row. |
| GPT2-B5 | minor | **STALE** | SH0ES tension + ΔNeff interaction. §V already provides chi-square decomposition by likelihood; ΔNeff impact is reported via H0 posterior shift table. |
| GPT2-B6 | minor | **STALE** | Abstract quantitative context for ΔNeff conclusion. Abstract already gives chi-square delta numerics in §V. |
| PER2-B1 | BLOCKER | **STALE** | Reflagged from round-1 PER-B1 (Liu et al. ECTorsionDESI2025 confabulation). `references.bib` L571-579 still resolves to real Liu+Li+Xu+Biesiada+Wang EPJC 2025 arXiv 2507.04265 entry. Sonar Pro's web-search continues to miss it; entry is real. |
| **PER2-M1** | **MAJOR** | **VERIFIED** | **Real factual error.** `references.bib` L1040-1052 Eskilt2022b title literally reads "from the **WMAP** and **Planck** cosmic microwave background polarization data" — ACT is NOT part of the cited dataset. Prose at L370-371 (abstract), L779-780 (§VI body), L854-855 (§VI Headline) said "joint Planck+ACT value" attributed to `\cite{Eskilt2022b}`. Round 1 had marked this FALSIFIED on bib-existence grounds (entry resolves), but round-2 sharper truth-audit upgrades the verdict because the prose attribution is wrong even though the cite-key resolves. **Bib-resolves ≠ prose-correctly-attributes; both must be checked.** |
| PER2-M2 | MAJOR | **STALE** | ALP MCMC 9,720 samples internal-vs-published framing. L898 already says verbatim "our internal model-independent MCMC fit ... 9,720 accepted samples". Framing is explicit. |
| PER2-M3 | MAJOR | **STALE** | β_combined = 0.241° ± 0.061° (3.9σ) "not tied to literature method". L883 already labels the equation "Summary-likelihood combination (auxiliary cross-check)"; L890-892 states "neglects shared calibration systematics; the published joint analysis at 3.6σ is the headline". |
| PER2-m1 | minor | **STALE** | DESI DR1/DR2 mixing. Round-1 PER-B5 FALSIFIED still holds. Bibkeys DESI2024 (DR1) and DESI2025DR2 (DR2 arXiv 2503.14738) are distinct, cited at distinct locations matching the data release each section uses. |
| PER2-m2 | minor | **STALE** | Riess year mismatch. Round-1 PER-B5 already addressed. "H0.riess2020Mb" is the cobaya YAML alias name, not a bibkey; the actual bibtex cite is `\cite{Riess2022}`. |

**Tally**: VERIFIED × 1 / STALE × 11 / OPINION × 3 / FALSIFIED × 0.

---

## 3. Closures

### VERIFIED — real-action closure (PER2-M1)

Relabel "joint Planck+ACT value" → "joint WMAP+Planck value" wherever attributed to `\cite{Eskilt2022b}`. Three sites fixed:

1. **Abstract L370-371** — `joint Planck+ACT value → joint WMAP+Planck value`.
2. **§IV body L779-780** — `For β=0.342° (the published joint Planck+ACT value)` → `For β=0.342° (the published joint WMAP+Planck value~\cite{Eskilt2022b})`. Inline cite added for traceability.
3. **§VI Headline observational constraint L854-855** — Replaced with full disambiguation: *"the published Eskilt~\&~Komatsu joint WMAP+Planck value $\beta=0.342°\pm 0.094°$ ($3.6\sigma$)~\cite{Eskilt2022b} (the PR4 NPIPE + WMAP analysis; ACT~DR6 enters only via the separate $\beta=0.215°\pm 0.074°$ measurement~\cite{DiegoPalazuelos2025}, used below only in the auxiliary inverse-variance combination)"*. This kills the ambiguity at the most-cited location.

Remaining "Planck/ACT DR6" mentions at L366, L411, L739, L1052 cite both Eskilt2022 AND DiegoPalazuelos2025 jointly — combined-literature-landscape shorthand, not Eskilt-alone attribution. Left as-is.

Changelog comment block in tex header documents the fix and the lesson (bib-resolves ≠ prose-correctly-attributes).

### STALE × 11 — no action

Every issue already disclosed in body text, Table app:claims, footnotes, or scope notes. Round-1 cascade addressed the same critiques; reviewers re-fired the same prompts and re-surfaced the same issues without integrating the round-1 disclosures.

### OPINION × 3 — no action

Grok-4's round-2 critique reduced to redundancy-removal preferences (1-of-3 disclosure sites versus all three). The paper deliberately repeats key caveats across abstract + §IV body + §VI body per v1B.0.27 cascade rule "in-cell caveat visibility wins on misread-prevention even at the cost of prose elegance". Houston's call to retain.

---

## 4. Recompile + mirror + bump receipt

- `pdflatex × 3` passes, halt-on-error, 0 undefined refs, 11 pages, 700,068 bytes, md5=`7fe91ba2698fbd82995a8290d3df62b3`.
- Mirrored to:
  - `site/public/papers/paper1b_mcmc_companion.pdf`
  - `site/public/papers/paper1b_mcmc_companion_v1B.0.32.pdf`
- Tex header: `\paperVersion` → `v1B.0.32`, `\paperTimestamp` → `2026-06-01 PDT`.
- Convex bump pending: `papers:upsert sitePdfPath=paper1b_mcmc_companion_v1B.0.32.pdf` + `paperVersions:bump v1B.0.32`. Bigbounce MCP tools not loaded in this triage thread; bump deferred to next bundled-commit step (per protocol step 7, do not commit here).

---

## 5. Cross-vendor convergence

- **Grok-4** halved its finding count (6→3) and all 3 are polish-tier OPINION — strong signal that round-1 closures landed.
- **GPT-4o** identical 6 findings; near-100% reflagged-stale. Indicates the reviewer is reading the v1B.0.31 PDF but not the in-body disclosures it explicitly cites.
- **Perplexity Sonar Pro** shifted from 4 MAJOR (round 1) → 3 MAJOR + 1 BLOCKER (round 2). The new BLOCKER is the same Liu et al. confabulation, escalated. **One genuine VERIFIED finding** (Eskilt dataset mislabel) was the round-2 yield — a prose-attribution drift round 1 missed because it audited only bib-key existence, not prose-attribution correctness.

3/3 reachable vendors. 1 finding produced real-action work; 11 reduced to STALE; 3 to OPINION.

---

## 6. Clean-round counter

**Clean-round-count = 0 (reset).** This round produced 1 VERIFIED closure; per the cascaded-R-rounds protocol, a round with any VERIFIED finding does not count toward the 2-consecutive-clean exit (AGENT_RULES §4.4.1). Next round (round 3) starts the clean-round counter from zero. Need 2 consecutive zero-VERIFIED rounds to claim convergent silence.

---

## 7. Next steps

- **Cascade round 3** on v1B.0.32 to confirm the Eskilt relabel landed cleanly and no new prose-attribution drift was introduced.
- Genuine open scope items (already openly disclosed, not new; unchanged from round 1):
  - Nested-sampling ln B against ΛCDM (queued v1B.0.15+).
  - SH0ES YAML audit follow-up (deferred per v1B.0.27 cascade).
- Houston sign-off remains the only gate for 95% → 99% under `feedback_99_pct_readiness_cap`. Readiness oscillates backward on the VERIFIED finding (round 1 had claimed "no body edits required" — that claim is now retroactively softened: 1 prose-attribution drift slipped through).
