# A3M v3M.0.24 — R9 verdict board (2026-09-18)

**Why this board exists.** Rounds were STOPPED on A3M after v3M.0.18 under directive R2, with the
stop lifted only "after a science decision on row 19". `NEXT_SCIENCE_LEDGER.md` row 19 is CLOSED
(**"DONE 2026-09-04 — NO-GO GENERALISED"**, decision `D-A3-14`, artifacts
`research/track_a3_multichannel/row19_lambda/`). Stop condition met → one board authorized.

**Exact artifact.** `research/track_a3_multichannel/paper/main.pdf`
sha256 `e0e923d6bdbc4eef7a1a57422e32e744c6f37c65258213166a579ec622d028c4`,
md5 `b29ebb90be09f8d0bbc3875647bb150a`, 19 pp.
Served mirrors `public/papers/a3_multichannel_arxiv_v3M.0.24.pdf` and
`site/public/papers/a3_multichannel_arxiv_v3M.0.24.pdf` — md5-identical to source and to the
Convex `paperVersions` current row (three-way verified before dispatch; no directive-G repair needed).
Receipt dir: `ROUND_2026-09-18-A3M-v3M.0.24-EXACTPDF-e0e923d6-R9VERIFY/`
(preflight receipt verdict **PASS**, `core_sha256 d7d4b7c5…`).

**Provider policy.** INT only — Grok API + Gemini API via `tools/v3_native_pdf_review.py`, plus one
Claude Fable 5.1 INT referee sub-agent under the de-biased paper-page referee prompt. No EXT browser
round and no Codex/OpenAI leg (Directive N; Portfolio Decision 2026-09-02 #6). The OpenAI column
remains frozen, displayed, never faked.

| leg | model | verdict (verbatim from the raw's own recommendation line) | raw findings | raw path |
|---|---|---|---|---|
| Grok_brutal | `grok-4.3` | **REJECT** | 20 (9 E / 5 M / 4 m / 3 N, incl. pass-2) | `../ROUND_2026-09-18-…-R9VERIFY_A3M_Grok_brutal.md` |
| Gemini_cosmology | `gemini-3.1-pro-preview` | **MINOR REVISIONS** | 8 (4 E / 3 M / 1 N, incl. pass-2) | `../ROUND_2026-09-18-…-R9VERIFY_A3M_Gemini_cosmology.md` |
| Claude Fable 5.1 (INT referee) | `fable-5.1` | **MAJOR REVISIONS** | 22 (2 M / 14 m / 6 Q) | `A3M_v3M.0.24_R9_claude_fable_2026-09-18.md` |

**Leg health.** No leg FAILED. Both API raws carry a wall time (103.1 s / 165.8 s), review-packet
hashes and a rendered-PDF confirmation; neither contains "Reviewer call FAILED". The Fable leg is
complete through all required sections and its integrity note records that it opened no prior review
material, no SSOT, no dispositions and no ledger, and was given no expected verdict; it verified its
findings by its own derivations, by executing/reading the named committed artifacts, and by fetching
Li *et al.* arXiv:1612.02036. Verdict words above are transcribed, never inferred or softened.

**Truth-audit:** `A3M_v3M.0.24_R9_TRUTH_AUDIT_2026-09-18.md`.

## Outcome

**24 genuinely-new-real** findings — 3 MAJOR, 1 MAJOR-lite, 17 minor, 3 nit — against 14 falsified
(each source-cited), 2 re-flags and 2 opinion/genre. **R9 is not a clean wave; clean-wave count 0.**

The three MAJORs:
1. `DA3M-R9-01` — the reproducibility statement pins to commit `68309c8`, which contains **none**
   of the ~12 artifacts it names; both published URLs return 200 only because the parent
   directories exist.
2. `DA3M-R9-12` — Eq. (15) is Li *et al.* Eq. (5.1) (the $P\propto X^n$ specialization), not their
   Eq. (4.19); the §VIII $\lambda$-scan measured from it double-counts $\lambda$ on the
   matter-contraction line, and the $\lambda=0$ baseline the scan's numbers actually come from is
   not printed anywhere. Conclusion unaffected — `D-A3-14` stands — but unverifiable from the PDF.
3. `DA3M-R9-13` — $f_{\rm NL}^{\rm after}=1.0$–$1.4\times10^{11}$ is printed in the abstract, §VIII
   and Table VII with no statement that tree-level control is lost ~7 decades earlier
   ($f_{\rm NL}\zeta\sim1$ at $|f_{\rm NL}|\approx2.2\times10^4$), though §V B already owns the
   perturbativity criterion.

Plus `DA3M-R9-02` (MAJOR-lite): v3M.0.19 dropped the whole "$\lambda=s=0$" qualifier when `D-A3-14`
proved $\lambda$-independence **only**; `row19_lambda/results.json` still records `s = 0, eta_sr = 0`,
so the abstract's "full $P(X)$ $k$-essence class" claim needs its constant-$c_s$ restriction back.

## Verdict-word note (pattern-066, recorded not weaponized)

Three legs on one byte-identical PDF returned REJECT / MINOR REVISIONS / MAJOR REVISIONS. Grok's
REJECT rests substantially on four items the audit falsified against the manuscript's own text and
the auditor's own arithmetic (E1 date, E2 "no labeled abstract", E8 1.84-vs-1.732, E9 the
$\sigma=0.53$ arithmetic) — yet Grok also produced the E5 and E7 kernels, one of which is the
round's most serious finding. Verdict words are diagnostic feedback under directive P; the gate is
0 genuinely-new-real outstanding. No verdict was faked, softened, or dismissed on the strength of
its label.

## Consequence

Readiness stays at the Convex cap **75** (computed, not chosen): with 3 MAJOR + 1 MAJOR-lite open
on the current exact PDF the automated-review-convergence gate is not met. Closure lands as
v3M.0.25 under full directive-G hygiene; the one confirmation board permitted by directive R2 then
runs on that exact PDF.
