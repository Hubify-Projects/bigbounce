# P1U (Unified Paper 1) — INT v3 Round 2026-07-09

Paper: `arxiv/paper1_unified.tex` / `.pdf`, v1U.0.1, 58pp.
First-ever INT on the MERGED unified Paper 1 (P1A theory body + folded P1B
appendices E–H: ΔNeff/MCMC, NaMaster, ALP, reproducibility).

Modality: Claude LEG 1 = full-source read (`.tex` line-cited). API legs =
native-PDF (OpenAI Files API; XAI /v1/files). All verdicts below are from raw
reviewer text READ before recording — nothing fabricated.

---

## LEG 1 — Claude full-source referee (this agent)

**VERDICT: MAJOR REVISIONS** — the science content is at the same LLM-referee
floor as the P1A/P1B components had before the merge (title/scope honesty is
carefully hedged and internally disclosed), BUT the merge introduced **two real
merge-seam defects** that must be fixed before this can be called a clean
unified paper. Neither is a physics error; both are stale-companion-language /
broken-cross-reference artifacts of folding P1B in.

### Merge-audit results (the four requested checks)

**(a) Internal `\ref` resolving where a companion `\cite` used to be — MOSTLY OK,
one STALE SEAM.**
The abstract correctly reframes the folded material as "documented in the
appendices of this paper (Appendices~\ref{app:cosmo_methodology}--\ref{app:data_availability})"
(L1183–1186) and the body's forward-references to `app:cosmo_methodology`
(cosmo/MCMC), `app:namaster`, `app:alp`, `app:data_availability` all resolve to
real internal appendices E–H (L4507/5068/5415/5953). Good.

- **[MAJOR] seam — L1429–1466 + Table `tab:companion_inputs` (L1468–1522):**
  the "\textit{Companion paper.}" paragraph and the whole `tab:companion_inputs`
  table STILL treat the now-internal MCMC/NaMaster/ALP numbers as
  *companion-imported*: L1438–1439 "drawn from the companion internal MCMC
  analysis (Appendix~\ref{app:cosmo_methodology}, \emph{companion; coordinated
  submission})"; L1440–1442 "not…independently peer-reviewable values until the
  folded MCMC/reproducibility appendices are publicly posted"; L1453 "All
  subsequent citations to Appendix~\ref{app:cosmo_methodology}…refer to this
  companion work"; the table's **"Companion" column literally points to
  `Appendix~\ref{app:cosmo_methodology}`** (L1493–1519), i.e. a self-reference
  calling an in-paper appendix a "companion." After the merge these numbers are
  computed in THIS paper's Appendix E; the "companion / not-yet-postable / audit
  without the companion papers in hand" framing is a stale seam that now reads as
  self-contradiction. FIX: rename the paragraph + table to "Imported observational
  inputs (Appendix E)"; drop the "until publicly posted / companion in hand"
  language for the folded quantities; keep genuine-companion language ONLY for
  the truly external siblings still cited (`Golden2026P2` = SPHEREx f_NL forecast
  row, `Golden2026P3`). Both API legs independently flagged this (OpenAI #14,
  Grok MINOR-4).

**(b) Folded appendices consistent with body claims (3 imported numbers each
way) — 5/6 CONSISTENT, one BROKEN CROSS-REF + COUNT MISMATCH.**
Verified body↔appendix agreement for: H0=67.68±1.06 (body L1437/table ↔ App E
L4532/4854); ΔNeff=−0.020±0.169 full-tension (table L1497 ↔ App E L4778/4833);
σ8=0.803 (L1500 ↔ L4834); Ωm=0.308 (L1503 ↔ L4836); β≈0.27° ALP benchmark
(table L1511 ↔ App G L5447/5476/5565). All match. Good.

- **[MAJOR] seam — L1429–1435: broken cross-ref + accepted-sample-count
  mismatch.** Body: "**309,189** frozen accepted samples across two converged
  dataset combinations: 176,240 full-tension + 132,949 Planck+BAO+SN; see
  **Appendix~\ref{app:cosmo_methodology} Table~I** for the per-dataset
  breakdown." Problems: (1) **there is NO `\begin{table}` anywhere in Appendix E**
  (L4507–5068) — the promised "Table~I" does not exist, so `Table~I` is a dangling
  pointer; (2) the appendix's OWN sample bookkeeping does NOT contain
  309,189 / 176,240 / 132,949 — it reports 216,432 both-chains post-burnin,
  123,129 full-tension post-burnin (L4730), 106,361 / 40,349-raw / 28,245-post-burn
  for the Planck+BAO+SN chain (L5042–5045). The headline 309,189=176,240+132,949
  appears ONLY in a version-comment (L320), never in the served appendix body.
  A referee cross-checking the sample count against Appendix E will find neither
  the table nor the numbers. FIX: reconcile the abstract/intro headline count to
  the appendix's actual reported totals (or add the promised Table I with the
  per-dataset accepted-sample breakdown that matches).

**(c) No duplicated/contradictory statements survived dedup — MOSTLY OK.**
No verbatim duplicated derivations found across the seam; the self-containment
paragraph was previously de-densified (per version log). The only surviving
contradiction is the (a)/(b) companion-vs-appendix framing above (internal
appendix described as an external companion). The completeness statement
("not proven to be a complete operator basis" vs "basis-complete at M_Pl
power-counting") is an intentional, disclosed hedge, not a dedup failure — but
Grok flagged it as reading like an internal tension (see below).

**(d) Abstract accurately reflects unified scope — YES.** The abstract (L1069–1187)
correctly (i) states the R1–R3 amplitude-closure / R4 naturalness split, (ii)
labels the paper channel-level not operator-level, (iii) folds the observational
programme into "the appendices of this paper," and (iv) carries the honest
Tier/scope hedges. Title unchanged and still accurate. No overclaim introduced
by the merge.

### Verdict summary
Science: at the disclosed LLM-referee floor (same as pre-merge). Merge integrity:
**2 MAJOR seam fixes required** (stale companion framing of internal appendices;
broken `Table~I` ref + 309,189 sample-count that does not match Appendix E) +
the disclosed completeness hedge to be stated once unambiguously. None are
physics errors or fabrications — all are mechanical merge-hygiene fixes.

---

## LEG 2 — API vendors (native-PDF)

- **OpenAI gpt-5.5 — REJECT.** 18 issues (15 MAJOR, 3 MINOR). Core: "channel-level
  closure" repeatedly weakened to conditional/ansatz-dependent naturalness (#1);
  Eq.(1) T·T on-shell-shorthand ambiguity (#2); dim-+1 operator not a valid 4D
  EFT density (#4); NDA ρ~M_Pl^4 is a naturalness statement not an exclusion (#5);
  Fierz completeness doesn't enumerate the full gravitational EFT basis (#6);
  R4 conceded not amplitude-excluded (#10); **MCMC/NaMaster/ALP appendices E–H
  largely irrelevant to the central no-go + depend on companion works/artifacts
  (#14)**; reliance on concurrent companion papers (#15). This is the structural
  harsh-referee floor (same reject-class points P1A hit RS5–RS8), NOT new merge
  bugs — EXCEPT #14/#15 corroborate the LEG-1 companion-seam finding.
  Raw: `API_P1U_openai.md`.

- **Grok grok-4.3 — MAJOR REVISIONS.** 4 issues (2 MAJOR, 2 MINOR). MAJOR:
  completeness internal tension ("not a complete operator basis" vs
  "basis-complete at M_Pl power-counting") must be stated once unambiguously;
  R2/R3 ansatz-level margins need explicit-derivation-or-disclaimer. MINOR:
  off-shell +1 vs +4 accounting only sketched; **"companion papers / coordinated
  submission" cross-references create unnecessary dependence, move to
  self-contained tables or remove** — directly corroborates the LEG-1 seam.
  Raw: `API_P1U_grok.md`.

- Gemini: not run this round (stored keys billing-blocked per CLAUDE.md I1;
  covered via EXT browser).

### 3-vendor INT matrix (P1U v1U.0.1)
| Vendor | Modality | Verdict |
|---|---|---|
| Claude (full-source) | .tex line-cited | MAJOR REVISIONS (2 merge-seam MAJOR) |
| OpenAI gpt-5.5 | native-PDF | REJECT |
| Grok grok-4.3 | native-PDF | MAJOR REVISIONS |

Convergent signal across all three legs: the folded-companion language + the
observational appendices' external-companion framing is the one genuinely-new,
merge-specific fixable item; the rest is the pre-existing disclosed
harsh-referee floor.
