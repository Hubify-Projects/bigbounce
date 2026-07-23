# TRUTH AUDIT — P2 v1.7.126 (EXACT-PDF 085bfcb5) — 2026-07-22 CLAUDESTACK-CONFIRM

- **Paper:** P2 "The Exact Matter-Contraction Non-Gaussian Amplitude: Four-Vertex Derivation and Conditional Large-Scale-Structure Mapping"
- **Version/binding:** v1.7.126, commit 44b666cb, pdf sha256 085bfcb5…5fd5e7 (Claude INT confirmed exact-PDF MATCH)
- **Legs audited:** Grok grok-4.3 (MAJOR-REVISIONS, 2 MAJOR + 2 MINOR); Gemini gemini-3.1-pro-preview (MINOR-REVISIONS, 3 MINOR); Claude INT Opus (MINOR-REVISIONS, 4 transparency MINOR)
- **Ledger:** `project-context/peer-reviews/DISPOSITIONS/P2.md` (DP2-xx). **Tex:** `research/focused_paper_source_integration/02_full_draft.tex`. **Artifacts:** `research/cubic_bounce_transmission/`
- **Verdict classes:** ALREADY-TRACKED-GATE / DISCLOSED-RE-FLAG / SCOPE-VENUE-OPINION / FALSIFIED / GENUINELY-NEW-REAL

## Verdict counts

| Class | Count |
|-------|-------|
| ALREADY-TRACKED-GATE | 2 |
| DISCLOSED-RE-FLAG | 2 |
| SCOPE-VENUE-OPINION | 2 |
| FALSIFIED | 0 |
| **GENUINELY-NEW-REAL** | **5** |
| **Total** | **11** |

**Headline: both Grok MAJORs resolve to non-real (disclosed / tracked). No MAJOR survives. The 5 GENUINELY-NEW items are all trivial numerical-transparency / one-line-disclosure edits; none touches −35/16 or any conclusion.**

## Finding-by-finding

| # | Reviewer | Sev | Gist | Verdict | Evidence |
|---|----------|-----|------|---------|----------|
| G1 | Grok | MAJOR | SPHEREx mapping framed as "core" while disclaimed illustrative/conditional → title↔abstract↔scope mismatch, "violates PRD self-contained-Article standard" | **DISCLOSED-RE-FLAG** | Falsified by the paper's OWN repeated disclosure: title says "…and **Conditional** Large-Scale-Structure Mapping"; abstract L1073 "These values are **illustrative conditional diagnostics, not an observational headline** … The **primary contribution is the exact contraction-phase amplitude derivation**"; Scope L1082 "observational numbers are illustrative conditional mappings, not a unified or independent survey forecast"; L1153 assumption (d) enumerated; L1149 "the algebraic coefficient and the cubic-transfer gate are separate claims." = standing DP2-13 conditional-framing + DP2-17 (recast-not-independent) + DP2-29 (single-source). The "violates PRD standard" flavor is presentation opinion (DP2-30). Nothing not already disclosed. |
| G2 | Grok | MAJOR | "Faithful cubic-order transmission rests on **linear-order verification only**, no explicit third-order calc; observational statements rest on an unproven model assumption not a completed derivation" | **DISCLOSED-RE-FLAG** | The paper explicitly agrees and foregrounds exactly this. L1082 "…is established at linear order … the nonlinear extension is motivated by single-clock conservation and **is not claimed here as a completed third-order calculation**"; L1155 the v1.7.125 dressed-metric closure computes T_c(k)=1 identically (\|T_c−1\|=2.7e-10…2.2e-5; \|δf_NL\|≤6.8e-8 at kη_B=1e-2) and states plainly "This is explicitly a **scheme-specific statement, not a scheme-independent theorem** … we still do not claim a closed cubic-transfer theorem valid across all schemes … a fully nonlinear third-order branch calculation **remains open** … Every late-time sensitivity … remains conditional." Artifacts `research/cubic_bounce_transmission/g1_dressedmetric_ic_close.{py,json}` (committed e641cb1c). = standing DP2-13 (RE-FLAG-DISCLOSED, load-bearing caveat ★). Identifies nothing not disclosed/tracked → NOT genuinely-new. |
| G3 | Grok | MINOR | Fisher rests on in-house surrogate covariance (not Heinrich per-triangle) + 30% b_φ prior "justified internally"; "cannot be presented as quantitative diagnostics without external covariance" | **ALREADY-TRACKED-GATE** | External per-triangle Cov_B is the tracked OPEN-COMPUTE gate DP2-26 (Heinrich matrix unpublished — no arXiv ancillary / no Zenodo, `INT_v3/DATA_UNLOCK_2026-07-05.md`); surrogate labeled a validation not a forecast = DP2-22/-34. Disclosed verbatim: L1082 "The latter does **not replace the unpublished external per-triangle covariance**"; L1224 "**Neither replaces the missing external per-triangle covariance**, and no endpoint is presented as a guaranteed floor." The 30%-prior-motivation sub-point → see GN1 (Gemini M3). |
| G4 | Grok | MINOR | App B symbolic scripts' provenance (GitHub commit / Zenodo) cited but not deposited as supplementary; impedes referee re-verification of vertex-sum algebra | **ALREADY-TRACKED-GATE** | DP2-27 (add per-vertex print loop for third-party reproducibility; values already hand+2×sympy certified so not a math defect) + DP2-30/-11 (real Zenodo DOI pending at camera-ready; GitHub pointer already in DAS). Repo-hygiene / deposit-at-submission, non-blocking, Houston-gated. |
| M1 | Gemini | MINOR | Inline file paths / script names in main narrative prose should be relegated to footnotes / Data-Availability per PRD style | **SCOPE-VENUE-OPINION** | Presentation preference = DP2-30 (code-filename-density, OPINION-class, "does not change any number"). `\path{}` usage in body is a deliberate reproducibility choice; relegation is editorial taste. |
| M2 | Gemini | MINOR | Migrate the term-by-term vertex walkthrough + Table V from Appendix B into main-text Sec II to highlight the primary result | **SCOPE-VENUE-OPINION** | Content-placement preference = DP2-30. The core result IS in the main text (abstract + Sec II coefficients (3,1,−9,5,−33,9), Table I); appendix depth is editorial taste, not correctness. |
| GN1 | Gemini | MINOR | 30% b_φ Gaussian prior: physical/observational motivation for exactly 30% not stated — arbitrary illustrative benchmark, or theory-derived? | **GENUINELY-NEW-REAL** | Adjacent to DP2-34/-04 but the *motivation clause* is genuinely absent. Tex L1224/L1270 call it a "declared 30% Gaussian theory prior … conditional," and the ladder is "illustrative," but the term "theory prior" implies derivation while no basis is given. One-line editable disclosure closes it. |
| GN2 | Claude | MINOR | r_eff=0.9929 not reproducible from printed σ's: 0.626/0.631=0.9921 (4th-decimal disagreement); reader cannot reproduce r_eff from the quoted 3-decimal σ's | **GENUINELY-NEW-REAL** | Recomputed: 0.626/0.631 = **0.9921** ≠ printed 0.9929 (paper L1220). Not a math error — r_eff is a survey-weighted Fisher information-cosine (different inner product, stated L1200/L1220 "not interchangeable"), but "giving r_eff=0.9929" invites the bare-ratio computation. Same for 0.687/0.688→0.9985 vs printed 0.9986. Not in ledger. Tiny editable transparency fix. |
| GN3 | Claude | MINOR | Planck consistency printed "0.37σ" but recomputes to 0.36σ | **GENUINELY-NEW-REAL** | Recomputed from L1290's own values f_NL^bounce=−0.11±5.71 vs −2.1875: (2.1875−0.11)/5.71 = **0.3638 → 0.36σ**, not 0.37σ. Trivial rounding, one unit in the 2nd decimal. Not in ledger. |
| GN4 | Claude | MINOR | "34.7% … (0.687→0.449)" baseline-label mismatch | **GENUINELY-NEW-REAL** | Recomputed: (0.688−0.449)/0.688 = **34.74%** (bounce real-space 0.688 baseline); (0.687−0.449)/0.687 = **34.64%** (the parenthetical's 0.687). Text L1222 states 34.7% but parenthesizes 0.687 (which gives 34.6%). Cosmetic baseline-labeling fix. Not in ledger. |
| GN5 | Claude | MINOR | "2.61σ (rounded to 2.63σ for the adopted r=0.84)" wording imprecise — 2.63 is a recomputation, not a rounding of 2.61 | **GENUINELY-NEW-REAL** | Recomputed: 2.1875·0.84/0.7 = **2.625→2.63σ** (r=0.84); 2.1875·0.8354/0.7 = **2.611→2.61σ** (r=0.8354). So 2.63 ≠ round(2.61); the rounding lives in r (0.8354→0.84). Substance (2.63-from-r=0.84) is tracked DP2-14, but the "rounded to" phrasing (L1218, L1265, abstract L1073) is a genuinely-new wording imprecision. |

## Notes on the two Grok MAJORs (special-care audit)

- **G1 / G2 both resolve non-real.** Neither identifies anything the paper does not already disclose and track. G1 is the long-standing conditional-framing disclosure (DP2-13/-17/-29) — the title, abstract, Scope paragraph, and every late-time sentence subordinate the observational numbers to the amplitude result and label them "illustrative conditional diagnostics." G2 is the DP2-13 load-bearing caveat, now *strengthened* in v1.7.125 by the committed dressed-metric T=1 computation with an explicit "not a scheme-independent theorem / third-order branch remains open" disclosure. Per protocol these are DISCLOSED-RE-FLAG, **not** soft-dismissals: each is source-cited to the paper's own disclosure sites + the committed artifacts, and neither is falsified — the paper concedes the exact limitation each MAJOR names.
- Grok's own closing line (3) affirms the central algebraic claim (coefficients (3,1,−9,5,−33,9), f_NL^local=−35/16) is "supported by the explicit symbolic summation and cross-checks in Appendix B." Not a finding.

---

## GENUINELY-NEW-REAL FIX LIST (concrete tex edits — `02_full_draft.tex`)

1. **GN1 (30% prior motivation)** — L1224 / L1270: after "declared 30\% Gaussian theory prior on $b_\phi$" add a clause identifying it as an illustrative benchmark, e.g. "(an **illustrative benchmark** bracketing typical assembly-bias departures from the universal-mass-function $b_\phi$, not a first-principles bound)"; mirror one phrase in the Table caption L1270.

2. **GN2 (r_eff reproducibility)** — L1220: replace "giving $r_{\rm eff}=0.9929$ and $0.9986$" with wording that stops the reader inferring a bare σ-ratio, e.g. "with **survey-weighted Fisher recovery** $r_{\rm eff}=0.9929$ and $0.9986$ (a covariance-weighted information cosine, **not** the bare $\sigma$ ratio $0.626/0.631=0.992$)"; or quote both σ pairs to 4 decimals and state the r_eff inner-product formula explicitly.

3. **GN3 (Planck 0.37σ→0.36σ)** — L1290: change "only $0.37\sigma$ from the predicted $-35/16$" to "$0.36\sigma$" ((2.1875−0.11)/5.71 = 0.364).

4. **GN4 (34.7% baseline label)** — L1222: align the parenthetical to the value that yields 34.7%: "$34.7\%$ … ($0.688\to0.449$)" (bounce real-space baseline), OR change the figure to "$34.6\%$" if the 0.687 local baseline is intended. Pick one baseline consistently.

5. **GN5 ("rounded to 2.63σ" wording)** — L1218 and L1265 (and optionally abstract L1073): replace "rounded to $2.63\sigma$ for the adopted $r=0.84$" with "$2.63\sigma$ when the adopted $r=0.84$ convention is used (the rounding is in $r$: $0.8354\to0.84$)", so 2.63 reads as a recomputation, not a rounding of 2.61.

**Integrity:** none of these changes any headline number; −35/16 quadruple-certification untouched; all are display/label/one-line-disclosure edits. After applying, run directive-G PDF hygiene (bump patch, recompile 0 undef-refs, `/latex-audit`, re-mirror, Convex bump) per standing rules.
