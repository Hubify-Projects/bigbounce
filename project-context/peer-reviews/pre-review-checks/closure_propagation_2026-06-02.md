# Pattern-030 closure-propagation audit — 2026-06-02

**Scope**: every VERIFIED closure in `findings-archive/` whose action was a
numerical-claim update or framing fix. For each, the audit greps the live
.tex (active text, comments stripped) for residual pre-closure language.

**Sources**:
- `findings-archive/ALL-FINDINGS.json` (8 rolled-up rounds, 40 VERIFIED/PARTIAL closures)
- `findings-archive/2026-06-02_P1A_external.json` (45 VERIFIED, 5 numerical-claim subset)
- `findings-archive/2026-05-15_P4_v1066_external.json` (12 BLOCKER + 12 MAJOR convergent; the original pattern-030 fingerprint)

---

## P1A — paper1a_ech_nogo.tex (v1A.0.40)

### Closures audited

| ID | Round | Closure action | Status |
|---|---|---|---|
| PER-m1 | round-3 (v1A.0.39) | "drop misleading Planck/ACT~DR6 joint framing for the 0.342±0.094 measurement; relabel as WMAP+Planck (Eskilt&Komatsu 2022)" | **PARTIAL — pattern-030 regression in 2 sites** |
| GRO-B1 | 2026-06-02 ext (v1A.0.40 pending) | "ALP birefringence central-value mismatch — Planck/ACT DR6 3.6σ → WMAP+Planck" | superseded by PER-m1; see same residual sites |
| GEM-B2.1 | 2026-06-02 ext (v1A.0.40 pending) | "remove embedded AI-agent + multi-vendor review logs from paper body" | propagated (live text is clean of `v1A.0.28 R7 GPT-ml` style markers; closure log lives in `%` comments only — correct) |
| CGT-M5 | 2026-06-02 ext (v1A.0.40 pending) | "DESI motivation acceptable but should not be used as support for ECH; 3.1-4.2σ wording reframed as DESI 2024-2025" | propagated (line 353 reads "DESI 2024--2025 BAO results suggest dynamical dark energy at $3.1$--$4.2\sigma$" — neutral framing) |
| CGT-m1 | 2026-06-02 ext (v1A.0.40 pending) | "drop bibliography prose about bibkeys" | NOT YET CLOSED in PDF (Eskilt2022b body in P1B .bbl still carries `note {alias of @Eskilt2022 ...}`) — minor |

### Pattern-030 hit detail

**P1A line 1209 — §Systematic Analysis**:
> "The CMB birefringence channel provides the surviving parity-violation evidence from
>  **published Planck/ACT measurements**. For the $\fnl$ channel..."

**P1A line 1727 — §Robustness to Galaxy Spin Null Results**:
> "The parity-violation case rests entirely on CMB birefringence from **published
>  Planck/ACT measurements**."

Both sites are the *body-summary* prose that should have been rewritten when
PER-m1 closed (v1A.0.39). The abstract + §IV (lines 317-318, 1086-1087, 1626-1627)
correctly attribute to "Eskilt & Komatsu" / "WMAP+Planck"; the two §Systematics +
§Robustness summary clauses still carry the pre-closure "Planck/ACT measurements"
shorthand. Counts: 2 active-text Planck/ACT hits remain (vs 0 expected).

**Subtlety**: lines 1209 + 1727 *could* be read as referring to the combined
literature (Eskilt WMAP+Planck + Diego-Palazuelos ACT~DR6), in which case the
honest framing would be "from published WMAP+Planck and ACT~DR6 measurements"
not "Planck/ACT". The shorthand "Planck/ACT" specifically conflates the WMAP+Planck
Eskilt measurement with the ACT-DR6 Diego-Palazuelos measurement — exactly the
error PER-m1 closed.

**Severity if external reviewer surfaces**: MAJOR (pattern-030 reproduces the
exact closure-revert example from P1A v1A.0.39 → v1A.0.40).

### Closures that propagated cleanly

- GRO-m4 (DESI 2025 future-dated citations) — active text uses Diego-Palazuelos 2025 with arXiv:2509.13654 (real preprint).
- GEM-B2.1 (review-log scrubbing) — live text clean.
- CGT-M5 (DESI motivation framing) — line 353 + 1756 neutral.

---

## P1B — paper1b_mcmc_companion.tex (v1B.0.34)

### Closures audited

| ID | Round | Action | Status |
|---|---|---|---|
| PER2-M1 | round-2 (v1B.0.32) | "Eskilt2022b 'joint Planck+ACT' → 'WMAP+Planck'" | **propagated cleanly** (line 520, 930, 1002, 1004 active text all say WMAP+Planck) |
| PER3-B2 | round-3 (v1B.0.33) | "Eskilt 'PR4 NPIPE + WMAP' → 'WMAP9 + Planck 2018 (PR3)'" | **regressed by PER4-B2** (the PR4 NPIPE attribution was correct; over-correction to PR3 reverted) |
| PER4-B2 | round-4 (v1B.0.34) | "Eskilt 'PR3' → 'PR4/NPIPE' restoration" | **propagated cleanly** — line 1004 reads "joint WMAP9 + Planck PR4/NPIPE analysis; ACT~DR6 enters only via the separate" |

### Pattern-030 hit detail

The PR3 ↔ PR4/NPIPE oscillation is **the textbook pattern-030 example** captured
across three rounds (R2 → R3 → R4):
- R2 introduced disambiguation clause "PR4 NPIPE + WMAP" (correct)
- R3 over-corrected to "WMAP9 + Planck 2018 (PR3)" (incorrect — closure-introduced regression)
- R4 restored "PR4/NPIPE" (correct)

The .tex *comment block* preserves this history transparently (lines 68-99 +
115-152 carry the R3 / R4 / R5 closure log). Live text at v1B.0.34 is consistent
with the most recent (correct) state. **No active regression in v1B.0.34.**

This is the canonical pattern-030 case study and is appropriately documented;
the only risk is future cleanup of the comment block re-reverting. Houston has
already filed `% pattern-030-shielded` proposal in the catalog.

---

## P2 — 02_full_draft.tex

### Closures audited

| ID | Round | Action | Status |
|---|---|---|---|
| (none explicit in archive's VERIFIED bucket) | — | — | — |
| Cross-paper PER-m1 ripple | round-3 P1A | "WMAP+Planck attribution" should propagate to P2 since P2 cites the same number | **GAP — P2 line 532 carries `Eskilt \etal~\cite{Eskilt2022} joint Planck analysis` (missing 'WMAP+Planck')** |

### Pattern-030 hit detail

P2 line 532:
> "the $3.6\sigma$ Eskilt \etal~\cite{Eskilt2022} joint Planck analysis and the
>  $2.9\sigma$ ACT~DR6 measurement of Diego-Palazuelos..."

This says **"joint Planck analysis"** which is incorrect — Eskilt 2022 is the
**joint WMAP+Planck** analysis. The active text later in the same sentence
correctly says "joint WMAP+Planck analysis $\beta_{\rm obs} = 0.342^\circ \pm 0.094^\circ$"
so the sentence is internally inconsistent.

This is a **cross-paper pattern-030 hit**: the WMAP+Planck attribution closure
was applied to P1A + P1B but not propagated to P2 (which also cites the same
measurement). External reviewer reading both P1A and P2 sees a "WMAP+Planck" vs
"Planck" inconsistency.

**Severity if surfaced**: MAJOR (cross-paper attribution drift on the same source).

---

## P3 — paper3_draft.tex

### Closures audited

| ID | Round | Action | Status |
|---|---|---|---|
| R3-R7 cumulative | various | "378,280 catalog count headline; 378,080 point-source tier + 200 Planck CMB tier" | **propagated cleanly** (abstract + §Survey Summary + Table I all consistent) |
| Cumulative | various | "319,443 cross-transfer total quarantined as before/after diagnostic, NOT science result" | **propagated cleanly** (line 641 Table caption explicit: "319{,}443 cross-transfer baseline ... preserved as a before/after diagnostic only and is not used as a science result") |
| Cumulative | various | "195,829 = DESI DR1 alone with S>5 cut" | **propagated cleanly** (consistent label across the .tex) |
| Fisher (a) (b) (c) etc | R3-R7 carry | "5-grid Fisher refit, σ(fNL) full Fisher, GR projection" | DEFERRED carries; not closed yet — not in scope for closure-propagation audit |

### Pattern-030 hit detail

**P3 is clean on Pattern-030.** The 378,280 / 378,080 / 200 stratification is
explicit throughout the active text and the deprecated 319,443 + 195,829 numbers
are always presented as diagnostics with explicit "not headline" framing.

Comment-block carries one Planck/ACT mention (line 1 of grep) but on inspection
it's inside the §-comment for the ACT cross-transfer artifact context (correct usage).

---

## P4 — chirality_catalog_paper.tex (v1.0.139)

### Closures audited

| ID | Round | Action | Status |
|---|---|---|---|
| R-multi B11 / cumulative | v1.0.139 | "block-bootstrap σ corrects 264σ naive → 18σ formal exclusion" | **propagated cleanly** (line 1928 active text carries both numbers with explicit "264σ reported only as the upper limit corresponding to the unrealistic assumption of fully uncorrelated per-pixel residuals; 18σ is the headline number for the formal-exclusion claim") |
| R42 carry | v1.0.66 → v1.0.139 | "drop Shamir2022 PASP → MNRAS regression" | not audited here (out of grep target set; flagged in pattern-030 origin doc but appears stable in current PDF per regression-since-R42 in archive) |

### Pattern-030 hit detail

**P4 is clean on the 18σ vs 264σ propagation.** Line 1928 + 4 surrounding
sentences carry the corrected framing. The naive number is *retained* but
labeled as an upper limit; the headline is 18σ. Good practice — see pattern-030
detection rule "if closure was a value update, grep for the new value" → passes.

P4 has one residual `\bibitem{Eskilt:2023}` (line 4469) that points to the
**Cosmoglobe Collaboration** version (a different Eskilt paper) — bibkey shape
collides with P1B's `Eskilt2022b` / P2's `Eskilt2022`. This is a Step-3 (cross-paper)
issue rather than Step-1 (closure propagation), routed to the bibkey audit.

---

## P5 — p5_desi_chirality.tex (v0.1.35)

### Closures audited

| ID | Round | Action | Status |
|---|---|---|---|
| GRO-R2-B1 | round-2 (v0.1.35) | "V-Web void n=428 — abstract led with per-class line; reframe as systematic-dominated for filament/cluster, statistical-dominated for void" | **propagated cleanly** (abstract lines 343-347 carry the exact reframe) |
| GRO-M1 | true95 (v0.1.34) | "V-Web void label dominated by survey-edge artifacts" | **propagated cleanly** (lines 411, 769, 793 all explicit on the systematic) |
| GRO-M2 | true95 (v0.1.34) | "raw |σ|_max=3.94 cited alongside null tests" | **propagated cleanly** (line 793 + Table 822 carry the number with proper null-test context) |

### Pattern-030 hit detail

**P5 clean.** The V-Web environmental-null framing is consistent abstract →
methods → results → discussion, and the n=428 + |σ|_max=3.94 numerics carry
their qualifications everywhere they appear.

---

## Summary table

| Paper | Closures audited | Clean propagation | Pattern-030 hits |
|-------|------------------|-------------------|------------------|
| P1A   | 5                | 3                 | **2 (lines 1209, 1727)** |
| P1B   | 3                | 3 (R4 restored R2)| 0 active (history correct) |
| P2    | 0 (cross-paper)  | 0                 | **1 (line 532 — cross-paper attribution drift from P1A's PER-m1)** |
| P3    | 4                | 4                 | 0 |
| P4    | 2                | 2                 | 0 |
| P5    | 3                | 3                 | 0 |
| **Total** | 17           | 15                | **3 active sites across 2 papers** |

## Recommended closure actions before next external R-round

1. **P1A line 1209** — change "from published Planck/ACT measurements" → "from
   published WMAP+Planck (Eskilt \& Komatsu 2022) and ACT~DR6
   (Diego-Palazuelos \& Komatsu 2025) measurements".
2. **P1A line 1727** — same fix.
3. **P2 line 532** — change "Eskilt \etal~\cite{Eskilt2022} joint Planck analysis"
   → "Eskilt \etal~\cite{Eskilt2022} joint WMAP+Planck analysis". (The sentence
   already says WMAP+Planck two clauses later — fix is local, ~10 chars.)

Each fix is a single `Edit` call. Without them, external R-round will surface
these as MAJOR pattern-030 hits and trigger another round-trip.
