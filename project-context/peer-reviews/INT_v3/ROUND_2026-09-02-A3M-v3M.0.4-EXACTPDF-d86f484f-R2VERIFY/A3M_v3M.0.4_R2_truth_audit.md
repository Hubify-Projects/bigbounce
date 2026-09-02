# A3M v3M.0.4 — R2 verification-pass truth audit (Opus, independent)

- **Round:** `ROUND_2026-09-02-A3M-v3M.0.4-EXACTPDF-d86f484f-R2VERIFY`
- **Manuscript:** `research/track_a3_multichannel/paper/main.pdf`, v3M.0.4, 8 pp
- **sha256 (verified this session):** `d86f484f5d4f83fb7b4a339cced6a9c4bf9482f5f5bc206a55bdbfe2270e277c` ✓ matches every leg header
- **Auditor:** Opus, skeptical both ways; verdicts decided from source (tex lines, committed JSON, own re-execution), never from verdict words.
- **Date:** 2026-09-02

## 0. Leg census (Rule 4 / Rule 8)

| Leg | Model | Verdict word (diagnostic only) | Tagged items in raw | Dispositioned | Gap |
|---|---|---|---|---|---|
| Claude Fable INT | claude-fable-5-1 | MINOR REVISIONS | 0 MAJOR / 9 MINOR (m-R2-1…9) | 9 | no |
| Grok API | grok-4.3 | REJECT | 3 ESSENTIAL / 3 MAJOR / 2 MINOR / 1 NIT = 9 | 9 | no |
| Gemini API | gemini-3.1-pro-preview | MAJOR REVISIONS | 4 ESSENTIAL / 4 MAJOR / 3 MINOR-NIT = 11 | 11 | no |
| Perplexity | — | **ABSENT** (leg not run — recorded absent, never as clean) | — | — | — |

**BLOCKERs: 0** (explicit observation, all legs). Total raw findings 29; canonical after
fingerprint-dedup across legs and against `DISPOSITIONS/A3M.md` (R1): **11 new + 5 carried-open R1 minors**.

## 1. Independent recomputation performed by this auditor

| Object | Command / source | Result |
|---|---|---|
| PDF binding | `shasum -a 256 research/track_a3_multichannel/paper/main.pdf` | `d86f484f…e277c` ✓ |
| PBH abundance formula vs code | printed Eq. (10) `main.tex:594–599` vs `pbh_compaction_fnl.py:265–271` | **identical term-by-term** (`1/Ω_DM · (M_⊙/M_H)^{1/2} · (g_*/106.75)^{3/4} · (g_{*s}/106.75)^{-1} · β/7.9e-10`) |
| Gaussian calibration | module-loaded `f_pbh(0, A*=0.131446)` | **1.000032** ✓ (paper: calibrated to 1) |
| Table III row (0.5,1.0,0.5) | `f_pbh(-35/16,A*)`, `f_pbh(-35/8,A*)` | **3.62e−14**, **1.569e−2** ✓ (paper: 3.6e−14, 1.6e−2) |
| Gemini's "unphysical" arithmetic | `f_pbh_of_beta(7.9e-10)` | 6.62e6 — reproduces Gemini's number, but 7.9e−10 is a **reference normalisation**, not β at M_H=10²⁰ g |
| Eq. (8) ceiling | `zeta_ceiling` in `pbh_abundance_fnl.py:93–95` vs `main.tex:449–451` | formula identical; quoted 0.09524 / 0.19048 = **first term only** (−5/12f_NL) |
| "synthetic injection" provenance | `pipelines/p3_pta_mcmc/free_spectrum_real_2026-05-01/emcee_freespec.py:176–183`; `h200_scripts/experiments/nanograv_ptarcade.py:60–120`; `pipelines/h200_results/phase4_science/nanograv_ptarcade/nanograv_ptarcade_summary.json` | **injected γ = GAMMA_NANO = 3.2, not 13/3**; 6 signal bins, Gaussian χ² likelihood, seeded scatter + noise-floor bias; recovery 3.19255 ± 0.42326 → **−0.018σ** |
| r = 0.84 | `main.tex:627–637`, Table IV caption `644–646` | numeral still printed; projected column dropped; no result depends on it |
| "method-independent" occurrences | `grep -n method-independent main.tex` → 48, 260, 671, 703 | every one says such a confirmation **remains open**; none labels the result method-independent |
| Abstract PBH caveat | `main.tex:73–82` | perturbativity + non-monotonicity caveats **present verbatim** |
| Abstract DESI | `main.tex:80–83` | quotes **only** the merger-prior −3.6 / 0.16σ; universality (+3.5 / 0.77σ) omitted |
| Zenodo DOI | `grep -n -i zenodo main.tex` → 763, 826 | the only DOI is NANOGrav's data DOI; **no frozen release DOI for this work's code** |

## 2. Per-finding table

Severity read from per-item tags (Rule 8), never from the leg's verdict word.

| # | Leg · id | Claim · location | Verification (source-cited) | Verdict | Sev | Closure |
|---|---|---|---|---|---|---|
| 1 | Gemini M3 | §IV C injection is a *failed* test: injected 13/3 vs recovered 3.19±0.42 = 2.72σ bias | Gemini's premise is wrong but the underlying defect is **worse**. `nanograv_ptarcade.py:97–108` builds the mock from the NANOGrav **published power law at γ=3.2** plus noise-floor bias and seeded scatter, fits **6** signal bins with a Gaussian χ² likelihood; recovery 3.19255±0.42326 = **−0.018σ** of the *actual* injection. The 30-bin free-spectrum KDE refit (`emcee_freespec.py`) merely **hard-codes** those two constants at lines 177–178. So (a) nothing was injected at 13/3, (b) it is **not** "the identical pipeline", (c) `main.tex:416–419` misdescribes its own artifact and the unbiasedness claim it supports is **unsupported**. | **GENUINELY-NEW-REAL** | **MAJOR** | **DA3M-R2-01** — either rewrite §IV C to the truth (injection at γ=3.2, earlier 6-bin power-law-summary pipeline, −0.02σ) and delete "identical pipeline"/"SMBHB-like"/"injected γ=13/3", **or** run a real γ=13/3 injection through `emcee_freespec.py` at 30 bins (~minutes) and report it. Science decision required — see §4. |
| 2 | Gemini M4 | Eq. (8) numbers silently drop the σ² term; "scales as 1/\|f_NL\|" and "exactly a factor of 2" are false for the full expression | Correct. `main.tex:449–454`: ζ_max = −5/(12f_NL) + (3/5)\|f_NL\|σ²; 0.09524 and 0.19048 are exactly 5·8/(12·35) and 5·16/(12·35) — the **first term alone**. At σ=0.1 the full values are 0.1215 / 0.2036 (ratio 1.68). Repeated at `main.tex:470` ("exactly doubles … remains arithmetically true"). Confined to the superseded first pass the paper already calls "physically empty"; no headline number depends on it. | **GENUINELY-NEW-REAL** | MINOR (substantive) | **DA3M-R2-02** — qualify both places: the *leading* term scales as 1/\|f_NL\| and doubles exactly; state the σ² term is subleading and dropped for the quoted numbers. |
| 3 | Gemini E4 | "Ω_DM = 0.674" is Planck's *h*; Ω_DM ≈ 0.26 | The value is faithfully carried from Choudhury *et al.* Eq. (66) as recorded in `PBH_COMPACTION_NOTE_2026-09-02.md:108–111` and `pbh_compaction_fnl.py:156` ("their Eq. 66 value"), so it is not an arithmetic slip by this paper — but 0.674 **is** numerically the Planck 2018 *h*, and Ω_DM ≈ 0.264. Downstream effect is bounded: `main.tex:518` states Ω_DM cancels in the ratio, and the Gaussian calibration to f_PBH=1 absorbs the rest, so Eq. (9), Table III and every quoted result are unchanged. Not verifiable further without the source paper. | **GENUINELY-NEW-REAL** | MINOR (substantive) | **DA3M-R2-03** — one footnote: the value is quoted as printed in Choudhury *et al.* Eq. (66), note it coincides with Planck *h* and that every result reported here is independent of it (it cancels in the ratio and is absorbed by the Gaussian calibration). Do **not** silently change it. |
| 4 | Fable m-R2-1 | 13/3 Savage–Dickey precision inconsistent with the paper's own "one significant figure" rule | Confirmed: `main.tex:379–380` states one s.f.; Table II prints 4.5×10⁻⁴ and `409–410` prints 7.1×10³ / +3.85. 9 tail samples ⇒ ~±0.2 dex. Residual of R1 **DA3M-02** (PARTIAL). | **GENUINELY-NEW-REAL** | MINOR | **DA3M-R2-04** — print 5×10⁻⁴, ~7×10³, log₁₀B ≈ 3.9 (or +3.9±0.2). |
| 5 | Fable m-R2-2 ≡ Gemini N3 | Duplicated clause, §VII C (ii) | `main.tex:715–718` verbatim duplication introduced by the R1 rewrite. | **GENUINELY-NEW-REAL** | MINOR | **DA3M-R2-05** — delete the duplicate clause. |
| 6 | Fable m-R2-3 ≡ Gemini N1 | "(deviation D1 above)" / "deviations (D1–D5)" never defined | `main.tex:516` precedes the only mention at `603–605`; D1–D5 live only in `PBH_COMPACTION_NOTE_2026-09-02.md`. Directive-Q1 internal-note leakage. | **GENUINELY-NEW-REAL** | MINOR | **DA3M-R2-06** — replace with plain prose ("the unreconstructible source spectrum, Sec. V B"). |
| 7 | Fable m-R2-4 | "the refit's 3.1–4.6σ" spans two conditionings; L370's σ unlabelled | `main.tex:427`: 3.1σ is the official-posterior tension, 4.63σ the refit's. `370`: the 1.20σ offset uses the quadrature σ=0.53. | **GENUINELY-NEW-REAL** | MINOR | **DA3M-R2-07** — one clause each. |
| 8 | Fable m-R2-5 | "3.13–4.38σ bare once a shape-overlap projection is derived" is logically inverted | `main.tex:683–684`; the bare value does not depend on the projection. | **GENUINELY-NEW-REAL** | MINOR | **DA3M-R2-08** — reword. |
| 9 | Gemini E1 | Abstract quotes only the DESI merger-prior constraint | Confirmed: abstract `main.tex:80–83` gives −3.6 / 0.16σ only; body `619–625` states the two priors are mutually exclusive and not directly comparable. Real abstract-vs-body calibration gap. | **GENUINELY-NEW-REAL** | MINOR | **DA3M-R2-09** — name the prior in the abstract, or quote both. |
| 10 | Gemini E2 (residual) | r = 0.84 imported from an unpublished draft — standalone-reader violation | The *load-bearing* half is FALSIFIED: `main.tex:633–637` and Table IV caption drop the r-projected column, and the abstract quotes only bare σ, so **no result depends on r** (= R1 DA3M-06 closed, option b). Residual real bit: the numeral 0.84 is still printed with no derivation and no public source. | **GENUINELY-NEW-REAL** (residual) | MINOR | **DA3M-R2-10** — drop the numeral (keep the qualitative statement) or derive it in an appendix. |
| 11 | Gemini E3 | No frozen-release DOI for code/data | Confirmed: the only DOI in the paper is NANOGrav's Zenodo 8060824 (`main.tex:763, 826`); this work's artifacts are pinned by a GitHub commit hash only. Directive-Q2 class; packaging, not science. | **GENUINELY-NEW-REAL** | MINOR (VENUE/packaging) | **DA3M-R2-11** — mint a Zenodo DOI for the exact commit in the P-round. |
| 12 | Fable m-R2-6 | Five R1 minors unaddressed | Verified on the exact PDF: **m04** Table II caption `387–388` unchanged; **m09** `225–227` still "without identifying the exact algebraic line" vs the note's Eqs. (38)–(40); **m11** Table I row `197–207` unqualified; **m12** `283–288` r's complex nature unstated; **m15** `410–411` "nested factor" undefined. None appears in the SSOT item→edit table ⇒ omissions, not mis-closures. | **GENUINELY-NEW-REAL** (carried) | MINOR (m11, m12 are correctness qualifiers) | close **DA3M-m04, m09, m11, m12, m15** as originally specified. |
| 13 | Grok E1 | Abstract "No channel is in tension with another" incompatible with the scheme-dependent transmission bound | The same abstract states the conditionality two sentences earlier (`main.tex:50–56`: "within a handoff scheme … no bound on the physical post-bounce f_NL follows"), and the transmission bound is not a channel measurement, so no incompatibility exists. | RE-FLAG-OF-DISCLOSED | — | none (optional: the abstract-trim pass may sharpen the sentence). |
| 14 | Grok E2 | Abstract quotes 1.732[1.610,1.809] stripped of its regime-of-validity caveat | **FALSIFIED.** `main.tex:73–82` carries "within a quadratic local map that is not always perturbatively controlled … (1.2\|f_NL\|σ_r≈0.5–2)" and the ~55-decade non-monotonicity, in the abstract. | FALSIFIED | — | none. |
| 15 | Grok E3 | Paper labels the in-in result "method-independent" while a cross-check remains open | **FALSIFIED.** All four occurrences (`main.tex:48, 260, 671, 703`) say a method-independent confirmation **remains open**; R1 DA3M-05 removed every "CLOSED". Grok inverted the sentence. | FALSIFIED | — | none. |
| 16 | Grok M1 | Withdraw the 1.732 ratio as a primary result / replace with the full curve | = R1 **DA3M-04**, closed by decision D3 (`main.tex:525–544`): non-monotonicity, anti-correlated branch and per-candidate excursions are all now stated. Demotion was explicitly rejected at R1 as an unjustified weakening; the ratio holds at all 27 grid points (std 0.050). | RE-FLAG-OF-DISCLOSED | — | none. |
| 17 | Grok M2 | 1.14σ / 4.63σ Gaussian approximations need a "not directly comparable" tag at every juxtaposition | Disclosed once, correctly: `main.tex:404–406` ("Gaussian approximations … P(γ>3)=8.97 %") and `427–430`. "At every juxtaposition" is a style preference; the substantive half is DA3M-R2-07. | RE-FLAG-OF-DISCLOSED / OPINION | — | folded into DA3M-R2-07. |
| 18 | Grok M3 | Abstract quotes un-re-derived SPHEREx forecast significances | = R1 **DA3M-06**, closed: the abstract itself says "pending a shape-overlap projection this paper has not yet re-derived at the −35/16 fiducial", and the bare numbers are elementary \|f_NL\|/σ arithmetic (recomputed: 3.125, 4.375, 2.19 ✓). | RE-FLAG-OF-DISCLOSED | — | none (residual = DA3M-R2-10). |
| 19 | Gemini M1 | "Severe numerical inconsistency in the PBH abundance formula"; exponent should be (M_H/M_⊙)^{−1/2}; 7.9e−10 gives f_PBH = 6.6e6 | **FALSIFIED, two ways.** (a) (M_⊙/M_H)^{1/2} ≡ (M_H/M_⊙)^{−1/2} — Gemini's "correction" is algebraically the same expression, and both `pbh_abundance_fnl.py:98–100` (Sasaki 1.68e8 (M/M_⊙)^{−1/2}β) and `pbh_compaction_fnl.py:265–271` carry that sign. (b) 7.9×10⁻¹⁰ is the **reference normalisation** in the denominator, not β at M_H = 10²⁰ g; the actual β there is ~10⁻¹⁶. Printed Eq. (10) is term-by-term identical to the executed code, and the code reproduces the paper's numbers exactly (f_PBH(0,A*) = 1.000032; 3.62e−14 / 1.569e−2 vs Table III's 3.6e−14 / 1.6e−2). **No recomputation is required.** | FALSIFIED | — | none. (Residual real item is the Ω_DM *label*, DA3M-R2-03.) |
| 20 | Gemini M2 | 55-decade non-monotonicity and "dominates formation" unsupported; points to an external JSON | The scan is a committed artifact (`outputs/pbh_compaction_fnl.json → f_NL_continuity_scan`), independently reproduced at R1 (1 → 7.50e−55 at −0.35 → 1.57e−2 at −35/8), disclosed in-text `535–544`, and the Fig. 1 caption points to it. "Add a plot/table" is a presentation preference; the unquantified "dominates formation" is one clause. | RE-FLAG-OF-DISCLOSED (+ GENRE) | — | optional: add the scan as a Fig. 1 inset in the venue pass. |
| 21 | Gemini N2 | Table II caption "differences from the archived record are ≤3×10⁻¹⁵" is version-history language | Identical fingerprint to R1 **DA3M-m04**, still open — counted at row 12, not double-counted. | (dup of m04) | MINOR | see row 12. |
| 22 | Grok N1 | Internal-audit phrasing, commit hashes, reproducibility statement in the body | R1 **DA3M-08** closed the tags (`grep "A3-[0-9]\|superseded\|prior version\|CLOSED"` → 0 body hits); repo URLs are consolidated in the Reproducibility statement `733–737`, which is standard PRD Data-Availability content. Residual = AI-disclosure placement. | RE-FLAG-OF-DISCLOSED / GENRE | — | venue pass. |
| 23 | Grok N2 | Fig. 1 / Table III notation inconsistent (f_NL vs A); x-axis units unstated | The axis is `pbh_compaction_fnl.py:607` "lognormal curvature power-spectrum amplitude A" — dimensionless, so there are no units to state; Table III tabulates f_PBH *at* the calibrated A. Presentation preference. | OPINION/GENRE | — | optional. |
| 24 | Grok N3 | References lack DOIs; NANOGrav 14-bin posterior unverifiable from abstracts | Bibliography style item (= DA3M-G1); the 14-bin posterior was verified from the arXiv:2306.16213 source PDF at R1 and re-fetched by the Fable leg. | OPINION/GENRE | — | venue pass. |
| 25 | Fable m-R2-7 | Abstract ≈500 words vs PRD ≈250 | = DA3M-G2. Content is now stable, so the trim is unblocked. | OPINION/GENRE | — | venue pass, after DA3M-R2-01/09. |
| 26 | Fable m-R2-8 | Mixed bibliography style; AI-disclosure placement | = DA3M-G1 / DA3M-08 residual. | OPINION/GENRE | — | venue pass. |
| 27 | Fable m-R2-9 | `.tex` header comment still reads "SKELETON … stubs pending" | Source hygiene; not in the PDF. | OPINION/GENRE | — | trivial. |

### Correction to an R1 disposition (recorded, never backfilled silently)

**DA3M-F1** (R1, FALSIFIED) cited "the lab's own synthetic power-law injection recovers γ = 3.1925 ± 0.4233
**with the same 30-bin pipeline**". Row 1 above establishes that this is not what the artifact is: the
injection is at γ = 3.2 through a different 6-bin pipeline. F1's **second** leg — that NANOGrav's ±0.6 is a
5–95 % half-width (1σ ≈ 0.365 < the refit's 0.382), so the refit error is not narrower — is unaffected and
stands, so F1's verdict (FALSIFIED) survives on that leg alone. The bin-choice-bias half is downgraded to
**unproven pending DA3M-R2-01's closure**. Dated 2026-09-02, R2 pass.

## 3. Closure plan for v3M.0.5

**SUBSTANTIVE (must close):** DA3M-R2-01 (the only MAJOR), R2-02, R2-03, R2-04, R2-05, R2-06, R2-07,
R2-08, R2-09, R2-10, plus carried R1 minors m04, m09, m11, m12, m15. Every one but R2-01 is a
one-sentence or one-clause edit requiring no new computation.

**GENRE/LENGTH/VENUE (P-round, not a review item):** abstract trim to ≈250 words (G2); bibliography
style + DOIs (G1, Grok N3); AI-disclosure placement; `.tex` header comment; optional Fig. 1 continuity
inset (Gemini M2); Zenodo frozen-release DOI (DA3M-R2-11).

Directive-G hygiene applies to the bundle: bump `\paperVersion`/`\paperTimestamp`, recompile to 0
undefined refs, `/latex-audit`, re-mirror byte-identical, re-verify the sha256 binding.

## 4. Convergence statement (directive R2)

**NOT converged at v3M.0.4, and a science decision is outstanding.**

The convergence budget is now **2 of 2 rounds consumed**, and the R2 verification confirms R1's closures
were real (17/20 as specified, 1 PARTIAL, 5 minors omitted) with **no closure introducing a new factual
error** and **no number in the manuscript failing recomputation**. Gemini's headline "severe numerical
inconsistency in the PBH abundance formula" is **FALSIFIED** — the printed equation is term-by-term
identical to the executed code and the code reproduces the paper's numbers exactly — so **no PBH
recomputation is required**, and its "imported un-derived parameter" (r = 0.84) is **no longer
load-bearing** (projected column dropped at R1); only the printed numeral needs removing or deriving.

The one item that is **not** a copy-edit is **DA3M-R2-01**: §IV C's injection-validation subsection —
itself added by the R1 closure — misdescribes the artifact it cites. Its claim ("identical pipeline …
injected γ = 13/3 … approximately unbiased") is not what `nanograv_ptarcade.py` did (γ = 3.2, 6 bins,
different likelihood). Two honest closures exist: **(a)** restate §IV C truthfully as a γ = 3.2 injection
through the earlier pipeline (−0.02σ) and drop the unbiasedness claim for the 30-bin refit, or **(b)** run
a genuine γ = 13/3 injection through `emcee_freespec.py` at 30 bins (minutes of compute) and report the
recovered value whatever it is. **(b) is the stronger close** and is the only path that actually supports
the unbiasedness statement the paper wants to make; it is a Houston/owner decision, not a referee item.

**Per directive R2, this is the last review round.** After v3M.0.5 closes the 15 substantive items above,
rounds STOP: every remaining finding on the ledger is genre, length, or venue. A further round would be
budget-violating noise. Re-testing is warranted only if closure (b) changes a reported number.
