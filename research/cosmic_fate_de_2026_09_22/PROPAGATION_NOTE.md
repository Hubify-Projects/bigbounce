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

---

## P-5 — GAP-2 closed as a NULL (added 2026-09-22 by lane `bb-LS8-row23-growth`)

**Numbering note for the site lane:** this section was commissioned as "P-3", but P-3 and
P-4 already existed in this file. It is filed as **P-5** so that P-1…P-4 are preserved
verbatim. Where P-5 supersedes earlier wording, the exact text to replace is quoted.

**What changed:** the growth observable that P-3 bullet 4 lists as *not computed* has now
been computed (`gap2_growth/GAP2_MEMO.md`, `gap2_growth/growth_separation.{py,json}`).
**No public number in P-1 or P-2 changes** — the `w₀ ≈ −0.95` threshold and the factor-4
fate ambiguity stand exactly as published. What changes is that a stated gap is now a
stated null.

### P-5a — sentences to APPEND to the end of the P-1 Open-Questions entry

> We then closed the one loophole in that answer. Two of the three surviving classes —
> quintessence and k-essence — share an identical expansion history, so distances can
> never tell them apart; only the growth of cosmic structure could, through the k-essence
> sound speed. We computed it. Over the entire range of sound speeds the model permits,
> the difference is **0.004σ** — the data would have to improve by a factor of **233** to
> see it. The two are observationally the same theory at today's precision, and growth
> also turns out to be roughly nine times weaker than distances at constraining how fast
> dark energy is evolving. **The fingerprint is in the expansion history or nowhere.**

### P-5b — exact replacement for P-3 bullet 4

Replace:

> - Two gaps must be shown as gaps, not omitted: non-minimally coupled scalars have **no**
>   turnaround verdict (the condition is frame-dependent), and growth (`fσ8`) was **not**
>   computed.

with:

> - One gap must be shown as a gap: non-minimally coupled scalars have **no** turnaround
>   verdict (the condition is frame-dependent). The growth gap is now **closed, as a
>   null** — growth was computed and separates nothing (0.004σ between the k-essence and
>   quintessence members; 0.113σ against ΛCDM where distances give 1.00σ). Render it as a
>   completed negative result, never as an open question and never as a positive hint.
> - If the growth number is quoted, it **must** carry "at DESI DR1 full-shape precision".
>   There is no DESI DR2 growth measurement: DR2 is BAO-only, and the one DR2 full-shape
>   analysis that produced an `fσ8` (the Lyα forest, arXiv:2607.27411) **withdrew it for a
>   verified bias**. Never imply a DR2 growth constraint exists.

### P-5c — exact replacement for the P-2 one-liner

> Row 23 — cosmic fate under bounce-compatible DE: **intersection non-empty (3 classes),
> >1σ DR2-era separation exists above w₀ ≈ −0.95, fate epoch ambiguous by ×4 across
> potential families. Growth closed as a null — the k-essence sound speed is
> unmeasurable (0.004σ, 233× short) and growth is ~9× weaker than BAO, so the k-essence
> and quintessence members are observationally degenerate. Open Question; forecast lane
> open and bounded, now resting entirely on the expansion history.**

### P-5d — artifacts to ADD to the P-4 list

- `research/cosmic_fate_de_2026_09_22/gap2_growth/GAP2_MEMO.md` (growth verdict + QC)
- `research/cosmic_fate_de_2026_09_22/gap2_growth/PREREGISTRATION_GAP2.md`
- `research/cosmic_fate_de_2026_09_22/gap2_growth/growth_separation.{py,json}`
- `reproducibility/manifests/experiments/row23-gap2-growth-2026-09-22.json`

### P-5e — additional guardrails for this result specifically

- **Publish the null as a null.** Do not render "growth may yet distinguish them", "future
  surveys could see it", or any forward-looking softening. The measured shortfall is a
  factor of 233 and it is structural: across the whole family the sound-speed signature
  stays a fixed 3.8% of the background signature.
- **Never quote a forecast.** The "233×" is a statement about this calculation against
  this published precision. It is **not** a DESI DR2/DR5 projection and must never be
  rendered as one.
- Do not present the M2 (interacting dark sector) growth numbers as final: that model's
  coupling changes matter–radiation equality, which was not modelled (no Boltzmann code).
  The quintessence/k-essence results carry no such caveat.
- The row-20 verdict is still unchanged and still absolute: under a constant Λ > 0 a
  turnaround is **impossible**. Nothing in P-5 touches it.
