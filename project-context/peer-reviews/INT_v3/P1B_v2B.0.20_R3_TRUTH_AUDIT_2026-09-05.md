# P1B v2B.0.20 R3 — TRUTH AUDIT (skeptical, verdict-first)

- Auditor: Claude Opus, independent skeptical truth-auditor. No expected outcome supplied.
- Date: 2026-09-05
- Exact artefact: `arxiv/paper1b_namaster_proof.pdf`
  sha256 `cf57f485c20acd8c5e9dc8277a65ca9a6ce1dac8db4b2e360be98845e7ee50cf`, 15 pp.
  Byte-identical to `site/public/papers/paper1b_namaster_proof_v2B.0.20.pdf` (verified, same sha256).
- Legs audited: Grok_brutal (grok-4.3, JORS-SOFTWARE adversarial) — REJECT;
  Gemini_cosmology (gemini-3.1-pro-preview, PRD-referee) — MAJOR REVISIONS;
  Claude Opus INT leg — major-revisions.
- Protocol: lab truth-audit, directive H-refined. Every finding fingerprinted and
  classified (a) genuinely-new REAL / (b) re-flag of already-addressed-or-disclosed /
  (c) FALSIFIED against source / (d) OPINION-or-venue-preference / (e) OUT-OF-SCOPE
  disclosed limitation. Citations to code/artefacts required for (b)/(c).
- Reference material: `DISPOSITIONS/P1B.md`, R1/R2 audits, `pipelines/namaster_proof/blind_test/`
  (`verify3.py`, `RULES_v3_FROZEN.md`, `RULES_v4_FROZEN.md`, `public3/scorecard.json`).

## PLAN
1. Board (`P1B_v2B.0.20_R3_BOARD_2026-09-05.md`) — per-leg verdicts + counts from raw text.
2. Verify Opus M1 (R7 spot-row predictability), M2 (r7_residual fail-open),
   M3 (batch-3 Clopper-Pearson vs batch-2 refusal; 24/24 vs 30/30) against the code.
3. Freivalds / Fiat-Shamir prior-art check; N3 wording; venue.
4. Grok REJECT rationale item by item; Gemini items.
5. Canonical finding list with class + citation + closure action.
6. CLOSURE PLAN — (i) editorial v2B.0.21, (ii) science (batch 4).
7. R2 statement; DISPOSITIONS/P1B.md update.

*(sections filled below as the audit proceeds)*

---

## 1. Independent verification against the code and artefacts

Everything below was re-derived from source; no reviewer's assertion was accepted on its word.

### 1.1 Opus M1 — R7's spot rows *are* predictable to the runner. **The claim is correct.**

`pipelines/namaster_proof/blind_test/verify3.py:32–45`:

```python
def spot_rows(mask_sha256: str, result_hash: str, lmax: int, k: int = K_SPOT) -> list[int]:
    """Receipt-bound row draw: depends on the run's own result hash."""
    ...  sha256(f"{mask_sha256}|{result_hash}|{salt}")  ...
```

and `verify3.py:57–58` supplies its two arguments as
`receipt["inputs"]["mask_sha256"]` and `band_hash(payload["bandpowers"])`.

**What R7 actually binds:** the row draw is a *public deterministic function of the
contract's mask hash and of the runner's own published bandpowers*. Both values are in the
runner's hands **before it publishes anything**. Therefore:

* The paper's sentence at `arxiv/paper1b_namaster_proof.tex:573` — "the rows depend on the
  run's own result and cannot be chosen by the runner" — is *literally* true in a weak
  sense (the runner cannot name an arbitrary row set) and **false as a security property**.
  Unchoosable is not the property that matters; **unpredictable** is, and R7 has none. The
  runner can also grind the low bits of a bandpower to redraw the row set at negligible cost,
  which makes even the weak "cannot be chosen" reading effectively false.
* The cost claim is also overstated. S6 builds the full operator honestly (that is exactly
  why R3/R4 never fire on it), so an R7-aware S6 runner already holds every row of `M`;
  writing a `pseudo_cl` exact on six known rows and effective-multipole elsewhere costs it
  **zero** marginal work, not "one matrix–vector product".
* In Fiat–Shamir terms R7 is the transform applied to a **prover-chosen** commitment, which
  does not satisfy the transform's soundness condition.

**Empirically confirmed, and already answered.** `RULES_v4_FROZEN.md` (frozen 2026-09-05,
before the batch-4 scripts, the verifier-seed commitment and the seal) records M1 verbatim
and pre-registers arm **S7 = R7-aware effective multipole** to escape R7. Batch 4 has
**landed**: `public4/scorecard.json::per_arm.S7_r7_aware_effective` gives
`n = 6, r7_fired = 0, r7_residual_max = 0.0, r8_fired = 6`. R7 was evaded 6/6 at exactly
zero residual — the prediction is measured, not argued. **Class (a) genuinely-new REAL.**

### 1.2 Opus M2 — R7 fails OPEN on a missing intermediate. **The claim is correct.**

`verify3.py:48–56`:

```python
p_declared = receipt.get("intermediates", {}).get("pseudo_cl")
if not isinstance(p_declared, list) or len(p_declared) != lmax + 1:
    return False, float("nan")          # "does not fire"
mask = pcl.make_mask(int(contract["nside"]))
if band_hash(mask) != contract["mask_sha256"]:
    return False, float("nan")          # "does not fire"
```

`(False, nan)` is consumed at `verify3.py:90–92` as "R7 did not fire". No other rule
(R0–R6) requires `intermediates.pseudo_cl` to be present, so **omitting the field silently
disables the package's only value-level rule** — in a package whose §5 selling point is
fail-closed verification. Every batch-3 arm happened to emit the field, so batch 3 never
exercised the path. This is a **real hole**, not a hypothetical.

**Empirically confirmed, and already answered.** Batch-4 arm **S8 = omit `pseudo_cl`**:
`public4/scorecard.json::per_arm.S8_omit_pseudo_cl` → `r7_fired = 0` of 6 (R7 fails open,
as predicted), `r8_fired = 6`, `shortcut_suspect = 6`. R8 is fail-closed on a missing
contract-declared intermediate. **Class (a) genuinely-new REAL.**

### 1.3 Opus M3 / Gemini E1 / Grok M2 — batch-3 statistics. **Both halves correct.**

**(a) The interval inconsistency is real, and the artefact contradicts itself too.**
The paper's batch-2 presentation (`…tex:479–491`) pre-declares the caveat properly:
"the five replicates within an arm are seed-varied executions of one deterministic variant
… effective independent *n* per class is 1 … **no run-level detection-probability interval
is claimed**". The batch-3 paragraph (`tex:584–586`) then quotes **0.607** (S6, 6 runs),
**0.393** (honest FP, 6 runs) and **0.905** (pooled structural) and calls them "class-level
detection rates, not per-run probabilities". Recomputation settles what was actually
computed: `0.05^(1/6) = 0.6070`, `1 − 0.05^(1/6) = 0.3930`, `0.05^(1/30) = 0.9050`. Every
one of the three is a Clopper–Pearson bound whose *n* is the **number of runs**. Calling a
run-level bound class-level does not change what was computed.
`public3/scorecard.json::independence_caveat` states the same thing against itself — R7's
replicates are "class-level evidence, not a run-level interval" — while the same file
reports `S6_detection.lower95_one_sided = 0.607` and
`detection_structural_S1_S4b.lower95_one_sided = 0.905`.
Gemini's proposed corrections check out arithmetically (batch 1 `n=4 → 0.4729`; batch 3
structural `n=5 → 0.5493`), but the cleaner fix is the one batch 4 already adopted.

**(b) The `24/24` is an arithmetic slip.** `tex:586` reads "Structural arms S1–S4b pool to
24/24 (lower bound 0.905)". S1, S2, S3, S4, S4b is **five** arms × 6 = **30** runs, and
`0.05^(1/30) = 0.905` confirms the bound was computed for *n* = 30, against
`public3/scorecard.json::detection_structural_S1_S4b`. The text should read **30/30**.
The slip runs *against* the authors' interest, which is the signature of an honest error.
`RULES_v4_FROZEN.md` §M3 already records the correction and states that batch 4 reports
**class-level counts only, no run-level Clopper–Pearson intervals** — the treatment the R2
audit asked for, applied at the source. **Class (a) genuinely-new REAL** (both halves).

*Not a re-flag.* Standing rule 1 of the R2 ledger (`DISPOSITIONS/P1B.md`) would make a
run-level-CP complaint against a post-v2B.0.19 PDF a re-flag of D-R2-01/D-R2-02 — but that
rule was written for the **batch-2** presentation, which v2B.0.19 fixed and which survives
intact here. The defect is a *recurrence of the same failure class in newly written
batch-3 text*, so it enters R3 as genuinely-new.

### 1.4 Prior art: Freivalds and Fiat–Shamir. **Absent. The gap is real.**

`grep -n "Freivalds\|Fiat\|Klein" arxiv/paper1b_namaster_proof.tex` → **no matches**.
Freivalds (1979) randomized verification of matrix products is the direct ancestor of R7
(check `M C = p` on a random subset of rows rather than rebuilding `M`), and Fiat–Shamir
(1986) is the transform whose soundness condition R7 violates and R8 restores. Neither is
cited. §7 is the correct home. **Class (a) genuinely-new REAL.**

### 1.5 The N3 / priority question. **No priority claim exists in v2B.0.20.**

`grep -n "first\|novel\|to our knowledge"` returns only non-priority uses — "the first
must return a finite …" (`tex:284`), "first, from one honest reference run" (`tex:393`),
"S4b is the first replicate set to exercise R6's cross-run disjunct" (`tex:586`), "the
first batch-3 seal" (`tex:629`). The "to our knowledge this is the first" sentence flagged
as **D-R2-08** was deleted in v2B.0.19 and has not returned. The Opus leg reaches the same
finding independently ("the manuscript makes no explicit priority claim at all"). This is
therefore **not a finding** but a standing guardrail: if any N3 language is ever added it
may claim **only** "first such measurement *for pseudo-C_ℓ execution receipts*", and only
alongside the Freivalds / Fiat–Shamir / blind-analysis (Klein & Roodman 2005) /
in-toto-SLSA / OpenTimestamps-Sigstore citations. Recorded as a guardrail, not an item.

### 1.6 Venue. **Two independent legs converge; this is a decision, not an edit.**

Grok E5 (JORS expects ≤8 pp; this is 15) and the Opus venue section ("§6 is now the paper:
a measurement, with a pre-registration, a seal, a confusion matrix and an adversary model")
disagree about severity but agree about the diagnosis. Opus recommends **ACM REP** primary,
CiSE or Nature Scientific Data as alternates, with a short JORS/JOSS software paper for the
package cross-citing; arXiv `astro-ph.IM` primary, `cs.SE` secondary. Under directive R3 a
venue change is a recorded lineup decision, not a referee fix. Logged in §4(ii).

---

## 2. Canonical findings (33) — class · citation · closure action

Classes: **NEW** genuinely-new REAL · **RF** re-flag (disposition id) · **FAL** falsified ·
**OPI** opinion/venue-preference · **OOS** out-of-scope, disclosed limitation.
"Src" gives the raw item(s) that raised it.

| id | finding | src | class | citation | closure |
|---|---|---|---|---|---|
| D-R3-01 | R7's spot rows are prover-predictable; "cannot be chosen by the runner" is the wrong property; adaptive evasion is zero-cost, not one matvec | Opus M1 | **NEW** | `verify3.py:32–45,57–58`; `tex:573`; `public4/scorecard.json` S7 `r7_fired 0/6, r7_residual_max 0.0` | restate honestly + report S7 + cite Freivalds/Fiat–Shamir + present R8 |
| D-R3-02 | R7 fails **open** when `intermediates.pseudo_cl` is absent/malformed (and on mask-hash mismatch); no other rule requires the field | Opus M2 | **NEW** | `verify3.py:48–56` returns `(False, nan)`, consumed at `:90–92`; `public4` S8 `r7_fired 0/6, r8_fired 6/6, suspect 6/6` | report S8; state the fail-open in §11; present R8 as fail-closed |
| D-R3-03 | batch-3 run-level Clopper–Pearson bounds (0.607 / 0.393 / 0.905) contradict batch 2's pre-declared refusal to claim run-level intervals | Opus M3a, Gem E1, Grok M2 | **NEW** (recurrence of D-R2-01/02 class in new text) | `tex:188,584–586` vs `tex:479–491`; `public3/scorecard.json::independence_caveat` vs its own `lower95_one_sided` | adopt batch 4's treatment: class-level counts only, no run-level intervals, uniformly across batches 1–4 |
| D-R3-04 | "S1–S4b pool to **24/24**" — five arms × 6 = **30**; `0.05^(1/30)=0.905` shows n=30 was used | Opus M3b, Gem E1 | **NEW** | `tex:586`; `public3/scorecard.json::detection_structural_S1_S4b`; `RULES_v4_FROZEN.md` §M3 | correct to 30/30 (and drop the bound per D-R3-03) |
| D-R3-05 | abstract and §6 still say "run in two batches" / "run twice"; batch 3 missing from protocol steps (1)–(5) | Opus M4 | **NEW** | `tex:169,392,403` | rewrite the protocol paragraph for four batches (pilot / primary / value-level / post-commitment) |
| D-R3-06 | batch-3 audit trail incomplete: no commit-ordered trail; no pre-registered abort criterion; no fresh-key/fresh-assignment non-contamination sentence; attempt-1 assignment unpublished | Opus M5 | **NEW** | `BATCH3_PREREGISTRATION.md` (no stopping rule); `BATCH3_ABORT_NOTE.md`; `tex:629` | add the four sentences + the trail `dcf96696→…→bf7d26e3` |
| D-R3-07 | the blind-test corpus (batches 2–4, seals, keys, verdicts, scorecards, OTS proofs, `verify3/4.py`) is not archived immutably; Zenodo pins only `packages/namaster-proof@0a587b58` + manuscript source | Opus M6, Grok M3(part) | **NEW** (packaging/science) | `tex` §12 | deposit `pipelines/namaster_proof/blind_test/` as its own Zenodo record, cite the DOI + checksum |
| D-R3-08 | two broken cross-references — "batch-3 science item S2 (§11)" and "(Sec. 11, item S3)" resolve to nothing and collide with shortcut-class names | Gem M1, Opus min2 | **NEW** (recurrence of D-R2-06 class) | `tex:252,652`; §11 numbers L1–L4 | repoint to §6's per-band-deviation discussion; drop the S-tags |
| D-R3-09 | "**Both** batches' manifests" then lists three | Gem N1 | **NEW** | `tex:998` | "All four batches'" after batch-4 integration |
| D-R3-10 | title-page revision stamp `v2B.0.20(2026-09-05 09:00 PT)`, the §12 sentence explaining it, and the `p1b-`-prefixed artefact filenames are internal bookkeeping | Gem E2, Grok N1, Grok E3(part) | **NEW** (stamp half = **RF** of D-R2-19, deferred to the submission build per directive G) | `tex` title page, §12 p. 12–13 | strip stamp + sentence in the submission build; rename the `p1b-…json` manifests |
| D-R3-11 | manuscript says `pymaster 3.0.1`; the artefact records `"pymaster": "3.0"` | Opus min1 | **NEW** | `tex:196,684,700,892,1024` vs `pymaster_crosscheck_result.json` | correct to 3.0 or bind 3.0.1 to a recorded conda package version |
| D-R3-12 | Freivalds (1979) and Fiat–Shamir (1986) — the exact prior art for R7/R8 — are uncited | Opus M1(2nd half) | **NEW** | `grep Freivalds\|Fiat` → no match | add a §7 prior-art paragraph |
| D-R3-13 | abstract says the primitive is "not a detector … of value-level shortcuts" while R7 catches value-level S6 6/6 | Grok E2 | **NEW** | abstract vs `tex:584` | restate: R7 detects *rule-unaware* value-level shortcuts; R8 extends to rule-aware; metadata forgery remains open |
| D-R3-14 | uncomputed quantitative claims: "order-unity fractional deviations … large enough to bias a fit"; "agrees to 6×10⁻¹⁶ on six cases" (six cases unspecified) | Gem M2 | **NEW** | `tex:246`, §6 p. 8 | quantify or cite the bias; name the six cases |
| D-R3-15 | the frozen rule set is not bound by a digest quoted in the paper | Grok M1 | **NEW** | `RULES_v3_FROZEN.md` is committed alone (`dcf96696`); `public4/frozen_rules_digest.json` gives per-file sha256 | quote the rule-file digests in §6/§12 |
| D-R3-16 | §6 is one long unnumbered section with ~12 internal "(§6)" self-references | Opus min3 | **NEW** (recurrence of D-R2-10 class) | `tex` §6 | split 6.1–6.8 (protocol / batches 1–4 / abort / scope / PyMaster) |
| D-R3-17 | no per-run appendix table for batch 3 (the headline); batch 2 has one | Opus min4 | **NEW** | `public3/verdicts.json` carries `r7_relative_residual` | add batch-3 (and batch-4) per-run tables with the residual column |
| D-R3-18 | abstract is ~500 words with five numeric bounds | Opus min5, Grok E5(part) | **NEW** | `tex:165–200` | cut to ~half; leave interval arithmetic to §6 |
| D-R3-19 | "`ots verify` requires a Bitcoin node, which this machine does not run" — the OTS client falls back to public block explorers | Opus min6 | **NEW** (recurrence of D-R2-12 class) | §6 scope limits | re-check and report attested block heights, or name precisely which verification mode was declined and why |
| D-R3-20 | Table 1's trust taxonomy has no category for asserted fields whose *absence* disables a rule | Opus min7 | **NEW** | `tex:356`; D-R3-02 | add the third category |
| D-R3-21 | §9's 500-realization campaign reports σ for one injected angle; the other two are "expected" comparable | Opus min8 | **NEW** (recompute) | `tex:833` | recompute (seeds deterministic, cheap) or drop the expectation clause |
| D-R3-22 | §8's `1.41e-18` hedge sits away from the `rebuild_workspace_check.py` sentence it belongs beside | Opus min9 | **NEW** | §8 | move two lines |
| D-R3-23 | released 0.1.7 contains no R7 (nor R8/`verify3.py`/`verify4.py`) | Opus min10 | **NEW** | §12; `frozen_rules_digest.json` | say where batch-3/4 code sits relative to the release |
| D-R3-24 | §7 reads as if a transparency-log entry nearly closes S5 | Opus min11 | **NEW** | §7 | one sentence: Rekor anchors the receipt, not the trace's truthfulness |
| D-R3-25 | Q2 — a "semantically wrong but equally expensive" run (e.g. wrong pixel ordering) passes R7 **and** R8, since `M C = p` stays self-consistent | Opus Q2 | **NEW** | R7/R8 definition | one sentence in §11 beside the existing hedge |
| D-R3-26 | Q3 — R7's marginal contribution is exactly one class (S6); the four-mechanism claim is now three mechanisms across seven classes | Opus Q3 | **NEW** | `public3/scorecard.json` per_arm | restate the mechanism count |
| D-R3-27 | Q4 — S4b's cross-run source-selection rule is not stated; it determines whether 4/6 is a property of R6 or of the arm | Opus Q4 | **NEW** | `sealed3/crossrun_sources.json`; `public3/scorecard.json::S4b_crossrun_sources` (`run_037 ← run_036`, itself an S4b source) | state whether the rule was pre-registered |
| D-R3-28 | Grok E1: "the abstract quotes 20/20 and 0.473 with no independence caveat" | Grok E1 | **FAL** | the abstract carries the caveat verbatim (`tex:179–182`) and "All detection claims are at class level, never per run" (`tex:195`); `0.473` does **not** appear in the abstract (only `tex:480`, adjacent to the caveat) | none; re-flag of D-R2-01, closed in v2B.0.19 |
| D-R3-29 | Grok E3: "complete rewrite removing all review-process bookkeeping (pilot, post-hoc rule changes, abort, R7)" | Grok E3 | **OPI** (part actionable as D-R3-10) | the pilot demotion, disclosed post-hoc rule changes and the preserved abort **are** the required scientific disclosure; the Opus integrity note cites them as honesty markers | refuse the disclosure-stripping half — removing it would water down the paper; act only on D-R3-10 |
| D-R3-30 | Grok E4: "retract the claim that the detector works for the production NaMaster library" | Grok E4 | **OOS**, disclosed (premise **FAL**) | no such claim is made: the abstract states PyMaster is not installed and exposes no Wigner-3j counter (`tex:171–174`); §11 states the scope limit; Table 5's cross-check validates the *estimator*, not a hook | none; re-flag of the D-R2-03/D-R2-23 family |
| D-R3-31 | Grok E5: 15 pp vs JORS ≤8 pp; "reduce to 4–6 pp or submit elsewhere" | Grok E5 | **OPI** → escalated to a **scope decision** | converges with the Opus venue section; re-flag of D-R2-20 | §4(ii): venue decision (ACM REP primary), not a referee fix |
| D-R3-32 | Grok M3: "commit `0a587b58` predates the manuscript revision date" | Grok M3(part) | **FAL** | §12 explains the software release line is deliberately independent of the manuscript revision — the sentence Gemini quotes in its own E2 | none; the archive half survives as D-R3-07 |
| D-R3-33 | Grok N2: Table 1 caption "by trust level" vs column header "Trust" | Grok N2 | **OPI** (no contradiction; the caption names the taxonomy, the column is its header) | `tex:356` | harmonise for free while doing D-R3-20 |

### Per-leg counts (gross → canonical)

| leg | gross items | NEW | RF/FAL | OPI | OOS |
|---|---|---|---|---|---|
| Grok_brutal (REJECT) | 10 | 4 (E2→D-R3-13, M1→D-R3-15, M2→D-R3-03, M3→D-R3-07) | 2 (E1, M3-part) | 3 (E3, E5, N2) | 1 (E4) |
| Gemini_cosmology (MAJOR) | 5 | 5 (E1→D-R3-03+04, E2→D-R3-10, M1→D-R3-08, M2→D-R3-14, N1→D-R3-09) | 0 | 0 | 0 |
| Claude Opus INT (major-rev) | 17 + 5Q | 22 | 0 | 0 | 0 |

**Canonical total 33 · genuinely-new REAL 27 · FALSIFIED 2 · OPINION 3 · OUT-OF-SCOPE
disclosed 1.** No fabricated number was found in the manuscript, and no leg fabricated a
finding. The three legs' *severity* words diverge widely (REJECT / MAJOR / major-revisions)
while their *content* converges on one hard defect class (the R7 security claim, D-R3-01/02,
raised only by Opus) plus one presentation defect class (the batch-3 statistics, D-R3-03/04,
raised independently by Gemini and Grok and by Opus). Grok's REJECT is carried almost
entirely by items this audit classes OPI/OOS/FAL (E1, E3, E4, E5 = 4 of its 5 essentials).

---

## 3. Convergence R1 → R3

| round | PDF | pp | canonical | genuinely-new REAL | non-real (FAL/OPI/OOS) |
|---|---|---|---|---|---|
| R1 v2B.0.17 | `0d0c92ab…` | 8 | 23 (C1–C23) | — | — |
| R2 v2B.0.18 | `354d63b2…` | 12 | 27 (D-R2-01…27) | 19 | 8 |
| **R3 v2B.0.20** | `cf57f485…` | **15** | **33** | **27** | **6** |

The genuinely-new count went **up**, not down, and that is the honest reading: the paper
grew by a whole batch between rounds (12 → 15 pp; batch 3, rule R7, the S4b arm and the
PyMaster cross-check are all new content), and **new content carries new findings**. Of the
27 genuinely-new items, 22 are in text that did not exist at R2. Two of the three
recurrences (D-R3-03 run-level intervals, D-R3-08 dangling S-tags) are the R2 defect classes
reappearing in the newly written batch-3 prose — the v2B.0.19 fixes were applied to the
batch-2 text and not carried forward as a rule for new text. That is the single most useful
process lesson of this round.

This is **not** convergence, and it is not divergence either — it is the expected signature
of a paper still gaining science. The correct inference under directive R2 is that the
round-driven phase has done its job: the remaining agent-visible defects are 24 editorial
items plus one recompute, and the two that actually matter (D-R3-01, D-R3-02) were answered
by **science**, not by another round.

**What the rounds bought, measured.** R3's decisive contribution is a single finding
(D-R3-01/02) that no external leg raised and that only repo-level code inspection could
produce, and which was immediately converted into a pre-registered batch 4 that
**empirically confirmed both halves** (S7: R7 evaded 6/6 at zero residual; S8: R7 fails open
6/6, R8 catches both 6/6). A verdict word did not move; the science did.

---

## 4. Closure plan

### (i) Editorial — v2B.0.21 (no new computation required)

Exact edits, by `arxiv/paper1b_namaster_proof.tex` line:

1. **`:573` — restate the R7 property honestly (D-R3-01).** Replace "the rows depend on the
   run's own result and cannot be chosen by the runner" with a statement that the draw is
   *receipt-bound but prover-predictable*: it binds the check to the published result, but a
   runner that knows R7 can compute the rows before publishing and make exactly those rows
   exact at zero marginal cost, since S6 already builds the full operator. Say plainly that
   **R7's 6/6 is a measurement against a rule-unaware adversary**, and point to R8/S7.
2. **`:584–586` — the statistics presentation fix, again (D-R3-03, D-R3-04).** Delete the
   three run-level bounds (0.607, 0.393, 0.905), correct "24/24" → **30/30**, and report
   batch 3 the way batch 2 and batch 4 report: counts per arm, class-level detection,
   inferential unit named once. Apply the identical treatment to batch 1's 12/12 and 0/3.
   Add one sentence stating the rule for all future batches so this class does not recur.
3. **`:169, :392, :403` — four batches, not two (D-R3-05).** Rewrite the protocol paragraph
   as pilot / primary / value-level extension / post-commitment challenge, with the aborted
   attempt located, and extend steps (1)–(5) to cover batches 3–4.
4. **New §7 paragraph — prior art (D-R3-12).** Freivalds (1979) as R7/R8's direct ancestor;
   Fiat–Shamir (1986) as the transform whose soundness condition R7 violates and R8 meets;
   Klein & Roodman (2005) for blind analysis. One paragraph, three citations.
5. **`:252, :652` — repoint the two dead cross-references (D-R3-08)**; `:998` "Both" → "All
   four" (D-R3-09); `:196,684,700,892,1024` pymaster 3.0.1 → 3.0 (D-R3-11); `:356` Table 1
   caption/header and the third trust category (D-R3-20, D-R3-33); §8 move (D-R3-22).
6. **Abstract (D-R3-13, D-R3-18).** Cut to ~half; replace "not a detector of value-level
   shortcuts" with the post-batch-4 scope: structural shortcuts (R3/R4/R6); rule-unaware
   value-level shortcuts (R7); rule-aware value-level shortcuts and omitted intermediates
   (R8); metadata forgery still open by construction.
7. **§6 subsectioning 6.1–6.8 (D-R3-16); batch-3/4 per-run tables (D-R3-17); batch-3 trail
   + abort disclosure, four sentences (D-R3-06); rule-file digests quoted (D-R3-15);
   0.1.7-contains-no-R7/R8 note (D-R3-23); S5/Rekor sentence (D-R3-24); §11 additions for
   the fail-open and the semantically-wrong-but-expensive case (D-R3-02, D-R3-25);
   mechanism recount (D-R3-26); S4b source rule (D-R3-27); §14 quantifications (D-R3-14);
   OTS verification mode (D-R3-19).**
8. **Submission build only — strip the title-page revision stamp and its §12 sentence,
   rename the `p1b-` manifests (D-R3-10).** The internal build keeps the stamp under
   directive G; this is a build-flag item, not a content edit.

Directive-G hygiene applies to the v2B.0.21 bundle in full: bump `\paperVersion` + `\date`,
recompile to 0 undefined references, `/latex-audit`, re-mirror byte-identical to every
served path, Convex `paperVersions:bump` with the real md5/pages, three-way md5 check.

### (ii) Science

1. **Integrate batch 4 — the round's real output (D-R3-01, D-R3-02).** `RULES_v4_FROZEN.md`
   was frozen 2026-09-05 before the batch-4 scripts, the verifier-seed commitment and the
   seal, and it names M1/M2/M3 as its reason for existing. The batch has **landed**:
   `public4/` carries `verifier_seed_commitment.json` (sha256 `efef74f2…`, committed before
   the seal), `verifier_seed_reveal.json` (opens it, seed `06e39b7a…`, revealed after every
   receipt digest was committed), `frozen_rules_digest.json` (13 per-file sha256 including
   `RULES_v4_FROZEN.md` = `a59caaf8…`), `assignment.json` sealed as `dbe6a713…`, 8 arms × 6
   = 48 runs, `scorecard.json`, `verdicts.json`, and OTS proofs on both the seal and the
   commitment. Headline results to write up:
   * **S7 (R7-aware effective multipole): R7 fired 0/6, residual max exactly 0.0; R8 fired
     6/6.** M1 measured, not argued.
   * **S8 (omit `pseudo_cl`): R7 fired 0/6; R8 fired 6/6; suspect 6/6.** M2 measured.
   * S1–S4, S6: R7 and R8 both 6/6. S5 metadata forgery still escapes 0/6 flagged — the
     stated limit holds. Honest false positives **0/6**.
   * Report **counts only** — no run-level Clopper–Pearson intervals — per `RULES_v4_FROZEN.md`.
   * Disclose honestly that R8's randomness is a **commit–reveal verifier seed**, not a
     public beacon; `verifier_seed_commitment.json` itself declares a Bitcoin OTS blockhash
     as the drop-in upgrade, and that sentence belongs in §11.
2. **Zenodo deposit of the blind-test corpus (D-R3-07)** — batches 1–4, `public3_aborted/`,
   seals, keys, verdicts, scorecards, OTS proofs, `verify3.py`/`verify4.py`. This is what
   makes the OTS anchors independently useful and is the last packaging gap.
3. **Recompute the two remaining §9 injected-angle σ values (D-R3-21)** — cheap, deterministic.
4. **Venue decision (D-R3-31), under directive R3.** Two independent legs agree §6 is now a
   measurement rather than a software description. Recommended: **ACM REP** primary (CiSE or
   Nature Scientific Data alternates), with a short JORS/JOSS software paper for the package
   cross-citing; arXiv `astro-ph.IM` primary, `cs.SE` secondary. Record in `PAPER_LINEAGE`
   with the original claim beside the new claim if the split is taken.

### (iii) R2 statement (directive R2 — convergence budget)

**Rounds STOP after v2B.0.21.** R2 and R3 are the two permitted consecutive review rounds on
this paper. The v2B.0.21 bundle closes the 24 editorial items, the batch-4 integration and
the Zenodo deposit; **no further sweep may be run against P1B unless a new science or scope
decision intervenes**. The two decisions that would license a new round are already named:
(1) the venue split of §(ii)4, and (2) any successor to R8 (a public randomness beacon
replacing the commit–reveal seed). A leg re-raising JORS length/genre, the in-house-estimator
scope, or the abstract's independence caveat is a re-flag of D-R3-28/29/30/31 and is
dispositioned by citation, not by another round.

## 5. Integrity note

Nothing in this round reads as engineered. Three checks support that: (1) the `24/24` slip
runs *against* the authors' interest (the true figure is 30/30, a stronger number) — the
signature of an honest arithmetic error; (2) the hardest finding of the round (D-R3-01) was
raised by the lab's **own** INT leg against its own headline result, and was answered by
pre-registering an arm designed to make that result look worse (S7 escapes R7 6/6) rather
than by softening the text; (3) `RULES_v4_FROZEN.md` was committed alone and before the
batch-4 scripts, the seed commitment and the seal, and `frozen_rules_digest.json` binds
thirteen files by sha256 — the ordering is externally checkable. No verdict was recorded
from a label, no leg was dropped, no finding was dismissed without a source citation, and
no ACCEPT exists or was implied anywhere in this round.
