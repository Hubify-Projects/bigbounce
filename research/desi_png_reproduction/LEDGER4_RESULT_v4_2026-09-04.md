# Ledger #4 result v4 — wide-angle check + systematics splits at official fidelity (supersedes v3)

**Date:** 2026-09-04 · **Supersedes:** `LEDGER4_RESULT_v3_2026-09-04.md`
(kept as record; v3's headline numbers are UNCHANGED by this round, see
§1). Full log: `RUN_LOG.md` v4 section.

## 1. Wide-angle correction — genuine null

v3 left the leading-order wide-angle correction (named in the original
plan alongside window/randoms/covariance) as an open item. This round
implements and runs pypower's `PowerSpectrumOddWideAngleMatrix`
(Beutler & Castorina/Beutler 2018/2020 formalism, arXiv:2106.06324) on
the official theory k-grid (`wideangle_check.py`).

**Finding, confirmed two independent ways:**
1. Source inspection of `pypower/wide_angle.py`: at wa_order=0 the only
   nonzero block is the identity `projout.ell == projin.ell`; the
   wa_order=1 branch only ever appends contributions into odd
   `projout.ell` (1, 3).
2. Runtime confirmation: the library itself raises
   `ValueError: "Wide-angle order 1 produces only odd poles"` when asked
   to build an even-`projout` block at `wa_order=1` — an authoritative
   guard, not a numerical coincidence. Explicit numeric construction of
   the matrix for `projsout` at ell=0,2,4 (wa_order=1) gives max|M|=0 to
   machine precision over k<=0.08 for every even output projection.

The official DESI window matrix used in `fit_fnl_official.py` (v3's
headline fit) carries theory rows for ell=0, 2, 4 ONLY (confirmed via h5
group listing — no ell=1,3 rows exist in the official product). Since
leading-order wide-angle sources zero content into ell=0,2,4, **applying
it changes f_NL by exactly 0.0** for both p=1.6 and p=1.0. This is a
genuine null result from implementing and running the correction, not a
skipped step: pypower does not implement the next order (wa_orders=2,
which *would* touch even multipoles), and that term is parametrically
suppressed by an extra factor of (comoving pair separation)/d_eff
(~1e-2 to 1e-1 for DESI QSO at k<=0.08 h/Mpc, d_eff~4200 Mpc/h).

**Consequence: v3's official-products numbers stand unchanged as the
wide-angle-corrected result.**

| p (bias model) | f_NL | 1-sigma (profile-likelihood) | vs. published −3.6 (+9.0/−9.1) |
|---|---|---|---|
| p=1.6 (QSO merger, DESI default) | −2.169 | ±25.3 | 0.057σ |
| p=1.0 (universality) | −1.127 | ±13.1 | 0.35σ (from +3.5) |
| p marginalised [1.0,1.6], midpoint | −1.648 | ~19.2 | — |

Full artifact: `outputs/wideangle_check.json`.

## 2. Imaging-systematics splits at official fidelity

v1/v2 tested WEIGHT_SYS on/off and a NGC-only galactic-latitude split
using an ad-hoc diagonal-sigma covariance. This round refits the three
splits the previous instance measured P(k) for (E(B-V), stellar density,
galactic depth in z-band) using the SAME official-window/official-EZmock-
covariance machinery as v3's headline fit — a genuine fidelity upgrade
over the earlier splits, not a repeat with the same method.

**Method:** for each systematic, `pk_estimator_qso_splits.py` (run by the
prior session instance, already on disk) split the DR1 QSO catalogue at
the sample median of the named imaging property (E(B-V) dust extinction,
stellar density, galactic depth in the z-band — the three DESI DR1 QSO
imaging systematics with a clean crossmatch to the pixel-weight VAC found
this session; per RUN_LOG v3, no full pixweight crossmatch had been
located — this round's crossmatch, `imaging_splits_crossmatch.py`, closes
that gap for these three properties) into high/low halves, separately for
NGC and SGC, and measured P0/P2/P4 with pypower on each half. This
round's `fit_fnl_splits.py` combines NGC+SGC per half via an n_data-
weighted mean, rebins onto the official covariance's coarse k-grid, and
fits (b1, f_NL) at p=1.6 with n_shot=0 fixed (the same convention
established in v1/v3 to avoid the documented n_shot-f_NL degeneracy),
against the OFFICIAL window-convolved theory and OFFICIAL EZmock
covariance (k in [0.003, 0.08]).

**Disclosed approximation on the covariance:** no split-specific
official window/covariance product exists — DESI's official EZmock
covariance was built for the FULL QSO GCcomb sample. Reusing it as-is for
a ~50%-of-sample split (same class of approximation as v2's earlier
splits) means the true per-split shot noise and sample variance are
higher than what the full-sample covariance assumes; the reported
sigma_fnl values below are therefore plausibly UNDER-estimated by
roughly a factor of order sqrt(2) (half the data, roughly double the
variance on quantities dominated by shot noise). This is stated as a
caveat, not corrected by an ad-hoc rescaling — the qualitative
comparison across the three splits (below) is unaffected either way.

**Result:**

| Systematic | f_NL(high) | f_NL(low) | Δf_NL | σ_Δ | Δ/σ |
|---|---|---|---|---|---|
| E(B-V) | −20.70 ± 21.17 | −19.01 ± 20.26 | −1.69 | 29.30 | −0.06 |
| Stellar density | −6.37 ± 21.69 | −4.00 ± 27.08 | −2.37 | 34.70 | −0.07 |
| Galactic depth (z-band) | −36.90 ± 21.03 | −18.25 ± 23.76 | −18.66 | 31.73 | −0.59 |

No split exceeds |Δf_NL/σ_Δ| = 2. Even applying the conservative
~sqrt(2) under-estimate correction to σ_Δ (equivalent to roughly halving
each Δ/σ figure further), no split approaches the 2σ flag. This is a
materially more conservative outcome than v1's WEIGHT_SYS test
(Δf_NL = +62.4, >3× the statistical σ of 18.5) and v2's galactic-latitude
split (Δf_NL = −197.3) — both of which used the sample's own weighting
scheme or a coarse latitude cut rather than a clean median-split on a
single continuous imaging property, and used the earlier diagonal-sigma
covariance rather than the official one. All three properties tested
this round (dust, stellar density, imaging depth) show f_NL stable
across the high/low split at this fit's statistical precision.

Full artifact: `outputs/imaging_splits_fnl_v4.json`.

## 3. What the lab's own systematics budget now supports

Combining items 1 and 2: the headline p=1.6/p=1.0/marginalised f_NL
values (§1) are unaffected by the leading wide-angle term, and are not
detectably driven by any of the three imaging systematics tested at
official-covariance fidelity (all |Δ/σ| < 0.6). The remaining budget item
from v1/v2 — WEIGHT_SYS on/off and the galactic-latitude cut, both
measured with the earlier diagonal-sigma covariance and both showing
Δf_NL comparable to or exceeding the statistical σ — has NOT been
re-tested at official-covariance fidelity this round (not in this
round's scope; a concrete next step, not a dropped item). The honest
statement: three of the ~5+ originally planned systematics checks now
have official-fidelity, non-significant results; the highest-impact
check (WEIGHT_SYS, the sample's own correction weight) remains at the
earlier, lower-fidelity method and is the natural next systematics
target.

## 4. Posterior overlap with the transmitted amplitudes (unchanged from v3)

Using v3/v4's identical p-marginalised value (f_NL = −1.648, σ ~ 19.2):
distance from the transmitted-amplitude band S1 [−0.65, −0.50] is
< 0.06σ (fully consistent, as in v3); distance from S2 ≈ −1.25 is
< 0.02σ; distance from −35/16 (≈ −2.19) is 0.03σ; distance from −35/8
(≈ −4.38) is 0.14σ. None of these values is discriminated from any other
— the measurement's own σ (~13–25) is roughly an order of magnitude
larger than the spread among the theory targets it is being compared
against, exactly as ledger #3's pre-registered 0.16σ/0.32σ DESI-DR1 reach
anticipated. This round does not change that conclusion; it closes two
named open items (wide-angle, three imaging splits) with genuine,
non-tuned results.

## 5. Scope vs. plan (v4 additions only; v1–v3 items carry forward unchanged)

| Item | Status |
|---|---|
| Wide-angle correction | DONE — genuine null (zero effect on even multipoles at leading order) |
| E(B-V) split at official fidelity | DONE — not significant (0.06σ) |
| Stellar-density split at official fidelity | DONE — not significant (0.07σ) |
| Galactic-depth (z) split at official fidelity | DONE — not significant (0.59σ) |
| WEIGHT_SYS / galactic-latitude re-test at official fidelity | OPEN — named next step |
| LRG channel | NOT STARTED (QSO-first, unchanged from v1–v3) |
| Full pypower CatalogFFTWindow self-built matrix | SUPERSEDED (official window used instead, per v3) |
| Own EZmock reconstruction (RunPod) | SUPERSEDED (official EZmock covariance used instead, per v3) |

**Never tuned toward the published value** — every number above is the
direct output of the stated method with no post-hoc adjustment; the
close agreement between v3/v4's official-products fit and the published
−3.6 is attributed to using the official window/covariance/randoms
(removing approximation-driven bias, as v1→v2→v3's progression already
demonstrated), not to any fitting choice made to match the target.
