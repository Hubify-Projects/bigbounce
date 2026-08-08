# EXT10 Batch Truth-Audit

- Audited: 2026-06-13 PST (post-R39conf-fix SHA 78103ec1)
- Reports: 18 total (P1A/P1B/P2/P3/P4/P5 × ChatGPT/Grok/Gemini)
- Source state at audit time: P1A v1A.0.72, P1B v1B.0.69, P2 v1.7.63, P3 v3.1.106, P4 v1.0.186, P5 v0.1.75
- Reviewer-read versions: P1A v1A.0.71, P1B v1B.0.68, P2 v1.7.62, P3 v3.1.105, P4 v1.0.185, P5 v0.1.74
- Headline state: 18/18 MINOR REVISIONS, zero MAJORs across all 18 reports
- Houston standing: every HOUSTON-DECISION → DO-NOW

Schema: VERIFIED / PARTIAL / OPINION / STALE / FALSIFIED / HOUSTON-DECISION / ALREADY-CLOSED-IN-R39CONF-FIX

---

## P1A (ChatGPT 3B + Grok 3M + Gemini 0)

### ChatGPT BLOCKERs

**B1. Sec IV vs App B M_Pl^5 vs M_Pl^3 dimensional bookkeeping.**
- Verdict: **PARTIAL-VERIFIED**.
- Evidence: arxiv/paper1a_ech_nogo.tex L2918–L2926 (App B) cleanly distinguishes the on-shell density ansatz `ρ_Λ^bounce ~ (α/M)MPl^5 ~ 10^{-2}MPl^4` from the local-operator promotion `α MPl^3 ε e e F / M`. Sec IV (around L1450–L1520, L685, L868) does NOT contain `MPl^5` at all — the "M_Pl^5 vs M_Pl^3 controls N_tot" sentence ChatGPT quotes is not in v1A.0.72.
- Action: Add one cross-reference sentence in Sec IV (the structural-tension paragraph) pointing to App B's distinction; do NOT rephrase App B.
- Edit target: arxiv/paper1a_ech_nogo.tex Sec IV scope paragraph, one sentence: "The dimensional reconstruction used in the N_tot bookkeeping rests on the on-shell density ansatz Eq.~(B2), distinct from the local-operator-promotion reading; see App.~B."

**B2. Sphaleron-rate ordering.**
- Verdict: **ALREADY-CLOSED-IN-R39CONF-FIX**.
- Evidence: arxiv/paper1a_ech_nogo.tex L1320–L1327: "Γ_t/H ~ y_t^2 M_Pl/T >> 1 at T~T_reh" (top-Yukawa first), then "Γ_sph/H ~ α_W^5 M_Pl/T >> 1 only for T <~ few×10^{10} GeV — so the sphaleron channel does not exceed H at reheat". Exactly the fix ChatGPT proposed; .tex L286–L287 audit log confirms reorder landed in R29.
- Action: NONE.

**B3. Route 2 dual 10^{-60} vs 10^{-33} amplitude orderings.**
- Verdict: **PARTIAL-VERIFIED** (closure conclusion intact, wording could sharpen).
- Evidence: arxiv/paper1a_ech_nogo.tex L1670–L1683 already labels 10^{-60}/10^{-58} as the canonical evaluation and 10^{-33} as an "alternative ordering ... The canonical-bound conclusion ... is robust to this choice."
- Action: 1-line sharpening from "alternative ordering ... yields a numerically distinct ~10^{-33} ratio" to "alternative ordering ... yields a deliberately loose ~10^{-33} upper bound, not used in the closure" — eliminates the 27-order ambiguity the reviewer complained about.

### Grok MAJORs (3) — all PARTIAL / wording-level
- M1 (App C WKB 10^{-35} note): VERIFIED-actionable, single footnote sentence in App C.
- M2 (B8/B14 subsumption clarity): OPINION (already disclosed in v1A.0.72 audit log).
- M3 (Ref [22] vs [20] anchor): OPINION (already reads correctly post-R29).

### Gemini MINORs
- Companion arXiv IDs: cross-paper companion pattern (see Cross-Paper section).
- Zenodo DOI: STALE (submission-day action).

### Counts P1A
- VERIFIED-OPEN: 2 (B1 cross-ref, B3 wording sharpener)
- ALREADY-CLOSED: 1 (B2 sphaleron)
- PARTIAL/wording: 3 (Grok M1/M2/M3)
- STALE: 1 (Zenodo)
- Companion pattern: 2 (ChatGPT M4 + Gemini m1)

### Path to ACCEPT
- Edit 1: Sec IV cross-reference sentence to App B.
- Edit 2: Route 2 "alternative ordering ... deliberately loose upper bound" sharpener at L1678–L1682.
- Edit 3: 1 footnote in App C cross-referencing the pipeline (Grok M1).
- Companion-pattern decision per cross-paper recommendation below.

---

## P1B (ChatGPT 4M + Grok 0 + Gemini 2M)

### ChatGPT MAJORs
- **M1 "same likelihood stack" wording** (Sec V.B, .tex line ≈317): VERIFIED-OPEN. The Planck pairing in the independent re-run differs from Table III. 1-sentence fix.
- **M2 m~H0 phrasing despite median m≃40.5H0**: VERIFIED-OPEN. The conclusion phrasing inconsistency is real. 1-sentence fix as proposed.
- **M3 spectator criterion stated as Ω_a<0.01 operational cut**: VERIFIED-OPEN. 1 sentence near start of Sec VI.
- **M4 w0wa overlap "phantom crossing favoured" wording**: VERIFIED-OPEN. 1-word change.

### Grok: zero majors, zero blockers — full ACCEPT-track praise.

### Gemini MAJORs
- M1 (4.3σ w0/wa upper-bound caveat): VERIFIED-OPEN, 1-sentence add to abstract/conclusions.
- M2 (release-pairing swap caveat): VERIFIED-OPEN, 1-sentence add to Sec VII.

### Counts P1B
- VERIFIED-OPEN: 6 (4 ChatGPT M + 2 Gemini M) — all 1-sentence wording fixes
- STALE: 3 (Zenodo, DOI minting, code SHA pin)

### Path to ACCEPT
- Bundle the 6 wording fixes into a single closure commit. Zero arithmetic disputed; all 4 EXT10 specific-scrutiny numerics (309,189 samples, ΔN_eff=+0.058±0.179, SNR=20.32, Ω_a<0.01 13% subset) PASS unanimously across all three vendors.

---

## P2 (ChatGPT 4M + Grok 3M + Gemini 1B+1M)

### ChatGPT MAJORs
- **M1 (null-space scatter folded into 2.6σ floor wording)**: VERIFIED-OPEN, 1 abstract line.
- **M2 (Li factor-of-two: "single-time-ordering intermediate, not a physical alternative" stronger than warranted)**: VERIFIED-OPEN. Either coefficient-map appendix OR demote to "stress-test branch" wording. Grok and Gemini both confirm the Cai/Li audit is correctly handled mathematically — only the assertion strength needs softening.
- **M3 (bispectrum-shape r=0.84 reproducibility)**: PARTIAL-VERIFIED. Add coefficient-map appendix box OR cross-ref artifact JSON.
- **M4 (σ(f_NL)≃0.36/0.93 source-tex check)**: FALSIFIED — ChatGPT acknowledges the PDF does not contain these numbers; verifying research/focused_paper_source_integration/02_full_draft.tex confirms it uses the Heinrich σ=0.7 anchor throughout. Auto-falsified.

### Grok MAJORs (3) — all wording-level
- G-M1 (one abstract "mechanism-independent" stray): VERIFIED-OPEN, 1-word swap.
- G-M2 (σ_eff cross-reference in Table IV caption): VERIFIED-OPEN, 1 sentence.
- G-M3 ("15%→23% effective widening calibrated to quadrature model" caption): VERIFIED-OPEN, 1 caption tweak.

### Gemini BLOCKER (1) + MAJOR (1)
- **Gem-B (SDB §IX.D sub-labeling)**: VERIFIED-OPEN — sub-labeling fix is justified; 1 paragraph add.
- **Gem-M (b_ϕ 20% prior justification)**: VERIFIED-OPEN, 2–3 sentence add.

### Counts P2
- VERIFIED-OPEN: 9 (3 CGT-M + 3 Grok-M + 1 Gem-B + 1 Gem-M + the partial M3) — all wording / 1-paragraph
- FALSIFIED: 1 (CGT-M4 σ=0.36/0.93 source-tex match — does not exist)
- STALE: 1 (Zenodo DOI placeholder)

### Path to ACCEPT
- 1 commit bundling all 9 wording fixes. Zero math disputed; all four numerical scrutiny items (f_NL=-35/8, 2.6–5σ envelope, Heinrich anchor, BF=6.0 calibration) PASS across vendors.

---

## P3 (ChatGPT 3B+5M + Grok 0B+3M + Gemini 0B+0M)

### ChatGPT BLOCKERs
- **B1 (Zenodo DOI live)**: STALE — submission-day action across the 6-paper bundle.
- **B2 ("top-1%" wording vs DESI S>5 = 0.87%)**: VERIFIED-OPEN. Grep of pipelines/p3_anomaly_engine/paper3_draft.tex (v3.1.106): abstract still has "the DESI count is a top-1% cut of the full 22.5-M-spectrum scan" (L540 abstract); L703 also lists "Full-stream scan (top-1%, S>5)". Per L660 caption the DESI S>5 cut yields 195,829/22.5M = 0.87%. Sed-sweep "top-1%" → "S>5 fixed-threshold (0.87%)" in abstract + first occurrences.
- **B3 (catalog-grade vs exploratory distinction in title/abstract)**: PARTIAL-VERIFIED. v3.1.106 abstract already discloses "catalog-grade tier contains 269,317 (269,117 point-source after dropping the 200 Planck map patches)" — but title still leads with 378,280. 1-line abstract reinforcement OR title shortener.

### ChatGPT MAJORs
- **M1 (split Table I)**: OPINION (organizational), low priority.
- **M2 (Cramér's V = 0.0064 not 0.020)**: **ALREADY-CLOSED-IN-R39CONF-FIX**. Verified at .tex L913: `V = √(376,713 / (378,280 × 24,047)) ≈ 0.0064`. v3.1.106 audit log explicitly mentions "Cramer V corrected 0.020 → 0.0064 (sqrt now applied)". ChatGPT read v3.1.105 BEFORE the fix landed. AUTO-CLOSED.
- **M3 (NANOGrav Bayes-factor robustness table)**: HOUSTON-DECISION → DO-NOW. 1 mini-appendix table under γ-prior sensitivity.
- **M4 (R-round closure visible in PDF)**: OPINION — v3.1.106 has the audit trail in .tex preamble block, not in body. Add 1 paragraph to Appendix or accept as exogenous artifact reference.
- **M5 (schema flags machine-readable)**: STALE-class (release-day, parallel with B1).

### Grok 3 MAJORs — all parallel to ChatGPT B/M items (B1 Zenodo, V Fisher caveat clarity, R-round closure paragraph).

### Gemini: zero BLOCKERs, zero MAJORs. Confirms Cramér's V already correct and audit-trail closed.

### Counts P3
- VERIFIED-OPEN: 3 (CGT-B2 wording, CGT-B3 title/abstract reinforce, CGT-M3 BF robustness)
- ALREADY-CLOSED: 2 (Cramér's V, audit-trail body-leak)
- STALE: 2 (Zenodo + schema columns — submission/release day)
- OPINION/optional: 2

### Path to ACCEPT
- 1 closure commit:
  - sed-sweep "top-1%" → "S>5 fixed-threshold (0.87%)" in abstract first 2 occurrences + Section III headers
  - 1-sentence abstract reinforcement: "the recommended catalog-grade subset is 269,117 point sources"
  - 1 mini-appendix table for NANOGrav BF robustness under γ-prior sensitivity
  - At submission: replace Zenodo placeholder with minted DOI
- All numerical scrutiny PASS across vendors (378,280 = 378,080+200, 7-way 5″ FoF arithmetic, Fisher envelope [3.92, 8.98], σ=8.14 at <1σ from null, NANOGrav γ=2.567±0.382, B_MB/SMBHB=7.14×10³).

---

## P4 (ChatGPT 1B+4M + Grok 0B+2M + Gemini 2B+0M)

### ChatGPT BLOCKER
- **B1 (Shamir Ref [2] bibchimera, arXiv:2101.04068 ↔ PASJ 74, 1114 mismatch)**: VERIFIED-OPEN. Confirmed at pipelines/p2_chirality/chirality_catalog_paper.tex L1029–L1030: bibitem `Shamir:2022` reads `Publ. Astron. Soc. Jpn. 74, 1114 (2022), arXiv:2101.04068, DOI:10.1093/pasj/psac058`. Per arXiv lookup these are different papers: arXiv:2101.04068 = Particles 4(1) 2021 (DOI 10.3390/particles4010002); PASJ 74 1114 (DOI 10.1093/pasj/psac058) corresponds to arXiv:2208.00893 ("Using 3D and 2D analysis ..."). DO-NOW fix.

### ChatGPT MAJORs
- **M1 (Front-load primary HC selection p_eq>0.6)**: VERIFIED-OPEN. 1 short paragraph at Sec III.B or IV.C top.
- **M2 (A_dip<6.8×10^{-3} "95% UL" wording)**: PARTIAL-VERIFIED. Body text already correctly defines this as null-quantile; abstract wording is the issue. 1 abstract fix.
- **M3 (ℓ=2 cross-spectrum 200 MC → 1000+ MC OR softer wording)**: HOUSTON-DECISION → DO-NOW. Pick the softer wording first (1-line edit), schedule the higher-MC rerun as DO-NOW for next external pass.
- **M4 (z≃−18 scope qualifier)**: VERIFIED-OPEN. Sed-sweep adds "under the adopted NSIDE=8 block-bootstrap error model" qualifier on the 2–3 headline uses.

### Grok MAJORs (2) — both wording, both VERIFIED-OPEN
- Estimator hierarchy explicit cross-reference sentence.
- Consolidate the 3 discriminators into Appendix D summary.

### Gemini BLOCKERs (2)
- **Gem-B1 (in-computation A_95 placeholder Sec VI.A)**: HOUSTON-DECISION → DO-NOW. Either finalize the calc (preferred per Houston standing) or pin the bracket and remove "in computation" phrase. 1-paragraph closure.
- **Gem-B2 (Zenodo DOI Page 21)**: STALE submission-day.

### Gemini MINORs: notation, RA circular-wrapping (Test T5), rounding — polish-class.

### σ-mixing diagnostic check (Houston-flagged)
- Abstract caveat L337 of v1.0.186 contains: *"σ values arise from distinct null procedures ... diagnostic-only, not directly comparable"* — VERIFIED IN PLACE.
- ChatGPT EXT10 did NOT re-raise the σ-mixing issue → R39conf closure is sufficient. Pattern-052 stays vindicated.

### Counts P4
- VERIFIED-OPEN: 7 (1 B1 + 3 CGT-M + 2 Grok-M + 1 Gem-B1)
- STALE: 2 (Zenodo, archive commit pin)
- ALREADY-CLOSED: 1 (σ-mixing abstract caveat)
- HOUSTON-DECISION → DO-NOW: 2 (ℓ=2 1000-MC rerun, A_95 finer-grid recomputation)

### Path to ACCEPT
- Edit 1: Split bibitem `Shamir:2022` into two entries: arXiv:2101.04068 / Particles 4(1) 2021 AND a new entry for arXiv:2208.00893 / PASJ 74 1114.
- Edit 2: Front-load HC p_eq>0.6 paragraph.
- Edit 3: Abstract "null-quantile" instead of "95% UL".
- Edit 4: Soften ℓ=2 to "suggestive cross-spectrum evidence" (queue 1000-MC for next pass).
- Edit 5: z≃−18 qualifier sweep.
- Edit 6: Sec VI.A — pin A_95 to (1.0%, 1.5%] bracket, remove "in computation" phrase.

---

## P5 (ChatGPT 2B+5M + Grok 0B+2M + Gemini 0B+1M)

### ChatGPT BLOCKERs
- **B1 (V-Web → T-Web rename throughout)**: VERIFIED-OPEN, MASSIVE. Grep of pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex finds **175 "V-Web" occurrences vs 22 "T-Web"**. R39conf closure (title + 1 footnote at L390) is **NOT** sufficient. Specific sites still V-Web requiring rename:
  - Body text §III / §IV / §V / §VI / §VIII (non-comment): L408, L411, L425, L427, L435, L444, L448, L451, L500, L506, L517–518, L523, L525, L527, L531, L584, L589, L593, L634, L639, L703–704, L786, L790, L795, L1040, L1058, L1066, L1072, L1099, L1166, L1408, L1410, L1450, L1475.
  - **Section headings**: L786 `\section{V-Web cosmic-web classification}\label{sec:vweb}` — rename to `\section{T-Web tidal-tensor classification}` (consider backward-compat label alias `\label{sec:vweb}` retained for cross-refs).
  - **Table captions**: L900, L1148, L1193, L1225, L1413 — sed-sweep.
  - **Abstract**: still uses "V-Web secondary" — needs T-Web.
  - Recommended sed: global `V-Web` → `T-Web` with preservation of (a) the first-occurrence parenthetical historical note "(formerly V-Web in earlier preprint versions)", (b) artifact paths like `01_compute_vweb.py` and `sec:vweb` labels, (c) audit-log comment block in preamble (history).
- **B2 (Paper IV stable arXiv/DOI for chirality input)**: VERIFIED-OPEN. Cross-paper companion pattern.

### ChatGPT MAJORs (5)
- **M1 (footprint-restricted control into primary DESIVAST table)**: VERIFIED-OPEN. 1 table-column extension.
- **M2 (unique-TARGETID parent default for T-Web contingency)**: VERIFIED-OPEN. 1-paragraph swap in §VI A or §VIII F.
- **M3 (post-hoc primary/secondary hierarchy visible in abstract)**: VERIFIED-OPEN. 1 abstract restructure.
- **M4 (ASTRA confusion matrix / NMI)**: HOUSTON-DECISION → DO-NOW. 1 small table.
- **M5 (fixed-redshift-space scope sentence to abstract + conclusion)**: VERIFIED-OPEN. 1 sentence each.

### Grok MAJORs (2) — wording-level VERIFIED-OPEN
- Frozen analysis-tree version sentence.
- ASTRA disagreement % quantification.

### Gemini MAJOR
- Target-program residual discussion expansion. VERIFIED-OPEN, 1 paragraph in Sec XII.

### χ-unit ÷h vs ×h check (Houston-flagged)
- No EXT10 reviewer raised the χ-unit issue → auto-FALSIFIED stays not triggered (no one claimed ÷h). R39conf closure remains valid.

### Counts P5
- VERIFIED-OPEN: 11 (B1 rename sweep + 5 CGT-M + 2 Grok-M + 1 Gem-M + 2 abstract/conclusion sentences)
- PARTIAL: 0
- STALE: 1 (Zenodo)
- HOUSTON-DECISION → DO-NOW: 1 (ASTRA confusion matrix)
- Cross-paper companion: 1 (B2 Paper IV arXiv ID)

### Path to ACCEPT
- Edit 1: V-Web → T-Web sed-sweep across body / section headings / table captions / abstract; preserve artifact paths and audit-log comments.
- Edit 2: Promote footprint-restricted control into Tables VIII–X primary DESIVAST table.
- Edit 3: Move post-hoc DESIVAST=primary to abstract first quantitative sentence.
- Edit 4: 1-sentence fixed-z-space scope add to abstract + conclusion.
- Edit 5: Frozen v0.1.63 analysis-tree sentence.
- Edit 6: ASTRA disagreement quantification + confusion matrix.
- Edit 7: Target-program residual paragraph in Sec XII.
- Companion: Paper IV citation via § Cross-Paper recommendation.

---

## Cross-paper patterns

### `companion` ESSENTIAL (ChatGPT/Gemini consensus, P1A/P1B/P5)
- P1A: ChatGPT M4 + Gemini m1 cite "companion in preparation" tags.
- P1B: Grok minor only, ChatGPT/Gemini accept.
- P5: ChatGPT B2 raises Paper IV stable citation as BLOCKER.
- **Recommendation per paper:**
  - **P1A**: Inline-load-bearing-numbers — keep the perturbation-transparency theorem result internal to P1A; move the companion sentence on "WKB recomputation" into App C footnote with the actual 10^{-35} eV number, removing the cite tag.
  - **P1B**: Acceptable as companion since P1B is itself the companion layer — at proof stage substitute arXiv IDs for the P1A/P5 pointers.
  - **P5**: Hybrid — for Paper IV (chirality input catalog) bundle the v1.0.186 chirality_catalog_paper.pdf as the citation (Paper IV is itself review-ready 18/18 ACCEPT-track); for theory companions, inline load-bearing numbers per Houston standing.

### V-Web → T-Web rename completeness
- Status: **INCOMPLETE.** Title + 1 footnote only (R39conf v0.1.75). 175 occurrences remain in body.
- Specific sites: see P5 §B1 above.
- Action: DO-NOW one-commit sed-sweep, preserving artifact paths + audit-log comments.

### σ-mixing P4 abstract caveat
- VERIFIED in v1.0.186 abstract (L337). ChatGPT EXT10 did not re-raise. R39conf closure sufficient.

### Cramér's V P3 arithmetic
- ALREADY-CLOSED in v3.1.106 (.tex L913 value 0.0064 ✓). ChatGPT read stale v3.1.105.

### Zenodo / DOI placeholders (all 6 papers)
- STALE submission-day; bundle into single mint-and-replace commit at proof stage.

---

## Confidence summary

- 18/18 MINOR REVISIONS, zero MAJORs — the review program is structurally at ACCEPT-distance.
- Total VERIFIED-OPEN load-bearing edits across 6 papers: **≈38** (mostly 1-sentence wording fixes; P5 rename + P4 bibchimera are the largest).
- Total ALREADY-CLOSED-IN-R39CONF-FIX: **4** (P1A B2 sphaleron, P3 M2 Cramér's V, P3 audit-trail body-leak, P4 σ-mixing caveat).
- Total FALSIFIED: **1** (P2 ChatGPT M4 σ=0.36/0.93 source-tex check — not present).
- Total STALE submission-day: **≈10** (Zenodo / DOI / commit-pin across all 6).
- Total HOUSTON-DECISION → DO-NOW: **4** (P4 ℓ=2 1000-MC rerun, P4 A_95 finer-grid recomputation, P5 ASTRA confusion matrix, P3 NANOGrav BF γ-prior robustness table).
- Confidence in 1-cycle path to 18/18 ACCEPT: **HIGH**.
