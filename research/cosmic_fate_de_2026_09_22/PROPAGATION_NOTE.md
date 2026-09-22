# PROPAGATION NOTE — row 23 → public Open-Questions / genealogy surface

**From:** lane `bb-LS7-row23-fate-de`, 2026-09-22.
**For:** a site lane. This lane edits no site data, no SSOT, no paper `.tex`.
**Layer:** Open Question. This is NOT a BigBounce claim and must not be rendered as
a result, a prediction, or a readiness input.

## P-1 — exact printable text (Open Questions entry, replaces/extends the row-20 entry)

> **Does bounce-compatible dark energy leave a fingerprint we can already see?**
> A future turnaround — the universe stopping its expansion and contracting — is
> impossible under a constant, positive cosmological constant, so it requires the
> dark-energy density to fall to zero and go negative. We crossed the dark-energy
> classes that are compatible with a bounce against that requirement and found three
> that qualify: quintessence and k-essence whose potential crosses zero, and a dark
> sector that steadily drains energy into dark matter. We then asked whether today's
> data can tell any of them apart from ΛCDM. They can — but only above a threshold,
> and the threshold is in the *present-day* equation of state, not in the fate. At
> DESI DR2 precision the separation reaches 1σ once w₀ ≳ −0.95, while the turnaround
> epoch that same threshold corresponds to shifts by a factor of four (54 Gyr vs
> 14 Gyr) depending only on the shape of the potential assumed. Current data
> constrain how fast dark energy is evolving now; they do not measure when, or
> whether, the expansion ends. **Open question.**

## P-2 — one-line status for the ledger/genealogy index

> Row 23 — cosmic fate under bounce-compatible DE: **intersection non-empty (3 classes),
> >1σ DR2-era separation exists above w₀ ≈ −0.95, fate epoch ambiguous by ×4 across
> potential families. Open Question; forecast lane opened, bounded.**

## P-3 — guardrails for whoever renders this

- Never render "a Crunch is possible/likely" — the row-20 verdict is unchanged: under a
  constant Λ > 0 a turnaround is **impossible**, not merely improbable.
- Never present DESI's preferred `w₀ > −1, w_a < 0` quadrant as evidence for a turnaround.
  CPL's own `ρ_DE(a)` is positive for every `a` and never crosses zero (verified
  symbolically, `cross_table.py` lemma L4; memo Eq. 4.1).
- The `1σ` figures are **fixed-parameter** separations, i.e. upper bounds on a
  marginalised result. If a number is quoted publicly, quote `w₀ ≈ −0.95` (the measured
  direction), not a turnaround date.
- Two gaps must be shown as gaps, not omitted: non-minimally coupled scalars have **no**
  turnaround verdict (the condition is frame-dependent), and growth (`fσ8`) was **not**
  computed.

## P-4 — artifacts to link

- `research/cosmic_fate_de_2026_09_22/ROW23_MEMO.md` (verdict + full tables)
- `research/cosmic_fate_de_2026_09_22/cross_table.{py,json}` (symbolic cross-table)
- `research/cosmic_fate_de_2026_09_22/observable_separation.{py,json}` (separations)
- `reproducibility/manifests/experiments/row23_cosmic_fate_de_2026_09_22.json`
- predecessor: `research/archaeology_2025/memos/COSMIC_FATE_MEMO.md` (row 20)
