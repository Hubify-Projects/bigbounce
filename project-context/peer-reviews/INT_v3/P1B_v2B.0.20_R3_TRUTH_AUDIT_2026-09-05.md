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
