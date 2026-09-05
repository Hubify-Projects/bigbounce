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
