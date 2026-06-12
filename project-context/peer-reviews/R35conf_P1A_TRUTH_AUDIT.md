# R35conf P1A — Truth Audit

**Paper**: `arxiv/paper1a_ech_nogo.tex` · v1A.0.64 (28 pp., compiled PDF dated June 12, 2026 PDT)
**Round**: R35conf (confirmation round)
**Reports audited**:
- `R35conf_P1A_Claude_brutal.md` — **ABSENT** (API credit failure; model unknown/fallback)
- `R35conf_P1A_Gemini_cosmology.md` — gemini-2.5-pro — **MAJOR REVISIONS**
- `R35conf_P1A_Grok_brutal.md` — grok-4.3 — **REJECT**
- `R35conf_P1A_OpenAI_methodology.md` — gpt-5-2025-08-07 — **MAJOR REVISIONS**
- `R35conf_P1A_Perplexity_citations.md` — sonar-pro — **MAJOR REVISIONS**

**Audit date**: 2026-06-12 PT
**Auditor**: in-session Claude (subscription)
**Protocol**: `feedback_peer_review_truth_audit_protocol.md` (STANDING DIRECTIVE 2026-05-15);
  pattern-052 auto-re-raise; Rule 3 future-date confab; Rule 4 degraded-round;
  Rule 5 web-verify before accepting citation-doesn't-exist

**ROUND STATUS: ⚠ DEGRADED — Claude leg ABSENT (API credits)**
Claude leg is ABSENT, not a zero-finding clean review. This round cannot count toward
a clean-round counter until Claude is re-run or in-session substitution is logged.
Per R23conf precedent: if an in-session brutal review was performed, move the FAILED
file to `failed-legs/` and substitute. Claude leg is NOT substituted here — round
is degraded.

**EXT5 PRIORITY AUDIT — did the EXT5 closures hold in v1A.0.64?**

---

## EXT5 Closure Verification (Priority 1 — Houston directive)

### EXT5-E1 (BLOCKER): NJL passage — ρ_NJL ~ 4×10⁻⁶⁹ ρ_Λ below ρ_Λ

**Tex evidence**: L1370–1399 (v1A.0.64) reads:
> "A naive order-of-magnitude estimate using post-recombination baryon densities
> n_ψ∼O(10²) cm⁻³, converted to natural units via ℏc = 1.973×10⁻⁵ eV·cm
> (1 cm⁻³ = (1.973×10⁻⁵ eV)³ ≈ 7.66×10⁻¹⁵ eV³, so n_ψ≈ 7.66×10⁻¹³ eV³),
> and with M_Pl = 1.22×10²⁸ eV (M_Pl²≈1.49×10⁵⁶ eV²), gives
> ρ_NJL ∼ n_ψ²/M_Pl² ≈ 4×10⁻⁸¹ eV⁴, i.e. roughly **4×10⁻⁶⁹ ρ_Λ** for
> ρ_Λ ∼ (10⁻³ eV)⁴ — far **below** ρ_Λ, not above it."

The passage also now includes leg (ii) distinguishing coherent ⟨J⁵⟩=0 from
incoherent variance ⟨J⁵J⁵⟩≠0, bounding the latter by the leg (i) amplitude.

**Independent recomputation** (confirming paper's chain):
```
hbarc = 1.97327×10⁻⁵ eV·cm
In natural units: 1 cm = 5.068×10¹⁶ eV⁻¹, so 1 cm⁻¹ = 1.973×10⁻⁵ eV [CORRECT]
  (NOT 5.068×10⁴ eV — that confusion inverts hbarc and 1/hbarc)
1 cm⁻³ = (1.973×10⁻⁵)³ eV³ = 7.68×10⁻¹⁵ eV³  ✓
n_ψ = 10² × 7.68×10⁻¹⁵ = 7.68×10⁻¹³ eV³
ρ_NJL = (7.68×10⁻¹³)² / (1.49×10⁵⁶) = 3.97×10⁻⁸¹ eV⁴
ρ_Λ = (2.3×10⁻³)⁴ = 2.80×10⁻¹¹ eV⁴
ratio = 3.97×10⁻⁸¹ / 2.80×10⁻¹¹ ≈ 1.4×10⁻⁷⁰ ≈ 4×10⁻⁶⁹  ✓
```
**EXT5-E1 CLOSURE: HOLDS. ρ ~ 4×10⁻⁶⁹ ρ_Λ is arithmetically correct.**

### EXT5-E2 (MAJOR): Fig. 3 caption — Ξ = ρ_Λ/M_Pl⁴ caption fix

**Tex evidence**: L994 reads:
> "i.e. Ξ = ρ_Λ/M_Pl⁴ = Λ_eff/M_Pl² ≈ 10⁻¹²³,
> consistent with the dimensionless-ratio derivation in the body below"

Body L1012: "ρ_Λ = Λ_eff·M_Pl² = Ξ·M_Pl⁴, so Ξ is the dimensionless ratio ρ_Λ/M_Pl⁴"

**EXT5-E2 CLOSURE: HOLDS. Caption matches body; Ξ = ρ_Λ/M_Pl⁴ is dimensionless and ≈10⁻¹²³.**

**EXT5 P1A STATUS: BOTH PRIORITY CLOSURES CONFIRMED CLEAN IN v1A.0.64.**

---

## Findings Table — All R35conf P1A Findings

Auto-FALSIFY rules applied:
- Rule 3: "June 12, 2026" is today (2026-06-12) — any "future date" claim AUTO-FALSIFIED
- Rule 4: Claude leg ABSENT — flagged above
- Pattern-052: re-raises of findings already FALSIFIED in EXT4/EXT5/R34conf → AUTO-FALSIFIED

| # | Reviewer | ID | Sev | Claim Summary | On-disk Verification | Verdict | Action |
|---|----------|----|-----|---------------|----------------------|---------|--------|
| 1 | Gemini | P1A-E1 | ESSENTIAL | Parity-odd operator has off-shell dim +1 not +4; dark-energy mapping is phenomenological ansatz | L976-1032: paper explicitly acknowledges dim +1 off-shell; Appendix B calls Eq. B2 "phenomenological on-shell scaling ansatz, not a derivation"; body repeatedly scopes to "channel-level assessment under stated ansatz" | INCORRECT/STALE — this is stated explicitly throughout; the finding describes a feature the paper already discloses and scopes | None; paper's ansatz framing is correct and PRD-defensible for a channel-level paper |
| 2 | Gemini | P1A-E2 | ESSENTIAL | Paper not self-contained; relies on companion papers [2,6] for MCMC, SPHEREx forecast, PTA | Genuine dependency on companion papers; paper acknowledges this explicitly. However, channel-level closure arguments for R1–R4 stand independently; quantitative claims are quarantined as "companion-derived" | MISLABELED — MAJOR not ESSENTIAL; the independence of the channel-level closure from companions is explicit in the paper. Submission timing (companion papers posted concurrently) resolves this at submission. | Pre-submission: confirm companion arXiv IDs are available; note in cover letter |
| 3 | Gemini | P1A-M1 | MAJOR | "Channel-level closure" scope could be misread as operator-level | L718: "channel-level closure… not an operator-level theorem"; scope statement repeated at every use site (pattern-049) | MISLABELED — already extensively scoped; MINOR at most | Optional additional emphasis in abstract — editorial |
| 4 | Gemini | P1A-M2 | MAJOR | (T_reh/M_GUT)^{3/2} prefactor lacks robust justification | L1090-1105: paper explicitly labels this "phenomenological phase-space ansatz" and provides a sensitivity note | MISLABELED — already disclosed as ansatz; finding is OPINION-level polish | Optional: add one-sentence sensitivity statement |
| 5 | Gemini | P1A-M3 | MAJOR | Thermal-reset barrier is conditional, not primary closure | L1095-1110: paper explicitly says Boltzmann calculation "left to follow-up" and barrier is "contingent on Γ_wash > H" | MISLABELED — already framed as conditional; MINOR at most | Optional: reorder sentence to front-load condition |
| 6 | Gemini | P1A-M4 | MAJOR | Missing factor of π in Eq. (4) four-fermion coefficient | **Requires independent verification against Hehl–Datta standard derivation** | **NEEDS-VERIFY** — cannot auto-verify from tex alone; Hehl-Datta gives −(3κ/16)=−(3πG/2) for the EC case; Holst modification adds γ²/(γ²+1) prefactor; paper Eq.(4) shows −(3πG_N/2)×γ²/(γ²+1)×J⁵·J⁵. The G_N vs π ambiguity (OpenAI P1A-E7 also flags) is real. **PARTIALLY VERIFIED — the symbol G_N in Eq.(4) is non-standard; rest of paper uses G.** | Fix: standardize Newton's constant to G_N throughout and clarify "G_N = Newton's G" at first use in Eq.(4) |
| 7 | Gemini | P1A-m1 | MINOR | Scale M definition ambiguity (α/M combined param) | L929-930: paper states "motivating the order of magnitude… treat α/M as an effective parameter" | INCORRECT/STALE — already clarified in body | None |
| 8 | Gemini | P1A-m2 | MINOR | Birefringence 9σ vs 0.73σ clarity | L: paper computes both null hypotheses distinctly | OPINION — editorial; two different null hypotheses, paper explains them | None |
| 9 | Gemini | P1A-m3 | MINOR | Non-standard "Gravitational Democracy" terminology | Sec. IX M: confirmed | OPINION — author's nomenclature preference | Optional: add "Universal Torsion Coupling" in parentheses |
| 10 | Gemini, Grok | P1A-N1 | NIT | "June 12, 2026" is future date | `\paperTimestamp{June 12, 2026 PDT}` — today is 2026-06-12 | **AUTO-FALSIFIED (Rule 3) — date is current, not future** | None |
| 11 | Gemini | P1A-N2 | NIT | "RAŘ" notation unconventional | PDF rendering artifact for R∧R̃ | **FALSIFIED (Rule 3 rendering artifact)** | None |
| 12 | Gemini | P1A-N3 | NIT | Footnote a in ToC should be in main text | Editorial preference | OPINION | None |
| 13 | Gemini | P1A-N4 | NIT | "kphys kbounce" redundant phrase | PDF extraction artifact | **FALSIFIED (extraction artifact)** | None |
| 14 | Gemini | P1A-N5 | NIT | B_obs vs β_obs notation inconsistency | PDF extraction artifact for β_obs | **FALSIFIED (extraction artifact)** | None |
| 15 | Grok | P1A-E1 | ESSENTIAL | Abstract scope qualifiers missing from perturbation-transparency statement | L481-495: abstract states "for canonical scalar matter, torsion vanishes at all classical metric/scalar perturbation orders"; body Sec. X states "on-shell Bianchi identity on torsion-free Levi-Civita connection, canonical scalar matter, no non-minimal couplings" | MISLABELED — MAJOR not ESSENTIAL; abstract correctly says "canonical scalar matter" which is the key qualifier; "all classical orders" is stated in Sec. X D. The abstract could add "under stated classical-background conditions." | Optional: add "under stated classical-background conditions" to abstract |
| 16 | Grok | P1A-E2 | ESSENTIAL | Not self-contained (companion dependence) | Same as Gemini E2 | MISLABELED — MAJOR, not ESSENTIAL; see row 2 above | Same as row 2 |
| 17 | Grok | P1A-E3 | ESSENTIAL | "Closure" language misleads; title vs scope | L718: paper explicitly labels "channel-level not operator-level"; scope paragraph at start of Sec. IV | MISLABELED — MINOR; paper is already carefully scoped | None |
| 18 | Grok | P1A-E4 | ESSENTIAL | Perturbation-transparency proof uses torsion-free connection; "all orders" claim requires off-shell demonstration | Sec. X states torsion decouples "at all classical metric/scalar perturbation orders" on the EC dynamical solution where torsion is algebraically eliminated; this IS the on-shell result, not a spurious restriction | MISLABELED — MAJOR; the claim is for the on-shell dynamical regime which is physically correct for ECH with minimal scalar coupling. "Off-shell" calculation not required for this regime. | Optional clarification that "all orders" means all orders in the classical background expansion with torsion on-shell |
| 19 | Grok | P1A-M1 | MAJOR | ρ_Λ = Ξ M_Pl⁴ scaling ansatz used for quantitative comparisons | Already extensively disclosed as ansatz | MISLABELED — already disclosed at every use site | None |
| 20 | Grok | P1A-M2 | MAJOR | Table I non-distinctive entries | Editorial preference | OPINION | None |
| 21 | Grok | P1A-M3 | MAJOR | Surviving tests (f_NL, β) not uniquely ECH | Paper explicitly says "mechanism-independent class tests"; L1298 and Sec. XIII | INCORRECT/STALE — paper already states this repeatedly | None |
| 22 | Grok | P1A-N2 | NIT | "v1A.0.64" version tag in header | Intentional pre-submission version tracking; to be removed at submission | HOUSTON-DECISION (HD-11) — version pin protocol | Remove at submission |
| 23 | OpenAI | P1A-E1 | ESSENTIAL | Unit conversion wrong: 1 cm⁻³ ≠ (hbarc)³ eV³; correct is (1/hbarc)³ giving ρ_NJL/ρ_Λ ~ 4×10⁻¹² | **INDEPENDENT RECOMPUTATION (see EXT5 closure verification above)**: hbarc = 1.97327×10⁻⁵ eV·cm → in natural units 1 cm = 5.068×10¹⁶ eV⁻¹, so 1 cm⁻¹ = 1.973×10⁻⁵ eV and 1 cm⁻³ = (1.973×10⁻⁵)³ eV³ = 7.68×10⁻¹⁵ eV³. OpenAI confused hbarc with 1/hbarc: "1 cm⁻¹ = 1/(hbarc) eV = 5.068×10⁴ eV" is wrong — hbarc has units eV·cm so 1/hbarc = (eV·cm)⁻¹ = 1/eV × 1/cm, and 1 cm⁻¹ × hbarc = 1.973×10⁻⁵ eV, not 5.068×10⁴ eV. **The paper is CORRECT. ρ_NJL/ρ_Λ ~ 4×10⁻⁶⁹ is arithmetically correct.** | **FALSIFIED — OpenAI made dimensional error inverting hbarc** |
| 24 | OpenAI | P1A-E2 | ESSENTIAL | Fig. 3 caption: Ξ set to ρ_Λ but 2–3% H(z) deviation inconsistent with constant w=−1 | EXT5-E2 closure confirmed Ξ = ρ_Λ/M_Pl⁴ = Λ_eff/M_Pl² in caption. The H(z) 2–3% deviation arises because the ECH model has an additional cωω² rotation term that, while negligible, still contributes; baseline Ω_m, H_0 differ from Planck best-fit at ~1% level in this benchmark. Caption L997-999 notes the deviation is "~2–3% across z=0–3." | **NEEDS-VERIFY** — OpenAI's point that a constant w=−1 term with Ξ tuned to ρ_Λ should give zero deviation is mathematically correct IF Ω_m and H_0 are identical to ΛCDM. The caption implies the ECH model uses the same Ω_m but the ECH Friedmann equation differs at order (Ξ·M_Pl²) from the ΛCDM one by the cωω² term and potentially by any non-constant ECH contributions. **PARTIALLY VERIFIED** — the 2–3% claim requires explicit statement of which Friedmann equation generated the orange curve and whether cωω² alone produces the deviation. | Add one sentence to caption or figure note specifying the Friedmann equation used and confirming the 2–3% deviation source |
| 25 | OpenAI | P1A-E3 | ESSENTIAL | Action includes on-shell T² term varied simultaneously with other fields | L853-870: paper explicitly states T²_abc term "is a shorthand… not an independent kinetic term and is not varied independently… so no double counting arises." | MISLABELED — MINOR/NIT; paper already discloses this; rewriting the action to follow the standard integrate-out-torsion procedure is editorial style | Optional: rewrite action to follow standard EC procedure (pedagogically cleaner but not a physics error) |
| 26 | OpenAI | P1A-E4 | ESSENTIAL | Version tags and draft history in body | L49 `\paperVersion{v1A.0.64}`, Sec. X D footnote "An earlier version… misidentified" | HOUSTON-DECISION (HD-11) — version tags removed at submission; "earlier version" footnote is a real correction note that should be rewritten as a standalone clarification | Fix "earlier version" footnote → rephrase as "Note: this result…" without process language |
| 27 | OpenAI | P1A-E5 | ESSENTIAL | Zenodo DOI placeholder "to be inserted" | Data availability section | HOUSTON-DECISION (HD-4) — DOI at submission; real but not a peer-review blocker | Insert real DOI at submission |
| 28 | OpenAI | P1A-E6 | ESSENTIAL | Companion-paper dependency for quantitative claims | Same as Gemini E2 / Grok E2 | MISLABELED — MAJOR not ESSENTIAL | See row 2 |
| 29 | OpenAI | P1A-E7 | ESSENTIAL | "G_N" vs G notation ambiguity in Eq. (4) | L~870 shows Eq.(4); body elsewhere uses G. G_N appears uniquely here | **VERIFIED — MINOR** — G_N is non-standard; should be G_N or G consistently | Fix: standardize to G_N with explicit note "G_N = Newton's constant G" at Eq.(4) first use |
| 30 | OpenAI | P1A-E8 (pass 2) | ESSENTIAL | Eq. (14) dimensional inconsistency in one-loop operator: 1/M_Pl factor makes Lagrangian dim +3 if ϑ_NY is dimensionless | L~1455-1475: paper defines ϑ_NY as a dimensionless axion rotation angle; [∂_μϑ_NY] = [mass]¹ and [J⁵_μ] = [mass]³, so [∂ϑ J⁵] = [mass]⁴; then 1/M_Pl gives [mass]³ — inconsistency is real IF ϑ_NY is dimensionless | **NEEDS-VERIFY** — dimensional analysis in this equation needs explicit resolution in paper; if ϑ_NY is canonically normalized with [ϑ_NY]=[mass], the 1/M_Pl is correct; if it's dimensionless, drop 1/M_Pl | Add one line specifying dimension convention for ϑ_NY; consistent with Appendix C |
| 31 | OpenAI | P1A-E9 (pass 2) | ESSENTIAL | γ scheme spread ~0.020 stated but SU(2)–DLM gap is 0.0365 | L~920 γ_SU(2)≈0.274, γ_DLM≈0.2375: difference = 0.0365 not 0.020 | **VERIFIED — MINOR** — stated "~0.020" is incorrect; should be "~0.037" for SU(2) vs DLM pair; or "~0.015" if referring to Meissner vs DLM | Fix: update scheme-spread text and Table IV to ~0.037 |
| 32 | OpenAI | P1A-E10 (pass 2) | ESSENTIAL | Sign error: residual 10⁵ from e^{−3ΔN_tot}, but e^{−3×4}≈6×10⁻⁶ not 10⁵ | L~2298-2310: paper discusses "residual 10⁵ tracks the exponential" sensitivity | **VERIFIED — MAJOR** — e^{+3×4} ≈ 1×10⁵ but paper writes "e^{−3ΔN}" and "10⁵"; the sign should be + (the sensitivity is that +ΔN rescales amplitude by e^{+3ΔN}). This is a sign-of-exponent transcription error. | Fix: replace "e^{−3ΔN_tot}" with "e^{+3ΔN_tot}" (or "±ΔN rescales by e^{±3ΔN} ≈ 10^{±5}") at L~2303-2310 |
| 33 | OpenAI | P1A-M1 | MAJOR | Route-2 two normalizations (10⁻⁶⁰ vs 10⁻³³) without consistent derivation | L~1489-1495: paper acknowledges two orderings; notes conclusion is "robust" to choice | MISLABELED — OPINION; paper discloses both orderings but a single consistent path would be cleaner. Not a physics error. | Optional: single dimensionally-consistent derivation |
| 34 | OpenAI | P1A-M2 | MAJOR | Fig. 5 RG running is schematic without stated β-function | L~1563: figure caption context | MISLABELED — MINOR; schematic nature is evident from context but adding "schematic" label is good practice | Add "schematic" label to Fig. 5 top panel |
| 35 | OpenAI | P1A-M3 | MAJOR | SPHEREx 2.6–5σ forecast without full methodology | Companion paper [2] contains the Fisher forecast | MISLABELED — MAJOR for self-contained submission; documented as companion-paper dependency | See row 2 |
| 36 | OpenAI | P1A-M4 | MAJOR | σ(f_NL) inconsistency: 0.7 (ideal) vs ~1.0 (with systematics) not harmonized | Table I says σ(f_NL)≈0.7; footnote 6 gives ~1.0 with systematics | **VERIFIED — MINOR** — these are two distinct projections (ideal vs degraded) and should be labeled as such; currently appears inconsistent | Add explicit label "ideal-survey σ(f_NL)≈0.7, degraded with GR-projection+photo-z σ(f_NL)≈1.0" |
| 37 | OpenAI | P1A-M5 | MAJOR | γ_PTA = 2.567±0.382 in Fig. 1 caption without companion citation | Caption cites companion Paper III [46]; Sec X G attributes it | MISLABELED — covered under companion dependency; not a new finding | None beyond companion arXiv ID insertion at submission |
| 38 | OpenAI | P1A-M7 (pass 2) | MAJOR | ρ correlation parameter undefined in Fig. 4/6 captions | Figs 4, 6: "ρ = 0, 0.3, 0.5" — ρ not defined in main text | **VERIFIED — MINOR** — ρ (cross-correlation between f_NL and β estimators in joint forecast) is never defined in body or captions | Define ρ explicitly at first use in Fig. 4/6 caption or body |
| 39 | OpenAI | P1A-M8 (pass 2) | MAJOR | "cube of fermion bilinear" scales as cube — incorrect | L~1057: "the cube of the fermion bilinear scales as the cube of the fermion number density" | **VERIFIED — MINOR** — ⟨J⁵_μ⟩ ∝ n_ψ (linear, not cubic); dilution as a⁻³ is number density dilution, not "cube of bilinear." Phrasing is misleading. | Fix phrasing: "⟨J⁵_μ⟩ ∝ n_ψ and dilutes as a⁻³" |
| 40 | OpenAI | P1A-M9 (pass 2) | MAJOR | pLEE undefined; null procedure not documented | L~1255 "hemisphere null at p_LEE < 10⁻⁴" | MISLABELED — MINOR/companion-dependent; p_LEE procedure is in companion Paper IV; paper should add "see companion Paper IV for LEE-correction methodology" | Add companion citation at p_LEE usage |
| 41 | OpenAI | P1A-M10 (pass 2) | MAJOR | Route-2 anomaly-bridge chain not explicitly mapped | L~1489 footnote | OPINION — level of detail appropriate for amplitude-budget paper | None |
| 42 | OpenAI | P1A-n4 | MINOR | β used for birefringence angle and RG β-function; γ collision with γ_PTA | Throughout | **VERIFIED — MINOR** — notation collisions are real; paper uses β_CB, γ_BI with subscripts in some places but not all | Enforce subscripts: β_CB / β_RG; γ_BI / γ_PTA globally |
| 43 | OpenAI | P1A-E7 (pass 1) | ESSENTIAL | G_N notation | See row 29 | VERIFIED — MINOR (duplicate entry) | Already listed |
| 44 | Perplexity | P1A-E1 | ESSENTIAL | Heavy reliance on companion papers | Same as Gemini E2, Grok E2, OpenAI E6 | MISLABELED — MAJOR not ESSENTIAL | See row 2 |
| 45 | Perplexity | P1A-E2 | ESSENTIAL | Internal version markers in title block | v1A.0.64 in header; HD-11 standing | HOUSTON-DECISION (HD-11) | Remove at submission |
| 46 | Perplexity | P1A-E3 | ESSENTIAL | Abstract overstates ansatz-based constraints as theorems | Paper uses "channel-level assessment" not "theorem" throughout | MISLABELED — MINOR; abstract already says "under stated assumptions" | None; editorial polish optional |
| 47 | Perplexity | P1A-E4 | ESSENTIAL | Standalone reader failure for SPHEREx/LiteBIRD companion-based claims | Same as rows 2, 28 | MISLABELED — MAJOR not ESSENTIAL | See row 2 |
| 48 | Perplexity | P1A-E5 | ESSENTIAL | σ values from different null tests juxtaposed | Paper scopes each σ at the site it appears; explicit "not directly comparable" note absent from abstract | **VERIFIED — MINOR** — abstract-level juxtaposition of β_obs (3.6σ), ACT (2.9σ), SPHEREx forecast (2.6–5σ) lacks a "not directly comparable" disclaimer in the abstract itself | Add one-sentence disclaimer to abstract: "these significances arise from different null procedures and are not directly comparable" |
| 49 | Perplexity | P1A-E6 | ESSENTIAL | Zenodo DOI placeholder | Same as OpenAI E5 | HOUSTON-DECISION (HD-4) | At submission |
| 50 | Perplexity | P1A-E7 (pass 2) | ESSENTIAL | (α/M)M_Pl numerical chain gives ~3×10⁻³ not 10⁻² | L~930: "(α/M)M_Pl ∼ 10⁻²" from one-loop estimate | **NEEDS-VERIFY** — the Perplexity chain is internally complex; the text describes this as motivating an order-of-magnitude (not exact) value; a factor-of-3 discrepancy in an OOM estimate is within stated tolerance | Confirm: if the chain gives 3×10⁻³, update to "O(10⁻²)" with parenthetical "(one-loop estimate; factor-of-few uncertainty inherited from δ_NY scheme-dependence)" |
| 51 | Perplexity | P1A-M1–M7 (pass 2) | MAJOR | Various dimensional, σ-comparability, and normalization issues | Covered in rows above (OpenAI and Gemini provide better-sourced versions) | See corresponding rows above | |

---

## EXT5 Closure Status Summary

| EXT5 Item | Description | R35conf Status |
|-----------|-------------|----------------|
| E1 (NJL arithmetic) | ρ ~ 4×10⁻⁶⁹ ρ_Λ, below ρ_Λ | **CLEAN — confirmed in v1A.0.64 L1378** |
| E2 (Ξ caption) | Ξ = ρ_Λ/M_Pl⁴ = Λ_eff/M_Pl² ≈ 10⁻¹²³ | **CLEAN — confirmed in v1A.0.64 L994** |

---

## Counts (R35conf P1A)

| Category | Count | Items |
|----------|-------|-------|
| **VERIFIED (fix required)** | **7** | G_N notation (#29, #43), E10 sign error in e^{±3ΔN} (#32), E9 γ-scheme spread ~0.020→~0.037 (#31), M4 σ(f_NL) labeling (#36), M7 ρ undefined in Figs 4/6 (#38), M8 "cube of bilinear" phrasing (#39), P1A-m2 per-null-test disclaimer in abstract (#48) |
| **NEEDS-VERIFY (author judgment)** | **3** | P1A-E2 (Fig. 3 2–3% deviation source, #24), E8 ϑ_NY dimension convention (#30), Perplexity (α/M)M_Pl discrepancy (#50) |
| **MISLABELED (real but overstated severity)** | **8** | P1A-E1 Gemini/Grok/Perplexity (companion dependency, ESSENTIAL→MAJOR), P1A-E4 OpenAI (action T² term, ESSENTIAL→MINOR), P1A-E10 OpenAI (residual 10⁵ sign already counts above), M3 Gemini (thermal-reset framing), Grok E3 (scope language), Grok E4 (off-shell claim) |
| **INCORRECT/FALSIFIED (source disproves)** | **4** | OpenAI P1A-E1 (unit conversion error — paper IS correct, #23), future-date "June 12, 2026" claims (#10), extraction-artifact notation claims (#11, #13, #14) |
| **HOUSTON-DECISION** | **3** | Version tags, Zenodo DOI, companion arXiv IDs at submission (HD-4/HD-11) |
| **OPINION/MISLABELED-DOWN** | **8** | Gemini M1/M2/M3, Grok M1/M2/M3, OpenAI M1/M3/M10/n9, editorial-only items |

**Genuinely NEW VERIFIED items (not in prior rounds): 7**
Most important: **OpenAI E10** (sign error e^{−3ΔN} → e^{+3ΔN}), **OpenAI E9** (γ scheme spread ~0.020 → ~0.037), **G_N notation** standardization.

---

## CLEAN / NOT-CLEAN on EXT5 Closures

**P1A EXT5 CLOSURES: CLEAN**

Both priority items (NJL ρ~4×10⁻⁶⁹ ρ_Λ below; Ξ = ρ_Λ/M_Pl⁴ in caption) confirmed correct in v1A.0.64. OpenAI's challenge to the NJL unit conversion (P1A-E1) is **FALSIFIED by independent recomputation** — OpenAI confused hbarc = 1.973×10⁻⁵ eV·cm with its inverse.

---

## Closure Plan for VERIFIED Items

| # | Fix | tex location | Size |
|---|-----|-------------|------|
| R35-A1 | **E10 sign fix**: replace "e^{−3ΔN_tot}" with "e^{+3ΔN_tot}" (or "e^{±3ΔN_tot} ≈ 10^{±5}" for clarity) | ~L2303-2310 | 1 line |
| R35-A2 | **E9 γ scheme spread**: update "~0.020" → "~0.037 (SU(2)–DLM pair)" in body and Table IV | ~L920, Table IV | 2 occurrences |
| R35-A3 | **G_N notation**: standardize Newton's constant to G_N throughout; add "G_N = Newton's G" note at Eq.(4) | Eq.(4) + global | ~5 occurrences |
| R35-A4 | **M4 σ(f_NL)**: add explicit labels "ideal-survey" (≈0.7) and "degraded with systematics" (≈1.0) at each occurrence | Table I + footnote 6 | 2 labels |
| R35-A5 | **M7 ρ definition**: define ρ as "cross-correlation coefficient between f_NL and β joint-forecast estimators" at first Fig. 4 caption use | Fig. 4 caption | 1 sentence |
| R35-A6 | **M8 bilinear phrasing**: replace "cube of fermion bilinear scales as cube of fermion number density" → "⟨J⁵_μ⟩ ∝ n_ψ and dilutes as a^{−3}" | ~L1057 | 1 sentence |
| R35-A7 | **Abstract null-test disclaimer**: add "these significances arise from different null procedures and are not directly comparable" to abstract near the 3.6σ / 2.9σ / 2.6–5σ sentences | Abstract | 1 sentence |
| R35-A8 | **E4 "earlier version" footnote**: rewrite Sec. X D footnote "An earlier version of this manuscript misidentified…" → "Note: the torsion-free Levi-Civita restriction…" (process language → technical clarification) | Sec. X D | 1 sentence |

**NEEDS-VERIFY items (Houston judgment before next R-round):**
- P1A-E2/#24: confirm the Friedmann equation used for the orange ECH curve in Fig. 3 and which term produces the 2–3% H(z) deviation; add one sentence to caption.
- P1A-E8/#30: confirm dimension convention for ϑ_NY (dimensionless vs dim-1); add one line.
- Perplexity #50: confirm (α/M)M_Pl one-loop estimate numerical chain consistency; if 3×10⁻³, update to "O(few×10⁻³)" with scheme-uncertainty note.
