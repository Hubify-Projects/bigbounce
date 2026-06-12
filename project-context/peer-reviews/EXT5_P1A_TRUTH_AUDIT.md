# EXT5 P1A — External Truth-Audit (Round EXT5, in-thread delta)

**Paper**: `arxiv/paper1a_ech_nogo.tex` · v1A.0.63 (28 pp., compiled PDF dated June 11, 2026 PDT)
**Reports audited**:
- `EXT5_P1A_ChatGPT.md` — GPT Pro Extended — **MAJOR REVISIONS** (F63-B1 Route 1 NJL regression; F63-M1 Ξ dimensional typo; F63-M2 PTA companion miscite; F63-M3 README/version pin)
- `EXT5_P1A_Grok.md` — Grok Heavy — **ACCEPT** (0 fresh blockers/majors; 4 minors)
- `EXT5_P1A_Gemini.md` — Gemini Thinking — **MINOR REVISIONS** (1 major: anisotropic stress bookkeeping; 1 minor: chiral washout literalism)

**Audit date**: 2026-06-12 PT
**Protocol**: feedback_peer_review_truth_audit_protocol (verify against `.tex`/compiled PDF/artifacts BEFORE verdict; extraction-artifact claims checked against SOURCE; correction-note/journal-policy = HOUSTON-DECISION; pattern-051 self-closure regression check, pattern-052 re-raise auto-rule)

**Carried-forward rulings** (NOT re-litigated):
- EXT4 FALSIFIED: F2 (Eq.15 inversion), F8 (Sec X.B step 5), F10 (PACS), F11 (Pop\l{}awski diacritics), K1 (3-5σ stray), K2 ("Falsification Criteria"), Ge2 (Table IV column), Ge3 (Sec IX L_r/M).
- EXT4 HOUSTON-DECISION: K5 (in-prep arXiv IDs at upload).
- R34conf FALSIFIED/STALE: A4 (Eq.14 coefficient), A21/A29 (June 2026 = current), A24 (EXT4-F1 re-raise), A25 (Eq.15 arithmetic), A26 (arXiv 25xx valid).
- R34conf VERIFIED & closed in v1A.0.63: A1 (NJL unit error, replaced by parity-even closure narrative), A3 (4 version-history body sites), A12 (Fig.3 Ξ value added to caption), A13 (Bianchi metric-compatible qualifier), A17 (Saadeh Bianchi-IX scope).

---

## EXT5-closure regression check (pattern-051 — self-audit of R34conf closures)

**Houston's priority directive**: judge our own R34conf closures honestly. R34conf-A1 closure
replaced the wrong "330 cm⁻³ ≈ 2.5×10⁻¹² eV³ → 10⁻⁶⁹ρ_Λ" chain with parity-even `<J⁵>≈0`
language plus a "naive estimate" parenthetical. R34conf-A12 added Ξ value and baseline
cosmology to Fig. 3 caption.

**ChatGPT's priority claims are BOTH VERIFIED**: the R34conf closure wave introduced TWO new
genuine errors in the replacement text. Independent recomputation below.

---

## Findings table — all EXT5 findings (fresh items only)

EXT4 + R34conf rulings auto-disposed per pattern-052. Items textually identical to prior
FALSIFIED rulings auto-falsified.

| # | Reviewer | Label | Sev | Finding | Verdict | tex Evidence + Recomputation |
|---|----------|-------|-----|---------|---------|------------------------------|
| **E1** | ChatGPT | F63-B1 | BLOCKER | Route 1 NJL "naive estimate" replacement (Sec IV A) gives ρ_NJL ∼ O(1) eV⁴ from n_ψ ∼ 10² cm⁻³ — off by ~80 orders, and ⟨J⁵⟩=0 alone does not imply ⟨J⁵J⁵⟩=0 | **VERIFIED — pattern-051 self-closure regression; R34conf-A1 fix introduced new arithmetic error** | tex L1335-1346 reads "n_ψ ∼ O(10²) cm⁻³ gives ρ_NJL ∼ O(1) eV⁴ ... far above ρ_Λ ∼ (10⁻³ eV)⁴." **Recomputation**: ℏc = 1.973×10⁻⁵ eV·cm → 1 cm⁻³ = (1.973×10⁻⁵ eV)³ = 7.66×10⁻¹⁵ eV³. n_ψ = 10² cm⁻³ → n_ψ ≈ 7.66×10⁻¹³ eV³. n_ψ² = 5.87×10⁻²⁵ eV⁶. M_Pl (unreduced, per tex L982-983) = 1.22×10²⁸ eV → M_Pl² = 1.49×10⁵⁶ eV². n_ψ²/M_Pl² ≈ 3.9×10⁻⁸¹ eV⁴. Compared to ρ_Λ ≈ (10⁻³ eV)⁴ = 10⁻¹² eV⁴: ρ_NJL/ρ_Λ ≈ 4×10⁻⁶⁹ — that is ~69 orders **BELOW** ρ_Λ, not "far above". The previous v1A.0.61-style 4×10⁻⁸⁰ eV⁴ ∼ 10⁻⁶⁹ ρ_Λ was the correct OOM. The current paper text has the inequality literally inverted. Second-leg claim about ⟨J⁵⟩=0 also correct: vanishing mean axial current does not imply vanishing variance ⟨J⁵J⁵⟩ for a four-fermion contact operator; a coherent-vs-incoherent distinction is needed. **VERIFIED.** Both legs of F63-B1 stand. |
| **E2** | ChatGPT | F63-M1 | MAJOR | Fig. 3 caption: "Ξ = ρ_Λ/M_Pl² ≈ 10⁻¹²³" is dimensionally wrong; correct dimensionless ratio is ρ_Λ/M_Pl⁴ | **VERIFIED — pattern-051 self-closure regression; R34conf-A12 fix introduced dimensional typo** | tex L961-962 (Fig. 3 caption): "Ξ set to reproduce ρ_Λ (i.e. Ξ = ρ_Λ/M_Pl² ≈ 10⁻¹²³)". Body L976-981 correctly defines: "Λ_eff carries curvature units ([mass]²)... ρ_Λ = L_eff·M_Pl² = Ξ·M_Pl⁴, so Ξ is the dimensionless ratio ρ_Λ/M_Pl⁴". **Recomputation**: ρ_Λ has dim mass⁴; M_Pl² has dim mass²; ρ_Λ/M_Pl² has dim mass² — NOT dimensionless. The body's ρ_Λ/M_Pl⁴ is dimensionless and ≈ 10⁻¹²³ (with M_Pl ≈ 10²⁷ eV and ρ_Λ ≈ 10⁻¹² eV⁴ → ratio ≈ 10⁻¹²³ ✓). The caption typo conflicts with the body's own derivation. **VERIFIED — one-character fix: change `M_Pl^2` → `M_Pl^4` in caption.** |
| **E3** | ChatGPT | F63-M2 | MAJOR | Sec X G attributes γ_PTA = 2.567±0.382 (NANOGrav 15-yr real-KDE GPU MCMC) to companion Paper III [46], but Paper III is described elsewhere as "multi-survey anomaly catalog" | **PARTIAL — citation precision item; companion role description inconsistent across paper** | Concrete cite/role mismatch. The PTA real-KDE analysis is in Paper III (per project SSOT — P3 anomaly engine includes a PTA real-KDE component in the multi-survey catalog), so the reference may be technically correct, but the description "multi-survey anomaly catalog" omits the PTA component. **Fix**: one-sentence amendment to Paper III description in the references / forward paragraph to identify the PTA real-KDE component explicitly. Not a physics error. PARTIAL — single-sentence clarification before submission. |
| **E4** | ChatGPT | F63-M3 | MAJOR | Public README still labels paper v1A.0.61 / bundle v1A.0.59 while manuscript is v1A.0.63; Zenodo DOI still pending | **VERIFIED — submission-prep pinning item; HD-4 / HD-11 standing ruling applies but specific README staleness is real** | `reproducibility/README.md` L5-6: "Paper version: v1A.0.61 (2026-06-11), Bundle version: v1A.0.59-bundle" while `arxiv/paper1a_ech_nogo.tex` is v1A.0.63. Per HD-4/HD-11 standing rulings, Zenodo tag at submission is HOUSTON-DECISION. But the README version label staleness is a real one-line fix (independent of DOI). **Fix**: update README v1A.0.61 → v1A.0.63 and bundle v1A.0.59 → v1A.0.63 (or current bundle stamp). DOI pin remains HD. PARTIAL → action: update README pin. |
| **E5** | ChatGPT | F63-Mn1 | MINOR | Fig. 3 legend still reads "Spin-Torsion" while caption now identifies the orange curve as the Ξ-fit ECH-DE ansatz | **VERIFIED — figure-label polish; survives R34conf-A12 closure** | Figure regeneration task. Legend label "Spin-Torsion" → "ECH-DE ansatz" or "Ξ-fit ECH ansatz". Low-priority cosmetic. |
| **E6** | ChatGPT | F63-Mn2 | MINOR | Fig. 1 "SPHEREx, mechanism-indep." label vs body "ECH-independent class test" | **STALE — EXT4 F5 ruled OPINION (PNG-embedded label, low priority)** | Auto-disposed. |
| **E7** | ChatGPT | F63-Mn3 | MINOR | Fig. 4 "parameter-independent" / "unique surviving minimal-ECH channel" overstated | **STALE — EXT4 F6 ruled OPINION** | Auto-disposed. |
| **E8** | ChatGPT | F63-Mn4 | MINOR | Fig. 6 "decisive (≳5σ)" vs same caption "2.6-5σ" | **STALE — EXT4 F7 ruled OPINION (different null hypotheses)** | Auto-disposed. |
| **E9** | ChatGPT | F63-Mn5 | MINOR | PACS — replace with journal keywords | **FALSIFIED — pattern-052, 5th re-raise** | EXT1 F18, EXT2 F20, EXT3 C9 (OPINION), EXT4 F10 (FALSIFIED). HD-3 standing journal-target ruling. Auto-falsified. |
| **E10** | ChatGPT | F63-Mn6 | MINOR | "Pop lawski" / "Domaga la" diacritics broken | **FALSIFIED — pattern-052, 5th re-raise** | EXT1 F26, EXT2 F23, EXT3 C10, EXT4 F11 all FALSIFIED. Source uses `\l{}`. Extraction artifact. Auto-falsified. |
| **G1** | Grok | TOC Falsification Criteria | MINOR | "Falsification Criteria" still in ToC vs body "Falsifiability Criteria" | **FALSIFIED — pattern-052, 3rd re-raise of EXT3 K3 / EXT4 K2 FALSIFIED** | tex L1707 `\section{Falsifiability Criteria}`. Extraction artifact in PDF ToC harvest. Auto-falsified. |
| **G2** | Grok | Sec IX repetition | MINOR | "channel-level not operator-level" disclaimer repeated | **OPINION — editorial preference** | Style; the redundancy is intentional per pattern-049 (scope-language at every use site). Not a factual error. |
| **G3** | Grok | Table I footnote b 3-5σ | MINOR | Stray "3-5σ" survives Table I footnote | **FALSIFIED — pattern-052, 3rd re-raise** | EXT3 K2, EXT4 K1: tex grep returns zero `3--5σ` body occurrences. Extraction artifact. Auto-falsified. |
| **G4** | Grok | Eq.(4) coefficient `-3πG/2 N×…` | MINOR | "N" instead of κ in Eq. (4) prefactor | **FALSIFIED — PDF rendering artifact; source is correct** | Grok itself notes "context and prior versions confirm this is a rendering artifact for κ ... already correct in the source .tex". Auto-falsified. |
| **Ge1** | Gemini | Major1 anisotropic stress | MAJOR | Eq. (10) treats Λ_eff = Ξ·M_Pl² + c_ω·ω² as isotropic, but cosmic vorticity dynamically sources anisotropic shear / Bianchi-type directional expansion differentials | **OPINION — already a Saadeh-style bookkeeping bound** | tex L975-992 already states the c_ω·ω² entry is "a phenomenological bookkeeping bound" with dim'less c_ω = O(1), "not a derived isotropic vacuum term", and notes "in rotating (Bianchi-type) cosmologies vorticity sources anisotropic stress rather than an isotropic Λ, and the entry is retained solely to demonstrate negligibility." Gemini's requested clarifying sentence is a re-statement of what's already there. OPINION — editorial preference, not a physics error. |
| **Ge2** | Gemini | Minor1 chiral washout literalism | MINOR | "⟨J^μ_5⟩=0" exactly over-erases primordial η_B ~ 10⁻¹⁰ asymmetry | **OPINION — already qualified** | tex L1340-1346 says "⟨J^5⟩ ≈ 0 in an unpolarized thermal bath" — already uses ≈, not =. Gemini's suggested "macroscopically" qualifier is a polish. Note: this is the same sentence implicated in ChatGPT E1's second leg (the variance argument), but the variance issue is a physics error while Gemini's η_B point is a literalism polish. Not in tension with E1. OPINION. |

---

## Per-reviewer verdict summary

| Reviewer | Claimed verdict | Fresh genuine findings (after audit) |
|----------|-----------------|--------------------------------------|
| ChatGPT | MAJOR REVISIONS | **E1 VERIFIED (NJL regression — BLOCKER), E2 VERIFIED (Ξ dimensional typo — MAJOR), E3 PARTIAL (Paper III description), E4 VERIFIED (README pin — submission-prep)**; E5 minor; E6-E10 STALE/FALSIFIED. **Justified MAJOR REVISIONS — two genuine R34conf-closure regressions caught.** |
| Grok | ACCEPT | 0 verified items; 4 minors all FALSIFIED (extraction artifacts) or OPINION. Grok missed E1 (severe arithmetic regression) and E2 (dimensional typo). **ACCEPT verdict not supported by the paper state — Grok over-trusted the R34conf changelog instead of recomputing.** |
| Gemini | MINOR REVISIONS | 0 verified items; Ge1 + Ge2 both OPINION (already disclosed at the relevant body sites). Gemini also missed E1 and E2. **MINOR REVISIONS verdict not supported — same blind spot as Grok.** |

---

## Counts (EXT5 P1A)

| Category | Count | Items |
|----------|-------|-------|
| VERIFIED (fix required) | **3** | E1 (NJL regression — BLOCKER), E2 (Ξ dimensional typo — MAJOR), E4 (README v1A version pin — submission-prep MAJOR) |
| PARTIAL (single-sentence fix) | **2** | E3 (Paper III description), E5 (Fig. 3 legend label) |
| OPINION / HOUSTON-DECISION | **2** | Ge1 (anisotropic stress already disclosed), Ge2 (chiral washout literalism) |
| STALE (EXT4/R34conf re-raise) | **3** | E6, E7, E8 |
| FALSIFIED (source disproves / pattern-052 re-raise) | **5** | E9 (PACS), E10 (diacritics), G1 (ToC), G3 (Table I), G4 (Eq.4 prefactor) |
| OPINION (editorial) | **1** | G2 (Sec IX repetition) |

**Genuinely new, VERIFIED substantive findings: 3** (E1 is the most important — pattern-051 self-closure regression introducing a wrong-direction OOM error and a coherent/incoherent distinction the parity-even-only argument misses; E2 is a one-character dimensional-typo fix; E4 is a one-line README pin).

**Pattern-051 self-closure regression count: 2** (E1 from R34conf-A1 wave; E2 from R34conf-A12 wave). Both replacements introduced new errors. R34conf had limited time to re-verify the replacement text. This is exactly the failure mode pattern-051 was added to detect; it caught both.

---

## CLOSURE PLAN (P1A → v1A.0.64)

| # | Fix | tex location | Diff size | Owner |
|---|-----|--------------|-----------|-------|
| C1 | **E1 BLOCKER — Route 1 NJL replacement text**: restore correct order-of-magnitude estimate (n_ψ ∼ 10² cm⁻³ → n_ψ²/M_Pl² ∼ 4×10⁻⁸¹ eV⁴ ∼ 4×10⁻⁶⁹ ρ_Λ, **below** ρ_Λ) AND split the closure into two parts: (i) late-time mean-field amplitude is negligible at any baryon/electron density (correct OOM stated), (ii) any incoherent thermal variance ⟨J⁵J⁵⟩ ≠ 0 is not a coherent w=−1 vacuum component (do NOT claim ⟨J⁵⟩=0 alone makes the four-fermion operator vanish). | L1335-1346 | ~6 lines | Houston |
| C2 | **E2 MAJOR — Fig. 3 caption dimensional typo**: replace `\Xi = \rho_\Lambda/\MPl^2 \approx 10^{-123}` with `\Xi = \rho_\Lambda/\MPl^4 = \Lambda_{\rm eff}/\MPl^2 \approx 10^{-123}` | L961-962 | 1 char + ~10 char explanatory clause | Houston |
| C3 | **E3 PARTIAL — Paper III description**: update the references entry and Sec X G forward-paragraph description to identify the PTA real-KDE NANOGrav component of the multi-survey anomaly catalog explicitly. | refs [46], Sec X G fwd paragraph | 1 sentence | Houston |
| C4 | **E4 MAJOR — README version pin**: update `reproducibility/README.md` L5-6 paper-version from `v1A.0.61 (2026-06-11)` → `v1A.0.63 (2026-06-12)` and bundle version to current bundle stamp. Zenodo DOI remains HD-pending. | reproducibility/README.md L5-6, L133 BibTeX block | 3 lines | Houston |
| C5 | **E5 MINOR — Fig. 3 legend**: regenerate `figures/figure5_rotation_expansion.png` with legend label "Spin-Torsion" → "ECH-DE (Ξ-fit) ansatz" | png regen | figure update | Houston |

**Acceptance criterion for closure of EXT5**: C1+C2+C3+C4 committed; pdflatex 4-pass clean (0 undef refs); `/latex-audit` pass; `/paper-pre-review-check` confirms zero open EXT5-VERIFIED items; tex stamp bumped to v1A.0.64.

**Pattern-051 / pattern-052 catalog updates required**:
- Pattern-051 (self-closure-regression) — confirmed twice in same round (R34conf-A1 → E1; R34conf-A12 → E2). Update catalog instance count and add as exemplar: "replacement text introduces NEW arithmetic / dimensional error after closure of original error." Mandatory recomputation of any replaced numerical claim before commit.
- Add ChatGPT-strong / Grok-weak / Gemini-weak signature for arithmetic-recomputation tasks: only ChatGPT recomputed both E1 and E2. Future R-rounds should weight ChatGPT recomputation findings higher when a closure wave just touched the relevant text.
