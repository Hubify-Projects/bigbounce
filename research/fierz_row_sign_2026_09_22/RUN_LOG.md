# RUN LOG — lane `bb-LS15-fierz-sign`

All times PT, 2026-09-22. Every step run in the FOREGROUND; no background task,
no `&`, no `nohup` (lanes L6b and L3b were lost that way).

---

**03:50 · START.** Read, in full: the campaign plan and the L1 brief STANDING
RULES; the five RULE lines near the end of the campaign Log (shared-site-data
dispatch block, shared git-index hazard, the `git add && git commit` one-command
amendment, background-poll death); lane `bb-LS13-p1n-essentials`'s complete
output (`DERIVATION.md`, `PROPAGATION_NOTE.md`, `MANIFEST.md`,
`outputs/eos_and_scales.json`) with particular attention to the three places it
flags the Fierz-row sign and says why it did not check it — `MANIFEST.md`
"Known limits" #2, `PROPAGATION_NOTE.md` §6, `DERIVATION.md` §1.7 scope
boundary. Read `arxiv/paper1bc_ech_note/main.tex` @ `v1N.0.7` around
`eq:fierz_row`, every definition and use of `G_s`, §II in full, and §VII.D;
`DISPOSITIONS/P1N.md` DP1N-60/61 via the LS13 ledger lines.

**03:52 · MILESTONE — pre-registration committed alone, `a44bc46d`,** before
any symbolic or numerical result existed: conventions to state and check, the
machinery to build, a validation set that must pass before the answer is
trusted, all three outcome branches (sign correct / sign wrong / undecidable),
and the conditions that would invalidate the lane's own result. START logged to
the campaign at `49db24e5`.

**03:57 · MILESTONE — the row, derived.** `scripts/fierz_row_sign.py`:
explicit 4×4 Dirac matrices in **three** representations (Dirac, Weyl, a real
Majorana basis) × **two** signatures × **two** `γ⁵` sign conventions = 12
combinations, each gated on `{γ^μ,γ^ν}=2η^{μν}`, `(γ⁵)²=1`, `{γ⁵,γ^μ}=0`. The
full 5×5 Fierz matrix was **solved** from the 256-component tensor identity, not
recalled. Results identical across all 12 combinations to `6.7×10⁻¹⁶`;
decomposition residual `1.1×10⁻¹⁵`; the five channel tensors independent at the
tensor level (rank 5).

Pre-declared gates, all **PASS**: `F² = 1` (max deviation `6.7×10⁻¹⁶`);
V−A self-conjugacy (c-number coefficient exactly `-1`, residual `0`, in both a
mostly-minus Dirac basis and a mostly-plus Weyl basis); the Grassmann sign
derived mechanically by adjacent-transposition count (`-1`); the row verified to
hold as an operator identity for a single Dirac field (residual `4.4×10⁻¹⁶`).

**Result: c-number axial row `(-1, -½, 0, -½, +1)`; Grassmann row
`(+1, +½, 0, +½, -1)`. The scalar coefficient is `+1` — the manuscript's
printed row, entry for entry. `G_s = -(3κ/16)γ²/(1+γ²) < 0` unchanged.**

**04:00 · MILESTONE — exact arithmetic + the published-number anchor.**
`scripts/fierz_exact_and_anchors.py` re-solved the same system in exact
rationals over `Q(i)` (`sympy.linsolve`, residual exactly the zero vector) in
both signatures: `S=1, V=1/2, T=0, A=1/2, P=-1`. Also proved that every
contracted channel is *literally the same 256-component tensor* in mostly-plus
and mostly-minus (difference exactly `0`), so "signature-independent" is a
theorem here, not a coincidence.

Poplawski arXiv:1005.0893 anchor: vacuum-saturating the derived row and feeding
his Eq. (9) colour factor reproduces his published Eq. (10)–(11) exactly —
`ρ_Λ = +8.320×10⁻⁶ eV⁴ = (53.71 meV)⁴`, positive, versus his stated
`(54 meV)⁴` — and `(3/16)·(16/9) = 1/3` exactly. The counterfactual `c_S = -1`
gives `ρ_Λ = -(53.71 meV)⁴`, a **negative** cosmological constant, contradicting
his published positive result. **The sign is confirmed against a number obtained
by someone else, by a different method, for a different purpose.**

Exact single-species relation module also computed: operator rank **3**, with
`O_S + ¼O_V + ⅙O_T − ¼O_A = 0` and `O_S + ⅓O_T + O_P = 0`, and the derived row's
self-application `O_A = 2O_S + O_V − 2O_P` verified exactly.

**04:01 · NOTE — the manuscript's own cited artifact.**
`research/theory_audit/fierz_adjudication_2026_08_05.{py,md}`, cited at
`main.tex:1125-1129`, was opened **after** the above results existed. It reaches
the identical row, the identical `F_op = -F_c` rule, `G_s = -3κ/16`, and records
the same single-species rank-3 caveat. The artifact link does what the paper
says it does.

**04:02 · MILESTONE — blind adjudication.**
`fable` leg attempted first per the lane rule: **HTTP 429, out of usage credits**
(`req_011CfJMnkioxuZFbia9FVoDR`). Recorded **FAILED-INFRA, never a verdict**;
substituted `opus` with the label changed to `blind-adjudicator-opus`.

The adjudicator was given the manuscript's quoted passage and the question only
— not this lane's conclusion, not its method — was forbidden to read
`research/fierz_row_sign_2026_09_22/` or `research/theory_audit/`, and was
explicitly permitted to answer "undecidable". Its report, in summary:

> Derived row `(+1, +½, 0, +½, -1)`, identical in all 12 convention
> combinations tested. Consistency checks: dual-basis orthonormality; `F² = 1`
> exactly (max dev `0.00e+00`), eigenvalues `{+1,+1,+1,-1,-1}`; V−A
> self-duality with coefficient exactly `+1`; **and an independent end-to-end
> brute-force Grassmann algebra over 8 generators with raw anticommutation
> only, no traces and no dual bases — residual `0.00e+00` in both signatures.**
> (1) scalar coefficient `+1`. (2) independent of signature, `γ⁵` convention and
> representation, "verified numerically, not just argued". (3)
> `G_s = -(3κ/16)γ²/(1+γ²) < 0`. (4) high confidence; "what I did **not** verify
> is the prefactor `-(3κ/16)` itself in the declared mostly-plus signature —
> that, not the Fierz row, is the remaining load-bearing sign". (5) "unique" is
> wrong as an unconditional operator statement: `rank(1−F) = 2`, two null
> relations, so `J₅·J₅ = 2λS + λV + (1−λ)A − 2λP` for every `λ` (verified at
> `λ = 0, ½, 1, 2, −3`).
> **Tier: CONFIRMED** (row and `G_s` sign correct) with a substantiated
> overstatement on "unique".

Its two null relations are algebraically identical to this lane's, its `λ`
family follows from them, and its unprompted flag on the prefactor is the same
gap this lane had already isolated. The blind leg agrees on everything and
independently corroborates the one wording item.

**04:04 · MILESTONE — the adjudicator's open item, answered as far as it can
honestly be.** The `eq:4fermi` prefactor is **not** this lane's derivation, and
is not left unchecked either: `research/theory_audit/ech_torsion_onshell_2026_08_08.py`
`[L27]` back-substitutes the solved contorsion into the ECH action and obtains
`L_int = -3γ²κλ²/[16(γ²+s_H²)](J⁵·J⁵)` — quadratic in both the source
normalization and the Holst sign, so its sign rides on neither. Independently,
combining `eq:4fermi` with LS13's derived `ρ_{4ψ} = -L_{4ψ}` and this lane's row
reproduces Poplawski's Eq. (10) in sign and coefficient. Reported as
verified-elsewhere, with its provenance stated.

**04:05 · MILESTONE — the multi-species question, settled by computation
rather than asserted.** `scripts/multispecies_rank.py`: operator rank of the
five species-singlet channels is **3** at `N=1` but **5** at `N=2` and `N=3`.
The degeneracy is an artifact of having only four Grassmann components and
evaporates at any multiplicity — including the `N_cN_f > 1` that `eq:gap`'s own
degeneracy factor assumes. So "unique" is correct in the setting the paper's
argument runs in, and the repair is a one-clause qualifier, not a correction.

**04:07 · MILESTONE — propagation hazard found while enumerating the
`G_s`-dependent claims.** The word "repulsive" carries **two different senses**
in P1N: the NJL scalar-channel sense (lines 79, 141, 296, 317, 831–833, 839,
1088 — **correct, must survive**) and the gravitational halts-collapse sense
(lines 126, 129, 209, 213, 1000, 1082 — **must be withdrawn** under DP1N-60).
Lines 1000 and 1082 sit far from §II and are easy to miss. Flagged prominently
for `bb-L3d-p1n-withdrawals` in `PROPAGATION_NOTE.md` §2.

**04:09 · DONE.** Outcome: pre-registration **Branch A** — the sign as printed
is correct. `G_s` unchanged, no claim moves, one MINOR wording qualifier
recommended. Readiness recommendation: hold at 85, no further drop on this item,
and no uplift from it either. No `main.tex`, SSOT, `DISPOSITIONS/` or site-data
file was touched by this lane. Convex is disabled (spending limit): no Convex
write attempted; the intended mutation is queued in
`project-context/CONVEX_BACKFILL_QUEUE_2026-09-21.md`.
