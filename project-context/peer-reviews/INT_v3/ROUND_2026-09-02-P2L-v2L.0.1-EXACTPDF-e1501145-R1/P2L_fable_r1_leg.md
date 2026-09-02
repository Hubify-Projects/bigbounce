# P2L — INT referee leg R1 (Fable tier)

- **Reviewer:** Claude INT leg (independent PRD-Letters referee stance, in-in formalism)
- **Model:** claude-fable (Fable 5.1)
- **Round label:** ROUND_2026-09-02-P2L-v2L.0.1-EXACTPDF-e1501145-R1
- **Manuscript:** `arxiv/paper2prime_fnl_letter/main.pdf` — v2L.0.1, 4 pages, dated September 2, 2026
- **sha256:** `e1501145bd314f85e54c928c579ec1e3ceb96bbdf078ba15ab02e2bb40ca4d12`
- **Bound to:** that exact file; pages rendered at 300 DPI (pdftoppm) and `main.tex` grepped before every equation/number claim below.
- **Date of review:** 2026-09-02
- **Independence:** verdict and findings 1–13 were formed before reading the Grok/Gemini raws; §C was written afterwards.

---

## A. What I recomputed myself (not taken from the manuscript or its scripts)

1. **Committed script re-run.** `research/theory_audit/fnl_matter_contraction_adjudication_2026_09_02.py` executed end-to-end (exit 0, ~2 min). Output reproduces Table I row-by-row, the dS/USR validations, the δN values −5 (comoving) and −55/16 (uniform-density), and `A_total − A_T(Cai Eq. 37, distinct-monomial reading) = 0`.

2. **Own in-in code for two vertices** (own mode functions, own E1-recurrence integrals, own Wick sum over S3; nothing transcribed):
   - mode function `u_k = e^{−ikη}(1 − i/kη)/(√3 c η² √(2k))`, Wronskian `i/(2a²ε)` verified;
   - vertex `(a²ε³/2) ζ(∂i∂jχ̃)²`: isoceles −15/32, equilateral −15/128, folded −15/32, fixed-μ −15/32 (no μ²) — **matches Table I**;
   - vertex `−2a²ε² ζ′∂ζ·∂χ̃`: isoceles 0, equilateral −5/8, folded 2, fixed-μ (15/8)μ² — **matches Table I**.

3. **Cai 2009 Eq. (37) from the arXiv source (`matterbounceng2.tex`)**, both index readings:
   - distinct-monomial reading: squeezed −35/16, equilateral −255/128, folded −9/8 — exactly half of Cai's quoted −35/8, −255/64, −9/4;
   - six-permutation reading: −305/64, −585/128, −237/64 — matches nothing.
   So "uniform factor 2 between Cai's printed polynomial and Cai's quoted amplitudes" is **confirmed** in all three configurations.

4. **Li et al. 2016 Eq. (4.19) at c_s=1 from its arXiv source (`general_matter_bounce_cosmology.tex`)**: isoceles −35/16, equilateral −255/128, folded −9/8; and — this is the decisive check for the novelty claim — the **fixed-angle squeezed limit of the published polynomial is `−35/16 + (15/16)μ²`**, using k₂,₃ = |±k k̂ − k₁/2|. The orientation dependence is therefore entirely contained in the shape function published in 2009/2016; nothing beyond the published polynomial is needed to obtain it.

5. Arithmetic: (5ε−35)/8 at ε=3/2 = −55/16 ✓; monopole −35/16 + (15/16)(1/3) = −15/8 ✓; Table I column sums ✓; 2.1875/0.7 = 3.13, 2.1875/0.5 = 4.38 ✓; DESI 2.1875/σ≈9 ≈ 0.24σ.

---

## B. Numbered findings

### MAJOR

**M1 — Wrong general-ε formula for the uniform-density δN result (p. 2, col. 2, lines 1–2; tex line "f_{\rm NL}^\rho=(5\epsilon-7)\cdot 5/8").**
`(5ε−7)·5/8` at ε=3/2 gives +5/16, not −55/16. The committed script (log line "f_NL(eps) = 5*(epsilon − 7)/8") and the adjudication brief both give `5(ε−7)/8 ≡ (5ε−35)/8`. Replace with `f^ρ_NL = 5(ε−7)/8`. As printed, the Letter's cross-check paragraph is self-contradictory.

**M2 — The "new result" claim for the orientation dependence is overstated (abstract; §III "Orientation dependence"; Summary).**
My recomputation (A.4) shows `f(μ) = −35/16 + (15/16)μ²` follows directly from Li et al.'s published Eq. (4.19) at c_s=1 (equivalently Cai's Eq. 37): the 1/k₁² monomials `k_i⁷k_j²/∏k²` etc. cancel exactly only at k₂=k₃ and leave an O(1) term ∝ [(k₂−k₃)/k₁]² = μ². What is genuinely new is (i) noticing it, (ii) the per-vertex attribution to the χ̃-vertices and (iii) the shear interpretation. The abstract's "We report a new result: the squeezed limit is orientation dependent" should be reworded to "a previously unremarked property of the (correct) published shape function", with the derivation from Eq. (4.19)/Eq. (37) stated in one sentence — this also answers Grok's M2/M4 without adding an appendix. Evidence grade is otherwise fine: it is exact algebra, not a conjecture.

**M3 — Which amplitude does a survey test? The Letter never says (Table II, §V, abstract).**
Having established that the squeezed limit is not a single number (isoceles −35/16, angle-averaged monopole −15/8, quadrupole 15/16), the Letter then forecasts "−35/16 vs −35/8" as if the isoceles value were the local-template amplitude. A scale-dependent-bias or bispectrum estimator fits the local template to the full shape; the effective amplitude is a projection, not the μ=0 slice. The A3 brief in fact uses a shape-projection factor r=0.84 — this is where the unexplained "2.6σ" (=3.13×0.84) and "3.7σ" (=4.38×0.84) come from, but neither r nor its definition appears in the Letter. Required: (a) state explicitly what amplitude enters each channel and why (isoceles / monopole / template projection with r defined), (b) state σ_fNL for DESI DR1 (≈9) and cite the DESI paper, (c) give the two ends of each σ range their meaning (bare vs projected). Without this, Table II is unverifiable from the Letter and the μ² result and the forecast contradict each other in spirit.

**M4 — Bibliography contains two entries that do not correspond to real papers (refs [2] and [6]).**
- Ref [2] "M. Li, J. Quintin, Y. Wang, and X. Cai, *Origin and reconstruction of non-gaussianity in matter bounce cosmologies*, JCAP 1603, 031" — arXiv:1612.02036 is Li, Quintin, Wang, **Yi-Fu Cai**, *Matter bounce cosmology with a generalized single field: non-Gaussianity and an extended no-go theorem*, JCAP 03 (2017) 031 (title and author verified from the arXiv source; a Dec-2016 preprint cannot be JCAP 1603).
- Ref [6] "X. Chen, M. H. Namjoo, Y. Wang, *Quantum primordial standard clocks*, JCAP 1302, 006, arXiv:1301.5699" — 1301.5699 is Chen, Firouzjahi, Namjoo, Sasaki, *A single field inflation model with large local non-Gaussianity* (EPL 102, 59001); *Quantum primordial standard clocks* is arXiv:1411.2349, JCAP 02 (2015) 006. The text cites "Chen, Namjoo and Wang" for the non-attractor clock argument; pick one paper and cite it correctly (the adjudication brief itself cites 1301.5699 with the correct authors).
A 16-reference Letter with two fabricated-looking entries will be returned by any editor.

**M5 — Load-bearing statements imported from unpublished repository markdown (§III "ζ_ρ = 2ζ_c"; §IV bound 0 < T ≤ 1/2 and 0.165–0.409; refs [13]–[15] are `blob/main` URLs).**
The Letter is honest that the bounce cubic term is not computed, and the linear-transfer bound is correctly described as a bound. But `T = [1−ρ(η_h)]/2`, its range, and `ζ_ρ = 2ζ_c` are stated with no derivation, no published citation, and only mutable GitHub links as evidence. For PRD-L self-containedness: give the one-line gauge argument for ζ_ρ = 2ζ_c (it is the ratio of the linear δN rows, `2√3 u_i/(√ε(3−ε))` vs `√3 u_i/(√ε(3−ε))`, and follows from ρ = ρ(φ, φ̇) on the growing mode), give the two-line origin of T = (1−ρ)/2 (growing/constant-branch mixing at handoff, parity of the even solution), and pin refs [13]–[15] to a commit hash or Zenodo DOI. Otherwise move §IV to the companion paper and keep only the honest one-sentence caveat.

### MINOR

**m1 — Abstract "SPHEREx reaches 2.6–3.7σ" is a composite of two lower bounds** (Table II: 2.6–3.1 and 3.7–4.4). Write "2.6–4.4σ depending on channel and projection" or name the channel. (Confirms Gemini E2 / Grok J1.)

**m2 — "isoceles" → "isosceles"** (abstract, §I, §III ×2, Table I caption; also in the scripts, but those are not refereed).

**m3 — "(§ 2311.13082, abstract)" (p. 3)** — should read "arXiv:2311.13082, abstract".

**m4 — DESI DR1 row**: σ_fNL is "–", the paper is not cited, and "≲0.2σ" understates the A3 brief's own 0.24σ. Fill σ≈9, cite Chaussidon et al. 2024 (arXiv:2411.17623), print 0.24σ.

**m5 — "This supersedes an earlier, narrower statement…" (§IV)** is drafting/version-history prose; delete. Same for "not an artifact of this one" tone at end of §III.

**m6 — "The μ² term comes entirely from the two vertices in which the long mode enters through ∂χ̃"** — Table I shows μ² in the field-redefinition row (−15/16) and ζ′∂ζ·∂χ̃ (+15/8), while ζ(∂i∂jχ̃)² — which also contains χ̃ — has none. Say "the non-local field-redefinition piece and the ζ′∂ζ·∂χ̃ vertex" explicitly.

**m7 — Attribution of Cai's factor 2 to "their amplitude-normalization step" (abstract, §III, Summary) is a slightly stronger localisation than the evidence supports.** What is established (and I confirm) is: printed polynomial = from-scratch vertex sum; quoted amplitudes = 2× that polynomial's limits, uniformly. Where in Eqs. 38–40 the 2 entered is inferred, not observed. Phrase as "between their printed shape function and their quoted amplitudes" and drop "normalization step", or say "presumably in".

**m8 — δK → εζ̇ sign/convention (§III).** With K^i_j = Hδ^i_j − ∂_i∂_jψ/a² and ψ = −ζ/H + a²ε∂⁻²ζ̇, the k→0 trace is −εζ̇ in Fourier space; state the convention or write |δK|. The shear magnitude and "same order as the trace" statement are correct.

**m9 — "Li et al. inherit Cai's correct polynomial and are therefore not an independent check"** — Li et al. redid the in-in for general c_s and λ/Σ and recover Cai at c_s=1; "same technique, same group, recovers the same polynomial" is fairer than "inherit". Their c_s=1 amplitudes (−35/16 etc.) are the correct ones; the Letter should say plainly that Li et al. already print the corrected number.

**m10 — Table I caption**: define f^sq(μ) (it is (10/3)𝒜/Σk³ at fixed μ, leading order in k₁/k) and note the μ=0 column equals the isoceles limit.

**m11 — Title "The exact local non-Gaussianity"** — since the Letter's own result is that the squeezed limit is direction-dependent, "exact local" is a mild overstatement; "The squeezed-limit non-Gaussianity of a matter-dominated contraction" would match the content.

**m12 — Version stamp "v2L.0.1" in the preprint slot and the dated author block** are house style; harmless for arXiv, remove for journal submission.

**m13 — Ref [9] title casing** ("sphere x", "f_nl" lowercase) and refs [13]–[15] "Track a2/a3", "Adjudication:" project tags — clean up.

---

## C. Cross-check against the Grok and Gemini raws (read after §B was drafted)

| Finding | My verdict | Evidence |
|---|---|---|
| Grok E1/E4 (abstract asserts an observable) | **Refute.** Abstract explicitly bounds transmission and says the bounce cubic term is not computed; title scopes to the contraction. | abstract lines 19–25 of tex |
| Grok E2 ("exact" overstated) | **Partly confirm** as my m11/M3 (the number is exact; "local" is what is imprecise). | A.4 |
| Grok E3/N1 (version tag, date) | House style; **minor** (m12), not essential. | — |
| Grok M1 (no per-vertex integrands) | **Refute as MAJOR**: per-vertex table is given and the committed script reproduces it; but pin to a DOI (my M5). | A.1 |
| Grok M2/M4 (15/16 not derivable from Letter) | **Confirm in spirit**, resolved more cheaply by my M2: it follows from published Eq. (4.19). | A.4 |
| Grok M3 (σ separations lack method) | **Confirm** — my M3. | A.5 |
| Grok N2 ("placeholder arXiv IDs that post-date the manuscript") | **Refute.** 2311.13082, 2409.18983, 2504.11641, 1712.08148 are real; only [13]–[15] are non-arXiv repo links (my M5). | arXiv sources fetched |
| Grok J1 (2.6–3.7 composite) | **Confirm** — my m1. | Table II |
| Grok A1 (0.16σ implies σ≈13.7) | **Refute the arithmetic** (0.16σ is the tension of −35/16 with the DESI central value, not the separation), **confirm the defect** (σ_fNL not given) — my m4. | A3 brief §3.2 |
| Gemini E1 ((5ε−7)·5/8 contradiction) | **Confirm** — my M1. Exact. | tex + script log |
| Gemini E2 (abstract 2.6–3.7) | **Confirm** — m1. | — |
| Gemini E3 (mutable blob/main links) | **Confirm** — M5. | refs [13]–[15] |
| Gemini E4 (§IV imported from GitHub) | **Confirm** — M5 (but §IV's honesty is a strength; keep the caveat, add the derivation or move). | — |
| Gemini M1 (2.6 vs 3.13 unexplained) | **Confirm and locate the cause**: r=0.84 shape projection in the A3 brief, absent from the Letter — my M3. | A3 §3.1 |
| Gemini M2 (ζ_ρ = 2ζ_c underived) | **Confirm** — M5; value itself is correct (script rows, all ε). | script log lines 123–124 |
| Gemini M3 ("supersedes" prose) | **Confirm** — m5. | — |
| Gemini M4 (1.64× vs 0.409/0.165=2.48) | **Refute the error, confirm the ambiguity**: 1.64 = 0.409/0.250 on the LQC background (two MS-variable schemes) as the parenthesis says; the full range spread is 2.48×. Rephrase to give both. | A2 brief lines 121–125 |
| Gemini N1–N3 | **Confirm** — m3, m2, m13. | — |

Neither reviewer caught M2 (μ² is contained in the published polynomial) or M4 (two incorrect bibliography entries); both are independently verified here.

---

## D. Verdict

**MAJOR REVISIONS.**

The physics is right: I independently reproduce −35/16 (three routes: own in-in for two vertices, Cai's printed polynomial, Li's printed polynomial), the per-vertex table, the uniform factor 2 relative to Cai's quoted amplitudes, and the (15/16)μ² coefficient. The δN cross-check is correctly described as a different variable and its values are reproduced by the committed script. The transmission section is honest.

What blocks acceptance is presentation and framing, not correctness: a self-contradicting formula (M1), a novelty claim the published shape function already contains (M2), a forecast that never says which amplitude a survey measures after the Letter itself shows the squeezed limit is not one number (M3), two bibliography entries that do not exist as cited (M4), and load-bearing statements resting on mutable repository links (M5). All five are addressable in one revision without new computation; after that the Letter is a clean, citable correction of the matter-bounce f_NL record and I would expect to recommend acceptance.

Counts: **5 MAJOR, 13 MINOR.**
