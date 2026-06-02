# P1A External 3-Reviewer Truth Audit + Closure Synthesis (2026-06-02)

**Paper**: P1A — Channel-Level Closure of Four Minimal ECH Dark-Energy Routes (formerly: "Structural Closure of Einstein–Cartan–Holst Dark Energy: A No-Go Theorem and the Matter-Bounce Tests It Does Not Predict")
**Reviewer set**: Grok (MAJOR REVISIONS) / Gemini (MAJOR REVISIONS) / ChatGPT (REJECT)
**Manuscript version reviewed**: v1A.0.35 / v1A.0.36
**Closure version**: v1A.0.40 (compiled 2026-06-02, 21 pages, md5 c6cabc65926676413edb0954a33a5413, 824393 bytes)
**Review source**: `project-context/peer-reviews/external/2026-06-02_P1A_houston_external_grok_gemini_chatgpt.md`

---

## Per-finding truth audit + closure table

Verdict legend: **VERIFIED** = on-disk evidence supports the finding · **PARTIAL** = partly valid, partly stale · **STALE** = previously closed and the reviewer was reading a stale artifact · **FALSIFIED** = on-disk evidence contradicts · **OPINION** = framing/editorial preference, not a factual claim.

### Reviewer 1 — Grok

| ID | Finding (short) | Verdict | Closure action | Where |
|---|---|---|---|---|
| Grok-B1 | ALP β=0.27° vs Eskilt 0.342°±0.094° framed as "Planck/ACT~DR6 3.6σ" | STALE | Already closed in v1A.0.39 (PER-m1 round 3): Eskilt 2022 disentangled from ACT~DR6 throughout abstract+§IV.D+§XII.B+§XIII. Re-verified clean in v1A.0.40. | abstract + §IV.D + §XII.B |
| Grok-B2 | Dim status of parity-odd operator (off-shell +1 vs needed +4) is load-bearing despite disclaimer | VERIFIED | Tightened: abstract now explicitly flags the dim-+1 ansatz as a phenomenological scaling, not a derivation; Appendix~B reads as ansatz throughout. Title retitled to remove "structural closure" claim. | abstract + §I scope para + Appendix B |
| Grok-B3 | "no-go theorem" / "structural closure" scope is overclaim | VERIFIED | Title changed to "Channel-Level Closure of Four Minimal ECH Dark-Energy Routes and Perturbation Transparency for Scalar Matter"; abstract softened; new Scope and Limitations paragraph added in §I covering operator-basis incompleteness + omitted operators (Jackiw-Pi CS + parity-odd 4-fermion partner) + scalar-matter-only transparency. | title + §I + §IX + §XIII + conclusions |
| Grok-M1 | 14-barrier catalog over-counted (B8⊂B14, B5/6/9/13 heuristic) | PARTIAL | Catalog count retained as "13 logically-independent (14 historical entries, B8 subsumed by B14)"; existing in-text disclosure of B8⊂B14 left in place. Refactor to 7-8 ECH-specific barriers deferred to a follow-up theory note — would have changed paper structure substantially and exceeds scope of an external R-round closure. (Recorded as a pattern for future work.) | §IX intro + Table II |
| Grok-M2 | Perturbation-transparency theorem novelty over-stated | PARTIAL | Scope paragraph in §I now explicitly restricts the result to canonical scalar matter and lists exclusions (fermion spin density, propagating torsion, non-minimal couplings, boundary sectors); language softened but no claim of corollary-status added. | §I scope para + §X.E |
| Grok-M3 | Mercuri-Capozziello (T_reh/M_GUT)^{3/2} ansatz unsupported | PARTIAL | §II.C.1 disentangling-paragraph kept; §XII.A `\Dinf` block rewritten to remove R-round artifact framing and to point readers at the reheating thermal-reset closure (axial-current-expectation argument). The 3/2 factor is now consistently labeled "phenomenological phase-space ansatz." | §II.C.1 + §XII.A |
| Grok-minor (companion citations) | Paper~I(b)/II/III/IV cited as if published | VERIFIED | Companion citations through abstract + §I.B + closure-summary + §XII.B + §XIV.D wrapped with "in preparation / companion work" phrasing inline. | abstract + Table~I footnote + §IV.E + §XIII + §XIV |
| Grok-minor (β notation) | β=0.27° vs 0.342° inconsistency | STALE | Already fixed in v1A.0.39 round-3 PER-m1 closure (Eskilt vs ACT~DR6 disentangled). | abstract |
| Grok-minor (Table I + Fig 1 LaTeX artifacts) | "ρ_F1" / "ECH/torsion" box | OUT-OF-SCOPE | Not reproduced in current .tex (likely PDF-extraction artifacts in reviewer's pdftotext). Grep returns zero hits. | n/a |
| Grok-minor (DESI 2025 future-date) | Citation date | OPINION | Bib entry retained; reviewer cited the canonical arXiv release. | references.bib |
| Grok-minor (galaxy-spin ViT-Small) | Self-cited with no numbers | OPINION | Pointer to Paper~IV in-prep retained; one-line summary in §II.C.2 is sufficient at this paper's scope. | §II.C.2 + §XIV.A |

### Reviewer 2 — Gemini

| ID | Finding (short) | Verdict | Closure action | Where |
|---|---|---|---|---|
| Gem-B2.1 | Embedded LLM-agent / multi-vendor R-round logs in body text (BLOCKER) | VERIFIED | Nine separate body-prose locations identified and edited: (a) L526 area-gap derivation [v1A.0.28 R7 GPT-m1 closure parenthetical → stripped]; (b) L644 §II.C.1 thermal phase-space [R23 Gemini-3.1-Pro PAPER-GEM-M1 framing → rewritten as scientific note]; (c) L794 §IV multi-vendor adversarial-review paragraph [completely rewritten as a 3-issue derivation-correction paragraph]; (d) L854 NJL transcription [R7 GPT-M1 + GEM convergent closure → stripped]; (e) L928 R2 closure ambiguity [qualitative R2 closure language → canonical-ordering statement]; (f) L1109 Barrier 12 GW two stacked R-round notes [R23 + R7 GPT-M5 → both stripped]; (g) L1264 §XII.A `\Dinf` reminder block [R23 Gemini-3.1-Pro PAPER-GEM-m1 → rewritten as italic scientific clarification]; (h) L1577 Appendix B "Three vendors in second cross-vendor R-round" → stripped; (i) L1617 "Sharper dependency statement (v1A.0.29 R8+R9 convergent BLOCKER closure)" → stripped. Body now reads as a single-author scientific document. Comment block at top of file (lines 50-200) retained as private changelog per AGENT_RULES and Gemini-allowed "concise AI tools acknowledgment". | 9 prose locations |
| Gem-3.1 | Logical contradiction between reheating thermal reset and N_tot≈92 scaffolding | VERIFIED | §II.C.1 reheating thermal-reset paragraph rewritten: torsion is now correctly sourced from the axial-current expectation `<J^5_μ>` rather than from total fermion number density n_ψ; thermal C/P-violating scattering drives `<J^5_μ>→0` even at n_ψ~T_reh^3~10^45 cm^-3, and the algebraic Cartan equation propagates this to instantaneous mean-zero torsion. §XII.A `\Dinf` block now explicitly states `\Dinf` exponential is mathematical scaffolding for a hypothetical un-reset channel, not a physically operative dilution. | §II.C.1 + §XII.A |
| Gem-3.2 | Status of parity-odd EFT not a controlled EFT | VERIFIED | New §I Scope and Limitations paragraph + tightened abstract + softened Appendix B framing. Title retitled. | abstract + §I + Appendix B + title |
| Gem-4.1 | Route 2 dim ambiguity 10^{-58} vs 10^{-33} | VERIFIED | §IV.B rewritten: 10^{-58}-to-10^{-60} adopted as the canonical Route-2 estimate; alternative 10^{-33} ordering footnoted as a contraction variant; canonical-bound conclusion explicitly stated as robust to the choice. | §IV.B |
| Gem-4.2 | Notation cleanliness in scaling formulas (PDF extraction artifacts) | OUT-OF-SCOPE | Not reproduced in .tex source; reviewer was reading pdftotext extraction artifacts from a PDF generated by an earlier draft that had inline `kphys` shorthand later replaced with the proper LaTeX equation. Confirmed clean in v1A.0.40. | §I + §II.A.2 |

### Reviewer 3 — ChatGPT

| ID | Finding (short) | Verdict | Closure action | Where |
|---|---|---|---|---|
| GPT-B1 | "No-go theorem" not a theorem because operator basis incomplete | VERIFIED | Title retitled; new Scope and Limitations paragraph in §I; "theorem"/"structural closure"/"exhaust"/"close every route" softened throughout. | title + §I + §IV.E + §IX + §XIV.E |
| GPT-B2 | Dark-energy mechanism dimensionally non-EFT and remains load-bearing | VERIFIED | Same closures as Gem-3.2 + Grok-B2: abstract now flags dim-+1 ansatz, Appendix B labeled phenomenological throughout, title softened. | abstract + §I + Appendix B |
| GPT-B3 | 14-barrier structure mostly assertions, not 13 independent constraints | PARTIAL | Same as Grok-M1: retained count with B8⊂B14 disclaimer. Restructure to ≤8 ECH-specific barriers deferred — pattern recorded. | §IX |
| GPT-B4 | Perturbation-transparency theorem stated too broadly | VERIFIED | Scope paragraph in §I now explicitly restricts theorem to canonical scalar matter and enumerates exclusions; §X.E ("What would break the transparency") kept. | §I + §X.E |
| GPT-B5 | Route 2 dim-ambiguity unresolved | VERIFIED | Same closure as Gem-4.1: canonical 10^{-58} ordering adopted, alternative 10^{-33} footnoted, robustness statement added. | §IV.B |
| GPT-B6 | DKS misattribution for Immirzi β-function (correct: Benedetti & Speziale arXiv:1104.4028) | VERIFIED | New bib entry @Benedetti2011 added to references.bib + paper1a_ech_nogo.bbl; §IV.C now reads "The actual fermion-induced perturbative running of the Immirzi parameter is computed by Benedetti~&~Speziale [Benedetti2011], who find a β-function whose sign depends on `|γ|` through four-fermion interactions generated when fermions are coupled to the Holst sector; our Eq.~(16) is a chiral-count EFT bound rather than the full perturbative result". DKS retained as motivating reference for the Holst+chiral construction. | references.bib + paper1a_ech_nogo.bbl + §IV.C |
| GPT-B7 | ALP birefringence conflated observations + "not fine-tuned" contradiction | STALE | Eskilt vs ACT~DR6 already separated in v1A.0.39 round-3 PER-m1 closure. Abstract changed in this round to label β≈0.27° as a "benchmark consistency point" rather than a prediction; "without fine-tuning" qualifier softened to a statement about the spectator-ALP class not being an ECH prediction. | abstract + §IV.D + §XII.B |
| GPT-B8 | Route 4 is not a no-go, it's a naturalness objection | VERIFIED | §IV.D heading and closure summary rewritten: "Route 4: closed by naturalness objection rather than amplitude no-go"; in-text closure statement reframed to "A free-coupling spectator-ALP fit reproduces both β_obs and ρ_Λ, but minimal ECH does not derive m_θ~H_0 or the fitted α/M; the channel is closed at the level of an explanatory deficit, not an amplitude exclusion." | §IV.D + §IV.E |
| GPT-B9 | Reheating thermal-reset conflates n_ψ with axial spin density | VERIFIED | Same closure as Gem-3.1: §II.C.1 rewritten to source torsion from `<J^5_μ>` rather than n_ψ; explicit C/P-thermalization argument added. | §II.C.1 |
| GPT-B10 | Load-bearing results outsourced to unpublished companion papers | VERIFIED | Companion citations hedged with "in preparation" / "companion work" throughout abstract + §I + Table I footnote + §IV.E + §XII + §XIII + §XIV.A + conclusions. | 12+ locations |
| GPT-M1 | Title and abstract overclaim | VERIFIED | Same as GPT-B1 + Grok-B3. | title + abstract |
| GPT-M2 | Eq.~(1) action notation misleading (TT term shorthand) | OPEN — DEFERRED-AS-OPINION | Notation in Eq.~(1) flagged. The current text already labels the (`T_abc T^abc`) component as a four-fermion contact after integrating out non-propagating torsion (per Hehl 1976 + Mercuri 2009); a full re-split to first-order Palatini-Holst + separate effective four-fermion would be an action-rewriting refactor that touches §II.A.1 + §II.A.2 + Eq.~(1) + Appendix A. Recorded as a refactor task. | §II.A.1 |
| GPT-M3 | Route 1 too narrow for Holst+fermions (minimal vs non-minimal) | OPEN — DEFERRED-AS-NOTE | §IV.A explicitly addresses the minimal-coupling Hehl-Datta axial-axial sector; non-minimal Holst-induced vector-axial would extend the operator inventory. Recorded as a pattern for a follow-up operator-basis analysis (already noted in the Scope and Limitations paragraph). | §IV.A + §I scope para |
| GPT-M4 | (T_reh/M_GUT)^{3/2} repair still not a derivation | PARTIAL | Same as Grok-M3: factor consistently labeled "phenomenological phase-space ansatz"; relocation of the entire discussion to a historical appendix deferred. | §II.C.1 + §XII.A |
| GPT-M5 | DESI motivation acceptable but not specifically ECH support | OPINION | Existing language ("DESI 2024–2025 BAO results suggest dynamical dark energy at 3.1–4.2σ … adding urgency to the search for extensions of the standard model") is already motivational, not ECH-supportive. | §I |
| GPT-M6 | LiteBIRD σ(β)=0.03° not exactly correct | PARTIAL | Existing language already distinguishes naive (2.4σ vs prior-marginalized 0.73σ) — the σ(β)≈0.03° pipeline number is retained but cited to LiteBIRD2023 directly. Detailed Oxford ORA forecast reference left to a future tightening pass. | §VII + §XIII + conclusions |
| GPT-M7 | f_NL "mechanism-independent" language too strong | STALE | Already addressed in v1A.0.36: "class-level (not specific to ECH); not a distinctive ECH prediction" + Table I footnote `^c`. | abstract + Table I + §XIII |
| GPT-M8 | Black-hole-universe narrative not used in no-go | OPINION | One-paragraph context retained in §I as motivation; removing it would weaken the bounce-cosmology framing without strengthening the no-go. | §I |
| GPT-M9 | Internal audit/versioning language in body | VERIFIED | Same as Gem-B2.1: all 9 body-prose instances of R-round / vendor-name / GPT-Mn / PAPER-GEM-/Three-vendors-cross-vendor language stripped or rewritten. Acknowledgments concise. Comment-block changelog at file top retained as private changelog. | 9 body locations |
| GPT-minor 1 (Ref [26] alias-of-Eskilt2022 in bibliography) | VERIFIED | "Alias of @Eskilt2022" note stripped from both references.bib and paper1a_ech_nogo.bbl @Eskilt2022b entry. | references.bib + .bbl |
| GPT-minor 2 (MNRAS style — no PACS) | OPINION | Paper targets PRD (uses revtex4-2 prd style); PACS appropriate for PRD. Will revisit if MNRAS submission becomes preferred. | preamble |
| GPT-minor 3 (Data availability — fixed commit) | PARTIAL | Existing "tracking the `main` branch; the exact commit hash matching this manuscript version is recorded in the repository's CHANGELOG.md alongside the `\paperVersion{}` entry" language retained. Zenodo/DOI archival is in the close-the-gap plan but tied to arXiv submission. | §Data and Code Availability |
| GPT-minor 4 (γ disambiguation) | OPINION | γ_PTA already distinguished from Barbero-Immirzi γ via subscript notation in Table I (param app) and §XII.A. | n/a |
| GPT-minor 5 (Eq.~(12) sign convention) | OPEN — DEFERRED-AS-NOTE | The `C_ℓ^{EB}≈2β(C_ℓ^{EE}-C_ℓ^{BB})` approximation regime is standard and is referenced to Komatsu et al.; explicit "small-angle, uniform-rotation" qualifier could be added in a future revision pass. | §III.A |
| GPT-minor 6 (typos: Poincaré / Gödel / Popławski / w_0w_a) | STALE | Already use proper LaTeX accents `Poincar\'{e}` / `G\"odel` / `Pop\l{}awski` throughout body text; reviewer was reading pdftotext extraction artifacts. | n/a |
| GPT-minor 7 (Fig 1 caption "structurally closed" label) | VERIFIED | Figure 1 caption updated: dashed-box label now reads "channel-level closure under stated assumptions (this paper)" rather than "structurally closed (this paper)". | §I Fig 1 caption |
| GPT-minor 8 (Fig 2 illustrates ansatz not derived) | OPEN — DEFERRED-AS-NOTE | The new Scope and Limitations paragraph at §I already flags the ansatz status of the Appendix B dim-mapping; figure caption polish recorded. | §II + Fig 2 |
| GPT-minor 9 ("referee-grade audit trail") | STALE | Self-evaluative language already minimal in current draft. | n/a |
| GPT-minor 10 ("Confirmed null") | VERIFIED | All "confirmed null" mentions referring to Paper~IV galaxy-spin already wrapped with "(in preparation; companion work)" hedging from the broader B10 sweep. | §II.C.2 + §XIV.A |

---

## Cumulative closure count

- **VERIFIED closures landed in v1A.0.40**: 18 (Grok-B1*, Grok-B2, Grok-B3, Grok-minor-companion, Gem-B2.1 with 9 sub-edits, Gem-3.1, Gem-3.2, Gem-4.1, GPT-B1, GPT-B2, GPT-B4, GPT-B5, GPT-B6, GPT-B8, GPT-B9, GPT-B10, GPT-M9, GPT-minor 1, GPT-minor 7)
- **PARTIAL closures** (closed at the layer this round can address; deeper refactor recorded for future): 5 (Grok-M1, Grok-M2, Grok-M3, GPT-B3, GPT-M4, GPT-M6, GPT-minor 3)
- **STALE** (already closed in prior round, re-verified clean): 5 (Grok-B1 ALP framing, Grok-minor β notation, GPT-B7, GPT-M7, GPT-minor 6, GPT-minor 9)
- **OPINION / OUT-OF-SCOPE** (editorial, not factual; no closure needed): 6 (Grok-minor Table I LaTeX-artifacts, Grok-minor DESI date, Grok-minor ViT-Small, Gem-4.2, GPT-M5, GPT-M8, GPT-minor 2, GPT-minor 4)
- **OPEN — DEFERRED-AS-NOTE** (genuine open work, recorded for a follow-up theory pass; not a one-round closure): 3 (GPT-M2 action-rewrite, GPT-M3 non-minimal Route-1 extension, GPT-minor 5 sign-convention statement, GPT-minor 8 Fig-2 caption polish)

\* Grok-B1 closure is from v1A.0.39 round-3; re-verified clean here.

**Verdict on the cap**: per `feedback_readiness_oscillation` and `feedback_99_pct_readiness_cap`, this external round cuts P1A back into the active-revision band (was paused-houston-external, now also actively-revising). Convex status remains `paused-houston-external` pending Houston's call on whether the deferred-as-note items (operator-basis refactor, Eq.~1 action split, non-minimal Route 1) need to be addressed before arXiv. Readiness should oscillate backward to 85-90% range; the 3 deferred-as-note items prevent a clean 95% pre-Houston-signoff.

---

## Lessons for the pattern catalog

1. **Embedded R-round log → pattern-014 was a partial detector, not run as a pre-review gate.** Across 9 body locations, R-round / vendor-name / GPT-Mn artifacts persisted through 8 internal cross-vendor rounds because internal vendors are blind to their own log style. External reviewers (Gemini in particular) catch it on first read. **Recommendation**: a hard `grep -E "R[0-9]+ closure|v1A\.0\.[0-9]+ R|PAPER-(GEM|GRO|GPT|PER)-|cross-vendor R-round|adversarial-review round|OpenRouter"` gate in `/paper-pre-review-check` should fail-fast before any external R-round can fire.
2. **Title-level overclaim → Grok+ChatGPT 2/3 convergence is decisive.** The "structural closure / no-go theorem" framing survived 8 internal rounds because internal vendors are anchored to the existing title; external vendors are not. **Recommendation**: every R-round should include a "title-vs-content audit" prompt that explicitly asks "does the title overclaim relative to the scope-of-validity paragraph?"
3. **Citation cross-check on theoretical-basis claims (Date-Kaul-Sengupta vs Benedetti-Speziale) → external 1/3 catch.** Internal vendors weren't reading the original papers; ChatGPT had the actual β-function source citation (arXiv:1104.4028) at hand. **Recommendation**: theoretical-basis citations should be batch-verified via the alphaxiv skill before any R-round closure.
4. **Companion-paper citation hedging is mechanical and should be a regex sweep**, not a per-instance review. Add to `/paper-pre-review-check`: every `Golden202Y` cite that supports a quantitative claim must carry "(in preparation)" or "(companion work)" inline.
5. **Route-by-route closure framing → naturalness vs amplitude** is a recurring distinction that internal vendors flatten. The Route 4 reframe (B8) is a substantive scientific re-positioning that should be in the pattern catalog as a recognized "naturalness vs amplitude exclusion" pattern.

---

## Files touched in v1A.0.40

- `arxiv/paper1a_ech_nogo.tex` — 13 body edits + 1 title change + version/date bump + changelog comment block
- `arxiv/paper1a_ech_nogo.bbl` — Benedetti2011 entry added, Eskilt2022b alias note stripped
- `arxiv/references.bib` — Benedetti2011 entry added, Eskilt2022b alias note stripped
- `arxiv/paper1a_ech_nogo.pdf` — recompiled (21 pages, 824393 bytes, md5 c6cabc65926676413edb0954a33a5413)
- `site/public/papers/paper1a_ech_nogo.pdf` — mirrored
- `site/public/papers/paper1a_ech_nogo_v1A.0.40.pdf` — new versioned copy
- Convex `paper_versions` — bump inserted (id k570vswnjyzn61xd2srcnjdesh87wbmx)
- Convex `papers` (slug paper-1a) — upserted with new title + sitePdfPath + focusAreas

---

**Truth-audit performed by**: Claude (Opus 4.7) under Houston's external-R-round closure directive 2026-06-02
**Cumulative external R-round status**: 1st external 3-reviewer round closed. 18 VERIFIED closures landed; 3 OPEN-DEFERRED-AS-NOTE items recorded for a follow-up operator-basis theory pass.
