# Reproducibility manifest (directive Q2) — `research/ech_contact_term_2026_09_22/`

**Program** BigBounce · P1N (`arxiv/paper1bc_ech_note`) science closure
**Lane** `bb-LS13-p1n-essentials` · opened & closed 2026-09-22
**Question** Is the ECH contact term's equation of state as §II states it
(`w=-1`), and does §VII.D's rebuttal of Popławski's dark-energy proposal hold?
**Closes** DP1N-60 (ESSENTIAL), DP1N-61 (ESSENTIAL)

## Compute venue and cost

| | |
|---|---|
| Venue | local workstation (macOS, darwin 25.5.0), CPU only |
| GPU / RunPod | **none** — no GPU work in this lane |
| Wall clock | < 1 minute for the full numerical script |
| Reproduction cost | **~$0** (pure arithmetic; no paid API, no cluster, no storage) |
| Peak memory | < 50 MB |
| Determinism | fully deterministic — closed-form arithmetic, no RNG, no seed |

## External data sources and APIs

| Source | Use | Link |
|---|---|---|
| N. J. Popławski, *Cosmological constant from quarks and torsion*, Ann. Phys. **523**, 291 (2011) | primary source for DP1N-61: mechanism, Eqs. (1)–(11), condensate value, `ρ_Λ` result | `arXiv:1005.0893` — abstract + ar5iv full text |
| L. Freidel, D. Minic, T. Takeuchi, *Quantum gravity, torsion, parity anomaly and all that* | provenance of the manuscript's on-shell torsion and contact-term coefficient (cited by `main.tex:176-178`) | `arXiv:hep-th/0507253` |
| Standard ECSK / Weyssenhoff spin-fluid result `ε_spin = p_spin = -κs²/4`, `s² = (ħcn)²/8` | independent cross-check of the derived `w=+1` | torsion-cosmology literature (see `DERIVATION.md` §1.5 check 4) |

No proprietary data. No dataset download. No HuggingFace / Backblaze artifact
(nothing large enough to mirror); `backup-3plus` not triggered — output is text
in-repo plus GitHub.

## Scripts and exact invocation

```bash
cd <repo-root>
python3 research/ech_contact_term_2026_09_22/scripts/eos_and_scales.py \
  > research/ech_contact_term_2026_09_22/outputs/eos_and_scales.json
```

Requires only CPython ≥ 3.8 standard library (`json`, `math`). No third-party
packages, no pinned environment needed. The script `assert`s its own four
known-answer validations and exits non-zero if any fails.

| File | Role |
|---|---|
| `scripts/eos_and_scales.py` | all numerics + the four self-validating known-answer checks |
| `outputs/eos_and_scales.json` | committed output of the above |
| `DERIVATION.md` | the analytic derivation, with primary-source citations |
| `PROPAGATION_NOTE.md` | exact printable sentences handed to the P1N lane |
| `RUN_LOG.md` | lane log (START / MILESTONE / DONE / BLOCKED) |

## Inputs taken from the manuscript (and nothing else)

* `main.tex` Eq. `eq:4fermi` — the contact-term Lagrangian and its coefficient.
* `main.tex:167-168` — signature, `ε_0123`, `κ`, `M_Pl = 1.22089×10²⁸ eV`.
* `main.tex:250-263` — the `n_ψ ∝ a^-3` parametrization and `ρ_Λ,obs = (2.25 meV)⁴`.

Everything else is derived or taken from the primary sources above. The
manuscript's *conclusions* were deliberately not used as inputs.

## Independent-verification legs

| Leg | Status |
|---|---|
| `fable` blind adjudicator | **FAILED-INFRA** — HTTP 429, out of usage credits (`req_011CfJL14ksKRvnaqNLPmeYv`). Recorded as infrastructure failure, never as a verdict. |
| `blind-adjudicator-opus` | substituted per the lane's 429 rule; label changed. Given both questions with neither this lane's conclusions nor its method, and explicitly permitted to answer "undecidable". Verdict recorded in `RUN_LOG.md`. |

## Known limits of this lane

1. §1.7's sign for `⟨J5·J5⟩` in the bounce configuration is established as
   *required* by the corrected condition plus the standard ECSK result, and is
   consistent with Popławski's SVZ evaluation — it is **not** re-derived here.
2. The sign consistency of the manuscript's Fierz row (`eq:fierz_row`, scalar
   coefficient `+1`) with that SVZ contraction is **flagged, not claimed**, and
   needs its own lane: `G_s`'s sign is a separate headline claim.
3. This lane makes no replacement rebuttal of Popławski at the condensate scale.

## Reproduce the whole lane

```bash
git show <this commit> --stat
python3 research/ech_contact_term_2026_09_22/scripts/eos_and_scales.py | diff - \
  research/ech_contact_term_2026_09_22/outputs/eos_and_scales.json
```
Byte-identical output expected.
