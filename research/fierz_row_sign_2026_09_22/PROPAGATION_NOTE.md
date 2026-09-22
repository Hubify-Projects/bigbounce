# PROPAGATION NOTE → the P1N lane

**From** `bb-LS15-fierz-sign` · 2026-09-22
**Subject** the scalar-channel sign of `eq:fierz_row`, flagged-but-unchecked by
lane `bb-LS13-p1n-essentials`, which drives `G_s`
**Evidence** `DERIVATION.md`, `outputs/*.json`, `MANIFEST.md`, `RUN_LOG.md`
**This lane did NOT edit** `main.tex`, SSOT, `DISPOSITIONS/`, or site data.
Line numbers are pinned to `v1N.0.7` at commit `27dd3143`; P1N is concurrently
owned by `bb-L3d-p1n-withdrawals` and the file will have moved — **match on the
quoted text, not on the number**.

---

## 0. Headline — the outcome is BRANCH A: the sign is CORRECT

The scalar-channel coefficient of `eq:fierz_row` is **`+1`**, exactly as
printed. The full row `(S,V,T,A,P) = (1, ½, 0, ½, -1)` is correct, tensor
channel absent. **`G_s = -(3κ/16)γ²/(1+γ²) < 0` is unchanged**, `eq:gap`'s
three-line argument stands, and **no claim in the paper has to move.**

Derived from scratch in exact rational arithmetic; identical in three Dirac
representations, both signatures, and both `γ⁵` conventions; `F² = 1` satisfied
to `6.7×10⁻¹⁶`; and confirmed against Poplawski arXiv:1005.0893's own published
Eq. (9) sign and his `(54 meV)⁴`, which the opposite sign would have made
negative. An independent blind adjudicator, told neither this lane's conclusion
nor its method and explicitly permitted to answer "undecidable", derived the
same row by its own route and returned **CONFIRMED**.

**This is worth recording rather than passing over.** After DP1N-60 confirmed a
real sign error in §II, the adjacent sign was checked rather than assumed, and
**P1N's remaining §II sign structure is now verified rather than presumed** —
the Fierz row, the `γ→∞` limit, the `G_s` sign, and the gap-equation step that
rides on it. The two withdrawals P1N is taking are its only sign-level
casualties in §II.

**Readiness recommendation: NO FURTHER DROP from 85 on this item.** See §4.

## 0b. Branch B ("sign wrong") — NOT TRIGGERED, stated so the P1N lane need not wonder

The pre-registration (`PRE_REGISTRATION.md` §4) declared, before any result,
what the P1N lane would have had to do if the sign had come out `-1`. It did
not. For the record, and so that no one has to reconstruct it: had the scalar
coefficient been `-1`, then `G_s = +(3κ/16)γ²/(1+γ²) > 0`, attractive;
`eq:gap` step (2) at `main.tex:314-315` would have failed (the right-hand side
`2G_sI` would be positive and a nonzero `M` solution could exist); and the
claims at lines 79–81, 296, 317, 831–833, 839 and 1088 — abstract item (i)
included — would all have had to be **withdrawn**, with `eq:Gs`, `eq:gap` and
the three-line argument deleted rather than reworded. **None of that applies.**
No sentence of P1N needs to change on account of this lane, beyond the optional
one-clause precision fix in §3 and the disambiguation in §2.

---

## 1. Every `G_s`-dependent claim, by line number — all VERIFIED

`v1N.0.7` @ `27dd3143`. Nothing in this column changes.

| Line | Claim | Status |
|---|---|---|
| 78–81 | abstract (i): "show its direct-channel, hard-cutoff, mean-field NJL scalar projection is repulsive, `G_s = -(3κ/16)[γ²/(1+γ²)]`, so the gap equation for this condensate channel has no nonzero solution" | **VERIFIED** |
| 140–141 | "states its conditional-sign gap-equation result" | **VERIFIED** |
| 273–281 | `eq:fierz_row` itself, all five coefficients | **VERIFIED** entry for entry |
| 282–288 | "scalar-channel coefficient is exactly `+1`, **unique**, and signature-independent … the single Grassmann exchange … supplying the overall minus sign relative to the c-number Nieves–Pal identity" | **VERIFIED** for `+1`, for signature-independence (which is a theorem, not a coincidence — §3), and for the Grassmann-exchange provenance. The word **"unique"** needs one qualifier — §3. |
| 289–296 | `eq:Gs`, `G_s = -(3κ/16)γ²/(1+γ²) < 0` at every finite `γ`, `→ -3κ/16` as `γ→∞`, "repulsive" | **VERIFIED** |
| 296–309 | `eq:gap`, `M ≡ -2G_s⟨ψ̄ψ⟩`, `I(M,Λ) > 0` manifest | **VERIFIED** |
| 310–322 | the three-line argument; step (2) "the right-hand side is negative for `G_s<0` while the left-hand side is `+1`" | **VERIFIED** |
| 322–324 | "This conditional-sign result does not exclude other truncations, species structures, non-minimal couplings, or propagating torsion" | **VERIFIED and load-bearing** — keep it; it is what makes §3 a non-issue |
| 831–833 | §VII.D: "the repulsive sign of `G_s` (Eq. `eq:Gs`) means the mean-field gap equation (Eq. `eq:gap`) additionally admits no nonzero condensate at any `n_ψ`" | **internally VERIFIED.** Separately, per DP1N-61, it does not bear on Poplawski — unchanged by this lane, see §5 |
| 839 | "the sign argument (Eq. `eq:Gs`–`eq:gap`)" | **VERIFIED** |
| 1088 | conclusion: "its NJL scalar projection admits no condensate in the declared truncation at any finite `γ`" | **VERIFIED**, and the "declared truncation" qualifier is exactly right |
| 1125–1129 | the artifact item citing `fierz_adjudication_2026_08_05.py` as certifying the scalar coefficient | **VERIFIED** — the artifact exists, does what the sentence says, and an independent re-derivation agrees with it |

---

## 2. ⚠ HAZARD FOR `bb-L3d-p1n-withdrawals` — "repulsive" carries TWO senses

The word **"repulsive"** appears in P1N in two *different* claims that share a
word and have opposite fates. Withdrawing or keeping it globally will be wrong
either way.

| Sense | Lines (`v1N.0.7`) | Fate |
|---|---|---|
| **(A) NJL scalar-channel** — `G_s < 0`, a repulsive scalar coupling, hence no chiral condensate | 79, 141, 296, 317, 831–833, 839, 1088 | **CORRECT — KEEP.** Verified by this lane. |
| **(B) gravitational / halts collapse** — the contact term is repulsive at high spin density | 126, 129, 209, 213, 1000, 1082 | **WITHDRAW** per DP1N-60 (LS13): the corrected `w=+1` equation of state makes the manuscript's own configuration *attractive* (Kerlick 1975 / O'Connell 1977). |

Concretely: `main.tex:1000` — "(a) repulsive at high spin density at every
finite `γ`" — and `main.tex:1082` — "a spin--spin four-fermion contact term,
repulsive at high density at every finite `γ`" — are sense **(B)** and must go
with the DP1N-60 withdrawal, even though they sit far from §II. Conversely
`main.tex:79` and `main.tex:296` are sense **(A)** and must survive it.

Suggested disambiguation where sense (A) is kept, so the distinction is on the
page rather than in a lane's head. Printable:

> its direct-channel, hard-cutoff, mean-field NJL scalar projection is
> repulsive \emph{in the scalar condensate channel},
> $G_s=-(3\kappa/16)[\gamma^2/(1+\gamma^2)]$, so the gap equation for this
> channel has no nonzero solution;

---

## 3. The one repair this lane recommends — the word "unique"

**Finding.** For a strictly **one-species** Dirac field the five quartics
`{SS,VV,TT,AA,PP}` are not independent: the operator rank is **3**, with
`O_S + ½O_V − ½O_A − O_P = 0` and `O_S + ⅓O_T + O_P = 0`. So the row can be slid
along `(J_5·J_5) = 2λO_S + λO_V + (1−λ)O_A − 2λO_P` for every `λ`, and the
scalar coefficient `2λ` is not fixed by algebra alone. Both this lane and the
blind adjudicator found this independently; the manuscript's **own cited
artifact** already records it (`fierz_adjudication_2026_08_05.md`, "Caveat").

**Why it changes nothing.** The `+1` is the canonical single-exchange projection
into the **declared** direct channel, which the manuscript declares explicitly
at `main.tex:288-290` and hedges correctly at `322-324` and `1088`. And the
degeneracy is an artifact of having only four Grassmann components:
`scripts/multispecies_rank.py` finds rank **3** at `N=1` but rank **5** at
`N=2` and `N=3` — so as soon as the field carries any colour/flavour
multiplicity the decomposition, and `G_s`, are unambiguous. `eq:gap` itself
assumes a degeneracy factor `N_cN_f/(4π²)`, i.e. `N_cN_f > 1`. **In the setting
the paper's own argument runs in, "unique" is correct.**

**Printable repair** for `main.tex:282-285`, replacing
*"the scalar-channel coefficient is exactly $+1$, unique, and
signature-independent"*:

> the scalar-channel coefficient is exactly $+1$, signature-independent, and
> unique for the declared direct-channel projection at the colour/flavour
> multiplicity $N_cN_f>1$ assumed in Eq.~\eqref{eq:gap}; for a strictly
> single-species field the five quartics obey two linear relations, so an
> identical-field rearrangement row is fixed only once that projection is
> declared~\cite{FierzAdj2026}.

This is a one-clause precision fix, not a correction: it costs the paper
nothing and closes the only thing two independent legs flagged.

---

## 4. Readiness recommendation — plainly

**Hold at 85. This item takes P1N no lower, and it does not by itself raise it
either.**

Against directive P's composition:

* **Science closure (25):** a flagged, unchecked sign that a headline claim
  rides on has been checked and is correct. No new open item; no withdrawal.
  The `G_s` leg and the no-condensate result are confirmed rather than assumed.
  → **no further drop.** This does not *add* points: verifying an existing claim
  restores confidence, it does not close the two open withdrawals, which is what
  the 95→85 drop was for.
* **Automated review convergence (25):** no genuinely-new real finding. The one
  wording item in §3 is a precision qualifier, not a defect — a MINOR at most.
  P1N's clean-wave clock is unaffected by this lane. → hold
* **Evidence & reproducibility (25):** improved — two self-validating scripts,
  a Q2 manifest, and the `FierzAdj2026` artifact link independently confirmed to
  do what `main.tex:1125-1129` says it does. → hold, marginally better
* **Packaging & PDF hygiene (20):** untouched by this lane. → hold
* **Houston's final personal review (5):** not reached. → 0

**What would raise P1N from 85** remains what `bb-LS13-p1n-essentials` said:
landing the two withdrawals cleanly (`bb-L3d-p1n-withdrawals`, in flight), a
clean recompile, and a fresh exact-version board on the new PDF. This lane
removes one risk from that path — the withdrawals can be landed without
worrying that a second sign is about to fall.

---

## 5. What this lane does NOT claim

* It does **not** re-open or soften DP1N-60 or DP1N-61. Both stand exactly as
  `bb-LS13-p1n-essentials` closed them.
* It does **not** claim the `G_s` argument rebuts Poplawski. It does not, per
  DP1N-61 — and this lane sharpens that *against* the paper: the manuscript's
  own interaction, vacuum-saturated at Poplawski's scale with his colour factor,
  **reproduces** his positive `ρ_Λ = (κ/3)⟨q̄q⟩² ≈ (54 meV)⁴` exactly, since
  `(3/16)·(16/9) = 1/3`. The `G_s` leg is internally sound and externally
  irrelevant to his mechanism.
* It did **not** re-derive the `-(3κ/16)γ²/(1+γ²)` prefactor of `eq:4fermi` from
  the action — the blind adjudicator named that, unprompted, as the remaining
  load-bearing sign. It is derived by a committed independent computation
  (`research/theory_audit/ech_torsion_onshell_2026_08_08.py` `[L27]`, in which
  it appears as `λ²`/`s_H²` and is therefore insensitive to both sign
  conventions) and is independently consistent with Poplawski per §5 above.
  Reported as verified-elsewhere, not as this lane's own derivation, and not as
  unchecked.
* One pre-registered validation gate (Kerlick/O'Connell) turned out **not to
  apply** to a Fierz coefficient — it is a stress-tensor result, already
  adjudicated under DP1N-60. Recorded, not silently dropped;
  `DERIVATION.md` §4.3.

---

## 6. Ledger line, if the P1N lane wants one

Not a disposition item (no reviewer raised it); suggested as a verification
note beneath DP1N-60:

> **Verification note (lane `bb-LS15-fierz-sign`, 2026-09-22).** The Fierz-row
> scalar sign flagged-but-unchecked by `bb-LS13-p1n-essentials` was derived
> independently and is **CORRECT**: row `(1, ½, 0, ½, -1)`, exact rational
> solve, three Dirac representations × two signatures × two `γ⁵` conventions,
> `F²=1` to `6.7×10⁻¹⁶`, and confirmed against Poplawski arXiv:1005.0893
> Eq. (9)–(11) (the opposite sign would give a negative `ρ_Λ`). `G_s =
> -(3κ/16)γ²/(1+γ²) < 0` is unchanged and `eq:gap` stands; no claim moves.
> A blind adjudicator (opus; `fable` leg FAILED-INFRA, HTTP 429) reached the
> same row by its own route: **CONFIRMED**. One MINOR wording item: "unique"
> at `main.tex:283` holds for the declared projection at `N_cN_f>1` but not for
> a strictly single-species reading (operator rank 3 at `N=1`, 5 at `N≥2`);
> printable qualifier in `research/fierz_row_sign_2026_09_22/PROPAGATION_NOTE.md`
> §3. Evidence: `research/fierz_row_sign_2026_09_22/`.
