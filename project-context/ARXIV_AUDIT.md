# BigBounce arXiv Readiness Audit

Last updated: 2026-03-03 (final — all items resolved)

## Verdict: ALL ISSUES RESOLVED THROUGH 5 REVISION ROUNDS

Paper is at v0.9.0. All P0, P1, and P2 items have been addressed across 5 revision rounds
(comprehensive audit → arXiv readiness → nuclear option → skeptical coauthor → reproducibility captain).

Remaining pre-submission task: execute actual MCMC runs using the 4 Cobaya YAMLs in `reproducibility/`.

---

## All Items — Resolution Status

### P0 Items (were arXiv blockers) — ALL DONE

#### P0-A: Scope the One-Loop Claim — DONE (Round 2)
- α treated as phenomenological free parameter throughout
- One-loop paragraph reframed as "motivation" not "derivation"
- RG equation removed; Shapiro-Teixeira cited as basis

#### P0-B: Rewrite Operator as Manifest 4-Form — DONE (Round 2)
- Holst term e∧e∧R used in first-order formalism
- All index conventions defined
- Consistent across main.tex, paper.html, mathematics.html

#### P0-C: Reproducibility Bundle — DONE (Round 5)
- Route 2 (Conservative): stock CAMB, no custom modifications
- Created 4 working Cobaya v3.5 YAMLs
- Created Stan galaxy spin model
- Created reproduce scripts
- IMPLEMENTATION_MAP.md and KNOWN_GAPS.md document what exists
- Removed fictional placeholder files (camb_modifications.diff, cobaya_config.yaml, params_bestfit.ini)
- Data & Code Availability section completely rewritten

### P1 Items — ALL DONE

#### P1-A: CMB EB Prediction Formalism — DONE (Round 2 + Round 3)
- Isotropic birefringence β≈0.30° producing C_ℓ^{EB} ≈ 2β(C_ℓ^{EE} − C_ℓ^{BB}) across all ℓ
- Removed narrow ℓ=2-4 bump claim
- All CMB values attributed to literature (Minami & Komatsu 2020, Eskilt 2022)
- β=0.30° removed from abstract (no photon coupling to derive it)

#### P1-B: Galaxy Spin Systematics Plan — DONE (Round 4 + Round 5)
- Galaxy spins reframed as "contested anomaly"
- Null-result paragraph added (Patel & Desmond 2024)
- 37-order-of-magnitude gap explicitly documented
- CNN classifier → "published CW/CCW labels from Shamir"
- A(z) labeled "phenomenological" throughout

### P2 Items — ALL DONE

#### P2-A: Narrative Tightening — DONE (Round 3 + Round 4)
- All "predictions" → "MCMC fits" or "testable outputs"
- All "resolves" → "partially reduces" for tensions
- "comprehensive framework" → "phenomenological framework"
- "uniquely provides" → "distinctive combination"
- Claims Classification Table added as Appendix K

---

## Previously Fixed Items (Rounds 1-2)

| Issue | Fix Applied | Round |
|-------|-------------|-------|
| 7σ → 2.4-2.7σ | Downgraded everywhere | 1 |
| A₀/rotation 9-OOM inconsistency | Parity-odd tidal torque mechanism | 1 |
| M/α normalization | M = M_Pl, α dimensionless | 1 |
| TB null test language | Cross-frequency calibration diagnostic | 1 |
| Appendix G unit error | ω₀ corrected to 1.1×10⁻²⁸ | 1 |
| paper.html dimension typo | "mass dimension 5" → "mass dimension 3" | 1 |
| Deterministic date | \today → "February 28, 2026" | 1 |
| Exclusivity language softened | "uniquely provides" → "distinctive combination" | 1 |
| ZIP README metadata | City, preprint ID, bib count corrected | 1 |

## Items Added in Rounds 3-5

| Issue | Fix Applied | Round |
|-------|-------------|-------|
| Section IX (Detection Timeline) | DELETED entirely | 3 |
| Appendix H (Forecast) | DELETED entirely | 3 |
| Ω_k removed from MCMC | Fixed to 0 (92 e-folds) | 3 |
| Parameter count | 8 → 7 | 3 |
| Inflation vs bounce relic contradiction | Kept inflationary dilution, dropped bounce relic claims | 4 |
| w=-1 freezing not derived | Added honest caveat | 4 |
| Action dimensional inconsistency | Fixed | 4 |
| f(tau_rec) undefined | Addressed | 4 |
| "Geometric Dilution Parameter" | Renamed to "Inflationary Suppression Factor" | 5 |
| MCMC: "modified CAMB v1.5" | → "stock CAMB (no custom modifications)" | 5 |
| CMB analysis implied original | → literature-reported with attribution | 5 |
| CNN classifier | → "published CW/CCW labels" | 5 |
| Fictional reproducibility files | Removed and replaced with working bundle | 5 |

---

## Key Literature References

- Freidel, Minic, Takeuchi (2005): Holst + fermions, Immirzi as parity-violating coupling
- Shapiro & Teixeira (2014): One-loop divergences in quantum EC with Holst term
- Mercuri (2006, 2009): Fermions in Holst action, Immirzi/Nieh-Yan/axion interpretations
- Chandía & Zanelli (1997): Nieh-Yan contribution to chiral anomaly (regulator-dependent)
- Rasulian & Torabian (2023): When Nieh-Yan contributes; IR-scale dependence
- Minami & Komatsu (2020): Planck cosmic birefringence β = 0.35° ± 0.14° (2.4σ)
- Eskilt & Komatsu (2022): Updated β extraction (2.7σ with PR4)
- Saadeh et al. (2016): CMB isotropy bounds on cosmic rotation
