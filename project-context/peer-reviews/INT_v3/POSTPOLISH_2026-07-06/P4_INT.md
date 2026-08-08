# P4 POST-POLISH INT (Claude leg, canonical spec §1) — v1.0.219

**Scope:** verify D-round polish (title/abstract/AI-methods) preserved the zero-numbers-changed guarantee + top-journal quality. Read-only. Commit `d932f4bc`; HEAD `062606eb`.

## Verdict: **ACCEPT (minor)** — polish is clean; two non-blocking MINORs below.

## Zero-numbers-changed: CONFIRMED (with 2 disclosure MINORs)

Diff `d932f4bc` touches only `.tex` (title + abstract + AI-methods para), 4 metadata/README files, and re-mirrored PDFs. No JSON / data / body-result touched. Abstract number-set old→new is identical for every substantive value:
- +0.41σ, p=0.31, 10⁴, z≈−18, 1.7%, 99.32%, +3.64σ / +7.28σ, ≈1.9σ Gaussian-equiv, A₉₅∈(1.0%,1.5%], A₅₀≈0.75%, N≈9.5×10⁵, 8,474,531, 3,201,160, p_eq∈{0.6,0.7,0.8}, z=0.58/0.70, z≈4.0–4.3, P(≥3σ)≥0.999 — ALL present, verbatim (`chirality_catalog_paper.tex` abstract, lines ~548–560).

**[MINOR-1]** Two numbers dropped from the abstract (still in body): the +7.93σ 10⁴-perm canonical-mask row (body 8×, incl. `tab:multipole`), and the `A_ref=0.034 in A_p units, A_p=2(f_CW−0.5)` mapping (body 7×). The A_p↔f_CW mapping was added in v1.0.201 *specifically* to stop a referee miscomputing z≈−7.6 from z≈−18. De-densifying the abstract by removing it is defensible (both numbers survive in-body), but a first-time referee reading only the abstract now sees z≈−18 without the factor-of-2 key. Suggest one clause restoring the A_p=2(f_CW−0.5) mapping to the abstract. Not a number change; a disclosure-completeness nit.

**[MINOR-2]** The retired +7.93 (vs +7.28) distinction — two different null-run sizes/mask conventions, previously reconciled in-abstract — is now only reconciled in body/`tab:multipole` caption. Fine for length, but abstract no longer pre-empts the "3.64 vs 7.28 vs 7.93" confusion that harsh referees have raised before.

## Title propagation: CONFIRMED consistent
New 12-word title "A Null Chirality Dipole in 8.5 Million DESI Galaxies from Equivariant Deep Learning" propagated identically to: `.tex` `\title`, `submissions/P4/ARXIV_METADATA.txt` (TITLE block), `README.md` (h1), `REFEREE_COVER_LETTER.md`. Site static (`papers.ts`/`reviewTimeline.ts`) synced (companion commit `39f380e5`). Zero stale "Survey-Scale Galaxy Chirality with Equivariant TTA" residue anywhere in submissions/site. Result-first title is a genuine improvement.

## PDF hygiene (directive-G): CONFIRMED
Four served paths byte-identical md5 `e8b4f10a9bcc9545aeb58869395e7d06` (compile dir, `site/public/papers/chirality_catalog_paper.pdf`, versioned `_v1.0.219.pdf`, `p4-chirality.pdf`) = commit-message md5. Versioned v1.0.219 mirror created. arXiv tarball rebuilt.

## AI-methods disclosure: CONFIRMED honest
Replaced the terse "LLMs used as assistive tools" with a reproducibility-framed statement (agentic pipeline under author direction; every result verified against committed artifacts; public audit trail; AI not an author). No honest disclosure lost; strengthened.

## Regressions introduced by polish: NONE found
- No caveat lost: harmonic-channel-is-a-diagnostic and sigmas-not-inter-comparable both stated (once each, cleaner) — the two Gemini-flagged repetitions consolidated, not deleted.
- Numbers still match committed JSONs (JSONs untouched; provenance established in prior R-rounds and unchanged here).
- `\paperTimestamp` bumped July 5→6; `\paperVersion` v1.0.218→219. Consistent.

**Bottom line:** presentation-only polish, guarantee held. Optional: restore the A_p↔f_CW mapping clause to the abstract (MINOR-1).
