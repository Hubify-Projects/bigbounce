# R27conf P1A — TRUTH AUDIT (v1A.0.55 → v1A.0.56, closures applied 2026-06-10)

Auditor: in-session Claude. Ground truth: `arxiv/paper1a_ech_nogo.tex`, `.bbl`, R26conf truth-audit precedents, verified Eq.(3) footnote chain (S²=−3/8(J⁵)², −3κ/16 — verified term-by-term by INSESSION leg).
Auto-falsify rules: future-date (June 2026 project dating; arXiv 25xx/26xx valid) → FALSIFIED; citation-nonexistence → `.bbl` checked; correction-note/length/REJECT recommendation → HOUSTON-DECISION/OPINION.

## In-session leg (Claude_brutal_INSESSION, M=4 pre-flagged NOT-closed → closed this wave)

| ID | Claim | Verdict | Disposition |
|---|---|---|---|
| M1 (substitution step not displayed) | presentation (verified algebra) | **VERIFIED** | **CLOSED**: footnote now displays ¼T·T = κ²/4 S·S on-shell + Hehl–Datta net +κ/2 S·S → −3κ/16(J⁵)², cross-ref Eq.(13). Coefficient forced by the two verified endpoints — no new derivation claimed |
| M2 (ε contraction signature pin) | presentation | **VERIFIED** | **CLOSED**: "mostly-plus $g=\mathrm{diag}(-,+,+,+)$, $\epsilon^{0123}=+1$" pinned at first use |
| M3 (Holst/fermion sentence asserted) | presentation | **VERIFIED** | **CLOSED**: demonstrative dropped; assertion grounded on Freidel et al. citation + forward pointer to the γ-dependence in Eq.(4) |
| M4 (Barrier-14 → §X no subsection pointer) | presentation | **VERIFIED** | **CLOSED**: labels added to §X.B (scalar proof) + §X.D (Holst verification); Barrier 14 now points to both |
| m1 (footnote-c tucked away) | presentation | **VERIFIED** | **CLOSED**: Table I row "Mechanism-independence?" added |
| m2 (half-weight mapping dictionary) | presentation | **VERIFIED** | **CLOSED**: full-weight T=2Γ absorbs the factor-2 parenthetical added (mapping verified correct by reviewer) |
| m3 (Fig.3 annotation ~6pt) | figure-regen | VERIFIED | **QUEUED** (figure regeneration, not textual) |
| N1/N2 + all-clears | — | N/A | Reviewer's own verifications (Cartan chain ✓, scope clause ✓, App C clean ✓) |

## META_REVIEW (gpt-5-pro)

| ID | Class | Verdict | Disposition |
|---|---|---|---|
| META-E1 (fa decay constant in β–ρ–m, θ vs φ) | claim-truth (derivation) | **FALSIFIED-as-stale** | App C convention block (L2480–2495, v0.55) explicitly declares $\alpha/M \equiv C_{a\gamma}\alpha_{\rm em}/(2\pi f_a)$ + $\Delta\theta=\Delta\phi/f_a$ "closing the normalization chain"; fa is absorbed into the g_aγ-basis α/M with f_a=M_Pl disclosed (Sec. IV.D footnote). Residual θ-symbol dual use = minor notation queue |
| META-E2 (Route-2 photon-bridge chain absent) | recompute (derivation) | VERIFIED-PLAUSIBLE | **QUEUED** — same family as R26conf META-M6 (already queued); paper labels Route-2 estimate heuristic |
| META-M3 (T² double-counting in Eq.(1)) | claim-truth (wording) | **VERIFIED** | **CLOSED**: "not varied independently … no double counting" clause added; consistent with footnote's stated variation procedure |
| META-M4 (Eq.(3) exact only at γ→∞) | claim-truth | PARTIAL/STALE | Footnote already derives total antisymmetry of S making the Cartan equation exact for minimal Dirac (trace parts vanish); γ-dependence enters Eq.(4) coefficient as stated. INSESSION verified chain incl. γ→∞ limit. No edit |
| META-M5 (αem in Eq.(7) ad hoc) | scope | STALE | R26conf precedent: heuristic status labeled at site ("electromagnetic estimate"); conservatism band disclosure |
| META-M6 (Shamir matched-footprint audit) | recompute | OUT-OF-SCOPE | R26conf META-m9 precedent: Paper-IV pipeline property; P1A carries matched-footprint caveat |
| META-M7 (vorticity→ρ fraction mapping) | claim-truth | STALE | L834–836 already labels c_ωω² "phenomenological placeholder … not a derived isotropic vacuum term" |
| META-m8/m9/m10 | presentation | STALE/MINOR | ⟨⟩ in Ξ, Eq.(12) caveat, γ-landscape phrasing — R26conf adjudicated heuristic-labeling family; non-blocking |

## Cross-vendor legs (Gemini / Grok / OpenAI / Perplexity)

| Group | Verdict | Disposition |
|---|---|---|
| Version-history/correction-note removal (OpenAI E2, Gemini E2, Perplexity E7) | HOUSTON-DECISION | R26conf precedent: deliberate transparency artifacts |
| Companion-paper self-containment (Grok E2/E3, OpenAI E1/E6/E8/M7, Perplexity E1/E3/E5/E6/E9/M2) | FALSIFIED/STALE | R26conf precedent: companions exist in-repo, post concurrently; `.bbl` verified (Golden2026P1b/P2) |
| Future dates / arXiv 25xx IDs (Gemini E3, Perplexity E2, M1-part) | AUTO-FALSIFIED | June 2026 project dating; arXiv:2503.14738 + 2509.13654 in `.bbl` |
| Operator dimension +1 ansatz (Gemini E1, Grok E1/M3, Perplexity E8) | STALE | Disclosed verbatim in abstract/§I/App B as ansatz-not-derivation (R3–R26 multi-round adjudication) |
| σ-mixing "not comparable" (OpenAI E3, Perplexity M4) | STALE | Sites carry "not directly comparable" qualifiers (R24conf closures); Perplexity itself concedes |
| Gemini M3/m3 (3–5σ should be 4–6σ) | FALSIFIED | 3–5σ is post-full-systematic-budget (GR-projection, b_φ, photo-z) per Table I footnote-b, not naive f_NL/σ division |
| OpenAI M10 (γ scheme range 0.020 vs 0.037) | FALSIFIED | L627–639 explicitly: spread is between counting prescriptions, "retained as an effective range only," not propagated; SU(2)–DLM = 0.037 vs quoted ~0.020 already disclosed as prescription spread |
| Grok E4 (B14 proof scope) | STALE | Scope restriction (canonical scalar, post-torsion) stated in §I, §X.A, Table II |
| Gemini M5 (Fig.1 stale PTA γ=3.20) | **VERIFIED** (figure) | **CLOSED (textual) + QUEUE**: caption now discloses the burned-in 3.20±0.42 as superseded pre-real-KDE value, points to 2.567±0.382 (Sec. XI); annotation regen queued with m3 |
| Length/REJECT/abstract-rewrite (Grok M1, summary recs) | OPINION | Editorial |
| Remaining minors/nits (typos, notation, Popławski spacing) | STALE/MINOR | Non-substantive; folded into next editorial pass |

**Substantive verified-and-closed this round: 8 textual (INSESSION M1–M4, m1, m2, META-M3, Fig.1 caption disclosure). Queued recompute/figure: META-E1, META-E2 (both prior-round queue merges), Fig.1/Fig.3 annotation regen. Zero verified number/claim-truth errors in v1A.0.55 body content.**
Recompile (v1A.0.56): pdflatex×2 + bibtex + pdflatex — 26 pp, 0 errors, 0 undefined refs, md5 `2dd38ef1f0941e1986399eaa5e2fc241`; 3 pre-existing sub-7pt equation overfulls (R26conf baseline, outside edited regions). Pages 4/6 visually verified (Table I new row renders; footnote clean).

**P1A ROUND VERDICT: CLEAN** — zero verified substantive (number/claim-truth/reproducibility) errors; 8 verified presentation findings closed same-day in v1A.0.56; recompute queue = prior-round merges + figure-annotation regen only. Final PDF md5 `96f18a36bdb84ad4919c6611f67f1034` (26 pp, 0 errors).
