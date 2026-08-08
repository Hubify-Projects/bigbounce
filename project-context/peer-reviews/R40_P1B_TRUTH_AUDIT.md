# R40 P1B — Truth-Audit Synthesis (pre-arXiv, v1B.0.74)

**Paper:** P1B MCMC companion — ΛCDM+ΔNeff proxy, NaMaster recovery, spectator-ALP check
**Source:** `arxiv/paper1b_mcmc_companion.tex` (2986 lines) · PDF md5=a29137f5 · 21 pp
**Audit lead:** Opus truth-audit + synthesis (R40 final)
**Vendor legs:** OpenAI (gpt-5, methodology, 23 findings incl. pass-2) · Gemini (2.5-pro, cosmology, 9) · Grok (4.3, brutal, 8) · Perplexity (**FAILED** — 100KB cap, 0 findings) · Claude Opus leg (**ACCEPT**, EXT19 fixes confirmed)

Per the peer-review-truth-audit standing protocol, every distinct finding is ground against the on-disk .tex / chains / bib before a severity is accepted. Reviewers lack repo context and over-call on artifacts the paper already addresses in prose.

## Verdict legend
VERIFIED-OPEN (real, needs closure) · STALE (already fixed in .tex) · MISLABELED (real but mis-severitied / opinion-as-essential) · OUT-OF-SCOPE (companion-paper boundary / external-bound) · DUPLICATE · OPINION

---

## EXT19 ALP-relic fix re-verification (highest scrutiny — Claude leg ACCEPT confirmed)

| Fix | On-disk check | Verdict |
|---|---|---|
| Anharmonic O(θ²/12) note | L2487 "anharmonic corrections enter at O(θ_i²/12)"; correct quadratic expansion of 1−cos θ. Doesn't feed a relic number. | CONFIRMED |
| z_osc≤0 frozen branch disjoint from oscillating evolution | L2529–2533: lightest masses held at ρ_a=V(θ_i) (CC-like), explicitly NOT diluted by (1+z_osc)⁻³ of Eq.(omega_a_def). Logically disjoint from Eq.(rho_a_evol) oscillating regime. | CONFIRMED |
| Small-θ prefactor Ω_a=m²θ²/(6H₀²(1+z_osc)³) | L2521, independently correct; ρ_crit,0=3H₀²M_Pl²≈3.7e-11 eV⁴ at L2519. | CONFIRMED |
| Table IV header has no spurious (C_aγ=8) | Confirmed by Claude leg; not re-contested by any R40 vendor. | CONFIRMED |
| β=0.28° derivation | L2249–2264: 5.81e-4 × 8 × 1.06 = 4.93e-3 rad = 0.28°. Reproduces. RK4 re-integration gives Δφ/f_a=1.0601. Artifact `c10b_alp_envelope_scan.json` + `alp_ode.py` exist on disk. | CONFIRMED |

**No R40 vendor claims the EXT19 fixes are wrong.** OpenAI-M7 (anharmonic error budget) and OpenAI-m4 (recast Eq.9 piecewise) touch this region but ask for *additional* validation, not correction — and the piecewise branch (m4) is already present at L2529–2533. EXT19 stands.

---

## Merged finding table (deduped across 4 legs)

| Merged ID | Vendor source(s) | Claim | On-disk verification | Verdict |
|---|---|---|---|---|
| **AB-SCOPE** | OAI-m9, GEM-E1, GROK-E1/E4 | Abstract framing of NaMaster bias / scope weaker than body | Abstract L1108–1121 carries full scope block: "MC pipeline-recovery figures, not sky-measurement systematics… not directly comparable… pipeline-validation figure, not a sky-detection significance claim." GEM-E1's requested inverse-variance context is at body L1997–2000 (β=0.264° weighted). | STALE (closed prior rounds; abstract already qualified) |
| **WEIGHTED-EST** | OAI-E1/E2/E5/E6/M10, GEM-E1 | Promote inverse-variance / (C_EE−C_BB) estimator to primary; rename χ² → S(β) | Body documents unweighted-as-canonical justification (L2034 "Canonical estimator choice"), weighted cross-check (L1997, β=0.264°, bias −0.006°), and attribution of ~80% bias to unweighted fit (L2000). Choice to keep the published-script-matching unweighted form as canonical is a documented methodological decision, not an error. | MISLABELED (OPINION-as-ESSENTIAL; legit referee preference, not a defect) |
| **W0WA-σ** | OAI-E3/M3, GEM-M1, GROK-M2 | +4.3σ/−3.6σ w0wa given undue prominence; SN overlap unmodeled; ΛCDM unsampled | fn:wcaveat (L1467) states verbatim: posterior-tail extrapolation, NOT Bayes-factor, NOT frequentist tension, Savage-Dickey not viable. w0wa is in §V.C cross-check (sec:w0wa_crosscheck L2140), **excluded from abstract** and **from headline Table I** (tab:verification "contains only the two frozen combinations", L1348). Overlap labeled "overlap-uncorrected/provisional" (L1496, L2143). | STALE (fully caveated + walled off) |
| **SN-CTRL-CHAINS** | OAI-E3, GEM-M1 | Provide Pantheon+-only / DES-only control chains, or remove w0wa | Control chains do NOT exist on disk; text (L1607–1612) defers them to "a separate follow-up note." BUT the w0wa block is a non-load-bearing caveated diagnostic, excluded from every headline surface; no claim gates on it. Vincenzi2025SNcompare (references.bib:447) cited for the rigorous overlap treatment. | OUT-OF-SCOPE (companion cross-check, non-load-bearing; running 2 new MCMC chains for a result already labeled non-evidence is gold-plating, not a pre-arXiv blocker) |
| **DOI-PENDING** | OAI-E4/M2, GROK-M3 | Frozen-chain DOIs "pending" | L2721, L2807, L2836: "DOI assignment is pending; identifiers will be inserted at submission." Zenodo DOI for P1A/P4 content already live (L2774, 10.5281/zenodo.4573248). DOI minting is a literal submission-day mechanical step (external-bound on arXiv/Zenodo handshake). | OUT-OF-SCOPE (submission-time mechanical; not a content defect) |
| **INTERNAL-PATHS** | OAI-M2 | Main text saturated with run-paths/pod labels | Paths are wrapped in `\path{}`/`\texttt{}` and concentrated in reproducibility prose + App. A; deliberate reproducibility posture for a *verification companion*. Style preference. | OPINION |
| **MB-H0-3.2σ** | OAI-M3, OAI-M8 (Mb vintage) | 3.2σ M_B offset readable as tension; 2020 M_B vs 2022 H0 vintage | L1639–1644 already states it is "a descriptive offset measure… not a properly conditioned tension statistic" and flags the estimator-mismatch / not-directly-comparable caveat. Riess+2020 anchor labeled explicitly (L1626). | STALE |
| **ALP-ANHARM-BUDGET** | OAI-M7 | Quantitative anharmonic error budget for Ω_a vs full EOM | Eq.(omega_a_def) verified against full EOM for committed params (L2528); spectator cuts use stored per-step Ω_a (L2534, c5_continuous). Anharmonic O(θ²/12) correction is sub-percent at the spectator-consistent θ_i∼0.1 sliver (the regime that matters); θ_i∼1 is the explicitly-excluded DE-ALP regime. | MISLABELED (extra validation request on a correct, already-EOM-checked calc) |
| **NAMASTER-extras** | OAI-M1/M9/M11/m10–m14 | β-indep χ² constant clarification, purify_b leakage diagnostic, ℓ-range sweep, βfree width, bootstrap on 42-sample slice | Polish-tier methods-appendix requests on an already-validated pipeline (500 MC, σ_β=0.046° rerun documented). None overturn a number. | OPINION / MISLABELED (polish) |
| **C_aγ benchmark** | OAI-M4 | "exceeds KSVZ/DFSZ" too categorical | Body states C_aγ≳8–10 lies beyond minimal |C_aγ|∼O(1); model-dependence acknowledged. Phrasing nit. | OPINION |
| **SELF-CONTAINMENT** | GEM-M2 | Add 1–2 ¶ summarizing Paper I(a) motivation | Companion-paper-by-design; Paper I(a) posted concurrently. Optional improvement. | OPINION |
| **LENGTH** | OAI (length note), GROK-M1 | 21 pp too long, condense to ≤12 | A verification companion's value IS its exhaustive reproducibility prose. Length is a deliberate choice; not a defect. | OPINION |
| **ECH-DERIVATION** | GROK-E3 | ALP coupling inserted by hand, not derived from Holst action | Paper *explicitly and repeatedly* states this is "not a distinctive ECH prediction" and a generic ALP consistency check (abstract L1138–1141, §VI). Grok's "fix" (re-title) is already the paper's own framing. Grok REJECT rests on this mischaracterization. | STALE / MISLABELED |
| **SAMPLE-COUNT** | GEM-m1 | 123,129 vs 119,617 getdist-thinned | Footnote 1 already explains getdist effective-sample thinning. Optional caption tweak. | OPINION |
| **FUTURE-DATE** | GEM-m3 | "June 14, 2026" date | Restamps each version bump; current date 2026-06-18. Will refresh at submission stamp. | STALE (handled by /pdf-restamp-bundle on next bump) |
| **COPYEDIT** | GROK-N1/N2, OAI-n1 | "the the", "deg vs °", hyphenation | Spot-checked: rendered-PDF justification artifacts, not source duplications. Minor copyedit. | OPINION |
| **Ref [4] arXiv ID** | OAI-n3 | Verify arXiv:2509.13654 | Placeholder companion-ref; resolves at concurrent posting. | OUT-OF-SCOPE (submission-time) |
| **Perplexity leg** | — | Call failed (100KB cap) | No findings produced; tool-level failure, not a paper defect. Citation forensics covered by OpenAI arithmetic spot-audit (all 6 checks PASS) + Claude leg (Eskilt2022 real). | N/A |

---

## Cross-leg dedupe summary

- 4 vendors × ~40 raw findings collapse to **18 distinct items**.
- **0 VERIFIED-OPEN.** Every item resolves to STALE (already in .tex), OPINION/MISLABELED (referee preference, not defect), or OUT-OF-SCOPE (submission-mechanical or companion-boundary).
- Grok's **REJECT** rests entirely on GROK-E3 (ECH-derivation), which is a mischaracterization — the paper's own thesis is that the ALP check is *generic, not ECH-distinctive*. Severity collapses to STALE.
- OpenAI/Gemini **MAJOR REVISIONS** verdicts are dominated by the weighted-estimator preference (OPINION) and the w0wa-σ framing (STALE — already walled off + caveated).
- Arithmetic spot-audit (OpenAI, independent): H0 tension 3.61σ/3.49σ, S8 2.59σ, β prefactor 0.282°, w_pivot −0.952, σ_pix 1.45µK, Ω_a small-θ scaling — **all CONFIRMED CORRECT**.
- EXT19 ALP-relic fixes: **all 4 re-verified intact and self-consistent** against alp_ode.py / c10b artifact / Eq.(omega_a_def).

## Closure list

**NONE.** Zero VERIFIED-OPEN findings. No source edits required before arXiv.

## Disposition

**ACCEPT.** P1B v1B.0.74 carries no real open defect. The two control chains (SN-CTRL-CHAINS) and DOI minting are the only non-present items and both are correctly classified out-of-scope for this companion paper at the pre-arXiv gate (non-load-bearing diagnostic + submission-day mechanical). P1B earns the 99 (final 1% reserved for Houston sign-off per readiness-cap-99).
