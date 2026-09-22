# Reproducibility manifest (directive Q2) — `research/fierz_row_sign_2026_09_22/`

**Program** BigBounce · P1N (`arxiv/paper1bc_ech_note`) sign verification
**Lane** `bb-LS15-fierz-sign` · opened & closed 2026-09-22
**Question** Is the scalar-channel coefficient of `eq:fierz_row` — the sign that
makes `G_s < 0` and drives the NJL no-condensate result — correct as printed?
**Answer** Yes, `+1`. `G_s` unchanged. No claim moves.
**Origin** flagged-but-unchecked by lane `bb-LS13-p1n-essentials`
(`research/ech_contact_term_2026_09_22/MANIFEST.md` "Known limits" #2)

## Compute venue and cost

| | |
|---|---|
| Venue | local workstation (macOS, darwin 25.5.0), CPU only |
| GPU / RunPod | **none** |
| Wall clock | ~11 s total for all three scripts |
| Reproduction cost | **~$0** — no paid API, no cluster, no storage, no network |
| Peak memory | < 300 MB |
| Determinism | fully deterministic; exact rational arithmetic over `Q(i)` in the primary result, no RNG, no seed |

## Scripts and exact invocation

```bash
cd <repo-root>
python3 research/fierz_row_sign_2026_09_22/scripts/fierz_row_sign.py \
  > research/fierz_row_sign_2026_09_22/outputs/fierz_row_sign.json
python3 research/fierz_row_sign_2026_09_22/scripts/fierz_exact_and_anchors.py \
  > research/fierz_row_sign_2026_09_22/outputs/fierz_exact_and_anchors.json
python3 research/fierz_row_sign_2026_09_22/scripts/multispecies_rank.py \
  > research/fierz_row_sign_2026_09_22/outputs/multispecies_rank.json
```

Requires CPython ≥ 3.8 with `numpy` and `sympy` (measured with numpy 2.5.1,
sympy 1.14.0). Every script `assert`s its own gates and exits non-zero if any
fails: the Clifford algebra and `(γ⁵)²=1` in every representation/signature, the
256-component decomposition residual, and the exact-solve residual.

| File | Role |
|---|---|
| `PRE_REGISTRATION.md` | method, validation set and all three outcome branches, committed at `a44bc46d` **before** any result existed |
| `scripts/fierz_row_sign.py` | float sweep: 3 Dirac representations × 2 signatures × 2 `γ⁵` conventions; full 5×5 Fierz matrix solved; `F²=1`; V−A self-conjugacy; mechanical Grassmann-sign derivation |
| `scripts/fierz_exact_and_anchors.py` | exact-rational re-solve over `Q(i)`; proof that the contracted channels are the same tensor in both signatures; exact single-species relation module; the Poplawski Eq.(9)–(11) published-number anchor and its counterfactual |
| `scripts/multispecies_rank.py` | operator rank of the five channels at `N = 1, 2, 3` species |
| `outputs/*.json` | committed outputs of the above |
| `DERIVATION.md` | the derivation, the validation table, the cross-checks, and what the lane does not claim |
| `PROPAGATION_NOTE.md` | printable sentences + the by-line-number claim table for the P1N lane |
| `RUN_LOG.md` | lane log (START / MILESTONE / DONE) |

## External data sources and APIs

No dataset, no download, no API call. Two external *papers* are used as
published-answer anchors and are cited, not re-derived:

| Source | Use | Link |
|---|---|---|
| N. J. Popławski, *Cosmological constant from quarks and torsion*, Ann. Phys. **523**, 291 (2011) | Eq. (9) colour-octet vacuum saturation `+(16/9)⟨ψ̄ψ⟩²` and Eq. (10)–(11) `ρ_Λ = (κ/3)⟨q̄q⟩² ≈ (54 meV)⁴`, positive — the external number the derived sign must hit | `arXiv:1005.0893` |
| G. D. Kerlick, PRD **12**, 3004 (1975); R. F. O'Connell, PRD **16**, 1247 (1977) | named in the pre-registration as a validation target; on working the problem, **not applicable** to a Fierz coefficient (stress-tensor result, already adjudicated under DP1N-60). Recorded as such in `DERIVATION.md` §4.3 rather than dropped. | — |

## Inputs taken from the manuscript (and nothing else)

* `main.tex:167-168` — signature, `ε_0123`, `κ`.
* `main.tex`, Eq. `eq:4fermi` — the contact-term prefactor (used, not re-derived).
* `main.tex:273-324` — `eq:fierz_row`, `eq:Gs`, `eq:gap` and the three-line
  argument, quoted as the claim under test.

Pinned to `v1N.0.7` at commit `27dd3143`. The manuscript's *conclusions* were
deliberately not used as inputs: the row was solved for, never matched to.

## In-repo artifacts consulted (read-only, after this lane's own results existed)

* `research/theory_audit/fierz_adjudication_2026_08_05.{py,md,json}` — the
  artifact `main.tex:1125-1129` cites. Independently reaches the same row and
  the same `G_s`; its "Caveat" already records the single-species rank-3 point.
* `research/theory_audit/ech_torsion_onshell_2026_08_08.{py,md}` — derives the
  `eq:4fermi` prefactor `[L27]` as `λ²`/`s_H²`-quadratic, i.e. insensitive to
  both sign conventions. Used to report the prefactor's status honestly, not to
  claim it as this lane's result.
* `research/ech_contact_term_2026_09_22/` — lane `bb-LS13-p1n-essentials`
  (DP1N-60/61), the origin of this lane's flag and the source of
  `ρ_{4ψ} = -L_{4ψ}` used in the Poplawski cross-check.

## Independent-verification legs

| Leg | Status |
|---|---|
| `fable` blind adjudicator | **FAILED-INFRA** — HTTP 429, out of usage credits (`req_011CfJMnkioxuZFbia9FVoDR`). Recorded as infrastructure failure, **never** as a verdict. |
| `blind-adjudicator-opus` | substituted per the lane's 429 rule, **label changed**. Given the manuscript's quoted passage and nothing about this lane's conclusion or method, forbidden to read this directory or `research/theory_audit/`, and explicitly permitted to answer "undecidable". Verdict and full report in `RUN_LOG.md`. |

## Known limits of this lane

1. The `-(3κ/16)γ²/(1+γ²)` **prefactor** of `eq:4fermi` was not re-derived here
   from the action. Its status (committed artifact `[L27]`, `λ²`-quadratic;
   independently consistent with Poplawski) is stated in `DERIVATION.md` §4.2 —
   verified elsewhere, not by this lane.
2. The single-species operator degeneracy means the `+1` is the canonical
   declared-projection coefficient, not an unconditional identity, at `N=1`.
   At `N_cN_f > 1` — the setting `eq:gap` assumes — it is unconditional.
3. This lane makes no statement about DP1N-60 or DP1N-61 beyond what
   `bb-LS13-p1n-essentials` established, and does not soften either.

## Reproduce the whole lane

```bash
git checkout 27dd3143           # the pinned manuscript state
for s in fierz_row_sign fierz_exact_and_anchors multispecies_rank; do
  python3 research/fierz_row_sign_2026_09_22/scripts/$s.py \
    | diff - research/fierz_row_sign_2026_09_22/outputs/$s.json && echo "$s OK"
done
```

(`fierz_row_sign.py`'s floating-point tails are platform-stable to the printed
precision; the load-bearing coefficients are the exact rationals in
`fierz_exact_and_anchors.json`.)
