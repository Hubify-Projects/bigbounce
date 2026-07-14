# P2 v1.7.122 convention-clarity closure audit

Date: 2026-07-14 PDT

Scope was deliberately bounded to the P2 manuscript, its compiled PDF, and this frozen proof directory. No readiness, SSOT, site, Convex, review-verdict, API, or deployment surface was changed.

## Closure implemented

- Foregrounded the exact matter-contraction amplitude in the title and removed “Testing” and SPHEREx prominence.
- Renamed the degree-nine momentum polynomial from `P` to `K_9`, leaving all six coefficients unchanged.
- Defined ordered pair and ordered all-distinct triple sums at first use.
- Made Table IV self-contained about `Pi k^2`, ordered sums, and the fact that its rows retain general epsilon dependence; epsilon equals 3/2 only for the stated evaluated limits.
- Added the convention-checked primordial bridge `B_zeta^loc = (6/5) f_NL [P_zeta P_zeta + cyc.]` to `B_Phi^loc = 2 f_NL [P_Phi P_Phi + cyc.]` under `Phi=(3/5)zeta`, explicitly declining an extra 3/5 rescaling.
- Connected the general response `Delta b=f_NL b_phi/M` to the universal-mass-function specialization `b_phi=2 delta_c(b_1-1)`.
- Rounded narrative-only surrogate significances to one decimal while retaining exact Table III and artifact values.

## Verification

- `scripts/p2_vertex_check.py`: squeezed `-35/16`, series correction `35 k_1^2/(64 k^2)`, equilateral `-255/128`, Li check `-35/16`.
- Convention arithmetic: `(3/5)^3 (6/5) / (3/5)^4 = 2` exactly.
- C13 frozen artifact declares `B_phi^loc = 2 f_NL [P_phi P_phi + cyc]`.
- C8 implementation declares `Delta b=f_NL b_phi/M`, `b_phi=2 delta_c(b-p)`, `p=1`.
- TinyTeX compile: clean; 10 pages; no LaTeX error, undefined reference/citation, rerun warning, overfull hbox, or overfull vbox.
- All 10 pages rendered at 144 dpi and visually inspected: no clipping, collision, column spill, broken table, or date/title overflow.
- Raw `texttt` path audit: no unsafe unbreakable repository path.
- Explicit source URL audit: `https://github.com/Hubify-Projects/bigbounce` returned HTTP 200.
- `git diff --check`: clean.

## Integrity boundary

The exact vertex coefficients and all certified algebra are unchanged. The cubic-transfer theorem, external Heinrich per-triangle covariance, fermion/torsion bound, and immutable archive/DOI remain open gates. No readiness uplift or observational detection claim is supported by this clarity closure.

## Hashes

- Baseline source (v1.7.121): `caf63ccd839e22935fd9737e243161e2fcf67a868b9f6a827e54e7b30f29169a`
- Baseline PDF (v1.7.121): `d75d7bfa2f7b8b9ba006137ed7b3da3f099475ba60f1db4886168750866f127e`
- Final source (v1.7.122): `9144e1be05ba38e37271f8ffbb44bf9d52b73235b352f6672abbbcdaf56aaf1a`
- Final PDF (v1.7.122): `4097bac5a9930df7fa73e4a4567a7c60156f6cadb4321e51146dd237e13225c9`
