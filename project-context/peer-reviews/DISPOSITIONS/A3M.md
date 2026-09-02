# Canonical dispositions — A3M (Track A3 multi-channel)

Paper: `research/track_a3_multichannel/paper/main.tex` + `main.pdf`, v3M.0.3, 7 pp,
sha256 `7e35caa05825af0e2cac5cadb21b50b68e913c32583914ca4b07ca23c1e469bd`.
Ledger opened 2026-09-02 at round `ROUND_2026-09-02-A3M-v3M.0.3-EXACTPDF-7e35caa0-R1`.
Full evidence: `INT_v3/ROUND_2026-09-02-A3M-v3M.0.3-EXACTPDF-7e35caa0-R1/A3M_v3M.0.3_R1_truth_audit.md`.

R1 verdicts (verbatim): Claude/Fable INT **MAJOR REVISIONS** (7M/16m) · Grok API `grok-4.3` **REJECT** ·
Gemini API `gemini-3.1-pro-preview` **MAJOR REVISIONS** · Perplexity **ABSENT** (leg not run — recorded
absent, never as clean, Rule 4).
Class counts: **20 GENUINELY-NEW-REAL** (7 MAJOR / 13 MINOR), **5 RE-FLAG-OF-DISCLOSED**,
**8 FALSIFIED**, **3 OPINION/GENRE**, 0 OUT-OF-SCOPE, **0 BLOCKER**.
Clean-wave count: **0** (not converged). Convergence budget (directive R2): 1 of 2 rounds consumed.

**Inherited-fingerprint matches from P2L.** Two P2L dispositions fingerprint-match A3M items and were
carried into this manuscript unfixed: `DP2L-03` (r = 0.84 undefined/unsourced) → **DA3M-06**, and
`DP2L-04` (reference metadata defects, incl. Li+2016 JCAP 03 (2017) 031 / arXiv:1612.02036) →
**DA3M-07 / DA3M-13**. They are genuinely-new *for A3M* (separate manuscript, never corrected here)
but are the same defect class; fix them together across both papers.

---

## OPEN — genuinely-new-real, MAJOR (must close before any convergence claim)

### DA3M-01: PTA channel omits NANOGrav's official γ posterior; SMBHB rejection overstated
- **class:** OPEN (MAJOR). Paper reports γ = 2.567 ± 0.382 from a **30-bin** free-spectrum refit
  (`emcee_freespec.py:37`, `results.json "n_bins": 30`) and a 4.63σ / log₁₀B = +3.85 rejection of 13/3.
  Official NANOGrav 15-yr HD power law (arXiv:2306.16213, verified from source PDF): **γ_HD = 3.2⁺⁰·⁶₋₀.₆
  (5–95 % quantiles, i.e. 1σ ≈ 0.365) on the lowest 14 frequencies**; NANOGrav call 13/3 "moderate
  tension … at the 99 % credible boundary". Against the official posterior 13/3 is **≈3.1σ**, γ=3 is
  0.55σ, and the refit sits **−1.20σ** from official. None of this appears in `main.tex`, though
  `results.json → compare_synthetic_powerlaw.agazie_2023_official` records the official value.
- **closure:** state the official posterior (value, interval type, 14-bin selection) in §IV and Table II;
  present the refit as a secondary, differently-conditioned analysis with its offset; soften abstract and
  §VII A. Optional strengthener: 14-bin refit (~25 s).
- **fingerprint:** NANOGrav official posterior, gamma 3.2, 14 bins vs 30 bins, Agazie 2023, SMBHB 13/3
  tension, 4.63 sigma, log10 B 3.85, undisclosed refit

### DA3M-02: Savage–Dickey factors at γ = 13/3 and γ = 5 are KDE extrapolation into an unsampled tail
- **class:** OPEN (MAJOR). Independent census of `chain_real_freespec.npy` (320 000 × 2):
  **0 samples at γ ≥ 5** (chain max 4.7048), **9 samples at γ ≥ 13/3**, 34 above 4.0.
  Auditor's own Scott-bandwidth KDE gives B(5) = 2.65×10⁻²⁵ vs the paper's 1.86×10⁻²⁴ and
  B(13/3) = 6.46×10⁻⁵ vs 4.52×10⁻⁴ — **bandwidth-controlled, not data-controlled**.
- **closure:** remove B(5)/"6.37σ" from the abstract or replace with an honest bound plus a labelled
  Gaussian z; quote B(13/3) to one significant figure with stated bandwidth sensitivity; drop the
  two-decimal log₁₀B from the abstract.
- **fingerprint:** Savage-Dickey, KDE tail, 6.37 sigma, gamma = 5, zero samples, 320000 chain, bandwidth
  sensitivity, unsampled tail

### DA3M-03: "universal suppression 0 < T ≤ 1/2" is a handoff-scheme bound, not a bound on physical f_NL
- **class:** OPEN (MAJOR). Eq. (5) is arithmetically correct given its premise (independently
  re-derived; no error found). The premise — cubic sourcing frozen at η_h — sits in tension with the
  adjudication note's proven **end-time independence** of the in-in limit
  (`fnl_matter_contraction_adjudication_2026_09_02.md:19`), and T itself spans **0.165–0.409** across
  schemes/backgrounds (`main.tex:288–293`), so "universal" overstates. Assumption **(A4) "the bounce's
  own cubic vertices are switched off"** is explicit in `A2_TRANSMISSION_BRIEF_2026-09-02.md:184–190`
  but absent from the paper. NOTE: the *conditionality on the uncomputed cubic term* is already
  disclosed at `main.tex:294–302` — that half is a re-flag (see DA3M-R1).
- **closure:** delete "universal" (abstract L51, §III L283); relabel as a handoff-scheme bound; add
  assumption (A4) verbatim and one sentence reconciling Eq. (5) with §II. No new computation.
- **fingerprint:** universal bound, T = (1-rho)/2, transmission, handoff eta_h, end-time independence,
  cubic vertices switched off, assumption A4

### DA3M-04: PBH non-monotonicity and anti-correlated-branch dominance undisclosed; "robust" unqualified
- **class:** OPEN (MAJOR). `outputs/pbh_compaction_fnl.json → f_NL_continuity_scan` shows f_PBH at fixed
  amplitude falling ~55 decades from f_NL = 0 to a minimum at −0.35 (7.50×10⁻⁵⁵) then rising ~53 decades
  to −35/8; both candidates sit on the **rising, anti-correlated (ζ_G < 0) branch**
  (`PBH_COMPACTION_NOTE_2026-09-02.md:245–249`). `grep -ni monoton main.tex` → **zero hits**.
  Abstract and §VII A call the ratio "robust" without inheriting §V B's shape-only scope.
- **closure:** publish the continuity scan (one sentence or one table row); state that both candidates
  lie on the rising anti-correlated branch; qualify every ratio statement "within the quadratic local
  map, at excursions where that map is not perturbatively controlled"; scope "robust" to spectrum shape.
  **Do not demote the ratio to an illustration** — it reproduces exactly and holds at all 27 grid points.
- **fingerprint:** f_PBH non-monotonic, continuity scan, anti-correlated branch, J > 1, robust ratio 1.732,
  55 decades, quadratic map truncation

### DA3M-05: four mutually inconsistent statements on whether the factor of two is settled
- **class:** OPEN (MAJOR). `main.tex:48` "has not been settled by an independent second method" vs
  `251–255` "is **CLOSED**" vs `605–612` "settling the factor of two … is a prerequisite" vs
  `624–627` "(item A3-2)". Grok E1 reaches the same defect from the abstract alone.
- **closure:** one wording in all four places, matching the adjudication note: the from-scratch in-in
  confirms the value **within the in-in method**; a method-independent (gradient-expansion / Bianchi-I
  δN) confirmation remains open (item A3-2). Remove "CLOSED".
- **fingerprint:** factor of two settled, CLOSED scope statement, independent second method, A3-2,
  abstract body contradiction

### DA3M-06: r = 0.84 unsourced and undefined in this paper (inherits DP2L-03)
- **class:** OPEN (MAJOR). `survey_reach_fnl.json:5–6` attributes r to an unpublished internal P2 draft;
  brief item **A3-4 is OPEN** ("re-derive at the −35/16 fiducial"); `main.tex:624–625` lists the
  re-derivation as future work while the abstract quotes the r-projected 2.63σ/3.68σ as results.
  No template, noise weighting, or ±0.02 uncertainty is given.
- **closure:** derive r in a short appendix with its uncertainty, **or** drop the r-projected column and
  the abstract's projected significances, keeping a verbal caveat.
- **fingerprint:** r = 0.84, shape overlap, noise-weighted, SPHEREx projected significance, A3-4,
  unsourced adopted number

### DA3M-07: Ref. [7] wrong arXiv ID and wrong journal reference (inherits DP2L-04 class)
- **class:** OPEN (MAJOR). `main.tex:705–707` prints arXiv:**1707.06661** (verified live: *"The Graphical
  Horseshoe Estimator for Inverse Covariance Matrices"*, Li/Craig/Bhadra, stat.ME) and PRD 96, 083521
  (2017). Correct: Agullo, Bolliet & Sreenath, *"Non-Gaussianity in Loop Quantum Cosmology"*,
  **arXiv:1712.08148, Phys. Rev. D 97, 066021 (2018)** (cited correctly in the A2 brief L52).
  Load-bearing for the "orders-of-magnitude enhancement" claim in §III.
- **closure:** fix ID **and** journal ref; re-verify every arXiv ID in the bibliography in the same pass.
- **fingerprint:** reference 7, 1707.06661, 1712.08148, Agullo Bolliet Sreenath, horseshoe estimator,
  LQC non-Gaussianity citation

### DA3M-08: internal audit tags, issue-tracker item numbers, version-history prose and in-body repo URLs
- **class:** OPEN (MAJOR — presentation/venue; both external legs rank ESSENTIAL). Verified at
  §II D:251 ("CLOSED"), §V A:407 ("flagged in the prior version of this paper"), §V B (markdown note
  path), §VII C:616–625 ("item A3-1b/1c/1d/2/3/4"), Reproducibility:642–643 ("superseded"),
  and `main.tex:663` (`\section*{AI Usage Disclosure}`). Directive Q1 points the same way.
- **closure:** sanitize the body to plain prose; move repo URLs/commit hashes into a single Data
  Availability footnote; keep the AI disclosure only if the venue requires it, otherwise move it to the
  cover letter (record the move, never silently delete a disclosure).
- **fingerprint:** internal audit tags, issue tracker item A3-n, CLOSED, superseded, markdown file path
  in body, AI usage disclosure, prior version of this paper, PRD house style

---

## OPEN — genuinely-new-real, MINOR

| id | item | evidence | fingerprint |
|---|---|---|---|
| DA3M-m01 | Fig. 1 caption promises "(top) … (bottom)"; figure has **one** panel | auditor opened `paper/pbh_compaction_fnl.png` (1110×780): single axes | figure caption two panels, one panel, top bottom mismatch |
| DA3M-m02 | "1.14σ" is a Gaussian z on a prior-bounded non-Gaussian marginal | chain gives **P(γ > 3) = 8.97 %** | Gaussian z approximation, P(gamma>3), prior-bounded marginal |
| DA3M-m03 | ESS convention (N/max τ) and τ ≈ 58 unstated | `results.json` ess 5507, autocorr_tau (58.10, 57.99) | ESS convention, autocorrelation time, 5.5e3 |
| DA3M-m04 | Table II caption's "≤ 3×10⁻¹⁵" implies external reproduction; it is self-reproduction | same script, same chain | archived record, 3e-15, self-reproduction wording |
| DA3M-m05 | "leverage grows with \|f_NL\|" true only beyond the −0.35 minimum | continuity scan | leverage grows, minimum at -0.35 (folded into DA3M-04) |
| DA3M-m06 | "1.2\|f_NL\|σ_r ≈ 0.5–2 across the grid" should be split per candidate | note L181: **0.54–1.01 at −35/16, 1.09–2.02 at −35/8** | perturbativity diagnostic per candidate, 1.2 f_NL sigma_r |
| DA3M-m07 | Gaussian-calibrated normalization A\* = 0.131446 absent from the paper (Grok M3) | value only in `pbh_compaction_fnl.json` | Gaussian-calibrated amplitude, A star, normalization, Fig 1 reproducibility |
| DA3M-m08 | 0.16σ and 0.77σ juxtaposed from mutually exclusive priors; asymmetric errors unstated (Gemini E2 ≡ Fable m8) | `main.tex:543–545`; σ 9.0 merger / 7.4 universality | DESI 0.16 sigma 0.77 sigma, not directly comparable, asymmetric interval |
| DA3M-m09 | §II C wording disagrees with the adjudication note on localising Cai's ×2 | note localises to Eqs. (38)–(40) | which line introduces the factor, Cai Eqs 38-40 |
| DA3M-m10 | §II A "exactly as in Refs. [1,4]" vs §II C "off by 2" reads ambiguous | `main.tex:159` vs `228` | same definition different evaluation, Cai Eqs 20-21 |
| DA3M-m11 | Table I ζ(∂ζ)² row is 0 only at leading order O(k²S²) | adjudication note L35 | zeta d-zeta squared row, leading order qualifier |
| DA3M-m12 | r in T = [1+r(1−ρ)]/(1+2r) is complex; text writes \|r\| ≫ 1 | A2 JSON: r = −9iA²I_∞/k³ | complex branch ratio r, mode-mixing weight |
| DA3M-m13 | Abstract cites "Li et al. (2016)"; bibliography JCAP 1703, 031 (**2017**) (Gemini M1; inherits DP2L-04) | `main.tex:41` vs `691–694` | Li 2016 vs 2017, 1612.02036, abstract bibliography year mismatch |
| DA3M-m14 | Chain SHA-256 elided ("50abc38a…10fc"); directive Q2 requires the full digest | reproducibility statement | elided hash, full 64 hex, Q2 reproducibility manifest |
| DA3M-m15 | "nested factor" / "Savage–Dickey factor" used without definition | `main.tex` §IV B | nested Bayes factor terminology undefined |

---

## RE-FLAG-OF-DISCLOSED (do not re-raise; already in the paper)

| id | item | where the paper already says it |
|---|---|---|
| DA3M-R1 | "the T ≤ 1/2 bound is conditional on the uncomputed bounce cubic term" (Grok M1; Fable M2 part a) | `main.tex:294–302` — "an open, potentially dominant, unknown" |
| DA3M-R2 | "the PBH regime is non-perturbative" (Fable M4 part a) | `main.tex:474–478` — "not always perturbatively controlled" |
| DA3M-R3 | "the PBH ratio is not convertible to an observable abundance" (Grok M2) | `main.tex:589` — "f_PBH itself is not quotable" |
| DA3M-R4 | "the in-in confirmation is a single pipeline; no method-independent check" (Grok E3) | agrees with two published results (`main.tex:228–231`); the open part **is** DA3M-05 / item A3-2 |
| DA3M-R5 | "the γ_cr ≲ 0.85 discrepancy with Choudhury et al. is unresolved" (Fable m7) | brief item **A3-1d**, OPEN, blocked on D1 |

---

## FALSIFIED (recorded so no leg re-raises them)

| id | item | why false |
|---|---|---|
| DA3M-F1 | "the 30-bin choice caused the downward γ pull and a narrower error" (Fable M1 sub-claim) | the lab's own synthetic power-law injection **recovers γ = 3.1925 ± 0.4233 with the same 30-bin pipeline** (`results.json`), so the bin choice is approximately unbiased; and official ±0.6 is a **90 %** interval (1σ ≈ 0.365 < the refit's 0.382), so the refit error is not narrower |
| DA3M-F2 | "against the official posterior 13/3 is only ≈ 1.9σ" (Fable M1 sub-claim) | treats ±0.6 as 1σ; it is the 5–95 % half-width. Correct value **≈ 3.1σ**, matching NANOGrav's own "99 % credible boundary" |
| DA3M-F3 | "September 2, 2026 is a future date" (Grok E2 part) | today **is** 2026-09-02. Auto-FALSIFY Rule 3 (training-cutoff artifact; 6+ consecutive rounds, 100 % falsified) |
| DA3M-F4 | "1.14σ should be 1.13σ" (Gemini N1) | (3 − 2.5664653285)/0.3818251516 = **1.13543** → 1.14 to two decimals. Gemini recomputed from the paper's own rounded inputs |
| DA3M-F5 | "'regularized-renormalized- resummed' has an errant space" (Gemini N2) | `main.tex:437–438` — source line break inside a compound; PDF-extraction artifact (Rule 7) |
| DA3M-F6 | "the PBH reversal is a J < 0 sign-flip artifact" (Fable F1, self-refuted) | J < 0 branch contributes ≤ 3×10⁻¹³ of β; the reversal is the anti-correlated J > 1 channel |
| DA3M-F7 | "−35/16 or Table I rows are wrong" (Fable F2, self-refuted) | script re-run reproduces every row; two rows hand-checked |
| DA3M-F8 | "survey-reach or DESI arithmetic is wrong" (Fable F3, self-refuted) | all 14 numbers recomputed exactly; Heinrich+2023 and Chaussidon+2024 abstracts fetched live |

---

## OPINION/GENRE (no closure required; optional in the venue pass)

| id | item |
|---|---|
| DA3M-G1 | Bibliography style inconsistency (JCAP 1703 vs JCAP03(2017)031); Ref. [17] journal ref if published (Fable m14) |
| DA3M-G2 | Abstract ≈ 480 words vs PRD norm ~250 (Fable m16) — do this **after** DA3M-01/02/03/06 so the cuts encode corrected claims |
| DA3M-G3 | "the operative uncertainty is internal rather than observational" undefined in one sentence (Grok N2) |

---

## Scope decisions taken at R1 (auditor recommendations; see §6 of the audit)

1. **PTA** — official NANOGrav posterior becomes the primary comparison; the 30-bin refit is retained as a
   secondary analysis (it is validated by synthetic injection, not discredited); the γ = 5 Bayes factor is
   removed from the abstract.
2. **Transmission** — relabelled a handoff-scheme bound with assumption (A4) explicit; "universal" deleted.
   Computing the cubic term is **not** required for this round (A3-2-class new science).
3. **PBH** — the 1.732 ratio is **kept as a result**, with its regime of validity stated and the
   non-monotonicity disclosed. Demoting it to an illustration is rejected as an unjustified weakening.

No new science is required to close R1. Open science (A3-1b/c/d, A3-2, A3-3, A3-4) belongs on
`project-context/NEXT_SCIENCE_LEDGER.md`, not in this round's closure (directive R1/R2).
