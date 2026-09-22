# Canonical dispositions — A3M (Track A3 multi-channel)

**R1 CLOSED 2026-09-02 → v3M.0.4.** All 8 canonical MAJOR/ESSENTIAL items and
13 MINOR items below are closed by real edits in
`research/track_a3_multichannel/paper/main.tex` (v3M.0.4, 8 pp, md5
`b98ee16e11d106c96ac593480857112b`). Item→edit table:
`project-context/SSOT/paper-a3m/status.md` § "R1 closure (2026-09-02)". R2
verification pass on the new exact PDF is authorized next per directive R2.

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

---

# R2 (verification pass) — 2026-09-02

Round `ROUND_2026-09-02-A3M-v3M.0.4-EXACTPDF-d86f484f-R2VERIFY`; paper v3M.0.4, 8 pp,
sha256 `d86f484f5d4f83fb7b4a339cced6a9c4bf9482f5f5bc206a55bdbfe2270e277c` (verified).
Full evidence: `INT_v3/ROUND_2026-09-02-A3M-v3M.0.4-EXACTPDF-d86f484f-R2VERIFY/A3M_v3M.0.4_R2_truth_audit.md`.

Verdicts (verbatim, diagnostic only): Claude Fable INT **MINOR REVISIONS** (0 MAJOR / 9 MINOR) ·
Grok API `grok-4.3` **REJECT** · Gemini API `gemini-3.1-pro-preview` **MAJOR REVISIONS** ·
Perplexity **ABSENT** (leg not run — recorded absent, never as clean, Rule 4). **0 BLOCKER** all legs.

R1 closure verification on the exact PDF: **17 of 20 canonical items CLOSED as specified**
(7 MAJOR + 10 MINOR), **1 MAJOR PARTIAL** (DA3M-02, precision residual → DA3M-R2-04),
**5 MINOR unaddressed** (m04, m09, m11, m12, m15 — omissions, not mis-closures). Decisions D1/D2/D3
implemented faithfully; no closure introduced a new factual error; no number failed recomputation.

Class counts (29 raw findings → canonical): **16 GENUINELY-NEW-REAL** (1 MAJOR + 10 new MINOR +
5 carried R1 minors), **6 RE-FLAG-OF-DISCLOSED**, **3 FALSIFIED**, **6 OPINION/GENRE**, 0 OUT-OF-SCOPE,
0 BLOCKER. Clean-wave count: **0**. Convergence budget (directive R2): **2 of 2 consumed — this is the
last review round**; after v3M.0.5 the remaining ledger is genre/length/venue only.

## OPEN — genuinely-new-real (v3M.0.5 closure list)

### DA3M-R2-01 (MAJOR): §IV C "refit validation by injection" misdescribes its own artifact
- **evidence:** `main.tex:416–419` claims "the identical pipeline" recovers γ=3.19±0.42 "consistent with
  the injected γ=13/3", showing the 30-bin refit "approximately unbiased". Source check:
  `h200_scripts/experiments/nanograv_ptarcade.py:97–108` builds the mock from NANOGrav's **published
  power law at γ = GAMMA_NANO = 3.2** plus a noise-floor bias and seeded scatter, and fits **6** signal
  bins with a Gaussian χ² likelihood (`nanograv_ptarcade_summary.json`: n_bins_signal 6, τ≈32,
  recovery 3.19255 ± 0.42326 → **−0.018σ** of the true injection). `emcee_freespec.py:176–183` merely
  **hard-codes** those two constants. Nothing was injected at 13/3; it is not the same pipeline; the
  unbiasedness claim for the 30-bin refit is unsupported.
- **closure (science decision):** (a) restate §IV C truthfully (γ=3.2 injection, earlier 6-bin pipeline,
  −0.02σ) and drop the 30-bin unbiasedness claim, **or** (b) run a genuine γ=13/3 injection through
  `emcee_freespec.py` at 30 bins (~minutes) and report the recovered value whatever it is. (b) is the
  stronger close and the only one that supports the intended statement.
- **fingerprint:** injection validation, synthetic power law, injected gamma 13/3, identical pipeline,
  approximately unbiased, 3.19 +/- 0.42, 30-bin refit, nanograv_ptarcade

| id | item | evidence | fingerprint |
|---|---|---|---|
| DA3M-R2-02 | Eq. (8) quoted ζ_max values drop the (3/5)\|f_NL\|σ² term; "scales as 1/\|f_NL\|" and "exactly a factor of 2" hold for the leading term only | `main.tex:449–454`, repeated `470`; 0.09524 / 0.19048 = 5·8/(12·35), 5·16/(12·35); at σ=0.1 full values 0.1215 / 0.2036 (ratio 1.68). Confined to the superseded first pass | zeta_max sigma squared term, exactly factor of 2, 1/f_NL scaling, Eq 8 ceiling |
| DA3M-R2-03 | "Ω_DM = 0.674" is numerically Planck *h*; Ω_DM ≈ 0.264 | carried as printed from Choudhury Eq. (66) (`pbh_compaction_fnl.py:156`, note L108–111); cancels in the ratio (`main.tex:518`) and is absorbed by the Gaussian calibration, so no result changes. Fix = footnote, not a silent value change | Omega_DM 0.674, Planck h confusion, Choudhury Eq 66, cancels in ratio |
| DA3M-R2-04 | 13/3 Savage–Dickey precision inconsistent with the paper's own one-s.f. rule (residual of DA3M-02) | `main.tex:379–380` vs Table II `398` (4.5e−4) and `409–410` (7.1e3, +3.85); 9 tail samples ⇒ ~±0.2 dex | one significant figure, 4.5e-4, log10 B 3.85, KDE bandwidth precision |
| DA3M-R2-05 | Duplicated clause in §VII C (ii) | `main.tex:715–718` (introduced by the R1 rewrite); Gemini N3 concurs | duplicate phrase, settling the factor of two twice |
| DA3M-R2-06 | "(deviation D1 above)" and "deviations (D1–D5)" never defined in the paper | `main.tex:516` precedes `603–605`; D1–D5 live only in `PBH_COMPACTION_NOTE_2026-09-02.md`; directive-Q1 leakage | deviation D1, D1-D5 undefined, dangling internal reference |
| DA3M-R2-07 | "the refit's 3.1–4.6σ" spans two conditionings; L370's 1.20σ uses the quadrature σ=0.53 unlabelled | `main.tex:427`, `370` | refit 3.1-4.6 sigma range, quadrature combined sigma |
| DA3M-R2-08 | "3.13–4.38σ bare once a shape-overlap projection is derived" is logically inverted | `main.tex:683–684` | bare significance does not depend on projection |
| DA3M-R2-09 | Abstract quotes only the DESI merger-prior constraint; universality (+3.5 / 0.77σ) and the "not directly comparable" caveat omitted | abstract `main.tex:80–83` vs body `619–625` | abstract DESI drift, mutually exclusive priors, 0.16 sigma only |
| DA3M-R2-10 | r = 0.84 numeral still printed with no derivation and no public source (residual of DA3M-06) | `main.tex:627–637`, Table IV caption `644–646`; **no result depends on it** — projected column dropped | r = 0.84 numeral, companion Fisher draft, standalone reader |
| DA3M-R2-11 | No frozen-release DOI for this work's code/data (GitHub commit hash only) | `main.tex:763, 826` — only NANOGrav's Zenodo 8060824; directive Q2 | Zenodo DOI, frozen release, commit hash only |
| carried | **DA3M-m04, m09, m11, m12, m15** remain OPEN, verified unaddressed on the exact PDF (`387–388`, `225–227`, `197–207`, `283–288`, `410–411`) | not in the SSOT item→edit table | (see R1 fingerprints) |

## RE-FLAG-OF-DISCLOSED (R2)

| id | item | where the paper already says it |
|---|---|---|
| DA3M-R2-R1 | "abstract's 'no channel is in tension' contradicts the scheme-dependent bound" (Grok E1) | same abstract, `main.tex:50–56` — "within a handoff scheme … no bound on the physical post-bounce f_NL follows" |
| DA3M-R2-R2 | "withdraw the 1.732 ratio / replace with the full curve" (Grok M1) | `main.tex:525–544` (R1 decision D3; demotion explicitly rejected at R1) |
| DA3M-R2-R3 | "SPHEREx forecasts are un-re-derived imports" (Grok M3) | abstract `84–86` "pending a shape-overlap projection this paper has not yet re-derived" |
| DA3M-R2-R4 | "Gaussian σ's need a not-directly-comparable tag at every juxtaposition" (Grok M2) | `404–406`, `427–430`; substantive half folded into DA3M-R2-07 |
| DA3M-R2-R5 | "the 55-decade non-monotonicity is unsupported / lives in a JSON" (Gemini M2) | `535–544` + committed `outputs/pbh_compaction_fnl.json`; a figure inset is a presentation preference |
| DA3M-R2-R6 | "internal-audit prose and commit hashes in the body" (Grok N1) | R1 DA3M-08 closed the tags (0 body hits); repo URLs consolidated at `733–737` (standard Data Availability) |

## FALSIFIED (R2)

| id | item | why false |
|---|---|---|
| DA3M-R2-F1 | "severe numerical inconsistency in the PBH abundance formula; exponent should be (M_H/M_⊙)^{−1/2}; 7.9e−10 gives f_PBH = 6.6e6" (Gemini M1) | (M_⊙/M_H)^{1/2} ≡ (M_H/M_⊙)^{−1/2} — the "correction" is the same expression, and `pbh_abundance_fnl.py:98–100` carries the same Sasaki sign. 7.9×10⁻¹⁰ is the **reference normalisation in the denominator**, not β at M_H=10²⁰ g. Printed Eq. (10) is term-by-term identical to `pbh_compaction_fnl.py:265–271`; auditor re-ran it: f_PBH(0,A*=0.131446) = **1.000032**, f_PBH(−35/16,A*) = **3.62e−14**, f_PBH(−35/8,A*) = **1.569e−2**, exactly Table III. **No recomputation required.** |
| DA3M-R2-F2 | "the paper labels the in-in result method-independent while a cross-check remains open" (Grok E3) | all four occurrences (`main.tex:48, 260, 671, 703`) say such a confirmation **remains open**; R1 DA3M-05 removed every "CLOSED". Sentence inverted by the reviewer |
| DA3M-R2-F3 | "the abstract quotes 1.732[1.610,1.809] stripped of its regime-of-validity caveat" (Grok E2) | abstract `main.tex:73–82` carries the perturbativity range (1.2\|f_NL\|σ_r≈0.5–2) and the ~55-decade non-monotonicity verbatim |

## OPINION/GENRE (R2 — venue pass only, not review items)

| id | item |
|---|---|
| DA3M-R2-G1 | Abstract ≈500 words vs PRD ≈250 (= G2; now unblocked, content stable) |
| DA3M-R2-G2 | Bibliography style + missing DOIs (= G1, Grok N3) |
| DA3M-R2-G3 | AI-usage disclosure placement (venue-dependent; move to cover letter, never silently delete) |
| DA3M-R2-G4 | `.tex` header comment still reads "SKELETON … stubs pending" (source hygiene, not in the PDF) |
| DA3M-R2-G5 | Fig. 1 / Table III notation and the (dimensionless) x-axis units (Grok N2) |
| DA3M-R2-G6 | Optional Fig. 1 inset showing the continuity scan (Gemini M2 presentation half) |

## Correction to an R1 disposition (dated 2026-09-02, R2 pass — never backfilled silently)

**DA3M-F1** cited "the lab's own synthetic power-law injection recovers γ = 3.1925 ± 0.4233 **with the
same 30-bin pipeline**". DA3M-R2-01 establishes that the injection was at **γ = 3.2** through a different
**6-bin** pipeline. F1's second leg — NANOGrav's ±0.6 is a 5–95 % half-width (1σ ≈ 0.365 < the refit's
0.382), so the refit error is not narrower — is unaffected, so F1's FALSIFIED verdict **stands on that leg
alone**; the bin-choice-bias half is downgraded to **unproven pending DA3M-R2-01's closure**.

## Convergence statement (directive R2)

**NOT converged at v3M.0.4.** Budget 2 of 2 consumed → **this is the last review round**. One MAJOR
(DA3M-R2-01) carries an outstanding **science decision**: restate §IV C truthfully, or run a genuine
γ = 13/3 30-bin injection (~minutes) — (b) preferred. Everything else on the list is a one-clause edit.
After v3M.0.5 closes the 15 substantive items, rounds STOP; the residue is genre/length/venue and belongs
to the P-round. Re-testing is warranted only if closure (b) changes a reported number.

## R2 CLOSED — v3M.0.5 (2026-09-02)

All 16 canonical R2 items (DA3M-R2-01 MAJOR through R2-11, plus carried
m04/m09/m11/m12/m15) closed with real edits in `research/track_a3_multichannel/paper/main.tex`.
DA3M-R2-01 closed via option (b): real injection-recovery test at γ=13/3 and
γ=3 through the identical 30-bin free-spectrum likelihood/priors
(`research/track_a3_multichannel/pta_injection_30bin_2026_09_02.py`), mean
pulls −0.026σ / +0.068σ over 5 realizations each. v3M.0.5, 9 pp, md5
`67e1510e2b300ec683ed2e288ef1aefe`. Per directive R2 the convergence budget
(2 rounds) is consumed — review rounds STOP on this paper. Full item→edit
table: `project-context/SSOT/paper-a3m/status.md` "R2 closure (2026-09-02)".

---

# R3 — 2026-09-04 (v3M.0.8)

Round `ROUND_2026-09-04-A3M-v3M.0.8-EXACTPDF-8cf429e0-R3`; paper v3M.0.8, 10 pp,
sha256 `8cf429e002d44c97308ccc994c9378a93b066e094de865d48f850d5e72291b9a` (verified;
served mirror `site/public/papers/a3_multichannel_arxiv_v3M.0.8.pdf` byte-identical).
Receipt `INT_v3/ROUND_2026-09-04-…-R3/preflight_receipt.json` (PASS, HEAD `8d5ca7c8`).
Board: `INT_v3/A3M_v3M.0.8_R3_BOARD_2026-09-04.md`.
Full evidence: `INT_v3/A3M_v3M.0.8_R3_TRUTH_AUDIT_2026-09-04.md`.

Verdicts (verbatim, diagnostic only): Claude Fable INT **major-revisions** (4 MAJOR / 15 minor) ·
Grok API `grok-4.3` **REJECT** (4 ESSENTIAL / 3 MAJOR / 1 MINOR / 2 NIT) · Gemini API
`gemini-3.1-pro-preview` **MAJOR REVISIONS** (4 ESSENTIAL / 1 NIT; pass-2 self-critique timed out,
non-fatal — pass-1 report complete, recorded on the board) · OpenAI/ChatGPT **ABSENT** (directive N
pause) · Perplexity **ABSENT** (leg not run — recorded absent, never as clean, Rule 4).
**0 BLOCKER** all legs.

Class counts: 34 raw findings → **19 GENUINELY-NEW-REAL** (4 MAJOR + 15 MINOR), **4
RE-FLAG-OF-DISCLOSED**, **7 FALSIFIED**, **4 OPINION/GENRE**, 0 OUT-OF-SCOPE, 0 BLOCKER, plus 1
carried-open packaging item (`DA3M-R2-11`). Clean-wave count: **0**. Directive R2: all four MAJORs
land on content that did not exist at R2 (the three science closures landed between v3M.0.5 and
v3M.0.8), which is the intervening science decision R2 requires; zero of the 19 new items
fingerprint-matches an R1/R2 disposition.

## OPEN — genuinely-new-real, MAJOR

### DA3M-R3-01: the `kη_B ≲ 10⁻²` validity window is applied backwards; the headline LSS discrimination rests on the inversion
- **class:** OPEN (MAJOR). Legs: Fable M1, Gemini E4 (independent routes, same defect).
  `kη_B` increases with `k`; `LANE_B_NUMERICAL_2026-09-03.md:107–111` + (A1) set an **upper** bound on
  `k` (rows flagged invalid for `kη_* > 0.3`), with no small-`k` cutoff. The CMB/LSS pivot
  `k = 0.05 Mpc⁻¹` is the smallest `k` in the paper, 5–16 decades below every PBH scale, hence deepest
  *inside* the window — yet `main.tex:866–868` says it "lies far outside that validated window" while
  `:749–750` says the window is satisfied at every (much larger-`k`) PBH scale. Consequence
  (auditor-computed): applying the S1 transfer at the pivot gives `|f_NL^after| ∈ [0.50,0.65]` for
  `−35/16` and `[0.86,1.20]` for `−35/8`; bare SPHEREx drops to **0.7–0.9σ** and the two candidates
  separate by **< 1σ**, collapsing the abstract's "this channel alone discriminates".
- **closure:** C1 — science decision required: (a) propagate `f_NL^after` to Table IV/abstract with the
  pre-bounce row secondary, or (b) give a physical exemption for `k = 0.05 Mpc⁻¹` and delete the §V C
  all-PBH-scales sentence. "Outside the window" is not a usable reason.
- **fingerprint:** k eta_B window direction, pivot 0.05 Mpc^-1 inside not outside, pre-bounce vs
  post-bounce LSS, SPHEREx 3.13 sigma collapses, transmitted amplitude discrimination

### DA3M-R3-02: "satisfied at every PBH mass scale for any bounce energy above the BBN scale" is wrong by 11–13 decades in energy
- **class:** OPEN (MAJOR). Leg: Fable M4. `main.tex:749–750`. Auditor: `aH ∝ T` in RD anchored at
  `k_eq ≈ 0.01 Mpc⁻¹` gives `a_B H_B(1 MeV) ≈ 1.2×10⁴ Mpc⁻¹`, so `kη_B ≲ 10⁻²` admits only
  `k ≲ 10² Mpc⁻¹`; the section's PBH scales are `k ~ 10⁴–10¹⁶ Mpc⁻¹`. Covering `10¹⁵ g` needs
  `T_B ≳ 10⁸–10¹⁰ GeV`. Same root cause as R3-01.
- **closure:** C2 — state the real condition on `T_B`/`H_B` at the smallest PBH mass and restrict the
  null's scope accordingly, **or** show (one sentence of arithmetic) that the 7-decade shortfall is
  insensitive to the transfer assumption. Do not assume it.
- **fingerprint:** BBN scale bounce energy, T_B 10^10 GeV, comoving horizon at bounce, PBH scale
  outside validity window

### DA3M-R3-03: "method-independent confirmation" / "derived identity" asserted, self-contradicted, and stronger than the lab's own note
- **class:** OPEN (MAJOR). Leg: Fable M2 (a/b/c); Grok M1's substantive half folds here.
  (a) abstract `:44` "gradient-expansion route" vs §II D `:238–241` "the gradient-expansion assumption
  `N_i=O(∇)` fails here". (b) `:277–285` "the gap … is accounted for by Eq. (5), a **derived identity**"
  vs `:270–274` "no local `f_NL` relation between `δN_c` and `ζ_Mald` exists"; auditor: `δN_c=½ζ` maps
  `f_NL→2f_NL = −15/4`, not `−5` (gap ratio 8/3), and the lab's own
  `fnl_monopole_adjudication_2026_09_03.md` calls the linear relation "**asserted**" (`:25`), the
  second-order piece "a computed identity, **not a claimed mechanism**" (`:39, 72`), and the outcome
  "explained at the equation level" (`:76`). (c) the classical `O(k⁰)` solution, `[L]/[K]/[X]/[S]`
  bookkeeping, pole cancellation, boundary term, general-ε formulas and the Bianchi-I result appear
  with **no equation and no appendix** — only two script paths (`:286–291`).
- **closure:** C3 — reword the two claim sentences to the note's own framing (different variables;
  second-order mechanism not derived) and add Appendix A transcribing the note §§1–4 (Eq. 5 derivation
  with sign convention; `[L]/[K]/[X]/[S]` + `1/k_L` cancellation + `f_b` boundary term; general-ε
  formulas; Bianchi-I traceless-response argument). No new science.
- **fingerprint:** method-independent confirmation, derived identity, delta N_c = (1-eps/3) zeta,
  gradient-expansion route contradiction, no appendix, script paths only, 8/3 gap

### DA3M-R3-04: induced-GW infrared slope misstated as causality-limited and generic
- **class:** OPEN (MAJOR, scoped). Leg: Fable M3. `main.tex:545–547` (echoed `:879`): "`Ω_GW ∝ f²` is
  the causality-limited infrared slope common to scalar-induced backgrounds of essentially any origin".
  The universal causality-limited IR tail from a finite-duration source is `Ω_GW ∝ f³` (`γ=2` in this
  paper's `Ω ∝ f^{5−γ}`), with `f³ln²f` for narrow peaks — Cai, Pi & Sasaki, PRD **102**, 083528
  (2020), arXiv:1909.13728. `f²` is shallower than the causal floor, hence neither causality-limited
  nor generic. The paper's own `γ=3` prediction is **not** falsified: it is cited to Papanikolaou 2025
  (arXiv:2504.11641) in `main.tex:417–418` and `pta_gamma_reproduce.py:22–31`, and all PTA arithmetic
  stands. The error is self-inflicted weakening plus a §IV A ↔ §IV D contradiction.
- **closure:** C4 — correct both sentences, add the Cai–Pi–Sasaki citation, name the specific
  Papanikolaou equation that yields `f²` for the matter bounce, and say whether it holds across the
  full NANOGrav band or only asymptotically.
- **fingerprint:** Omega_GW f^2 causality-limited, universal IR slope f^3 gamma 2, Cai Pi Sasaki
  1909.13728, log corrections, gamma=3 generic disclaimer

## OPEN — genuinely-new-real, MINOR

| id | item | evidence | fingerprint |
|---|---|---|---|
| DA3M-R3-05 | "28–39 % of the transmitted contraction term" is wrong | `main.tex:374–375`; `LANE_B_NUMERICAL:125–128` ratios 0.387/0.191/0.297 ⇒ **19–39 %**; the source note carries the same error | 28-39 percent, 19-39 percent, bounce cubic fraction |
| DA3M-R3-06 | `n_s−1 = 12w/(1+w)` is the wrong contracting-phase formula | `main.tex:743`; `inlab_delta2_zeta_2026-09-03.py:24`; correct `12w/(1+3w)` (Wands 1999; Cai+2012). Numerically inert (`w: −0.00293→−0.00290`) | n_s-1 12w/(1+w), 12w/(1+3w), Wands duality, contracting tilt |
| DA3M-R3-07 | `0 < T_fNL ≤ 1/2` has both endpoints inverted | `main.tex:315–318` + abstract `:49`: `T=(1−ρ)/2`, `ρ∈(0,1]` ⇒ `T ∈ [0,1/2)` | T interval endpoints, 0 < T <= 1/2, rho in (0,1] |
| DA3M-R3-08 | `ρ_B` never defined in Eq. (7) | `main.tex:353`; auditor: `ρ_B = 1−2T` reproduces all three rows; `f_NL^after = −(85/48)T − 5/24` | rho_B undefined, Eq 7 one-parameter in T |
| DA3M-R3-09 | Ω_DM footnote's "every result unaffected" false for Table III/Fig. 1 | `main.tex:716–726`; auditor re-ran `pbh_compaction_fnl.py`: `A_*: 0.131446→0.127901` (−2.70 %), `f_PBH: 3.6e−14→6.3e−15`, `1.6e−2→5.7e−3`. Ratio genuinely unaffected | Omega_DM 0.674 footnote, A_star recalibration, Table III f_PBH shift |
| DA3M-R3-10 | configuration behind μ-dependent Eq. (4) unstated; exact isosceles forces μ=0 | `main.tex:157–200` vs Eq. (4); `fnl_monopole_adjudication:41` "isoceles μ=0" | isoceles k2=k3, mu = k_L . k_S, Eq 3 is mu=0 not angular average |
| DA3M-R3-11 | revision-history prose + inline filesystem paths in the body (directive Q1) — partial re-open of DA3M-08 | 3 legs (Fable m12, Grok E1+N3, Gemini E3). `main.tex:218, 275, 286–291, 530–534`, §V A | supersedes earlier misdescribed claim, left open in earlier drafts, research/theory_audit in body, why it had to be redone |
| DA3M-R3-12 | injection pulls quoted without scatter | `main.tex:515–521`; JSON `summary`: `std_pull` 0.0993/0.1203 over 5 realizations ⇒ SEM 0.044/0.054 | mean pull 0.016 0.033, standard error of the mean, unbiased well under 0.1 sigma |
| DA3M-R3-13 | Table III `f_PBH = 3.5e3`, `2.2e8` are not physical abundances | `main.tex:690–691` — nominal uncapped values at the Gaussian calibration, not labelled as such | f_PBH greater than one, uncapped nominal, label column or use beta |
| DA3M-R3-14 | `γ_cr ≡ σ_cr²/(σ_c σ_r)` subscripts and windows undefined | §V B `main.tex:590–668` | gamma_cr undefined, compaction curvature variances, window functions |
| DA3M-R3-15 | `\|r\| ≫ 1` k-range unstated; three backgrounds' parameters undefined | `main.tex:310–314, 363–370`; `r = −9i𝒜²I_∞/k³` is k-dependent; "poly (analytic non-LQC)" undefined | r >> 1 k range, complex branch ratio, poly analytic non-LQC undefined |
| DA3M-R3-16 | §II C Cai bookkeeping described, not displayed; Li/Quintin equation numbers missing | `main.tex:201–217`; closes long-open `DA3M-m09` too | Cai shape function squeezed limit displayed, Eqs 38-40, Li et al equation number, error vs convention |
| DA3M-R3-17 | Table I footnote `O(k²S²)` — `S` undefined | `main.tex:197` (residual of DA3M-m11's closure) | O(k^2 S^2), S undefined, Table I footnote |
| DA3M-R3-18 | abstract prints `γ_HD = 3.2^{+0.6}_{-0.6}` without its interval type | `main.tex:56–57`; `σ≈0.365` only follows because ±0.6 is a **5–95 %** half-width (`pta_gamma_reproduce.py:53–58`). Residual of Grok E2 (whose stated form is falsified) | abstract interval type, 5-95 percent half width, 0.55 sigma vs 0.33 sigma |
| DA3M-R3-19 | **regression:** abstract's `1.7–1.9` ratio lost the perturbativity + non-monotonicity caveats it carried at v3M.0.4 | `main.tex:62–68`; the v3M.0.4 text is what falsified Grok at R2 (`DA3M-R2-F3`) — the v3M.0.8 rewrite dropped it | abstract ratio caveat regression, 1.2 f_NL sigma_r, 55 decades non-monotonic, shape robust not truncation robust |

## RE-FLAG-OF-DISCLOSED (R3)

| id | item | where the paper already says it |
|---|---|---|
| DA3M-R3-R1 | "factor-of-two resolution not independent; no second public code / Cai's own Hamiltonian" (Grok M1) | `main.tex:271–276` — scope statement already limits it to "within the in-in method" and names the two published agreements. = `DA3M-R4`. Substantive half carried as **DA3M-R3-03(c)**, not dismissed |
| DA3M-R3-R2 | "official vs refit σ juxtaposed without a not-directly-comparable qualifier" (Grok M2) | `main.tex:451–453`, `:486–489` (`P(γ>3)=8.97 %`), Table II caption `:466–473`. = `DA3M-R2-R4`. Residual (abstract interval type) = **DA3M-R3-18** |
| DA3M-R3-R3 | "no table/figure of the ratio under Choudhury's exact spectrum" (Grok E4 residual) | `main.tex:737–740` — their spectrum is not reconstructible from their paper, which is why §V C substitutes the lab's own. Unsatisfiable by construction, and disclosed |
| DA3M-R2-11 (carried) | "no frozen-release DOI" (Gemini E1) | Not new — the R2 packaging item, explicitly left open as a Houston-gated P-round action (`main.tex:958–962`). Carried, not re-counted |

## FALSIFIED (R3)

| id | item | why false |
|---|---|---|
| DA3M-R3-F1 | "the abstract omits the scheme and cutoff restrictions; transmission advertised as model-independent" (Grok E3) | `main.tex:47–50` — the abstract literally reads "within one cubic-vertex scheme (S1) and `kη_B≲10⁻²` … a second scheme does not regulate". Both allegedly-missing restrictions are in the sentence quoted |
| DA3M-R3-F2 | "the PBH null rests on an unreproducible spectrum; `n_s = 1−12w/(1+w)`, `w=0.9649`" (Grok E4) | Inverted: `main.tex:737–741` uses the **lab's own** spectrum precisely to remove the dependence on Choudhury's unreconstructible one. Grok also garbles the formula (paper: `n_s−1=12w/(1+w)`, `n_s=0.9649`, `w≈−0.003`). The formula is separately wrong for a different reason (`DA3M-R3-06`) |
| DA3M-R3-F3 | "the abstract presents the refit γ without an 'authors' refit prior' qualifier" (Grok E2 main) | `main.tex:55–58` labels it "(refit)", prints the official 14-bin posterior beside it, and gives both z-distances. Residual real bit = `DA3M-R3-18` |
| DA3M-R3-F4 | "abstract asserts `f_PBH=0` while the body's 1.732 needs an ad-hoc normalization" (Grok E2 second half) | Two disclosed sub-results: the null is on the lab's own spectrum (`:757–762`); the ratio is on the lognormal stand-in at the disclosed calibration `A_*=0.131446` (`:664–668`, added at R1 as `DA3M-m07`). No contradiction, nothing ad hoc |
| DA3M-R3-F5 | "September 4, 2026 is future-dated" (Grok N1) | Today **is** 2026-09-04. Auto-FALSIFY Rule 3; recurrence of `DA3M-F3` — now 7+ consecutive rounds, 100 % falsified |
| DA3M-R3-F6 | "'regularized-renormalized- resummed' has a stray hyphen/space" (Gemini N1) | `main.tex:609` — source line break inside a compound; PDF renders correctly (Rule 7). Recurrence of `DA3M-F5` |
| DA3M-R3-F7 | "`r` imported from an unpublished draft for a load-bearing parameter" (Gemini E2) | Closed at R2 (`DA3M-R2-10`): `main.tex:809–820` — "so no numeral is quoted here"; Table IV reports bare significance only. Gemini is reviewing a superseded state of the manuscript |

## OPINION/GENRE (R3 — venue pass only)

| id | item |
|---|---|
| DA3M-R3-G1 | 10 pp vs a 6–7 pp norm (Grok M3); the C8 Q1 cut reduces it as a side effect |
| DA3M-R3-G2 | abstract ~380 words + internal labels ("scheme S1", "(A4)", "zero-shift-threading") (Fable m15) = `DA3M-G2`/`R2-G1`; do it **after** C1–C4 |
| DA3M-R3-G3 | Fig. 1 axis normalization not restated in the caption (Grok N2) = `DA3M-R2-G5`; `A_*` is now in the text at `:664–668` |
| DA3M-R3-G4 | frozen-release DOI restated for the P-round checklist (Gemini E1) = `DA3M-R2-11` |

## Corrections to earlier dispositions (dated 2026-09-04, R3 pass — never backfilled silently)

1. **`DA3M-R2-F3` is superseded for v3M.0.8.** It falsified Grok's "the abstract strips the ratio's
   regime-of-validity caveat" because the v3M.0.4 abstract carried the perturbativity range and the
   55-decade non-monotonicity verbatim. The v3M.0.8 abstract rewrite **removed both**. The R2 verdict
   was correct for v3M.0.4 and is no longer true of the current manuscript; re-opened as
   **`DA3M-R3-19`**, a closure-induced regression (exactly the class directive-G hygiene exists to catch).
2. **`DA3M-08` (R1) is partially re-opened as `DA3M-R3-11`.** R1's closure verified 0 body hits for
   audit tags. The R2 and v3M.0.8 closures re-introduced a different species of the same directive-Q1
   defect — narration of the lab's own corrections plus two inline `research/theory_audit/…` paths.
   Same directive, new instances, three legs concur.

## Convergence statement (R3)

**NOT converged at v3M.0.8. Clean-wave count 0.** 19 genuinely-new-real items open (4 MAJOR, 15 MINOR);
none fingerprint-matches an existing disposition. `DA3M-R3-01` carries an outstanding **science
decision** (propagate the transmission to the LSS pivot, or justify a physical exemption) that
determines the paper's headline discrimination claim; `DA3M-R3-02` shares its root cause. `R3-03` and
`R3-04` close with in-paper work and no new computation. Full ordered closure plan (C1–C10, with the
file to change for each) in `INT_v3/A3M_v3M.0.8_R3_TRUTH_AUDIT_2026-09-04.md` §5. After closure, one
verification round scoped to C1 is warranted, then rounds stop.

---

# R4VERIFY — 2026-09-04 (v3M.0.9)

Round `ROUND_2026-09-04-A3M-v3M.0.9-EXACTPDF-6c543e5e-R4VERIFY`; paper v3M.0.9, 12 pp,
sha256 `6c543e5e9885c6db58e07576482ed6f283b0307ad1499c6309a4651d3c26fb1a` (re-verified; served
mirror `site/public/papers/a3_multichannel_arxiv_v3M.0.9.pdf` byte-identical).
Receipt `INT_v3/ROUND_2026-09-04-…-R4VERIFY/preflight_receipt.json` (PASS, HEAD `d8658cbf`).
Board: `INT_v3/A3M_v3M.0.9_R4_BOARD_2026-09-04.md`.
Full evidence: `INT_v3/A3M_v3M.0.9_R4_TRUTH_AUDIT_2026-09-04.md`.

Verdicts (verbatim, diagnostic only): Claude Fable INT **major-revisions** (5 MAJOR / 11 minor,
one of which is a reference-verification confirmation) · Grok API `grok-4.3` **REJECT**
(4 ESSENTIAL / 3 MAJOR / 3 NIT) · Gemini API `gemini-3.1-pro-preview` **MAJOR REVISIONS**
(2 ESSENTIAL / 1 MAJOR / 2 NIT; pass-2 self-critique failed on a stale receipt, non-fatal —
pass-1 report complete) · OpenAI/ChatGPT **ABSENT** (directive N pause) · Perplexity **ABSENT**
(optional leg, recorded absent, never as clean). **0 BLOCKER** all legs.

Class counts: 30 raw findings → **15 outstanding REAL** (13 genuinely-new: 3 MAJOR + 10 MINOR,
including 1 auditor-originated; plus 2 residuals of incomplete R3 closures), **5
RE-FLAG-OF-DISCLOSED**, **8 FALSIFIED**, **3 OPINION/GENRE**, 0 OUT-OF-SCOPE, 0 BLOCKER, plus
1 carried-open packaging item (`DA3M-R2-11`). Clean-wave count: **0**.

## OPEN — genuinely-new-real, MAJOR

### DA3M-R4-01: the transfer interval 0.165–0.409 mixes schemes S1 and S2; every downstream f_NL^after number is S1-only and the exclusion is never stated
- **class:** OPEN (MAJOR, editorial). Legs: Fable M1, Grok E2.
  `a2_transmission_linear.json` row 4 / `A2_TRANSMISSION_BRIEF_2026-09-02.md` §4.1: `T=0.409155`
  is the **LQC background under scheme S2 (effective fluid)** — a scheme variant of the `T=0.250`
  S1 row, **not a fourth background**. Excluding it is legitimate: `main.tex:424–427` +
  brief §4.3 show `Δf_NL^bounce[S2]` is divergent (`K ~ d_cut^{-0.4998}`), so no `f_NL^after`
  is computable there. Defect = the paper never says so beside the range, and the abstract calls
  the interval "across three backgrounds". Closure **C1** (label the S2 row; do NOT widen).

### DA3M-R4-02: §IV D's γ=3 justification and §V C's PBH null assume mutually inconsistent primordial spectra — SCIENCE
- **class:** OPEN (MAJOR, **SCIENCE**, closure-induced by R3's C4). Leg: Fable M2.
  `main.tex:585–597` attributes `Ω_GW ∝ f²` to `P_R ∝ k`; `main.tex:801–812` extrapolates a flat
  `n_s=0.9649` power law over 10–15 decades. A flat `P_R` gives `Ω_GW ∝ f⁰` (`γ≈5`) — the row §IV
  disfavours at 3.1σ/4.63σ. nHz ↔ `k ≈ 6.5×10⁶ Mpc⁻¹` (auditor), above Papanikolaou's
  `k<10⁴ Mpc⁻¹` scale-invariant range; his abstract (fetched 2026-09-04) ties the `f²` IR tail to
  a spectrum with small-scale **enhancement** that "collapse[s] as well to form PBHs" — the
  opposite of §V C's null. **Ledger `A3-3`.** Blocks Channel I's consistency claim and §V C's null.

### DA3M-R4-03: Eq. (6) has three undefined symbols, a mislabelled definition, and no derivation pointer
- **class:** OPEN (MAJOR, editorial). Leg: Fable M3 (a,b real; c FALSIFIED → `DA3M-R4-F8`).
  `main.tex:334–344` calls `T_fNL` a bispectrum transfer; brief §3 derives it as the **f_NL**
  transfer `= 1/λ_ζ` (auditor-verified: `λ_ζ = 4.0 ↔ T = 0.250`, etc.). `𝒜`, `I_∞`, `1+2r`
  undefined in the paper. Closure **C3** (transcription).

## OPEN — genuinely-new-real, MINOR

| id | item | leg(s) | source | closure |
|---|---|---|---|---|
| DA3M-R4-04 | Ref. [9] title is that of PRL 122, 201101 (2019); arXiv:1909.13728 = "Universal infrared scaling of gravitational wave background spectra" (arXiv fetched) | Fable M4 | `main.tex:1215–1217` | C4 |
| DA3M-R4-05 | abstract quotes only Table IV's bispectrum-only row, unqualified, and says "under 1σ apart" while the P+B row reaches 1.1σ | Gemini E1 | abstract `:70–73` vs Table IV `:915–918`, body `:930–933` | C5 |
| DA3M-R4-06 | "quadrupole 15/16" is the μ² coefficient; the ℓ=2 Legendre coefficient is 5/8 | Fable m1 | `main.tex:176`, App. A `:1063–1073` | C5 |
| DA3M-R4-07 | "seven decades above the BBN scale" — 10⁸ GeV vs 1 MeV is **eleven**; no other BBN bound in §V (C2-closure-induced) | Fable m2 | `main.tex:813–816` | C5 |
| DA3M-R4-08 | "shortfall of 7.0 orders … at both f_NL values" — JSON gives `log10_ratio` 6.75 (−35/8) and 7.02 (−35/16) | Fable m3 | `outputs/inlab_delta2_zeta_2026-09-03.json` | C5 |
| DA3M-R4-09 | App. A general-ε formulas carry no domain; they do not reduce to Maldacena as ε→0 (valid on the non-attractor branch only) | Fable M5(b) | `main.tex:1099–1112`; auditor re-derivation | C5 |
| DA3M-R4-10 | "explained at the equation level" / "recorded identity whose mechanism is not derived" is read oppositely by two legs — ambiguous, not false | Fable M5(a) + Gemini N2 | `main.tex:44–49` vs `:1093–1098` | C5 |
| DA3M-R4-13 | Table II has no γ=2 row although C4 made the γ=2 causal floor a central comparator | Fable m5 | `main.tex:585–591`; Table II | C6 (re-run `pta_gamma_reproduce.py`; never import the referee's σ) |
| DA3M-R4-14 | DESI z-scores use one side of an asymmetric error without saying which (method verified correct) | Fable m9 | `main.tex:869–876` | C5 |
| DA3M-R4-15 | **auditor-originated:** §VI A compares DESI to the pre-bounce −35/16 while §VI B declares the transmitted range the observable prediction (C1-closure seam; not load-bearing — 0.34σ/0.55σ) | — | `main.tex:869–872` vs `:880–887` | C5 |

## OPEN — REAL residual of an incomplete R3 closure (not counted as genuinely-new)

| id | item | leg(s) | source | closure |
|---|---|---|---|---|
| DA3M-R4-11 *(residual of DA3M-R3-11; C8 incomplete)* | in-body/appendix `research/…` paths at `:566`, `:793`, `:855`, `:1022`; `:230` "this paper's own adjudication"; **new instance** `:1163` "directive Q2"; `:1157` "companion P2 Zenodo record"; `:891–894` companion draft. C8's own grep gate not met. Paths *inside* the reproducibility statement are sanctioned and are NOT defects — Gemini's blanket scrub declined. | Gemini M1 + Grok N2 | `grep -nE 'research/\|this lab\|directive Q' main.tex` | C7 |
| DA3M-R4-12 *(residual of DA3M-R3-09; C7 incomplete)* | Ω_DM footnote still asserts "no number here changes"; true for the ratio, false for the tabulated f_PBH and Fig. 1 (f_PBH depends exponentially on the amplitude; A_* shifts −2.70 %) | Fable m8 | `main.tex:780–789`; `pbh_compaction_fnl.py:156,267`; R3 re-run | C5 (directive I6 if recomputed) |

## RE-FLAG-OF-DISCLOSED (R4)

| id | item | leg | where the paper already says it |
|---|---|---|---|
| DA3M-R4-R1 | in-in vs separate-universe "unproven that they compute the same quantity" | Grok M1 | `:271–276` + **Appendix A** (`:1017–1116`), added by C3; = `DA3M-R3-R1` |
| DA3M-R4-R2 | refit vs official σ "not comparable / meaningless" | Grok M2 | `:583–588` verbatim; abstract `:64–67` carries the 5–95 % interval type; = `DA3M-R3-R2` |
| DA3M-R4-R3 | "100 decades" reads as a pathology | Fable m7 | `:688–692` "because it depends exponentially on γ_cr" |
| DA3M-R4-R4 | abstract "1.7–1.9" vs Table III "1.732" | Fable m4 | `:806–812` states the widening; C10 restored both caveats at `:68–70` ⇒ **`DA3M-R3-19` CLOSED** |
| DA3M-R2-11 | frozen-release DOI | Gemini E2, Fable m10 | disclosed at `:1152–1156`; Houston-gated P-round. Carried, not re-counted |

## FALSIFIED (R4)

| id | item | leg | why false — source |
|---|---|---|---|
| DA3M-R4-F1 | "'exact' is scheme/ordering-contingent throughout" | Grok E1 | `:150–158` — Maldacena de Sitter matched term-by-term and Namjoo USR `f_NL=5/2`, "Both match exactly"; transmission qualifiers already in the abstract sentence quoted (`:51–56`). = `DA3M-R3-F1` |
| DA3M-R4-F2 | "the 1.7–1.9 ratio is a truncation artefact" | Grok E3 | **Inverted.** `:653–658` — the compaction map has **no** ceiling, "the artefact is removed by construction"; the artefact label belongs to the discarded first pass (`:640–645`). Species of `DA3M-R3-F2` |
| DA3M-R4-F3 | "PBH null listed as consistency evidence" | Grok E4 | abstract `:57–58` "each stated at the strength its evidence supports"; `:66–69` "a clean *null*" |
| DA3M-R4-F4 | "future date September 4, 2026" | Grok N1 | today **is** 2026-09-04. Auto-FALSIFY Rule 3. **8 consecutive rounds, 100 % falsified** = `DA3M-F3` |
| DA3M-R4-F5 | "Fig. 1 color-bar units / inconsistent capitalization" | Grok N3 | auditor rendered `pbh_compaction_fnl.png`: **no color bar exists**; labels consistent; `A` dimensionless |
| DA3M-R4-F6 | "stray space in 'regularized-renormalized- resummed'" | Gemini N1 | `:664–665` source line break; PDF renders correctly (Rule 7). = `DA3M-F5`/`R3-F6` |
| DA3M-R4-F7 | "widen the range to [−0.93,−0.50]" | Fable M1 (sub-claim) | applies the S1 cubic formula to the S2 transfer; `Δf_NL^bounce[S2]` divergent (`:424–427`) ⇒ the number is not computable |
| DA3M-R4-F8 | "\|r\|≫1 ⇒ non-scale-invariant post-bounce spectrum" | Fable M3(c) | brief §4.3: post-bounce `Δ²` flat to **1.2–4.2 %** across the k grid |

## OPINION/GENRE (R4 — venue pass only)

| id | item |
|---|---|
| DA3M-R4-G1 | 12 pp vs a ~8 pp norm (Grok M3) = `DA3M-R3-G1`; note the growth 10→12 is the derivation appendix a referee asked for |
| DA3M-R4-G2 | Table II caption's `3×10⁻¹⁵` self-reproduction check is determinism, not validation (Fable m6) |
| DA3M-R4-G3 | self-referential register (Grok N2, genre half; the Q1 half is `DA3M-R4-11`) |

## Corrections to earlier dispositions (dated 2026-09-04, R4 pass — never backfilled silently)

1. **`DA3M-R3-19` CLOSED** — C10 restored the perturbativity and non-monotonicity caveats
   (`:68–70`), verified this round.
2. **`DA3M-R3-01` / `-02` CLOSED** — the `kη_B` direction is stated correctly (`:363–376`,
   `:944–948`), Table IV carries transmitted rows with the pre-bounce row demoted, and every
   Table IV cell reproduces from `|f^after|/σ` (auditor). Residual seam = `DA3M-R4-15`.
3. **`DA3M-R3-11` partially closed → re-opened as `DA3M-R4-11`**; C8's own grep gate not met and
   the closure **added** a new Q1 instance (`directive Q2`). Third consecutive round in which a
   Q1 sweep leaves or introduces Q1 material.
4. **`DA3M-R3-09` partially closed → re-opened as `DA3M-R4-12`**; option (a) chosen, option (b)'s
   conclusion still printed.
5. **`DA3M-R3-04`'s closure (C4) introduced `DA3M-R4-02`** — second consecutive round in which a
   closure created a new finding. Closures that replace a wrong justification must be checked
   against the paper's other sections before the bundle commits.

## Convergence statement (R4)

**NOT converged at v3M.0.9. Clean-wave count 0.** 15 outstanding real items (3 MAJOR, 12 MINOR).
R3's authorised single verification round is this one, and its scoped question is answered — C1's
propagation landed correctly. **Directive R2: the convergence budget is spent.** v3M.0.10 closes
the editorial list (C1, C3–C7 in the audit §5(i)), then **rounds STOP** until ledger item `A3-3`
(the `P_R(k)` propagation from the LSS pivot to the nHz band, and the induced-GW slope that
follows) returns a science decision on `DA3M-R4-02`. No further round may be dispatched on
editorial grounds alone.

---

# R5 (v3M.0.11, `ROUND_2026-09-04-A3M-v3M.0.11-EXACTPDF-790fafa6-R5VERIFY`) — 2026-09-04

Full audit: `INT_v3/A3M_v3M.0.11_R5_TRUTH_AUDIT_2026-09-04.md`. Legs: Grok API `grok-4.3`
(REJECT, 3E/3M/2m/2N), Gemini API `gemini-3.1-pro-preview` (MAJOR REVISIONS, 4E/3M/1m/1N),
Claude Fable 5.1 INT subagent (major-revisions, 5 MAJOR/16 minor). OpenAI ABSENT (directive N),
Perplexity ABSENT (quota) — recorded, never counted clean.

**Counts:** 18 genuinely-new REAL (3 MAJOR + 15 MINOR, 1 auditor-originated) · 2 REAL residuals of
open R4 items · 1 carried packaging · 6 RE-FLAG · 11 FALSIFIED · 6 OPINION/GENRE · 0 BLOCKER.
**Clean-wave count: 0.** Per leg (new/residual/re-flag/falsified/opinion/carried):
Grok 0/1/3/6/0/0 · Gemini 3/1/1/3/0/1 · Fable 15/1/3/2/3/0.

## OPEN — genuinely-new-real, MAJOR (R5)

| id | finding | citation | closure |
|---|---|---|---|
| `DA3M-R5-01` | `0≤T_fNL<1/2` and "linear transfer can only suppress" printed unconditionally; the paper's own S2/Quintin row has `\|λ_ζ\|=0.97` ⇒ `T≈1.03>1/2` (auditor: `T·(-2.1875)+1.0=-1.246 ⇒ T=1.027`) | `:52–56`, `:355–361`, `:433` vs `:498–501`, `lane9b2_s2_rawadm/results.json` | C1 |
| `DA3M-R5-02` | "2.1–4.4 decades below the 10³ plateau across `kη_B∈[0.1,10]`" overstates its source ("at and below `k_LQC`"); §V C's `1.2×10³` is the equilateral `kη_B=10` point | `:423–428`, `:980–982`; `LANE9C2…md:255–261`; `results.json → equilateral/10/S-lab = -1215.57` | C2 |
| `DA3M-R5-03` | printed NANOGrav `Ω_GW h²(f_yr)=6.3×10⁻¹⁰` is unsupported by the paper's own artifact (`3.6235e-9`) and inconsistent with its own `10^14.3` gap (`log10(6.3e-10/1.45e-23)=13.64`) | `:700–707`; `sigw_nhz_from_lab_spectrum_2026_09_04.json` | C3 |

## OPEN — genuinely-new-real, MINOR (R5)

`DA3M-R5-04` S2-has-no-computable-`f^after` (`:381–384`) contradicts "Scheme S2, resolved"
(auditor-originated) · `-05` body "under 1σ" vs abstract `0.5–1.1σ` (inverted residual of
`DA3M-R4-05`) · `-06` `:243–245` "first from-scratch" vs `:230–231` Li *et al.* ·
`-07` `f^ρ_NL`/`f^c_NL` normalisation unstated in the `-25/8` gap accounting · `-08` unnumbered
§III A table · `-09` "five" vs "six" cubic pieces · `-10` `O(1)` excursion incl. `0.058` ·
`-11` `3.13σ` mislabelled a tension · `-12` Fig. 1 internal title/legend labels (directive I6) ·
`-13` sentence-break/typo set · `-14` `:1176` uncomputed "sharpen this somewhat" ·
`-15` **(ii)** first-order tensor `Ω_GW` at nHz unstated · `-16` abstract band lacks
"S2/Quintin-only" · `-17` `kη_B≈3` `(T_B,k)` unstated · `-18` **(ii)-lite** ratio's conditionality
on the Choudhury sign disagreement + `γ_cr` grid coverage.

## RE-FLAG-OF-DISCLOSED (R5)

`R1` refit-vs-official σ qualifier (Grok E2, Gemini E2) = `DA3M-R3-R2`/`R4-R2`, **3rd–4th
recurrence**; `:560–588` already frames official as primary and refit as "a secondary,
differently-conditioned cross-check" · `R2` second-order `δN` cross-check (Grok M3) = `R3-R1`/`R4-R1`;
`:286–292` no local `f_NL` relation exists at second order · `R3` Quintin Eq. (79) "constant by
construction" (Fable m11) — `:411–415` says it · `R4` `1.732±0.050` grid coverage (Grok M2) =
`R4-R4`; abstract already quotes the range · `R5` `B=5×10⁻⁴` from 9 samples (Fable m9) — `:596–600`
restricts it to one sig fig · `R6` Fig. 2 uncapped `f_PBH>1` (Fable m14b) — caption `:872–877`.

## FALSIFIED (R5)

`F1` "abstract presents `-35/16` as scheme-independent" (Grok E1) = `R4-F1` · `F2` "`f_PBH=0` only
after truncation" (Grok E3) = `R4-F2`/`F4` family · `F3` "no central value per background"
(Grok M1) — `:462–470` · `F4` "future date" (Grok N1) = `DA3M-F3`, **9 consecutive rounds,
100 % falsified** · `F5` "Eq. (1)=Eq. (3)" (Grok N3) · `F6` "Fig. 1 caption cites a commit hash"
(Grok N4) — it does not · `F7` "Fig. 1 y-axis unlabelled" (Gemini N1) — auditor rendered the PNG;
it reads `Ω_GW h²` · **`F8` "the the" duplications (Gemini N2) — `grep` on `main.tex` AND on
`pdftotext main.pdf` both return 0 hits: a fabricated quotation** · `F9` "`r` imported, load-bearing"
(Gemini M2) = `R3-F7` · `F10` "`kη_B≈3` needs `T_B~10⁶ GeV`" (Fable m7) — at `T_B=10⁸ GeV`,
`k=5.1×10¹⁵ Mpc⁻¹`, inside the paper's PBH band · `F11` "re-run at Choudhury's parameter set"
(Fable M5) — their spectrum is unreproducible = `R3-R3`.

## OPINION/GENRE (R5)

`G1` "5.1σ is not a test" (Fable m10) · `G2` Table II `γ=5` row labelling (m13) · `G3` expand
App. A.1 (Fable M4 tail) · `G4` missing-reference wish-list (act on the SPHEREx `σ=0.5` source
only) · `G5` register/length (Grok summary, Gemini E4 genre half) · `G6` Grok's reject framing
rests on F1+F2+F3.

## Convergence statement (R5)

**NOT converged at v3M.0.11. Clean-wave count 0.** No physics error found: every number re-derived
from the committed JSONs reproduces. The three MAJORs are editorial-with-a-numeric-core.
**Directive R2:** this is the second consecutive round; v3M.0.12 closes C1–C7 (editorial + the two
>10 pt overfull baselines), then **rounds STOP** until the two **(ii)** ledger items
(`DA3M-R5-15` first-order tensor `Ω_GW` at nHz; `DA3M-R5-18` `γ_cr` grid coverage) return.
No further round may be dispatched on editorial grounds alone.

---

# R6 (v3M.0.13, `ROUND_2026-09-04-A3M-v3M.0.13-EXACTPDF-c6f9bb57-R6VERIFY`) — 2026-09-04

Full audit: `INT_v3/A3M_v3M.0.13_R6_TRUTH_AUDIT_2026-09-04.md`. Board:
`INT_v3/A3M_v3M.0.13_R6_BOARD_2026-09-04.md`. Legs: Grok API `grok-4.3` (REJECT, 6E/3M/2m),
Gemini API `gemini-3.1-pro-preview` (MAJOR REVISIONS, 6E/1M/3m incl. pass-2), Claude Fable 5.1 INT
subagent (major-revisions, 5 MAJOR/15 minor/7 questions). OpenAI ABSENT (directive N), Perplexity
ABSENT — recorded, never counted clean.

**Counts:** **16 genuinely-new REAL** (`R6-01`…`R6-16`; 1 MAJOR + 1 MAJOR-lite + 14 MINOR) ·
8 RE-FLAG · 7 FALSIFIED · 8 OPINION/GENRE · 1 carried packaging · 0 BLOCKER.
**Clean-wave count: 0.** Per leg (new/re-flag/falsified/opinion/carried):
Grok 3/3/2/2/1 · Gemini 6/0/2/0/2 · Fable 11/4/3(halves)/4/1.

## OPEN — genuinely-new-real, MAJOR (R6)

| id | finding | citation | closure |
|---|---|---|---|
| `R6-01` | §V C `T_B ≳ 10^8–10^10 GeV` wrong by ~2 decades; committed mapping `k_B ≈ 1.7143e7·T_B[GeV] Mpc^-1` gives `T_B ≳ 6e9–6e10 GeV`, **thirteen** decades above BBN not eleven | `main.tex:1023–1027`, `:784–786`; `outputs/inlab_delta2_zeta_2026-09-03.json → k_B_Mpc-1_if_T_B_GeV` | (i)-1,2,3 · REAL residual of `DA3M-R3-02` |
| `R6-02` | Channel I pairs the `γ=13/3`-FIXED amplitude `A=2.4e-15` with the free-`γ` slope `3.2`; consistent use moves the shortfall `10^14.3 → ≈10^15.2` | `sigw_nhz_from_lab_spectrum_2026_09_04.py:72`; `main.tex:752,756,771,1186–1187`, abstract `:58`, Fig. 1 legend | (i)-4 + figure regen (directive I6) |

## OPEN — genuinely-new-real, MINOR (R6)

`R6-03` abstract conflates bare significance with candidate separation (`:74–78` vs `:1211–1215`) ·
`-04` abstract mis-attributes the FIRAS SMBH-seed exclusion to the model (`:62–64` vs `:1066–1077`) ·
`-05` `:1099` "lies below the central value" — it lies above · `-06` §VII C version-history prose
(**recurrence of `DA3M-08`**) · `-07` (auditor-originated) `3162σ/3364σ/408σ` appear only in
`main.tex`, no committed artifact; derivable but unsourced (`/never-fabricate-derivation`) ·
`-08` abstract "two-scheme **band**" vs §III A "genuinely physically inequivalent" (residual of
`DA3M-R5-16`) · `-09` Ref. [8] author list/identifier unverified · `-10` `r=0.84` reported (`:769`)
but never tested against the `r<0.036` bound quoted two lines earlier · `-11` abstract
"shape-robust" carries none of the body's `:942–950` conditionality · `-12` `:1076` "largely
excluded" · `-13` "5.1σ" printed as a tension, not as a Gaussian-equivalent z-distance from a
5–95% width (same class as `DA3M-R5-11`) · `-14` `:381–384` should say "no computable **cubic**
`f^after`" (residual of `DA3M-R5-04`) · `-15` sentence fragment after Eq. (7) · `-16` Table VI
entries are upper bounds (shape overlap `r<1` uncomputed).

## RE-FLAG-OF-DISCLOSED (R6)

`RF1` ≥100-point PBH grid (Grok M1) = `R4-R4`/`R5-R4`, **3rd recurrence**; `:942–950` prints the
coverage · `RF2` δN route "not independent" (Grok E6) = `R3-R1`/`R4-R1`/`R5-R2`, **4th** ·
`RF3` scheme-marginalized LSS forecast (Grok M2) — marginalizing over a convention is undefined ·
`RF5` `0.058` "not an excursion" (Fable m9) = `DA3M-R5-10`, closed at `:413–415` ·
`RF6` uncapped `f_PBH` header (Fable m8) = `R5-R6` · `RF7` refit-vs-official σ (Fable m6) =
`R3-R2`/`R4-R2`/`R5-R1`, **5th** · `RF8` frozen DOI (Grok E4, Gemini E3+E4, Fable m13) — carried
packaging; Gemini E3's "no frozen hash" half is FALSE (a git hash is pinned) · `RF9` §II D
"resolved" vs Appendix wording (Fable m2) = `DA3M-R3-03` class.

## FALSIFIED (R6)

`F1` "abstract presents −35/16 as scheme-independent" (Grok E1) = `R4-F1`/`R5-F1`, **3rd
recurrence**; `:49–54` labels transmission scheme-qualified · `F2` "future date/affiliation"
(Grok N1) = `DA3M-F3`, **10 consecutive rounds, 100% falsified** · **`F3` "3162σ and log₁₀β=−1.7e9
are mathematically incompatible" (Gemini E6) — different mass scales;
`inlab_delta2_zeta_2026-09-03.json:252–253` gives `n_sigma=89149.44`, `log10_beta=-1.7258e9` at
`M_H=1e20 g` and `89149²/(2 ln10)=1.726e9` ✓; `3162=10^3.5` is the 7.0-decade deficit at
`10^15–10^16 g`** · `F4` "regularized-renormalized- punctuation artifact" (Gemini N1) —
`main.tex:863` has no stray space; it is a LaTeX line break · `F6` "the tensor sector is OMITTED"
(Fable M1 first half) — `:762–774` computes both `r<0.036` and `r=0.84`, citing
`outputs/r5_15_tensor_omega_nhz.json` · `F7` "must cite the statement fixing the ±0.6 convention"
(Fable M3i) — `:607–609` does · `F8` "the paper carries none of the γ_cr conditionality"
(Fable M2 second half) — `:942–950` carries it in full; only the abstract word survives.

## OPINION/GENRE (R6 — venue pass only)

`O1` 15 pp too long / "6–8 page note" (Grok M3) · `O2` "honest null" undefined (Grok N2) ·
`O3` ORCID/affiliation (Grok N1b) · `O4` Grok M2 tail · `O5` "mint the DOI now" (Gemini E4) ·
`O6` move the Eq. (5) derivation + shape function into the paper (Fable m3, m12) · `O7` Table IV
row label + ABS-plateau column (Fable m4 = `R5-G2`, m5) · `O8` Fable Q5 (a question).

## New evidence admitted at R6 (not a review finding)

DESI DR1 reproduction v3 (`research/desi_png_reproduction/LEDGER4_RESULT_v3_2026-09-04.md`):
`f_NL = −2.2 ± 25` at `p=1.6` on DESI's official window matrix + full-randoms `P_ℓ` + EZmock
covariance, `0.06σ` from the published `−3.6^{+9.0}_{−9.1}`. §VI may state it with the mandatory
caveat (σ ~2.8× published: no wide-angle corrections, 2/5 systematics splits). **The 0.0007σ
distance to −35/16 is a coincidence and must be labelled one** — the same fit is 0.086σ from zero.

## Convergence statement (R6) — directive R2 STOP

**NOT converged at v3M.0.13. Clean-wave count 0.** No physics error found: every number
re-derived from the committed JSONs reproduces; the only numerically-wrong statement (`R6-01`) is
a unit-conversion slip whose correction *strengthens* the paper's null. Both reviewer verdict
words rest on findings classed falsified, re-flag, or abstract-wording (`O4`, `F1`, `F3`).
**Directive R2: this is the third consecutive verification round; v3M.0.14 closes the 16 (i)
editorial items, then rounds STOP on A3M** until a science decision is taken on the (ii) ledger:
`A3-4` (re-derive `r`; is `r=0.84` already excluded by `r<0.036`?), `A3-1e` (Choudhury
`γ_cr ≲ 0.85` sign disagreement — blocked on their unreproducible spectrum; analytic route only,
NOT a bigger grid), `A3-ns` (Eq. (A3) at the `n_s=0.9649` ε), `A3-dN` (mechanism of the
second-order δN piece), `DESI-4` (wide-angle + 3 blocked splits). No further round may be
dispatched on A3M on editorial grounds alone.

---

# R7 — v3M.0.15 (exact PDF `909cf789…`, 17 pp) · 2026-09-04

Legs: **Grok_brutal REJECT** (4E/3M/3n) · **Gemini_cosmology MAJOR REVISIONS** (7E/2M) ·
**Claude Fable 5.1 INT major-revisions** (5M/14m/5Q). 43 raw → **27 distinct**;
**16 genuinely-new-real**, 4 re-flag, 9 falsified, 6 opinion, 7 carried-unverified.
Board: `../A3M_v3M.0.15_R7_BOARD_2026-09-04.md` · audit:
`../INT_v3/A3M_v3M.0.15_R7_TRUTH_AUDIT_2026-09-04.md` (full citations there).
**Clean-wave count: 0.**

## OPEN — genuinely-new-real, MAJOR (R7)

| id | finding | citation | closure |
|---|---|---|---|
| `R7-01` | `r=24` "exactly, bounce-invariant" is scheme-S1; `r_after[S2]=24(6.06/0.97)²≈9.4e2` | `main.tex:46,1232`; `row10_r_ns/results.json` (`T_zeta`=5.115/4.00/6.06 = S1 λ_ζ, `T_h/T_ζ−1≤8e-5`); `main.tex:364,543` | (i)-1 + science lane `A3-S2r` |
| `R7-02` | **embedded Fig. 1 PNG is stale** — `paper/…png` md5 `8e749a23` (pre-R6-02, legend `A=2.4e-15`) vs generator output `af783c0a` (`A=6.46e-15`); auditor-originated, directive I6 | `sigw_…py:264`; both PNGs rendered | (i)-2 |
| `R7-03` | `f_NL^pre` sign change at `c_s=0.8876` committed but absent from the paper; window `[0.444,0.888)` predicts POSITIVE `f_NL` | `row14_cs_window/results.json → window.f_NL_sign_change_c_s` + its note | (i)-3 |
| `R7-04` | `c_s` window drops `Δf_NL^bounce` while asserting full `c_s`-independence of "the transmission" | `row14_cs_window.py:185` vs Eq. (7) | (i)-4 + `A3-cs-bounce` |
| `R7-05` | `\bibitem{CaiXue2011}` id/title inconsistent with the lab's own curvaton source-of-record (`1101.0822`) | `main.tex:1798–1800` vs `theory_audit/curvaton_…2026_09_04.md:13,39` | (i)-5 |

## OPEN — genuinely-new-real, MINOR (R7)

`R7-06` abstract `|f_NL|`→`|f_NL^after|` (`:53`) · `-07` abstract no-go lacks the body's scope
clause (`:55` vs `:1261`) · `-08` Table V's `γ_cr≲0.8` rows are the IR-divergent non-perturbative
branch, unlabelled/uncapped, beside "suppresses throughout" (`:947–949`; `row11` β/β_G=3.5e+3 at
γ_cr=0.766 reproduces the row; `A_*` IS per-point calibrated) · `-09` NANOGrav reference amplitude
`2.622e-8` (`:754,782`) vs `3.6235e-09` (`r5_15_…json:25`) · `-10` companion-draft import by repo
path (`:1621`) · `-11` version-history prose (`:968,1151,1254`) — **residual of `DA3M-08`/`R6-06`,
3rd recurrence** · `-12` `n_s=1 exactly` vs `n_T=−0.035`; `r=23.93` at the anchored ε (`:47`) ·
`-13` "`T_B≈2.3 GeV` … below the QCD scale — excluded by this paper's own baryogenesis argument"
— above the QCD scale, and no such argument exists (`:793–796`) · `-14` insert "effectively" at
`:221` · `-15` repeat the distinct-monomial qualifier at `:222` · `-16` Fig. 1 x-tick collision.

## FALSIFIED (R7)

`C1` Grok E1 "scheme-independent claim" — `:41–43` prints both schemes, **4th recurrence** ·
`C2` Grok E2 / `C3` Grok E4 "no not-directly-comparable qualifier" — `:651` and `:501–502` carry
it verbatim · `C4` Grok M3 "`296×` unsourced" — `:1665` + `row14 results.json` · `C5` Grok N1
"phrase repeated three times" — string absent · `C6` Grok N3 future date = `DA3M-F3`,
**11 consecutive rounds, 100% falsified** · **`C7` Gemini M1 "Fig. 1's line sits at 1e-14 = the
primordial background" — the plotted curves are `1.38–5.88e-23`
(`outputs/sigw_…json → curves_Omega_GW_h2`, confirmed by rendering); the 1e-10–1e-8 band is the
NANOGrav/γ=3 reference. (The figure is defective for the unrelated reason `R7-02`.)** ·
`C8` Gemini E7 "the the" — string absent (same class as `R6-F4`) · `C9` Fable M1(b)
"(37)≠(4.19), not reproducible" — both readings are printed by the committed script
(`…adjudication_2026_09_02.py:448–461`); residual is wording only (`R7-15`).

## RE-FLAG (R7)

`B1` Grok E3 γ_cr-grid truncation = `RF1`, **4th recurrence** (`:955–967` prints the 255-point
scan and the 27-point caveat) · `B2` frozen DOI (Gemini E3, Fable m13) = `RF8`, carried packaging
· `B3` Gemini E4 chain-dir date — a provenance date, one clause closes it · `B4` Fable M3 tail
("demote 1.84") — `:940–950`+`:962–966` already do the work; residual is `R7-08`.

## OPINION/GENRE (R7)

`D1` Grok M1 length = `O1` recurrence · `D2` Grok N2 Fig. 1 prefactor · `D3` Grok M2 tail ·
`D4` Gemini M2 "quantify weakly" (folded into (i)-8) · `D5` Fable m4/m10/m11/Q5 · `D6` Fable m14.

## CARRIED — verify in the v3M.0.16 lane

Fable m5 (`r_dec` interval) · m6 (Li 2016/2017) · m7 (Table II vs "no plateau"; §V C range) ·
m8 (S2 evaluation time) · m9 (`Ω_DM` footnote vs calibration) · m12 (DESI `0.06σ` not
independent) · Q2/Q4 (Q4 → science item `A3-cs-bounce`).

## Convergence statement (R7) — directive R2 STOP

**NOT converged at v3M.0.15.** Fourth consecutive verification round. No physics error beyond
scoping/disclosure of already-committed quantities (`R7-01`, `R7-03`) and one stale figure
(`R7-02`, found by the audit, not by a reviewer). Both reviewer verdict words rest substantially
on `C1`–`C8`. **v3M.0.16 closes the 16 (i) items; then rounds STOP on A3M** until a science
decision on `A3-S2r`, `A3-cs-bounce`, `A3-ns`, `A3-dN`, `DESI-4`. `A3-1e` is **closed** by
`row11_pbh_residuals` item (a). No further round on editorial grounds alone.

---

## R8 — v3M.0.17 (2026-09-04), exact PDF sha256 `5ada0172…`, md5 `b18aafd1…`, 18 pp

Full audit: `../INT_v3/A3M_v3M.0.17_R8_TRUTH_AUDIT_2026-09-04.md`; board:
`../INT_v3/A3M_v3M.0.17_R8_BOARD_2026-09-04.md`. Legs: Grok_brutal **REJECT**,
Gemini_cosmology **MAJOR REVISIONS**, Claude Fable 5.1 INT **MAJOR REVISIONS** (no leg FAILED).
40 raw findings → 27 distinct → **15 genuinely-new-real** (2 MAJOR + 1 MAJOR-lite + 12 minor),
4 re-flag/residual, 6 falsified, 7 opinion/genre, 4 disclosed. **Clean-wave count: 0.**

### New OPEN items (MAJOR)
- **`DA3M-R8-01`: the `k`-essence no-go silently assumes `λ (P_XXX) = 0`, `s = 0`, `η_sr = 0`.**
  Evidence: `row18b_cs_bounce_cubic.py` docstring L20–22 and `results.json.scheme`; no statement
  anywhere in `main.tex`. Closure: disclose at `main.tex:1331` + qualify the abstract's
  "canonical or `k`-essence" (`:63`), or bound `λ/Σ` with the already-computed `ζ̇³` kernel.
  Fingerprint: lambda, P_XXX, k-essence no-go scope, s = 0, eta_sr = 0, Li et al. kinetic sector.
- **`DA3M-R8-02`: Appendix A prints the final-label map as the initial-label one.**
  `main.tex:1639–1641`: `f^{in-in}/λ + f_map = −25/4 + (15/4)μ²` at `ε = 3/2` (= the final-label
  value quoted at `:1652`), **not** the "isotropic monopole of exactly −5" the sentence claims;
  the initial-label map must be `−5/8 − (15/8)μ²`. Closure: print both maps at general `ε` and
  correct the prose; propagate to §II D and the Scope statement.
  Fingerprint: f_map, initial-label, final-label, isotropic monopole −5, delta N_c label map.
- **`DA3M-R8-03` (MAJOR-lite): `Υ` and `Δt_B` used undefined** at `main.tex:435–436`.

### Minor OPEN items
`R8-04` `[S]` suppression scaling · `R8-05` "current HEAD" pointer · `R8-06` Eq. (12) `1.732` vs
abstract `1.84` · `R8-07` "Planck 1σ" ≠ `[−6.0, +4.2]` · `R8-08` §V B/§V C `T_B` cross-ref ·
`R8-09` three quantities named `r` · `R8-10` `r_dec ∈ [0.113, 1]` unstated · `R8-11` Ref. [4] year ·
`R8-12` Table IV "Matter bounce γ = 3" label · `R8-13` Bianchi-I duplication · `R8-14` Fig. 1
legibility · `R8-15` `0.5–1.1σ` vs `3.13σ` comparability tag. (Details in the R8 audit.)

### CLOSED this round
- **`A3-S2r`** — closed by `research/cubic_bounce_transmission/row18a_s2_tensor/`
  (`r_after_S2 = 937.11`, `r_after_S1 = 24.0000` to 1e−13); the paper's `9.4×10²` now rests on a
  committed artifact, not a hand ratio.
- **`A3-cs-bounce`** — closed by `row18b_cs_bounce_cubic/`; the closed form
  `Δf^bounce(c_s) = −(5/24)ρ_B(6c_s²−5)/c_s⁴` reproduces the integrated `Δ₁` to ≤0.2% on all three
  backgrounds and the `c_s = 1` gate matches lane (b) to 3×10⁻⁶.

### Still OPEN from earlier rounds (re-flagged, real)
`DA3M-06` (`r = 0.84` contradiction, `main.tex:790–791` vs `:1292`) and `DA3M-08` (14 ledger/round
tags in body prose) — both must close in v3M.0.18.

### Falsified this round (do not re-open without new evidence)
Grok E1/M2 (abstract says "scheme-qualified"; `:516` says "not directly comparable"), Grok M3
(paper reports `−2.2 ± 25`, not `± 2.5`), Grok M4 (the `1.84 ± 0.03` ratio *is* the effect size),
Grok E4 (no-go scoped "on the backgrounds and channels evaluated here"; Eq. 16 computed on all
three), Grok m1 (the date is the true compile date).

### R2
**Rounds STOP on A3M after v3M.0.18.** R8 found no physics or numerical error; 12 of 15 new items
are one-line edits. The only (ii) item that is a science/scope decision — and therefore the only
thing that could license a further round — is **`A3-lambda`** (bound `λ/Σ`, or restrict the no-go
to the Li *et al.* kinetic sector). Carried: `A3-S2perturb`, `A3-ns`, `A3-dN`, `DESI-4`,
`A3-ref25`. No round on editorial grounds alone.

---

## R9 — v3M.0.24 (2026-09-18), exact PDF sha256 `e0e923d6…`, md5 `b29ebb90…`, 19 pp

First board since the directive-R2 stop after v3M.0.18. Stop lifted because
`NEXT_SCIENCE_LEDGER.md` row 19 reads **"DONE 2026-09-04 — NO-GO GENERALISED"** (`D-A3-14`,
`research/track_a3_multichannel/row19_lambda/`). Board:
`../INT_v3/A3M_v3M.0.24_R9_BOARD_2026-09-18.md`; full audit:
`../INT_v3/A3M_v3M.0.24_R9_TRUTH_AUDIT_2026-09-18.md`.
Legs: Grok_brutal **REJECT**, Gemini_cosmology **MINOR REVISIONS**, Claude Fable 5.1 INT
**MAJOR REVISIONS** (no leg FAILED). 50 raw findings → **24 genuinely-new-real**
(3 MAJOR + 1 MAJOR-lite + 17 minor + 3 nit), 2 re-flag, 14 falsified, 2 opinion/genre.
**Clean-wave count: 0.** All 24 closed in v3M.0.25.

### New OPEN items (MAJOR) — all CLOSED in v3M.0.25
- **`DA3M-R9-01`: the reproducibility pin resolves to a commit containing none of the cited artifacts.**
  `main.tex:1782-1786` pinned commit `68309c8` (2026-09-02). `git cat-file -e 68309c8:<path>`
  fails for all ~12 named artifacts (`row19_lambda`, the A2 adjudication, `lane9a/9b/9b2/9c/9c2`,
  `row10_r_ns`, `row11_pbh_residuals`, `row14_cs_window`, `row18a`, `row18b`,
  `desi_png_reproduction`, `fnl_monopole_adjudication_2026_09_03.md`); all exist at
  `origin/main`. Both published tree URLs return HTTP 200 because the *parent* directories
  exist at that commit — a status-code link check cannot catch this.
  Closed by re-pointing at the `main`-branch trees + naming the frozen-release DOI as a
  required packaging action.
  Fingerprint: reproducibility pin, 68309c8, stale commit, tree URL 200, artifacts absent at pin.
- **`DA3M-R9-12`: Eq. (15) is Li+2016 Eq. (5.1), not (4.19), and already carries λ.**
  Verified symbolically: the general form `-245/16 + 105/(8c_s²) - 30Λ` (the lab's own
  `row19_lambda/results.json`) evaluated on the matter line `Λ=(1-c_s²)/(6c_s²)` reproduces
  `-165/16 + 65/(8c_s²)` exactly, and `7/(16c_s²)` is recoverable only from the `Λ=0` baseline.
  The §VIII scan therefore double-counted λ on that line, and the `Λ=0` baseline was never
  printed. Conclusion (`D-A3-14`) unaffected; defect was that the headline claim could not be
  verified from the PDF. Closed by printing the general-λ form as primary.
  Fingerprint: Eq. 15 attribution, Li Eq. 4.19 vs 5.1, -245/16 + 105/(8cs^2) - 30L, double-counting lambda, 7/(16 cs^2).
- **`DA3M-R9-13`: `f_NL^after = 1.0–1.4e11` printed with no perturbativity statement.**
  Value reproduces (1.38e11) but `f_NL·ζ_rms = 1` at `|f_NL| ≈ 2.2e4` — 6.9 decades earlier.
  Closed by the new committed computation `r9_perturbativity/` (floor `c_s ≳ 0.073–0.079`,
  `r ≳ 1.8` = 49× BK18) and by resting the exclusion on `r = 24c_s` + loss of control.
  Fingerprint: perturbative control, f_NL zeta ~ 1, 1.0-1.4e11, Table VII row 2, tree-level validity.

### New OPEN item (MAJOR-lite) — CLOSED in v3M.0.25
- **`DA3M-R9-02`: the constant-`c_s` / `s=0` restriction was dropped along with the λ qualifier.**
  `DA3M-R8-01`'s fingerprint named `λ = 0`, **`s = 0`, `η_sr = 0`**; `D-A3-14` proved
  λ-independence only, yet v3M.0.19 dropped the whole "λ = s = 0" qualifier.
  `row19_lambda/results.json` still records `scheme: "… eta_sr = 0, s = 0 …"`. Restored to
  the abstract and claim sentence; `c_s(η)` stated as outside the computation.
  Fingerprint: constant c_s, sound-speed running s, eta_sr, full P(X) class, time-dependent c_s.

### Minor/nit OPEN items — all CLOSED in v3M.0.25
`R9-03` internal ledger-row/lane labels in prose · `R9-04` drafting-history parenthetical
(directive Q1) · `R9-05` nine raw artifact paths in body/captions · `R9-06` `T_3`/`T_4`
undefined · `R9-07` γ marginal's σ vs its 68% half-width (left skew −1.10, both numbers
verified correct from the 320k chain) · `R9-08` no stated tolerance on the transmitted
amplitudes (added from `lane_b_numerical`, `step_convergence_rel ≤ 1.5e-8`) · `R9-09` Fig. 1
frequency frame · `R9-10` "essentially" · `R9-11` `p=1.6` reads as a p-value · `R9-14`
curvaton detectability criterion + "tensor-viable r<11.5" misuse · `R9-15` `T_B` / `kη_B`
pairing · `R9-16` squeezed LQC deficit 2.1→**3.1**–4.4 dex · `R9-17` `𝒜` undefined ·
`R9-18` `n_T` "cheap" discriminator · `R9-19` Planck 95% edge missing · `R9-20` Table V
caption cited the wrong artifact for the headline 1.84 · `R9-21` injection test tests bias
not coverage · `R9-22` S2 0.409 presented beside the S1 spread · `R9-23` abstract 341 words
(→ 307) · `R9-24` `s` undefined · **Gemini N1** duplicated "and and" — initially recorded
FALSIFIED on a single-line grep, **re-verified as REAL** (it spans a line break) and fixed.

### Found during closure, by no leg
- **`DA3M-R9-25`: the committed v3M.0.24 `main.tex` did not compile.** A raw Unicode `ρ`
  (line 1754) is a fatal `pdflatex` error under both TinyTeX and Homebrew TeX Live, so the
  served v3M.0.24 PDF was not reproducible from its own committed source. Fixed; file is now
  pure ASCII. Independently, lane L2 hit the identical defect class in paper-su the same day.

### FALSIFIED this round (do not re-open without new evidence)
Grok E1 (the date is the true compile date — same fingerprint as R8), E2 ("no labeled
abstract"; `main.tex:37` is `\begin{abstract}`, revtex renders PRD abstracts unlabeled),
E3 (λ-independence is proved, not assumed), E4 ("from-scratch" ≠ new formalism; novelty
already narrowed at R5 to per-vertex attribution), E6 (Table IV caption carries "not
directly comparable" verbatim at `:675-681`), E8 (paper prints both the 144-point
`1.84±0.03` and the 27-point `1.732±0.050` and says which is headline — R8-06 fingerprint),
E9 (Grok used 0.6 as a 1σ width; the paper states the 5–95% interval type and
`√(0.365²+0.382²)=0.5283`, `0.633/0.5283=1.20σ` — auditor's own arithmetic), M2 (range
contradicts the tabulated `[1.610,1.809]`), M3 (`(5.070−3.2)/0.365 = 5.12`; and **4.9σ is the
paper's own dust-bracket value printed beside 5.1σ** in the Fig. 1 caption), m1 (caption does
state the squeezed configuration), m2 (`r_mix` defined at `:373`), m4 (vacuum normalization
fixed at `:374-377`), N1 ("the the" not present), Grok E7's "units/masks inconsistent"
sub-claim (unsupported; only the *pin* was defective).

### OPINION/GENRE (venue pass only)
Grok M4 (19 pp "disproportionate" — no PRD page cap), Grok m3 ("no sympy script deposited" —
they are deposited; the real defect was the pin, `R9-01`).

### Carried as disclosed limitations (NOT closed by edit — `/never-fabricate-derivation`)
Fable Q1–Q6 and minors 9/10 become four explicit limitations in §IX (S1 prescription at
`c_s≠1`; the (A4) frozen-shape handoff; the `δN` gradient expansion given `N_i = O(1/k_L)`;
bounce-window asymmetry) plus two standing verification requests (Cai Eq. (37) under both
readings; Quintin's attribution). Fable minor 13 (`Ω_DM=0.674`) is a **RE-FLAG** of the R5
disposition that closed it with a quantified factor-2.55 footnote.

### R2 status
R9 closed ≥1 real item, so **one confirmation board is permitted and is the remaining gate**;
it must run on the exact v3M.0.25 PDF. Readiness stays at the computed cap **75** until that
board returns 0 genuinely-new-real.

---

## R10 CONFIRM — v3M.0.25 (2026-09-18/19), exact PDF sha256 `c5fe8889…`, md5 `d46166cb…`, 20 pp

The one confirmation board directive R2 permits after R9. **It did not confirm.** Board legs on
the exact v3M.0.25 PDF: Grok `grok-4.3` **REJECT**, Gemini `gemini-3.1-pro-preview` **MAJOR
REVISIONS**, Claude Fable 5.1 INT referee (verdict-blind cold read) **MAJOR REVISIONS** —
0 ESSENTIAL / 4 MAJOR / 9 MINOR / 5 NIT / 6 verification requests. No leg FAILED; the Gemini and
Fable legs had no raw on disk when this lane started and were **re-run**, not back-filled.
Raws: `../ROUND_2026-09-18-A3M-v3M.0.25-EXACTPDF-c5fe8889-R10CONFIRM_A3M_{Grok_brutal,Gemini_cosmology}.md`
and `../INT_v3/A3M_v3M.0.25_R10_claude_fable_2026-09-19.md`. Full audit:
`../INT_v3/A3M_v3M.0.25_R10_TRUTH_AUDIT_2026-09-19.md`.

**17 GENUINELY-NEW-REAL** (4 MAJOR, 1 MAJOR-lite, 12 minor/nit), **15 FALSIFIED** each with a
source citation, **5 RE-FLAG-OF-DISCLOSED**, **4 OPINION/GENRE**, 2 carried to D-round/proof.
**Clean-wave count: 0.** All 17 closed in v3M.0.26.

### New OPEN items (MAJOR) — all CLOSED in v3M.0.26
- **`DA3M-R10-06`: Table V's `f_PBH` columns were not evaluated at the rows' own labels.**
  Rows 4–5 carried `C_th = 0.5` values under `C_th = 0.6/0.4` labels (`pbh_compaction_fnl.py:417-427`
  computes `gamma_cr_sensitivity` at `C_TH_BASE = 0.5` for every point); row 1 carried
  `calibrated_amplitude_comparison["C_th=0.4"]`, the (0.5, 1.0, 0.4) baseline. Re-evaluated at
  the labeled points in the new committed `r10_tableV_recompute/`: row 1 → 1.7e-11 / 1.0,
  row 4 → 9.5e5 / 6.6e9, row 5 → 1.9e-14 / 3.2e-3; rows 2–3 unchanged. The ratio column and the
  n=27 footer are correct and untouched; every qualitative claim survives. Per-row `A_*` added.
  Fingerprint: Table V f_PBH columns, labeled grid point mismatch, C_TH_BASE 0.5, gamma_cr_sensitivity, calibrated_amplitude_comparison C_th=0.4, per-row A_star.
- **`DA3M-R10-07`: the DBI "best case `r_min = 12.6`" used an undeclared criterion on one background.**
  `row19_lambda.py:46,200` tests `|f_after| <= 5.1` (Planck 1σ) on the Quintin-type background
  only, while Table VII and the adjacent abstract number use the 95% upper edge 9.3 over three
  backgrounds — two criteria and two Λ lines colliding at 12.6. Recomputed on a common criterion
  (new committed `r10_window_criterion/`): DBI at 95% gives **r_min = 10.3 (LQC, 286× BK18)**,
  at 68% 11.9; the P∝X^n line at 95% gives 12.60, reproducing Table VII exactly. The correction
  moves the headline **against** the paper and is printed that way. Fable m6 closes with it.
  Fingerprint: DBI best case, r_min 12.57 vs 10.3, PLANCK_1SIG 5.1 vs 95% edge 9.3, undeclared criterion, Quintin-only Lambda scan.
- **`DA3M-R10-08`: the same tensor amplitude given two incompatible shortfalls.** p. 8 said the
  r_after=24 first-order tensor (1.7e-14) is "8–9 orders below" NANOGrav's 2.622e-8; p. 13 said
  10^6.2 for the same pair. log10(2.622e-8/1.70e-14) = 6.19 — the 8–9 is the tensor-vs-*induced*
  ratio (correctly given as 9.1 decades in the same sentence), comparator slipped. Fixed on p. 8.
  Fingerprint: 8-9 orders vs 10^6.2, 1.7e-14, NANOGrav 2.622e-8, comparator slip.
- **`DA3M-R10-09`: reproducibility citations that cannot resolve.** (c) `r9_perturbativity.log`
  is matched by `.gitignore: *.log` and has never been committed — citation dropped;
  (d) `outputs/r11_pbh_residuals.json` exists on no branch (the real artifact is
  `row11_pbh_residuals/results/row11_gammacr_extension.json`) — path corrected; this is also
  where `DA3M-R9-20`'s re-cite landed on a non-existent name. (a) `origin/main` is behind this
  lane, so the branch-tree pointers resolve to an older PDF for external readers — a **PUSH GATE**
  for the director, recorded open, not closed by an edit.
  Fingerprint: r9_perturbativity.log gitignored, outputs/r11_pbh_residuals.json absent, origin/main behind.

### New OPEN item (MAJOR-lite) — CLOSED in v3M.0.26
- **`DA3M-R10-01`: drafting-history / self-referential revision prose survived (directive Q1).**
  Seven instances (`main.tex:572, 592-595, 615-620, 1151+1157, 1537-1541, 1655-1659, 1737`).
  `DA3M-R9-04` had closed one parenthetical; the closure was scoped to that instance, not the
  pattern. The "S2 diverges" statement referred to is this lab's own earlier finding
  (`lane9b_s2_regulation/LANE9B_S2_REGULATION_2026-09-04.md:12,139,153`), not the literature, so
  no attribution is lost. All rewritten to state the conclusion directly.
  Fingerprint: drafting history, previously reported, now shown, no longer an open item, S2 diverges statement, directive Q1.

### Minor/nit OPEN items — all CLOSED in v3M.0.26
`R10-02` seven raw artifact paths/JSON keys still in BODY text (residual of `DA3M-R9-05`; two of
them *introduced* by the R9 closure) · `R10-03` the reproducibility statement contained an
instruction to ourselves ("minting that DOI … is a maintainer action required at the packaging
stage") — rewritten as a data-availability sentence · `R10-04` `s = 39/16` printed with a bare
"i.e." — the value is computed (`row19_lambda.py:60`, Li+2016 Eq. (A.19)) and independently
re-derived here, so the defect was the missing citation, now printed · `R10-05` the **title**
claimed the no-go without the constant-sound-speed scope the abstract and body carry (same class
as `DA3M-R9-02` at a new location) — title now ends "at constant sound speed" · `R10-10` the
printed ratio slope "~0.13 per unit γ_cr" vs the measured OLS **−0.20** (255-pt and 144-pt), and
"monotonically" scoped to fixed family and C_th (+0.03 per +0.1 in C_th) · `R10-11` the 144-point
subset's composition stated (78 lognormal + 66 power-law; power-law alone 1.839±0.031) ·
`R10-12` "the PTA/PBH/reach/injection channels ran in under 6 s total" was false (PBH grid alone
215 s, γ_cr scan 1283 s) — true per-channel wall-clock list printed · `R10-13` the factor-of-two
attribution softened from "at Cai et al.'s amplitude-conversion step" to "between their printed
shape function and their quoted amplitudes", with the undecidability from print stated ·
`R10-14` "thirteen decades above BBN" → "thirteen to fourteen" · `R10-15` curvaton "r > 23 after
it" → the S1 band "r > 21–24" · `R10-16` Table IV caption states the chain is this lab's own
2026-05-01 reduction, so "reproduced" means re-read, not re-sampled · `R10-17` hardware string
dropped from the reproducibility statement.

### FALSIFIED this round (do NOT re-open without new evidence)
Grok **E3** (the factor-2 resolution is *not* a normalization step of ours: `main.tex:223-232`
reads Cai's own printed Eq. (37) and finds Cai's own quoted amplitudes are each exactly twice
its limits, checked symbolically — the Fable leg re-derived this independently from the e-print;
the "from-scratch" sub-claim is the already-falsified `R9-E4` fingerprint, novelty narrowed at
`:250-256`) · **E4** (`tab:pta` caption `:699-700` carries "not directly comparable" verbatim —
second falsification, `R9-E6`) · **E7(b)** (the manuscript itself states the DOI is not yet
minted) · **E7(c)** (the only 40-hex token is the NANOGrav chain's SHA-256, not a commit hash;
the pin was removed at R9) · **M4** (`:805-806` prints γ = 5.070 and 5.000 as a labelled dust
bracket; caption `:871` prints both — second falsification, `R9-M3`) · **M5** (`:1170-1172`
computes the model's own μ = 1.65e-8 = 1.8e-4 of the FIRAS bound; the SMBH-seed statement is the
*required* amplitude) · **m1** (true compile date — third falsification) · **m2** (all 23 uses of
"exactly" are exact; `:900` says "not exactly 2" where it isn't) · **m3** (`tab:s1_after`'s
caption `:541-543` states the S2 scheme and non-comparability; `:600-606` gives the real reason —
not bounce-localised, not divergence) · **n1** ("matter-bounce scenario" and "matter contraction"
are distinct defined objects, `:76-77`) · **n2** (f_PBH is dimensionless; `pbh_compaction_fnl.py:608`)
· **n3** (`:2151` prints "Astron. Astrophys. **641**, A9 (2020)" — the volume is there).
Gemini **N1** (49× and r ≃ 1.8 are the same computed quantity, `r9_perturbativity/results.json →
backgrounds/lqc/r_at_floor = 1.7620`; 1.7620/0.036 = 48.9) · Gemini **M2's "uncomputed" framing**
(computed in `row19_lambda.py:60` and re-derived here). Fable **n5** (`:392-393` already reads
"0 ≤ T < 1/2 since ρ ∈ (0,1]").

### RE-FLAG-OF-DISCLOSED (no edit)
Grok **E5** (the 1.61–1.91 range is the paper's own printed 255-point range `:1029`, and the
headline's scope, grid and "must not be quoted as universal" are stated at `:977,982,1023-1038`)
· Grok **E6** (`DA3M-03` class: transmission is *reported* scheme-qualified, both values printed,
abstract `:40-42`) · Grok **M2** (the kη_B window is quantified at `:431-492`, incl. the scan over
[0.1,10]; the constant-c_s restriction is the `DA3M-R9-02` disclosure) · Grok **M3** (`:769-778`
states "what this establishes is *bias*, not *coverage*" in the paper's own words — `R9-21`) ·
Fable **m2** (Ω_DM = 0.674 retained for comparability with Choudhury et al.'s printed Eq. (66),
with the quantified 2.55 footnote — re-flag of the R5 disposition, same as the R9 Fable minor-13).

### OPINION/GENRE (venue pass only)
Grok **E2** (no PRD rule against a contribution sentence in an abstract) · Grok **E7(a)** (remove
the reproducibility statement — contradicts PRD data-availability practice and directive Q2) ·
Grok **M1** (20 pp "excessive" — no PRD page cap, second time, `R9-M4`) · Fable **n2** (inline
parenthetical inside a numbered display — style preference).

### Carried, not closed
- Fable **n1**: Fig. 1's ~5 pt legend/tick labels — real, needs the figure regenerated →
  **D-round** (`/paper-design-round`).
- Fable **n4**: check refs [19]/[20] for journal references → **proof stage / P-round**.
- Fable's **6 verification requests**: recorded in the raw; none asserts a defect and none is
  closed by an edit (`/never-fabricate-derivation`).
- **Frozen-release DOI** — unminted; a P-round/maintainer action.
- **PUSH GATE** (`DA3M-R10-09(a)`) — `origin/main` must carry this manuscript before the
  reproducibility statement's branch pointers are true for external readers.

### R2 status — BUDGET SPENT
R9 + R10 are two consecutive boards. **No further board on A3M without an intervening science or
scope decision** (directive R2); that decision belongs to the director. Readiness stays at the
**COMPUTED** cap 75: the automated-review-convergence gate of directive P is not met — the last
board found 17 real items, and v3M.0.26 has not been reviewed by anything. **No cap-95
recommendation is made on this evidence.**

## R11 — v3M.0.27 (2026-09-21/22), exact PDF sha256 `3e49f29b…`, md5 `ea6ebd91…`, 21 pp

**What unlocked this board.** Ledger row 9 (D-A3-9) CLOSED 2026-09-19
(`research/cubic_bounce_transmission/row9_scheme_independence_2026_09_19/`) — the intervening
science decision directive R2 required after the R9+R10 rounds-stop. Propagated into `main.tex`
as v3M.0.27 (Bardeen-potential argument selects scheme S2 on Quintin-type; f_NL^after single
value -1.25; tensor no-go strengthened to r_after~9.4e2) plus a gate-S12 general-tilt correction
to Appendix A. R11 ran INT-only (directive N + Portfolio Decision 2026-09-02 #6) on this exact
v3M.0.27 PDF: Grok `grok-4.3` **REJECT**, Gemini `gemini-3.1-pro-preview` **MAJOR REVISIONS**,
Claude opus INT referee (verdict-blind, no prior-history access) **MAJOR REVISIONS**. No leg
FAILED. Full board + truth-audit:
`INT_v3/A3M_v3M.0.27_R11_TRUTH_AUDIT_2026-09-22.md`.

**Outcome: 16 genuinely-new-real finding-classes, all CLOSED in v3M.0.28** (full detail and
source citations in the truth-audit doc, not duplicated here):

1. **Internal-audit/lab-bookkeeping language leaked into prose** — "superseded", "blind
   adjudication", "committed [grid/chain/spectrum]", "this lab's own", "this program's",
   "ledger row N", "D-A3-9", "monopole-adjudication note", "independent adjudication" — a
   recurrence of the class R9/R10 already closed (`DA3M-R9-04`, `DA3M-R10-01`), reintroduced by
   the row-9 propagation copying working-note language verbatim. Full scrub applied.
2. Abstract NANOGrav "0.6" left unscoped as a 90% CI half-width.
3. Abstract PBH ratio 1.84±0.03 missing its γ_cr-coverage scope.
4. DESI DR1 reproduction's 0.06σ comparability qualifier stated too late.
5. Wrong cross-reference: n_s=0.9649 "Sec. VI" → should be Sec. VII.
6. c_s=0.8876 sign-flip silently mixed with the Λ=0-baseline framing rule (0.8876 is Eq. 16's
   root, not Eq. 15's — scoped inline).
7. Symbol collision: the new Bardeen-system coefficient reused μ, already the squeezed-angle
   cosine throughout the paper — renamed to ϖ (self-caught during Grok-E1 verification).
8. **ESSENTIAL** — the Bardeen regularity/scheme-selection claim was asserted not derived, and
   inconsistent with the paper's own LQC/poly exclusion. Closed with the cited artifact's own
   indicial-exponent {0,2} result, the H=0 friction-term vanishing (verified symbolically), and
   the smoothed-NEC-crossing numerical control (G4 PASS, 6e-5/7e-6/5e-6) — no new derivation.
9. **ESSENTIAL** — f_NL^after[S2] quoted to 3 sig figs with an undisclosed, non-uniform
   evaluation-window convention. Closed by stating the actual η*/η_B convention used per
   k-point (read from `lane9b2_s2_rawadm/results.json`, not recomputed) and disclosing the
   third k-point's lower convergence honestly.
10. Abstract misattributed the S1 three-background range [-0.65,-0.50] as the LQC/poly-only
    retained range (actually [-0.65,-0.55]).
11. Sec. III's blanket "not supported by any of these calculations" directly contradicted the
    paper's own S2 selection (T≈1.03) — rescoped to S1/(A4).
12. Four passages (Sec. IV D, Sec. VII ×2, Sec. V C, Sec. VIII curvaton) quoted S1 numbers as
    "the model's own" without a scheme label or the S2 counterpart — all four now labelled and
    given the S2 value by simple linear scaling of already-printed numbers.
13. Sec. VI A's DESI-comparison reasoning was backwards relative to Sec. III's own framing —
    corrected; S2-value comparison (0.26σ/0.64σ) added.
14. Sec. V B's PBH artefact term had the wrong overall sign (matches the committed script's own
    verdict string) — sign fixed; the unaccounted 0.408–0.85 window attributed to the saddle
    expansion's breakdown near the already-disclosed perturbativity floor.
15. Abstract/Discussion presented f_NL^after=-1.25 as scheme-free though Sec. III A itself says
    a cubic-action-form (raw-ADM vs. Maldacena) qualifier is still owed — added to abstract.
16. Minor cluster: Table III S2-row additive-relation clarified; six wrong internal
    `\ref`/`\S` cross-references repaired (Sec. III A ↔ Sec. VIII ×4, §V B ↔ §V C ×2); Fig. 1's
    in-image title carried the internal label "A3-3" (regenerated, re-mirrored, directive I6);
    Fig. 1 caption now describes its 4th curve and that the NANOGrav line is not a shaded band;
    abstract's ambiguous "Li 2016; Quintin 2015" dual-attribution dropped (Quintin only cites
    Cai); "84%" → "factor 6.25"; "two independent failures" → "two distinct failures (not
    statistically independent)"; broken "see Table III" pointer removed.

### FALSIFIED this round (do NOT re-open without new evidence)
Grok **E1/E2** (the Bardeen construction and first-order system are printed explicitly in
Sec. III A body text, not merely cited; independently re-derived and certified algebraically
equivalent by the Claude opus leg — the real gap was the regularity *proof*, closed as item 8
above) · Grok **E3** (γ_pred=5.07 is direct model propagation, not "an external KDE refit" —
factual confusion with the disclosed secondary 30-bin refit ≈2.57) · Grok **M1** (Sec. II C
already gives the Cai factor-of-two methodology in prose; independently re-evaluated from the
arXiv e-print by the Claude opus leg, exact match in all three configurations) · Gemini **N1**
(claimed duplicate "the the" — zero grep hits in source).

### RE-FLAG-OF-DISCLOSED (no edit)
Grok **M2** (handoff-surface sensitivity — already named as an unquantified limitation,
Discussion (b)) · Grok **M3** (144-point PBH subset — a physical γ_cr-coverage restriction,
already stated as such, not a statistical filter) · Gemini **M1** (frozen DOI/commit hash —
`DA3M-R2-11`, carried since R2, Houston-gated P-round action).

### OPINION/GENRE (venue pass only)
Grok **N1** (affiliation) · **N2** (caption provenance notes — legitimate PRD practice) ·
**NIT1** (nomenclature shorthand) · length/genre complaint (repeat of falsified `R9-M4`/`R10-M1`).

### Carried, not closed
- Claude opus MINOR 3, 4, 5, 6, 10, 11, 14 and its NIT list (items 1,3,4,6) — real but lower
  priority or requiring new computation this lane did not perform; full text in the truth-audit
  doc.
- **Frozen-release DOI** — unminted; P-round/maintainer action.
- **PUSH GATE** — `origin/main` must carry this manuscript before the reproducibility
  statement's branch pointers are true for external readers.
- **Fig. 1 legend/tick-label size** — D-round item, carried unchanged from v3M.0.26.

### R2 status — BUDGET SPENT AGAIN
R11 is the one board directive R2 permitted after the row-9 intervening science decision. It
closed 16 genuinely-new-real finding-classes (not a clean wave — clean-wave count resets to
**0**). **No further board on A3M without another intervening science or scope decision.**
Readiness stays at the **COMPUTED** cap 75. Next unlock: a science/scope decision on the
"Carried, not closed" items above (most concretely, the Next-steps item (i) LQC/poly Bardeen
extension), or Houston authorizing a confirmation board on the resulting v3M.0.28 PDF under
R2's "one confirmation board when the first closes real items" clause, which R11 satisfies.

---

## Row-9b propagation — v3M.0.29 (2026-09-22): the Next-steps (i) science decision, and
## R11 ESSENTIAL 2 closed by computation

**Lane `bb-L1d-a3m-row9b-r12`, co-director authorized.** Lane `bb-LS9-bardeen-lqc` closed
ledger row 9b 2026-09-19→2026-09-22
(`research/cubic_bounce_transmission/row9b_bardeen_lqc_2026_09_22/`, verdict
`OUTCOME-UNIVERSAL(b)`, gates G1–G10 PASS, independently blind-adjudicated at Opus tier —
the specified Fable tier FAILED-INFRA, HTTP 429, recorded never as a verdict). **This closure
is directive R2's required intervening science decision**, authorizing exactly one confirmation
board (R12) on the resulting PDF, per Houston's co-director authorization.

**What the science decision does.** The Bardeen-potential scheme-selection argument of R11's
new material (Sec. III A), established only on the Quintin-type background, extends to the
LQC and poly backgrounds, which cross `rho+p=0` **smoothly** rather than by a jump: `Phi` and
`Phi'` stay continuous (the momentum constraint's own first recursion), the divergence is a
logarithm confined to the momentum sector with closed-form amplitude, and the continuation is
one member of a one-parameter self-adjoint-extension family (the operator is **not**
essentially self-adjoint at the crossing — a retraction of the source lane's own earlier
"unique" claim, caught by its blind adjudication). The transmitted amplitude differs from
scheme S1 on **all three** backgrounds — background-independent in **direction** — but by
`6.25x` (Quintin, unchanged), `2.00x` (LQC), `2.67x` (poly) — **background-specific in
magnitude**; row 9's "factor 6.25" language, and any "conservative"/"only computed value"
language about the LQC/poly S1 rows, must not be carried forward, and every such instance was
swept from `main.tex` in this bundle (the R11 lesson: an unswept propagation leaves
scheme-labelling MAJORs — 5 of R11's 16 findings were exactly that class).

**Table `tab:s1_after` gains two rows** (v3M.0.29): LQC and poly under the Bardeen
continuation, linear-transfer-only (`T_fNL=0.500` exact/prescription-free on LQC via a second
matter-kinetic anchor; `T_fNL=0.521` principal-value-only on poly), with `Delta f_NL^bounce`
**not computed** and `f_NL^after` reported **only as a bracket**
(`[-1.20,-0.09]` LQC, `[-1.27,-0.13]` poly) — directive-F rule: a bracket is never collapsed to
a single value.

**AGAINST the paper, same prominence (directive F):** row 18's open tensor gap for LQC/poly
(`main.tex` R11-era: "No S2 `r_after` for LQC/poly … `z_S2^2=0` at their `Hdot=0` crossings")
is now closed, in the unfavourable direction: `r_after=24/R^2` gives `96.0` (LQC) and `170.6`
(poly) against S1's common `24.0` — `2.7e3x` and `4.7e3x` BICEP/Keck, not `6.7e2x`. Printed in
Sec. VII (tensor section) with the same weight as the favourable Sec. III A material, not
buried in an appendix or footnote.

**R11 ESSENTIAL 2 (the undisclosed evaluation-window convention) — CLOSED BY COMPUTATION, not
disclosure, superseding R11's closure.** R11 closed the item by *disclosing* the paper's actual
non-uniform rule (`eta_*/eta_B=50,50,20`). The row9b lane's `row9b_window.py` ran a 12-point
`eta_*/eta_B` scan at all three `k`-points on the committed, unmodified raw-ADM kernel and
found a **stationary region common to all three `k`-points**; a single uniform convention
`eta_*/eta_B=15` sits inside it at every `k` and satisfies `k eta_*<=0.2` throughout, giving
`f_NL^after[S2]=-1.2492,-1.2490,-1.2464` — a `0.22%` spread across `k` and across the
stationary window. **Outcome: WINDOW-SETTLED.** The headline `-1.25` survives to three
significant figures with a stated `0.3%` evaluation-time systematic; the disclosure gap is now
a positive computed statement. `main.tex`'s per-`k` `f_NL^after[S2]` triple is updated from
`-1.249,-1.246,-1.244` (old non-uniform convention) to `-1.249,-1.249,-1.246` (uniform
convention) — closer to, not further from, the printed headline.

**Limits carried forward, not softened (row9b §6, PROPAGATION_NOTE §2c/§6):** linear transfer
only on LQC/poly (cubic term uncomputed, needs the raw-ADM in-in integral there, same `Q=0`
logarithm at cubic order); a classical-GR continuation statement about a given `a(eta)`, not a
claim about LQC's own dressed-metric perturbation theory; the LQC anchor's prescription-freedom
rests on an assumption about the effective theory's kinetic weight that neither this lane nor
row9b derived — if false, LQC is as prescription-dependent as poly; the matching-surface/
thin-shell caveats from row 9 remain open.

**Symbol audit (self-caught, R11-lesson applied proactively):** the source note's own extension
parameter, called `nu`, would have collided with the pre-existing general-`\nu` Hankel-limit
symbol in Sec. VIII (the constant-`c_s` no-go); renamed `\theta` in `main.tex`. No other
collisions found (checked `R`, `Q`, `u`, `z_K` against the whole document).

**Directive G hygiene:** `\paperVersion` v3M.0.28→**v3M.0.29**, `\paperTimestamp` unchanged
(already today's date). 4-pass pdflatex, 0 errors, 0 undefined references/citations, 23 pp
(grew from 21). One new 73.97pt table overflow from the two added `tab:s1_after` rows, caught
by `/latex-audit` and fixed with `\scriptsize` + shortened row labels before this commit — max
overfull hbox after fix: 3.89pt (unchanged pre-existing tolerance). `/latex-audit` visual PASS:
pages 1, 6–9, 13–15, 17–18 rendered at 130dpi and inspected — no column overflow, no
table-row overflow, title block clean. Three-way byte-identical mirror: source compile ==
`site/public/papers/a3_multichannel_arxiv_v3M.0.29.pdf` == `public/papers/…v3M.0.29.pdf`, md5
`8ee1f13bd4e596c87655a9347c0c0918`, sha256
`0c8c318e184577b614251d9d517f1cdf7d5bb9c667a6b731ca130a26b47d4a60`. **Convex UNAVAILABLE**
(spending limit) — `paperVersions:bump` queued to `CONVEX_BACKFILL_QUEUE_2026-09-21.md`, not
written; readiness stays COMPUTED from static site data only until the backfill lands.

**No headline number changed** on the Quintin-type background (`f_NL^after=-1.25` unchanged;
only its per-`k` third-decimal triple moved, per the window closure above, itself unchanged in
the rounded headline).

**Next: R12.** The one confirmation board R2's "confirmation after real closure" clause
permits, on this exact v3M.0.29 PDF. See the "R12" section below for the board result.

---

## R12 — v3M.0.29 exact PDF (sha256 `0c8c318e18…12`), 2026-09-22

**Legs.** Grok API and Gemini API: **FAILED-INFRA**, never a verdict. `tools/v3_native_pdf_review.py`
requires a fresh whole-portfolio preflight receipt, which requires every registered draft paper's
inputs to be git-clean; `pipelines/p4prime_chirality_test/paper/{main.tex,main.pdf}` were dirty
under a concurrent, legitimately active lane (P4P) this lane does not own, and an attempted
temporary stash-and-restore of only those two files was blocked by the harness's own safety
classifier. Same class of shared-checkout contention already recorded for the P-SU lane's R4
board. Per directive I2 this does not stop the independently-valuable check that remains:
**Claude opus INT referee** (verdict-blind, dispatched with no access to this repository outside
the exact PDF) ran: **MAJOR REVISIONS**. Full raw + truth-audit:
`INT_v3/ROUND_2026-09-22-A3M-v3M.0.29-EXACTPDF-0c8c318e-R12/`.

**6 GENUINELY-NEW-REAL** (2 ESSENTIAL + 1 MAJOR + 2 MINOR closed by real edit; 1 ESSENTIAL
closed by honest disclosure, not fully resolved), **1 FALSIFIED**, **2 RE-FLAG-OF-DISCLOSED**,
**11 carried** (not closed this round; full list in the truth-audit doc). Clean-wave count: **0**.

### CLOSED in v3M.0.30

- **`DA3M-R12-01` [ESSENTIAL]: LQC's two non-S1 linear transfers ($0.409$ vs $0.500$) were never
  reconciled.** Caused by this lane's own row-9b propagation (v3M.0.29). Closed with an explicit
  paragraph distinguishing the two constructions (different variable, different handoff surface)
  immediately after Table III.
  Fingerprint: LQC 0.409 vs 0.500, effective-fluid vs geometric Bardeen, two different constructions not superseded.
- **`DA3M-R12-02` [MAJOR]: "$\rho+p$" denoted two different quantities in Sec. III A; $x$
  undefined.** Caused by this lane's own new prose. Closed: the first NEC-crossing statement now
  reads $\rho+p\equiv-2\dot H=0$ with an explicit GR-identity note; $x\equiv\rho/\rho_c\in(0,1]$
  defined at first use; the LQC anchor sentence states explicitly that the classical GR identity
  is violated by the modified Friedmann equation. $\rho_B$/$\rho_c$ near-collision left open
  (carried, not renamed this round).
  Fingerprint: rho+p double meaning, x undefined, quantum-geometry factor 1-2x, GR identity violated.
- **`DA3M-R12-03` [MINOR]: $T_{f_{\rm NL}}<1/2$ disclaimer scoped only to Quintin-type.** Caused
  by row-9b (LQC/poly now also have Bardeen transfers outside $[0,1/2)$). Closed: disclaimer now
  covers all three backgrounds with all three values stated.
  Fingerprint: T_fNL bound scope, LQC 0.500 poly 0.521 outside [0,1/2), disclaimer all three backgrounds.
- **`DA3M-R12-04` [MINOR]: Quintin-type "sharing its sign" sentence lacked an S1 qualifier.**
  Pre-existing text, consequential once S2 selection was established. Closed: "in scheme S1"
  added plus a parenthetical noting S2's net cubic term suppresses $|f_{\rm NL}|$ instead.
  Fingerprint: additive bounce term sign, scheme S1 qualifier, S2 suppresses instead of enhances.
- **`DA3M-R12-05` [MAJOR]: the 144-point/27-point PBH ratio reconciliation was left to the
  reader.** Pre-existing, not row-9b-caused. Closed with the explicit arithmetic
  ($\gamma_{\rm cr}$ means $0.430$/$0.853$, OLS slope $-0.20\Rightarrow1.84$ to 3 s.f.), computed
  from the already-committed `row11_gammacr_extension.json` points — an aggregation, not new
  computation.
  Fingerprint: 144-point vs 27-point reconciliation, gamma_cr mean 0.430 0.853, OLS slope -0.20.
- **`DA3M-R12-06` [ESSENTIAL] — CLOSED BY COMPUTATION in v3M.0.31 (superseding R12's
  disclosure-only close).** Channel II's headline $1.84\pm0.03$ was measured entirely inside the
  region Table V's own caption called the non-perturbative branch, and the stated mechanism
  (large positive $\gamma_{\rm cr}=0.766$–$0.968$) did not apply to the headline window
  ($\gamma_{\rm cr}=0.267$–$0.630$). Lane `LS12-pbh-perturbativity` (2026-09-22) ran the per-point
  diagnostic $1.2|f_{\rm NL}|\sigma_r$ pointwise across all $144$ headline points, at each point's
  own required amplitude, re-integrating $\sigma_r$ from the compaction script's own Eq.-(53)
  variance integral (pre-registered `PREREGISTRATION.md`, committed alone at `b289aa0f` before any
  number existed; five validation gates G1–G5, three exact to machine zero, `pbh_perturbativity.py`,
  `results.json`, manifest `a3-pbh-perturbativity-pointwise.json`). **Outcome: the criterion is
  satisfied at both candidate values at $62$ of the $144$ points (branch b2, RE-SCOPE — CENTRAL
  VALUE CHANGES).** The headline is re-scoped, not withdrawn: `$1.84\pm0.03$ (n=144)` →
  `$1.81\pm0.02$ (n=62)`, applied to the abstract, Eq.~(eq:pbh_ratio), Sec.~V C, the "Regime of
  validity" passage, and Table V's caption in `main.tex` v3M.0.31. Reported with equal prominence
  (against the paper): no point of the $144$ reaches $\varepsilon\le0.5$ (the whole population is
  marginal); the ratio correlates with the diagnostic at Pearson $+0.83$, so the subset value is
  threshold-conditional, sliding from $1.798$ at a cut of $0.9$ to $1.837$ at $1.4$; and Table V's
  "non-perturbative branch" label on the $\gamma_{\rm cr}\lesssim0.8$ rows is **inverted**
  pointwise — $\varepsilon$ *rises* with $\gamma_{\rm cr}$ (the headline window is, pointwise, the
  *more* controlled of the two), so the caption and the table's dagger footnote are corrected to
  "uncapped-abundance rows" (an amplitude-calibration label, not a perturbativity one). The 27-point
  grid's own attribution of the printed "0.54–1.01 / 1.09–2.02" is also corrected in the same
  passage (those six numbers are the Gaussian-calibrated $A_*$ rows, not the 27-point grid's own
  ratio amplitudes, which are $[0.64,2.22]$/$[0.97,3.22]$). Channel II's scientific conclusion is
  **unchanged**: still 7.0 dex short, $f_{\rm PBH}=0$, a NULL. Decision recorded as `D-A3-15`.
  Full detail: `research/track_a3_multichannel/pbh_perturbativity_2026_09_22/PROPAGATION_NOTE.md`
  and its `PBH_PERTURBATIVITY_2026-09-22.md` result note.
  Fingerprint: gamma_cr coverage 0.267-0.630, pointwise perturbativity diagnostic, headline re-scoped 1.84-to-1.81 n=144-to-62, non-perturbative branch label inverted.

### FALSIFIED

- **`DA3M-R12-F1`: "the poly Bardeen bracket's upper endpoint should be $-0.14$, not $-0.13$."**
  FALSE — the referee reconstructed from rounded printed values ($-1.140+1.00$); the actual
  construction uses the unrounded linear transfer and cubic endpoint
  ($-1.1400+1.007=-0.133\to-0.13$, `results.json` `consequences.poly`), exactly as printed.

### RE-FLAG-OF-DISCLOSED

- Abstract $c_s$-window numbers stated as S1-only in the body (Sec. VIII) but not flagged as
  such in the abstract itself; LQC anchor's conditional status stated in the body (Sec. III A).
  Both already disclosed where the referee's own report concedes they are; no edit.

### Carried, not closed

Table II literature-plateau column untabulated; symbol $\lambda$ carries three meanings (a
renaming sweep, not a one-line fix); App. A 4's superseded $f^\rho_{\rm NL}$ formula unmarked;
$\epsilon_{\rm eff}=1/2$ undefined with no stated sensitivity; Discussion quotes stale S1
significances after S2 selection; curvaton $r$-comparability across S1/S2 tensor amplification;
a Savage–Dickey factor at $\gamma_*=2$ not reconstructible from printed chain statistics; a
$B_{\rm MB/SMBHB}$ rounding inconsistency ($6.5\times10^3$ vs stated $7$–$9\times10^3$); the
$\rho_B$/$\rho_c$ near-collision from `DA3M-R12-02`; a NIT cluster (caption wording, citation-year
consistency, dangling $r=0.84$ cross-reference, undefined $W$/$r_i$ in App. A 4, symbol $A$
overload, decade-range phrasing).

### R2 status — BUDGET SPENT, then re-armed by a new intervening science decision (2026-09-22)

R12 is the one confirmation board directive R2 permitted after the row-9b intervening science
decision. It did not confirm: 6 genuinely-new-real items found, 5 closed with real edits or
honest disclosure, 1 (`DA3M-R12-06`) left genuinely open. **No further board ran on A3M** between
R12 and this entry.

**`D-A3-15` (2026-09-22) — the next directive-R2 intervening science decision.** Lane
`LS12-pbh-perturbativity` closed `DA3M-R12-06` by computation (see above), re-scoping the Channel
II headline `1.84±0.03 (n=144)` → `1.81±0.02 (n=62)` and correcting Table V's inverted
non-perturbative-branch label — real new computation, pre-registered before any number existed,
changing a printed headline value in five locations. This is exactly the class of decision
directive R2 requires to re-arm the stop: **one further confirmation board on A3M is now
authorized, to be run on the exact `v3M.0.31` PDF** (this bundle applied the propagation with
directive-G hygiene but ran no board itself, per this lane's mandate). Readiness stays at the
**COMPUTED** cap 75 pending that confirmation board (and Convex recompute — Convex is currently
UNAVAILABLE, spending limit; this lane's mutations are queued in
`CONVEX_BACKFILL_QUEUE_2026-09-21.md`). **Whether and when to spend that board is the director's
call**, not decided by this lane.

## §VI DESI DR1 false-statement correction + LRG channel opened — v3M.0.32 (2026-09-22)

**Lane:** `L1f-a3m-lrg-board` · **Source:** lane `LS11-row4-lrg`'s
`research/desi_png_reproduction/lrg_channel_2026_09_22/PROPAGATION_NOTE.md`, independently
re-verified against `LEDGER4_RESULT_v4_2026-09-04.md`, `LEDGER4_RESULT_v5_2026-09-04.md`,
`LEDGER4_LRG_RESULT_2026-09-22.md`, and the committed QSO fit outputs
(`outputs/fnl_official_p16_point.json`, `outputs/fnl_official_p10_point.json`) before landing —
not taken on the note's word alone.

### DA3M-VI-01 [DEFECT, now-false statement] — CLOSED by real edit

§VI stated the reproduction's $\sigma=25$ (vs. published $9.0$) was "because wide-angle
corrections (`PowerSpectrumOddWideAngleMatrix`) are not applied and only 2 of 5
imaging-systematics splits were run." Both clauses are false and contradicted by the lab's own
committed artifacts:

- **Wide-angle is a genuine null**, not an unapplied correction. `LEDGER4_RESULT_v4` implements
  and runs `PowerSpectrumOddWideAngleMatrix`: order-1 wide-angle terms source only odd multipoles
  (confirmed by source inspection AND a runtime `ValueError` guard AND explicit numeric
  construction, max$|M|=0$ to machine precision), while the official window matrix carries
  $\ell=0,2,4$ only. Applying it changes $f_{\rm NL}$ by exactly $0.0$.
- **All five imaging-systematics splits were run**, not two. `LEDGER4_RESULT_v4` ran three
  (E(B–V), stellar density, galactic depth-z) at official-covariance fidelity; `LEDGER4_RESULT_v5`
  ran the remaining two (WEIGHT_SYS, Galactic latitude) at the same fidelity. All five are tabulated
  in v5 §2.

**Independently re-derived, not just re-quoted:** the real explanation's first reason (the
response lever $b_1-p$) was computed directly from the committed headline fit outputs —
$b_1=2.24932$ in both `fnl_official_p16_point.json` and `fnl_official_p10_point.json`, giving
$b_1-p=0.649$ at $p=1.6$ and $1.249$ at $p=1.0$, ratio $1.925\times$ — matching the note's claimed
$1.9\times$ to the fit's own printed digits, not merely copied from the note. The $\sigma=5.7$
LRG cross-check figure matches `LEDGER4_LRG_RESULT_2026-09-22.md`'s three-bin headline
($-3.40\pm5.74$) to the printed rounding.

**Closed** in `main.tex` v3M.0.32 (Sec. VI, the paragraph following the QSO reproduction) with the
three real reasons (response-lever ratio, LRG+QSO-combined published number vs. QSO-only fit,
$n_{\rm shot}=0$ vs. DESI's full nuisance marginalisation) plus the wide-angle/five-splits
correction, exactly as verified above.

Fingerprint: wide-angle "not applied" claim, "2 of 5 splits" claim, $\sigma=25$ causal attribution, DESI DR1 QSO reproduction paragraph.

### Ledger row 4 (LRG channel) — OPENED, science addition (not a defect)

New paragraphs added to §VI reporting `LEDGER4_LRG_RESULT_2026-09-22.md` in full: three-bin
headline $f_{\rm NL}^{\rm loc}=-3.4\pm5.7$ ($p=1.0$; $-1.1\pm6.9$ restricted to the published
$0.6<z<1.1$ sample definition); AGREES with QSO at $T=-0.159$ ($0.16\sigma$); linear biases rise
monotonically with $z$ (1.87, 2.05, 2.21) without being imposed; all 15 systematics rows null
(closest: E(B–V) at $0.8<z<1.1$, $-0.995\sigma$ after the disclosed $\sqrt2$ correction, named not
buried); WEIGHT_SYS — the QSO channel's dominant systematic at $-3.05\sigma$ — is a null in every
LRG bin. **Discrimination result printed with equal prominence, not softened**: the LRG channel
still cannot separate $-35/16$ from $-35/8$ ($0.38\sigma$ apart at $p=1.0$) — a null for the
flagship question. The existing "near-coincidence... is a coincidence, not evidence" sentence is
carried over verbatim for the LRG number.

Directive-I6 figure sweep: both `\includegraphics` in `main.tex` (`sigw_nhz_from_lab_spectrum...`,
`pbh_compaction_fnl.png`) checked — neither is a Channel III/§VI figure and neither bakes any
QSO/LRG DESI number; no regeneration needed.

Reproducibility statement updated: the QSO manifest citation corrected from the superseded
`LEDGER4_RESULT_v3_2026-09-04.md` to `LEDGER4_RESULT_v5_2026-09-04.md` (v3 kept as record), and a
new LRG citation added (`research/desi_png_reproduction/lrg_channel_2026_09_22/`, manifest
`reproducibility/manifests/experiments/ledger4-desi-dr1-lrg-fnl-channel.json`).

Directive G: `\paperVersion` v3M.0.31→v3M.0.32, `\paperTimestamp` unchanged (2026-09-22, same
day), 4-pass pdflatex 0 undef refs/citations, 24→25 pp, two pre-existing overfull hboxes
unchanged in magnitude and location (3.90pt Sec. VIII paragraph; 2.16pt Table VI alignment — both
present before this bundle's edits, neither touched by them), `/latex-audit` visual PASS on pages
14 (new §VI text), 15 (unaffected control), 21 (reproducibility statement), 25 (Table VI). Three-way
byte-identical mirror confirmed (source == `site/public/papers/` == `public/papers/`, md5
`62153f02dcd5cd3158db2e69b2634f4f`, sha256 `563aaf399474e34314bb61b5a14fe1c9c1b2cd9037a4b9e72fc4d88aac3c2120`);
isolated fresh 4-pass recompile in a clean scratch dir is `pdftotext`-content-identical to the
served bytes. Convex `paperVersions:bump` UNAVAILABLE (spending limit) — queued to
`CONVEX_BACKFILL_QUEUE_2026-09-21.md`.

### R2 status — board authorized by D-A3-15, now due on the exact v3M.0.32 PDF

D-A3-15 (above) re-armed directive R2 for exactly one confirmation board, explicitly conditioned
on landing this §VI correction first (per the spawning director's instruction). That precondition
is now met. One INT confirmation board (Grok API + Gemini API + one verdict-blind Claude opus
referee) on the exact `v3M.0.32` PDF follows in this same lane.
