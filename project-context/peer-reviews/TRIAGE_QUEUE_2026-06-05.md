# Triage Queue — R10v3p1 + Autoloop Fire 1 META findings

Findings that need Houston review or scientific judgment to triage (per `/peer-review-truth-audit` protocol — verdict-first before any closure work).

Severity legend:
- `MECHANICAL`: text/arithmetic fix, no scientific judgment needed
- `STRUCTURAL`: paper organization or new section needed
- `SCIENCE`: requires re-running analysis, new derivation, or interpretation change

---

## P4 (chirality catalog) — v1.0.159 shipped 3 mechanical fixes; deeper issues remain

### MECHANICAL — already shipped in v1.0.159 ✅
- ~~P4-E12 stale `N` (234,282 vs 240,919)~~ FIXED
- ~~P4-E13 dilution factor 0.63 → 0.398~~ FIXED
- ~~P4-E1/E5 abstract "Table II" → "Table I"~~ FIXED

### MECHANICAL — pending (autoloop fire 1 META)
- **P4-META-E1**: A_p has 3 conflicting definitions in same paper.
  Eq. (3): `(NCW-NCCW)/(NCW+NCCW)` ← THE SCIENCE ONE
  Appendix A(a): `f_CW(n) - 0.5` (equivalent to A_p/2 — needs factor-of-2 clarification)
  Appendix A(c): `(NCW-NCCW)/N_total` (WRONG — dilutes field by NS galaxies)
  **Fix**: Edit Appendix A(c) to use spirals-only denominator; add a sentence in App A(a) noting `f_CW - 0.5 = A_p/2`.

### STRUCTURAL / SCIENCE — needs Houston judgment
- **P4-META-E2**: NaMaster weight W_p = N_all (incl NS) but field A_p is spirals-only.
  Options: (a) keep current as "depth proxy" but add appendix justifying noise model; (b) switch to W_p ∝ N_spiral and re-run MASTER. The 0.122σ headline might shift.
  **Houston decision needed**: which weighting is publication-grade?

- **P4-META-E3**: The "99.3% reproduction" claim is for PRE-MASTER. The +3.64σ POST-MASTER residual is asserted to be leakage but not directly tested by passing the leakage-only null through MASTER on canonical mask.
  **Fix**: Re-run the generative monopole-only null end-to-end through full MASTER pipeline on canonical mask; report the +3.64σ-distribution percentile. This is a 1-day computation.

- **P4-META-E4**: Double LEE correction in Appendix C(c) — direct-MC max-stat already includes trials factor; Bonferroni on top is wrong.
  **Fix**: Drop the Bonferroni correction; keep only the direct-MC pLEE ≤ 10^-4. Recompute post-LEE significance accordingly. Mechanical — 1 paragraph rewrite.

---

## P5 (DESI environment) — UNFIXED critical findings

### STRUCTURAL — needs Houston decision
- **P5-META-E1**: Paper claims V-Web (velocity-shear), implementation is T-Web (Hessian of Φ).
  Options: (a) relabel "V-Web" → "T-Web" throughout (abstract, body, figures); (b) re-implement to actually use velocity field via linear theory.
  Option (a) is 30 min of text edits. Option (b) is 1-week of analysis work.
  **Houston decision needed**: which option?

### MECHANICAL — easy
- **P5-META-E2**: Eq. (1) algebra error.
  Currently writes: `σ_pred = ∆f_CW/0.5/√N = 2∆f_CW·√N`
  Should be: `σ_pred = ∆f_CW/0.5/√N = 2∆f_CW/√N` (the second `=` had wrong direction)
  Or: `σ_pred = 2∆f_CW·√N` (correct binomial z from half)
  **Fix**: 1-line text edit. Verify which σ_pred value is actually used in tables, recompute if needed.

### SCIENCE — major rework
- **P5-META-E3**: 3D overdensity δ built from raw spectroscopic counts without DESI radial selection function correction.
  Standard fix: build random catalog matched to selection function, compute weighted δ ∝ (n_data − α·n_rand)/α·n_rand, then smooth/Poisson/classify.
  **Estimated work**: 2-3 days of analysis + re-run + paper update.

### MECHANICAL — easy
- **P5-META-M1**: Table I p50 separation 0.0066″ implausibly small (likely deg-vs-arcsec unit bug).
  **Fix**: verify SkyCoord units, regenerate Table I, add CDF figure in appendix.

- **P5-META-M2**: Quartiles ρ̄ ≈ 0.90-2.21 stated as "log density" but values are not logarithms.
  **Fix**: clarify whether the interpolated field is δ+1, δ, or log(ρ), and rename consistently.

---

## P3 (anomaly catalog) — v3.1.75 shipped 49pp→20pp condensation, deep methodology gaps remain

### STRUCTURAL / SCIENCE — needs Houston judgment
- **P3-META-E1**: 5″ uniform positional dedup across DESI/SDSS/LAMOST (sub-arcsec) + Gaia (sub-0.1″ + PM) + NEOWISE (∼6″ PSF) is naive.
  **Fix**: replace with Budavári–Szalay probabilistic cross-match. **Estimated**: 1-2 days.

- **P3-META-E2**: Planck training set inconsistency — text says 2×10^5 patches but Input is 20,000 and Table V training time 10.6 (sec? min?).
  **Fix**: clarify data splits + correct units. **Estimated**: 30 min.

- **P3-META-E3** through **E7**: additional methodology gaps requiring per-finding analysis.

---

## P1A, P1B (companion bounce papers) — deep theoretical gaps

### SCIENCE — physics audit required
- **P1A-META-E1**: Same coupling implicitly equated across sectors. Needs explicit consistency check.
- **P1A-META-E2**: γ-dependence inconsistency between Sec II.A.2 Eq. (4) and Sec IV.A. Needs reconciliation.
- **P1B-META-E1, E3, E5**: CMB E-B analysis deep gaps.

---

## P2 (f_NL forecast) — meta findings less critical

### Pending review

---

# Cross-paper pattern firings (logged to pattern catalog)

Pattern-037 (future-dated `\date{}`): 6/6 papers, fires consistently. Needs `/paper-pre-review-check` enforcement.
Pattern-038 (σ-mixing without per-juxtaposition qualifier): 6/6 papers, fires consistently. Needs `/paper-pre-review-check` enforcement.
Pattern-039 (abstract Table II/IV cross-ref bug): 5/6 papers. Needs `\ref{tab:label}` audit in `/paper-pre-review-check`.

These 3 patterns will keep firing in every autoloop iteration until the prevention layer is wired up. Manual fixes are not scalable.

---

# Cumulative findings

- P4 closed 10 findings in autoloop fire 1 (the 3 v1.0.159 fixes verified working)
- Open ESSENTIALs across all 6 papers (post-fire-1):
  - P1A: ~10 (mostly theoretical, needs physics audit)
  - P1B: ~10 (CMB E-B gaps)
  - P2: ~5
  - P3: ~12 (catalog methodology)
  - P4: ~5 (post-fix, mostly META-level definition issues)
  - P5: ~10 (T-Web/V-Web critical, Eq.(1) algebra, selection function)
  - TOTAL: ~50+ ESSENTIAL findings across 6 papers
