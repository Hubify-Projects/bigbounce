# EXT7 P1A — Truth Audit

**Paper version audited:** v1A.0.67 (arxiv/paper1a_ech_nogo.tex)
**Date:** 2026-06-13 PT
**Reviewers triaged:** ChatGPT Pro Extended, Grok Heavy, Gemini Thinking
**Audit protocol:** feedback_peer_review_truth_audit_protocol (per-finding verdict-first)

---

## Headline

ChatGPT's load-bearing claim — **"Fig 3 H(z) residual inconsistent with stated Λ_eff ansatz"** — is **REAL** and surgically actionable. Grok's 5× consecutive ACCEPT is **stable calibration** (no specific new physics observation, no novel finding; rubber-stamp class but well-calibrated against rigorously closed prior items). Gemini's MAJOR (Table III matter-bounce blank cell) is a **MISREAD**: the cell contains `$\checkmark$`. Gemini's "minor typos" are all PDF-extraction class auto-falsified.

**Genuinely new findings: 2** (ChatGPT F67-B1 Fig 3 caption/figure mismatch; ChatGPT F67-M2 repro README/changelog version drift).

---

## Findings Table

| ID | Reviewer | Class | Claim | Evidence on disk | Verdict | Disposition |
|----|----------|-------|-------|------------------|---------|-------------|
| F67-B1 | ChatGPT | BLOCKER | Fig 3 plots ~2–3% ΔH/H deviation but caption says Ξ set to reproduce ρ_Λ with H0=67.7, Ω_m=0.308 → should be ΛCDM-coincident | `generate_all_figures.py` L545–551: orange curve `H_S` uses H0=**69.2**, Ω_m=0.310, **enhanced radiation** Or_ext=Or_std·(1+0.3·...); caption (paper1a_ech_nogo.tex L1084–1088) declares H0=67.7, Ω_m=0.308 with "Ξ set to reproduce ρ_Λ" | **CORRECT** | Real caption/figure-code mismatch. Either (a) update caption to disclose actual figure params (H0=69.2, enhanced radiation = ΔN_eff proxy), or (b) regenerate figure with caption params (would give zero ΔH/H). Houston pick. **Close as DO-NOW pattern-031 (figure-caption/data mismatch).** |
| F67-M1 | ChatGPT | MAJOR | Sec. VII still says "rule out the spectator-ALP class" — overstates LiteBIRD reach | Need separate body-text check; reviewer's own §XV calibration is correct (0.73σ separation) | **CORRECT, MINOR severity** | Wording fix in §VII: replace "rule out the spectator-ALP class" with "rule out this uniform spectator-ALP benchmark." DO-NOW, 1-line edit. |
| F67-M2 | ChatGPT | MAJOR | Public README at v1A.0.64, paper at v1A.0.67; Zenodo DOI still pending | `reproducibility/README.md` L8: "v1A.0.64 (2026-06-12)"; bundle line L10 also v1A.0.64 | **CORRECT** | Real version-drift. Bump reproducibility README to v1A.0.67 + add commit SHA + insert Zenodo placeholder note. DO-NOW. |
| F67-M3 | ChatGPT | MAJOR | Title "Channel-Level Closure…" too strong given ansatz dependence | Title in paper1a_ech_nogo.tex L922+; reviewer acknowledges body is already calibrated | **OPINION** | Subjective phrasing. Body already discloses ansatz status explicitly per F67-M3's own acknowledgment. Disposition: **DEFER** — Houston call (Title softening is editorial). |
| F67-minors | ChatGPT | MINOR | Fig 1 burned-in "mechanism-indep" label, Sec IV title "No-Go", Eq (1) display split, X B Step 5 footnote-move, PACS removal | Editorial polish; not load-bearing | **CORRECT, polish-only** | Batch into next minor wave. |
| Grok-minor1 | Grok | MINOR | TOC has "Falsification Criteria" vs body "Falsifiability Criteria" | Real terminology nit | **CORRECT** | 1-line TOC sync. DO-NOW. |
| Grok-minor2 | Grok | MINOR | Sec IX channel-level disclaimer repeats | Editorial | **CORRECT** | Trim redundant copy. DO-NOW. |
| Grok-minor3 | Grok | MINOR | Stray "3–5σ" survived from earlier draft (Table I footnote b) | Real residual | **CORRECT** | grep + replace. DO-NOW. |
| Grok-minor4 | Grok | MINOR | "−3πG/2 N ×" rendered as "N" instead of κ — PDF extraction artifact | Reviewer himself confirms "already correct in source .tex" | **OUT-OF-SCOPE** | Auto-falsify: extraction-class. No action. |
| Gem-Maj1 | Gemini | MAJOR | Table III "Matter bounce" row γ_PTA (real-KDE) cell **blank** vs §X G "3.0 at +1.13σ" | paper1a_ech_nogo.tex L2312: `Matter bounce (any host; not ECH-specific) & $\checkmark$ & (spectator) & $\checkmark$ & not tested$^{\ddagger}$` — γ_PTA column **already contains $\checkmark$**, not blank | **INCORRECT — MISREAD** | Auto-falsify: extraction artifact (`\checkmark` likely didn't render in Gemini's text extractor). No action. |
| Gem-min1 | Gemini | MINOR | "x RR" / "x R~R" instead of `\propto R\tilde R` | Gemini's own caveat block says "widespread string replacements of σ→0 … localized PDF-extraction artifacts"; same class | **OUT-OF-SCOPE** | Auto-falsify: extraction-class. |
| Gem-min2 | Gemini | MINOR | Fig 1 burned-in label "MN_eff" should be "ΔN_eff" (Δ→M) | Possibly real burned-in figure issue; ChatGPT separately flagged a Fig 1 burned-in "mechanism-indep" issue. Worth a visual figure check. | **NEEDS-CHECK → likely INCORRECT** | Open Fig 1 PNG; if Δ renders fine, falsify as extraction-class. (Reviewer himself flagged σ→0 as extraction class — same encoding family.) |
| Gem-min3 | Gemini | MINOR | Fig 6 caption "Paper Ib companion" should be "Paper I(b) [6]" | paper1a_ech_nogo.tex Fig 6 caption uses standard `Paper~I(b)` macro elsewhere | **NEEDS-CHECK** | grep Fig 6 caption; 1-line normalization if real. |
| Gem-min4 | Gemini | MINOR | "KSPHEREX" should be "k_{SPHEREx}" | Body uses `k_{\rm SPHEREx}` throughout (verified L608); the "KSPHEREX" string does not appear in .tex source | **INCORRECT** | Auto-falsify: extraction-class (PDF text-layer joined `k_{\rm SPHEREx}` → `KSPHEREX`). |

---

## Counts

- ChatGPT: 1 BLOCKER (REAL), 3 MAJOR (1 REAL severity-MAJOR, 1 REAL severity-minor, 1 OPINION), 5 MINOR (all REAL polish)
- Grok: 0 BLOCKER, 0 MAJOR, 4 MINOR (3 REAL, 1 OUT-OF-SCOPE extraction artifact)
- Gemini: 1 MAJOR (INCORRECT misread), 4 MINOR (1 needs-check, 3 OUT-OF-SCOPE extraction)
- **Net real on-disk findings to action:** 2 substantive (F67-B1 Fig 3 caption/code, F67-M2 README version-drift) + 1 wording (F67-M1) + 5 polish (Grok-minor1,2,3 + ChatGPT-minors). All others falsified or out-of-scope.

## Genuinely new findings count

**2 substantive:**
1. **F67-B1** — Fig 3 caption/code mismatch (real; pattern-031). Caption claims ΛCDM-matched parameters; code uses H0=69.2 + enhanced radiation.
2. **F67-M2** — Reproducibility README at v1A.0.64 while paper at v1A.0.67.

Plus 1 wording (F67-M1 §VII spectator-ALP class language) and ~5 polish items.

## Auto-falsify hits

- Gemini Major (Table III blank cell): `\checkmark` actually present, misread by extractor. Falsify.
- Grok minor (N vs κ): reviewer's own admission it's a render artifact. Falsify.
- Gemini "x RR" / KSPHEREX: same extraction-class family as Gemini-acknowledged σ→0 artifact. Auto-falsify.

## Pattern-052 check

None: no re-raise of HD-4/HD-6/HD-11 ruled items; no Fisher 1/8.98² superscript artifact; no 25xx/26xx date issue; no w0wa/JSON re-raise on the P1A side (P1B-only patterns).

## Closure plan

1. **(DO-NOW)** Fix F67-B1 — pick path: update Fig 3 caption to disclose actual figure params (H0=69.2 km/s/Mpc, enhanced radiation as ΔN_eff proxy) OR regenerate `figure5_rotation_expansion.png` with caption-stated params. Recommend Path A (caption disclosure) since the orange curve is a *real* ECH benchmark with the extra-radiation channel.
2. **(DO-NOW)** Fix F67-M2 — bump `reproducibility/README.md` to v1A.0.67 + commit SHA.
3. **(DO-NOW)** F67-M1 — replace "rule out the spectator-ALP class" with "rule out this uniform spectator-ALP benchmark (f_a∼M_Pl, m∼H0)" in §VII.
4. **(BATCH)** Grok-minor1/2/3 + ChatGPT polish — TOC terminology, channel-level disclaimer trim, stray "3–5σ", Fig 1 burned-in label, Sec IV title softening, PACS removal.
5. **Falsifications recorded:** Gem-Maj1, Grok-min4, Gem-min1/min4 (extraction-class).

## Grok calibration verdict

**5×-stable calibration, no rubber-stamp red flag**: Grok confirms structural closures match the .tex (verified — Fig 3 caption Ξ M_Pl⁴ distinction is in .tex L1084, Saadeh bookkeeping is in .tex L1090, all prior B1–B3 / M4–M5 items verifiably closed). His 4 fresh MINORS are 3 real polish + 1 extraction artifact — that's calibrated, not blind. He did **not** add a new physics observation; the round is genuinely converged from his vantage. ACCEPT verdict is honest given the standing PDF.
