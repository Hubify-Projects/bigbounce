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
