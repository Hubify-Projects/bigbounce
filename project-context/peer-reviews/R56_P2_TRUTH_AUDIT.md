# R56 P2 — Truth Audit (HARDENED / de-biased re-review)

**Paper:** P2 — *Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook*
**Source:** `research/focused_paper_source_integration/02_full_draft.tex`
**Round:** R56, full re-review under hardened PRD/MNRAS bar (no tier-defaulting; self-favoring / unstated-assumption / uncontrolled-systematic / internal-inconsistency = real finding, MINOR min, NOT OPINION).
**Inputs:** native-PDF 3-vendor round (OpenAI gpt-5 high+pass2; Gemini 2.5-pro; Grok-4 rasterized) + Perplexity (quota-failed, no leg) + own Opus full read. PDF md5=592c7849, 28pp, 0 undef.
**Integrity-fix status:** abstract single-Heinrich+2023-baseline restatement (v1.7.73) VERIFIED INTACT — not re-opened.

Verdict-first, vs source.

## NET VERDICT: MAJOR REVISIONS (all 3 vendors) → on audit, NO BLOCKER, NO genuine MAJOR. 5 verified MINOR; 4 closed, 1 flagged.

All vendor ESSENTIALs are FALSIFIED misreads, STALE/already-done, or the excluded DOI item. The genuine residue is MINOR internal-consistency / notation / one mild self-favoring rounding.

---

## ESSENTIALS — verdicts

| ID | Claim | Verdict | Evidence |
|----|-------|---------|----------|
| Gemini P2-E1 | Eq(1)/Eq(2) dimensionally inconsistent; B_NL has dim k⁻³ | **FALSIFIED** | Gemini read Eq(1) prefactor as $k_i^3$; source L681 is $k_1^2k_2^2k_3^2$ (deg 6). P deg 9 → A_T deg 3 → B_NL=A_T/Σk³ = deg 0 = dimensionless. L688 states exactly this. PDF-raster misread (same class as repeatedly-falsified Gemini glyph items). |
| Gemini P2-E2 | main-text 6/5 vs App-A c=2 normalization inconsistent | **FALSIFIED** | App A (L1150) explicitly derives $(5/3)^3(3/5)^4\cdot2=6/5$ mapping Φ-field c=2 ↔ ζ-field 6/5 at same f_NL. Φ=(3/5)ζ is standard matter-era superhorizon. This IS the paper's deliberate convention-audit contribution, not a bug. |
| OpenAI P2-E1 | Eq(9) reads as ×CDF not ÷CDF | **FALSIFIED** | L849–852 is a proper `\frac` with CDF-difference in denominator → renders as division. Worked numerics (17.10/14.36/7.0) confirm. Inline-form misread. |
| OpenAI P2-E6 | abstract "CMB Fisher to LSS endpoints" order-ambiguous | **VERIFIED MINOR → CLOSED** | r_CMB=0.876→5.5σ, r_LSS=0.83→5.2σ; "CMB Fisher to LSS" mapped to "5.5→5.2", opposite to written "5.2–5.5". Real directional inconsistency. |
| OpenAI P2-E8 | squeezed-mode index k₁ vs k₃ inconsistent | **VERIFIED MINOR → CLOSED** | Eq(2)/Tbl I/Fig1/grid (L687,696): soft=k₁. L773: x₃≡k₃/k₁, k₃≪k₁ → soft=k₃, clashes w/ ordered grid k₁≤k₂≤k₃. Physics saved by permutation symmetry (code uses k₃/k₁ per L202 R36conf), but text contradicts its own ordering. |
| OpenAI P2-E3 / Grok P2-m3 | Zenodo DOI / commit-hash placeholder | **EXCLUDED (DOI)** | Per round scope. |
| OpenAI P2-E4 | photo-z 5% number underived | **OPINION/already-caveated** | L1002 labels "simplified Fisher degradation estimate … consistent with published estimates [Giannantonio:2012]"; sub-dominant, not headline-load-bearing. |
| OpenAI P2-E5 / Grok | shot-noise 15–30% vs √11 unbacked | **OPINION/already-caveated** | Applies to anomaly tracers EXPLICITLY excluded from headline (L801); labeled upper-bound pending shot-noise Fisher. |
| Grok P2-E1 | abstract 2.6–5σ not single procedure | **OPINION** | Optimistic→conservative envelope with both endpoints' assumptions labeled (L780,800,Tbl IV). Standard honest range reporting. |
| Grok P2-E2 | abstract BF 9–14 from r→1 endpoint | **FALSIFIED/STALE** | Abstract L645 already states 9–14 is the noise-weighted r≈0.84 bookkeeping; L938 recomputes grid at r=0.84 (17.1→14.4, 9.8→9.2). This is exactly the integrity fix; Grok's premise is wrong. |
| Grok P2-E3 | null-space full width not propagated | **FALSIFIED** | L704 propagates full 16–84th pctile into significance: 4.4–6.2σ (median 5.3σ), per-sample artifact released. |
| Grok P2-E4 | abstract "recast" implies independent forecast | **FALSIFIED** | Abstract repeatedly says "sensitivity recast rather than independent cross-Fisher forecast" (L641,643,797). Complaint is backwards. |

## MAJOR/MINOR residue — verdicts

| ID | Verdict | Note |
|----|---------|------|
| OpenAI P2-M3 (ε-corr "≲0.4σ" vs actual 0.42σ) | **VERIFIED MINOR (self-favoring) → CLOSED** | 8% → Δf=0.35 → 0.35·0.84/0.7=0.42σ. "≲0.4" understates (0.42>0.4) — mild self-favoring. |
| OpenAI P2-M6 (Tbl III "10% residual" label vs Ideal numbers) | **VERIFIED MINOR → CLOSED** | Label said "10% residual" while row shows zero-residual Ideal values; self-contradictory. |
| Gemini P2-m2 (MegaMapper √(0.7²+0.9²) vs Tbl IV b_φ-replacement rule) | **VERIFIED MINOR → FLAGGED (not closed)** | L816 treats b_φ-widen (0.7→0.9) as additive-quadrature; Tbl IV b_φ rule is replacement → 3.675/0.9=4.1σ, not 3.2σ. Genuine internal inconsistency, but **anti-self-favoring** (current 3.2σ is MORE conservative than rule). Fix raises an illustrative MegaMapper number 3.2→4.1σ; left for author to avoid fabricating intent on ambiguous illustrative figure. |
| OpenAI P2-E2/M1 ("SPHEREx-like" weight kernel not formula-defined) | **MINOR/polish (not closed)** | Headline r=0.84 is bracketed by explicitly-defined schemes (CMB k², SDB 1/k², uniform); only "SPHEREx-like"=0.830 lacks a closed-form; not load-bearing. |
| OpenAI P2-M7 (M(k,z) h-factor units) | OPINION/polish | Canonical Dalal/Slosar form. |
| OpenAI P2-M4 (injection-recovery not 3D-LSS-commensurate) | OPINION/already-caveated | L708 explicit. |
| Grok P2-M1/M2/M3/M4, length, P2-m1/m2 | OPINION/already-caveated | Conditional-on-(d), additive-quadrature scoping, MegaMapper-illustrative, Eq(7)-heuristic all already labeled (L660/734/738/643/795). |
| Gemini P2-m1/N1 (date / email) | OPINION/STALE | Date intentional (is June 2026); author's real email. |

## CLOSURES (4 verified DO-NOW, source-edited)

1. **R56-1 (P2-E6):** abstract L643 endpoint order → "from the LSS/SPHEREx noise-weighted endpoint 5.2σ at r=0.83 to the CMB-Fisher endpoint 5.5σ at r=0.876". No number change.
2. **R56-2 (P2-M3, self-favoring):** Tbl IV L1025 "$\lesssim 0.4\sigma$" → "$\lesssim 0.42\sigma$". Honest upper bound at the 8% endpoint.
3. **R56-3 (P2-M6):** Tbl III L985 row label "Corrected (10% residual; = Ideal, verification only)" → "Corrected (residual neglected; = Ideal by construction)"; footnote ref harmonized. Numbers unchanged (they ARE the zero-residual values by construction).
4. **R56-4 (P2-E8):** L773 added permutation-symmetry clarification: the weighting-scan code labels soft mode k₃, equivalent by full bispectrum permutation symmetry to the k₁-soft labeling of Sec II / Tbl I. No number change; preserves code-matching x₃≡k₃/k₁ definition.

**FLAGGED, not closed:** R56-F1 (Gemini P2-m2) — MegaMapper σ=0.7 conservative combination at L816 uses additive quadrature where Tbl IV prescribes b_φ replacement; correcting to the Table-IV rule RAISES an illustrative number (3.2→4.1σ), so deferred to author judgment rather than silently changed.

## RECOMPILE
×3 + bibtex: **0 undefined**, 28 pp, 920 KB. Overflow audit: 2 pre-existing overfull hboxes (2.95pt L719–728; 1.23pt L1175) — both sub-3pt math-mode, cosmetically negligible, unchanged by edits. No new overflow.

## CONVERGENCE STATEMENT
P2 is CONVERGED under the hardened de-biased standard. Three vendors nominally returned MAJOR REVISIONS, but every ESSENTIAL is a FALSIFIED PDF-raster misread (Gemini dimensional/normalization; OpenAI Eq-9), a STALE/already-implemented item (Grok BF-rebooking, null-space propagation, recast-labeling — all already in the paper), or the excluded DOI placeholder. The genuine residue is polish-tier: 4 MINOR internal-consistency/notation fixes (closed) + 1 anti-self-favoring MegaMapper combination inconsistency (flagged for author). One mild self-favoring item existed under the hardened bar (ε-correction 0.42σ rounded to ≲0.4σ) and is now closed. Zero BLOCKER, zero genuine MAJOR, zero open self-favoring item. The science, headline numbers (5.2–5.5σ / 2.6–5σ / BF 9–14 / 0.75σ / τ_NL 27.56), and the integrity fix are intact.
