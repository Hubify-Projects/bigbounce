# A3M v3M.0.11 — R5VERIFY INT board — 2026-09-04

Round `ROUND_2026-09-04-A3M-v3M.0.11-EXACTPDF-790fafa6-R5VERIFY`; paper v3M.0.11, 14 pp,
sha256 `790fafa691e1a6ef0c476309d8224c5f2af2a59e4a3966f6afa0cf9d9dff4105` (exact-PDF binding;
served mirror `site/public/papers/a3_multichannel_arxiv_v3M.0.11.pdf` byte-identical to the
canonical `research/track_a3_multichannel/paper/main.pdf`).

Preflight receipt: `INT_v3/ROUND_2026-09-04-A3M-v3M.0.11-EXACTPDF-790fafa6-R5VERIFY/preflight_receipt.json`
(PASS, HEAD `da3bbb2aff946180e3fea9987c21e1f31cc4478a` after committing the pending
v3M.0.11 site-sync bundle that was blocking a clean mint). Dispatch log:
`INT_v3/ROUND_2026-09-04-A3M-v3M.0.11-EXACTPDF-790fafa6-R5VERIFY/api_legs_run.log`.
Directive N/N-amended routing: Codex/OpenAI PAUSED (not dispatched); Claude/Anthropic
API forbidden; this leg set is Grok API + Gemini API (directive-M-AMENDED active legs)
plus the optional Perplexity citation-forensics leg (recorded absent on failure, never
required) and the pre-existing Claude Fable subagent INT leg.

## Verdict matrix (verbatim, diagnostic only — per directive P, words are not the gate)

| Leg | Model | Verdict | Counts | Raw |
|---|---|---|---|---|
| Grok API | `grok-4.3` | **REJECT** | 3 ESSENTIAL / 3 MAJOR / 2 MINOR / 2 NIT | `project-context/peer-reviews/ROUND_2026-09-04-A3M-v3M.0.11-EXACTPDF-790fafa6-R5VERIFY_A3M_Grok_brutal.md` |
| Gemini API | `gemini-3.1-pro-preview` | **MAJOR REVISIONS** | 4 ESSENTIAL / 3 MAJOR / 1 MINOR / 1 NIT | `project-context/peer-reviews/ROUND_2026-09-04-A3M-v3M.0.11-EXACTPDF-790fafa6-R5VERIFY_A3M_Gemini_cosmology.md` |
| Claude Fable (INT subagent) | Claude Fable 5.1 | **major-revisions** | 5 MAJOR / 16 minor | `INT_v3/ROUND_2026-09-04-A3M-v3M.0.11-EXACTPDF-790fafa6-R5VERIFY/A3M_fable_r5_leg.md` |
| Perplexity (optional) | `sonar-pro` (primary) / fallback | **FAILED — ABSENT** | 401 `insufficient_quota` on primary; fallback dispatch then hit a stale-receipt race (non-fatal artifact of the retry, not the root cause) | `project-context/peer-reviews/_failed_stubs/ROUND_2026-09-04-A3M-v3M.0.11-EXACTPDF-790fafa6-R5VERIFY_A3M_Perplexity_citations.FAILED-quota.md` |
| OpenAI/ChatGPT | — | **ABSENT** (directive N pause, not dispatched) | — | — |

2/2 required active-API legs (Grok, Gemini) dispatched OK, 0 "Reviewer call FAILED" on
either. Perplexity is optional per directive I1/N and its absence does not fail this
wave. 0 BLOCKER on any leg.

## Cross-leg pattern (initial read, not a truth-audit)

All three substantive legs (Grok, Gemini, Fable) independently converge on the same
root issue: the abstract's headline number(s) and bound(s) do not match the body's
final calibrated statements once the S1/S2 two-scheme split (from the newly-integrated
D-A3-9 science decision) is taken into account —
Grok's A3M-E1/M1, Gemini's A3M-E1/E2, and Fable's M1 all independently flag the same
S1-only "< 1/2" transmission bound / scheme-dependent amplitude drift between abstract
and Sec. III/§V C. Gemini additionally flags internal lab-notebook language and a
missing frozen-release DOI (E3/E4) that are presentation/provenance items, not physics.
A full source-cited truth-audit disposition (per directive H-refined) is a separate
follow-up step, not performed in this dispatch-and-file pass.

## Provenance

- .env.local secrets used for dispatch; no secret values logged or printed.
- Dispatch PID 1908 (background), exited cleanly at wall-clock completion
  (Grok 70.5s, Gemini 155.9s, Perplexity primary+fallback 31.9s to failure).
- Round context: "Full adversarial first-read review against PRD standards." (matches
  the R4 convention). Venue binding: PRD (regular article), per
  `project-context/draft_paper_registry.json` A3M entry (unchanged from R4).
