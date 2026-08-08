# P2 — Non-local bounce-shape tails vs the r=0.84 local-template recast

**Date:** 2026-07-05
**Reviewer MAJOR addressed:** "The scalar r=0.84 template-overlap recast (local-template
amplitude recovery) does not model the NON-LOCAL bounce-shape tails. The bounce
bispectrum's deviations from a pure local shape at non-squeezed configurations
could carry signal the local estimator misses, biasing the forecast."

**Verdict:** (a) — the bounce bispectrum is dominantly local; the non-local
(equilateral + orthogonal) tails contribute a BOUNDED correction δr ≤ +0.002 to
the amplitude recovery, i.e. < 0.3 % of the r = 0.84 headline and far below the
quoted ±0.02. The single-template recast is robust. **NO number changed.**

**Artifacts (committed, reproducible):**
- `research/focused_paper_source_integration/scripts/c11_nonlocal_template_projection.py`
- `research/focused_paper_source_integration/scripts/c11_nonlocal_template_projection.json`

Reuses verbatim the committed shape machinery in `null_space_analysis.py`: the
reference coefficient set `c=(2,7,3,-12,-69,19)`, the symmetric degree-9 monomial
basis, the `10/(256 k1²k2²k3²Σkᵢ³)` prefactor, and the k1=1 / 23,098-triangle grid.

---

## Method

The physical bounce bispectrum on the grid is
`B_bounce(k) = BNL(k) × S_local(k)`, where `S_local = 1/(k1³k2³)+2 perms` is the
local geometric envelope and `BNL(k)` is the committed degree-9 polynomial
amplitude ratio (this is exactly the `S_bounce` variable in the committed code;
its `r_cos` reproduces to 0.985). We project `B_bounce` onto the standard
separable template basis (Senatore–Smith–Zaldarriaga 2010 / Planck 2018 NG):

- LOCAL:  `B_loc = 1/(k1³k2³)+1/(k2³k3³)+1/(k3³k1³)`
- EQUIL:  `B_eq  = −B_loc − 2/(k1k2k3)² + [1/(k1k2²k3³)+5 perms]`
- ORTHO:  `B_ortho = −3B_loc − 8/(k1k2k3)² + 3[1/(k1k2²k3³)+5 perms]`

Projection cosines `r_cos(B,T)=⟨B,T⟩_w/√(⟨B⟩_w⟨T⟩_w)` and a JOINT projection of
`B_bounce` onto span{LOCAL,EQUIL,ORTHO} (recovered fraction of the Fisher norm),
under three physically-motivated weights: uniform (the paper's `r_cos` measure),
CMB-Fisher `w∝(k1k2k3)²`, LSS `w∝(k1k2k3)¹`.

**Critical subtlety (why a naive projection misleads):** projecting the bare
amplitude ratio `BNL(k)` (which is nearly FLAT: −2.19 squeezed → −1.12 folded)
instead of the physical bispectrum `B=BNL·S_local` spuriously reports the shape as
"equilateral-like," because a flat ratio resembles the flat equilateral shape.
The physical signal carries the local 1/k³ envelope and IS ~97 % local. The
script projects the physical object.

## Results

| weight | r_cos(LOCAL) | r_cos(EQUIL) | r_cos(ORTHO) |
|---|---|---|---|
| uniform (paper) | −0.985 | −0.45 | +0.94 |
| CMB-Fisher k² | −0.986 | −0.10 | +0.75 |
| LSS k¹ | −0.985 | −0.18 | +0.89 |

**Joint recovered fraction of the Fisher norm** (LOCAL-only → LOCAL+EQUIL+ORTHO):

| weight | LOCAL-only | +EQUIL | +EQUIL+ORTHO | δr (single→multi) |
|---|---|---|---|---|
| uniform | 0.9701 | 0.9723 | 0.9737 | **+0.0018** |
| CMB k² | 0.9718 | 0.9718 | 0.9719 | **+0.0001** |
| LSS k¹ | 0.9708 | 0.9710 | 0.9711 | **+0.0002** |

## Interpretation

1. The bounce bispectrum has |r_cos| = 0.985 with the LOCAL template under EVERY
   weight — it is dominantly local, confirming the paper's 0.985 (which we
   reproduce exactly, −0.9849).

2. The high ORTHO cosine (0.75–0.94) is **not** independent non-local content: the
   orthogonal template is itself built as −3·local + …, so it is collinear with
   local. The JOINT projection removes this double-counting — adding both EQUIL and
   ORTHO raises the recovered Fisher-norm fraction by at most 0.004 (uniform) and
   ≤0.0002 (survey weights). The residual `1−r_cos²≈0.03` is genuinely orthogonal
   to the whole {L,E,O} span, i.e. it is not recoverable equilateral/orthogonal
   signal — it is projection noise, exactly as the paper states.

3. Therefore a joint local+equil+ortho estimator would recover at most
   δr ≤ +0.002 more amplitude than the local-only estimator. This is < 0.3 % of
   the r=0.84 headline and ≪ the ±0.02 quoted uncertainty. **The non-local tails
   contribute a bounded, negligible correction; the r=0.84 single-template recast
   is robust.** The concern is closed at level (a).

## Honest scope note

This projection is geometry-only (the standard shape-cosine metric), matching the
paper's `r_cos`. A fully rigorous statement of the *estimator-mismatch variance*
under the true 3D SPHEREx bispectrum Fisher covariance (with realistic mode
coupling and photo-z window) is not computable from what is in the repo — it needs
the multi-tracer bispectrum noise covariance, which the paper explicitly imports
from Heinrich et al. rather than reconstructing. The bounded δr≤0.002 here is the
shape-space bound; it establishes the non-local tails are geometrically negligible,
which is the specific claim the reviewer challenged.
