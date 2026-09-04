# A3M v3M.0.8 R3 — API legs board (Grok + Gemini)

**Round:** `ROUND_2026-09-04-A3M-v3M.0.8-EXACTPDF-8cf429e0-R3`
**PDF bound:** `research/track_a3_multichannel/paper/main.pdf` (byte-identical to
`site/public/papers/a3_multichannel_arxiv_v3M.0.8.pdf`)
**sha256:** `8cf429e002d44c97308ccc994c9378a93b066e094de865d48f850d5e72291b9a`
**Pages:** 10
**Preflight receipt:** `project-context/peer-reviews/INT_v3/ROUND_2026-09-04-A3M-v3M.0.8-EXACTPDF-8cf429e0-R3/preflight_receipt.json`
(verdict PASS, core_sha256 `fcc0c901fca52a75a65512e20b26ae58cc6c206253352aa9cfb228a5e7ad0d82`,
bound to HEAD `8d5ca7c8c611b341b86d89a7e91aed8a071e941e`; no commits occurred
between receipt mint and both legs saving raws)
**Dispatch:** `python3 tools/v3_native_pdf_review.py research/track_a3_multichannel/paper/main.pdf
ROUND_2026-09-04-A3M-v3M.0.8-EXACTPDF-8cf429e0-R3 A3M "R3 API legs, v3M.0.8, science-gate closures integrated"`
with `V3_REVIEWERS=Gemini_cosmology,Grok_brutal` (OpenAI/Codex paused per
directive N; Anthropic API not used — Codex/OpenAI routes remain disabled in
the script itself). Result: **2/2 reviewers OK**, 0 "Reviewer call FAILED" in
either raw (checked by grep).
**Venue binding:** Physical Review D, regular article, review_profile
PRD-REGULAR (from `project-context/SSOT/paper-a3m/status.md`), de-biased
referee prompt from `tools/v3_native_pdf_review.py` (Gemini_cosmology /
Grok_brutal personas, same prompt template used for the v3M.0.4/0.5 R1/R2
boards).

## Per-leg verdicts (read from raw text, not labels)

| Leg | Model | Verdict word (leg's own text) | ESSENTIAL | MAJOR | MINOR | NIT | Raw path |
|---|---|---|---|---|---|---|---|
| Gemini_cosmology | `gemini-3.1-pro-preview` | **MAJOR REVISIONS** | 4 (E1–E4) | 0 | 0 | 1 (N1) | `project-context/peer-reviews/ROUND_2026-09-04-A3M-v3M.0.8-EXACTPDF-8cf429e0-R3_A3M_Gemini_cosmology.md` |
| Grok_brutal | `grok-4.3` | **REJECT** | 4 (E1–E4) | 3 (M1–M3) | 0 | 3 (N1–N3) | `project-context/peer-reviews/ROUND_2026-09-04-A3M-v3M.0.8-EXACTPDF-8cf429e0-R3_A3M_Grok_brutal.md` |

No FAILED legs on this dispatch (OpenAI/Anthropic were never dispatched —
paused/disabled by design, not a failure; Perplexity not run, optional per
directive I1).

## Finding summary (not yet truth-audited — for the next closure pass)

- **Gemini E1** — reproducibility statement defers Zenodo DOI minting to
  packaging stage; PRD wants a frozen DOI now.
- **Gemini E2** — VI.B/reproducibility cite an unpublished companion P2/
  Fisher-forecast draft for the shape-overlap parameter `r`.
- **Gemini E3** — internal review-log/draft-history prose survives in body
  (pp. 3, 5, 8): "left open in earlier drafts...", "supersedes an earlier,
  misdescribed claim...", "omitted pending that re-derivation".
- **Gemini E4** — abstract's SPHEREx 3.13σ LSS discrimination uses the
  pre-bounce amplitude while §VII discloses the post-bounce (transmitted)
  amplitude is suppressed ~4x; flags as comparing incompatible amplitudes.
- **Gemini N1** — stray hyphen/space in "regularized-renormalized- resummed".
- **Grok E1** — literal filesystem paths / script names / commit-hash-style
  metadata ("research/theory_audit/...", "outputs/pbh_compaction_fnl.json",
  "R3", "v3M.0.8", "earlier synthetic-density result", "superseded claim")
  remain in the submitted PDF body.
- **Grok E2** — abstract γ=2.567±0.382/1.14σ presented without "under the
  authors' refit prior" qualifier next to the official NANOGrav 3.2±0.6
  posterior; f_PBH=0 stated without noting the ad-hoc Gaussian-calibrated
  normalization.
- **Grok E3** — transmission bound 0<T≤1/2 restricted to scheme S1 and
  kη_B≲1e-2 in body, but abstract states it as unqualified.
- **Grok E4** — PBH null relies on a lognormal spectrum shape stated (p.6) to
  be "not reconstructible from the published paper"; no side-by-side
  calculation on Choudhury et al.'s exact spectrum.
- **Grok M1** — factor-of-two resolution's only external validation is
  reproducing known dS/USR limits; no second independent bispectrum code
  cross-check.
- **Grok M2** — Table II juxtaposes official vs. refit γ posteriors without
  explicit "not directly comparable" qualifier at that table.
- **Grok M3** — length/contribution ratio: 10 pp for one per-vertex table +
  one transmission integral under one scheme; suggests 6–7 pp is typical.
- **Grok N1–N3** — future-dated Zenodo/abstract date artifacts; Fig.1 axis
  label normalization undefined; duplicated "research/theory_audit" phrase.

These findings are recorded verbatim from the raws for the next truth-audit/
closure pass (per directive H-refined) — several overlap with prior
disposition ledger entries (e.g. internal bookkeeping prose, γ posterior
juxtaposition) and should be checked against `DISPOSITIONS/A3M.md` before
being counted as genuinely-new.
