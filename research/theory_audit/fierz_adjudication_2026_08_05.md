# Independent Fierz adjudication — frozen monolith vs published P1A (2026-08-05)

## VERDICT: **P1A-CORRECT** — no published-P1A correction required

Adjudicated by independent computation (`fierz_adjudication_2026_08_05.py`,
machine output `fierz_adjudication_2026_08_05.json`; every claim below cites a
tagged line `[L##]` of the script's printed/JSON `log_lines` output). Explicit
4×4 Dirac matrices were constructed in both signatures and the full 5×5 Fierz
matrix for {S,V,T,A,P} was **solved for** from the 256-component tensor
identity; the anticommuting-field map was re-derived independently with an
exact Grassmann-algebra engine. No remembered coefficient table was used.

## The dispute

| | Monolith `arxiv/paper1_unified.tex` App B (L4918–4931, L4991–4994; verbatim twin in P1C App B) | Published P1A `arxiv/paper1a_ech_nogo.tex` (L4818–4855, L4877–4880) + `arxiv/scripts/fierz_lemma_check.py` |
|---|---|---|
| Matrix | ¼[[1,1,1,1,1],[4,−2,0,2,−4],[6,0,−2,0,6],[4,2,0,−2,−4],[1,−1,1,−1,1]] | ¼[[1,1,½,−1,1],[4,−2,0,−2,−4],[12,0,−2,0,12],[−4,−2,0,−2,4],[1,−1,½,1,1]], F_op=−F_c |
| (J⁵·J⁵) → | ¼SS + ½VV − ½AA − ¼PP | SS + ½VV + ½AA − PP |
| G_s | −3κ/64 | −3κ/16 |

## Computed ground truth

- **c-number axial row, physical basis** (Γ_A = γ^μγ⁵ on the physical
  (J⁵·J⁵), tensor half-sum): **(−1, −½, 0, −½, +1)** — identical under
  (+,−,−,−) [L03] and (−,+,+,+) [L05]; all 8 basis variants are
  signature-independent [L06]. Every solved matrix satisfies F²=𝟙 [L02, L04].
- **Operator (anticommuting) axial row**, derived by the exact Grassmann
  engine on four distinct fields (unique solution): **(J⁵·J⁵) → SS + ½VV +
  ½AA − PP**, i.e. row (1, ½, 0, ½, −1) [L08], with the single-Grassmann-
  exchange rule F_op = −F_c confirmed mechanically [L07] and identical in the
  mostly-plus signature [L09].
- **Scalar-channel coupling** from the computed operator row:
  G_s = (−3κ/16)·(+1) = **−3κ/16** [L16] — the published P1A value
  (repulsive; P1A's decisive sign-exclusion leg stands).

## What each source got right / wrong

**P1A (published, v1A.0.127) — CORRECT, every link of the chain:**
- Its tabulated F_c is an exact match to the independently computed c-number
  matrix with the axial class acting on the physical (J⁵·J⁵) and tensor
  full-sum normalization [L12] — so P1A's claim that the Nieves–Pal phases
  "combine to make e_A exactly the physical operator" is verified.
- (F_c)_AS = −1, F_op = −F_c, operator row SS+½VV+½AA−PP: all reproduced
  [L15]; the row is also verified as an exact identical-field Grassmann
  identity [L11]. G_s = −3κ/16 confirmed [L16].
- The released `fierz_lemma_check.py` checks the correct convention and its
  asserted rows agree with this computation.

**Monolith (frozen `paper1_unified.tex` App B, and its verbatim twin in P1C
App B) — WRONG in its stated application:**
- Its matrix (B1) *is* a valid c-number Fierz matrix, but only in the mixed
  basis Γ_A = iγ^μγ⁵ (so e_A = −(J⁵·J⁵)) with tensor half-sum [L13, L14] —
  not the "explicit Dirac matrices, mostly-plus, script-checked" provenance
  the monolith originally claimed (already retracted in P1C v1C.0.2).
- Its decomposition eq:AAdecomp, ¼SS+½VV−½AA−¼PP, matches **no** computed
  convention: not the c-number row and not the operator row, in any of the 8
  basis variants, in either signature [L17]. It is even internally
  inconsistent with B1's own axial row (a spurious extra ¼ on the S and P
  entries) [L18], and it fails the identical-field Grassmann identity test
  [L11].
- Its downstream G_scalar = −3κ/64 (eq:gscalar) inherits the spurious ¼ and
  is wrong; the correct value is −3κ/16 [L16]. (Sign — hence the monolith's
  "repulsive" qualitative conclusion — happens to survive; the magnitude is
  4× too small.)

## Convention statements under which each holds or fails

- P1A holds under its **stated** convention (Nieves–Pal normalized c-number
  matrix + one Grassmann exchange), which the computation shows is equivalent
  to the physical-basis operator rearrangement — convention-robust [L12, L15].
- The monolith's B1 holds **only** if read as a c-number matrix in the
  unstated (iγ^μγ⁵, tensor half-sum) basis [L13]; its eq:AAdecomp and
  G_s = −3κ/64 hold under **no** tested convention [L17].
- The discrepancy is **not** a metric-signature effect: all matrices are
  identical under both signatures [L06, L09].

## Caveat (unchanged from both papers' own scope statements)

For a single species the five quartics obey two exact linear relations
(rank 3) [L10], so *identical-field* rearrangement rows are not unique — the
declared direct-channel convention is what fixes the mean-field G_s. The
canonical distinct-field operator row, which is unique, is P1A's row.
The convention-independent content of the projection lemma (closure on
{SS,VV,AA,PP}, tensor channel absent, O(1) rationals, κ preserved) holds in
every tested convention — consistent with what P1C v1C.0.2's convention note
already asserts.

## Disposition

- Published P1A (Zenodo-archived, v1A.0.127): **no correction required**.
- The deferred item recorded in
  `project-context/peer-reviews/INT_v3/ROUND_2026-08-05-P1C-v1C.0.1-EXACTPDF-847fb143-INTERNAL-READTHROUGH/CLOSURE_NOTES_v1C.0.2.md`
  ("monolith-vs-script Fierz coefficient reconciliation → future dedicated
  verification") is now **resolved by this adjudication**: the frozen
  monolith's App B eq:AAdecomp/eq:gscalar are erroneous; any future thaw or
  reuse of that appendix (including P1C's verbatim App B display) should
  adopt the P1A presentation. This file is adjudication only — no paper was
  edited.
