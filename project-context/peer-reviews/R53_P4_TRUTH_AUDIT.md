# R53 P4 — Truth Audit (verdict-first vs source)

**Paper:** P4 — "Survey-Scale Galaxy Chirality with Equivariant TTA" (chirality catalog)
**Round:** R53 convergence pass · **Prior state:** ACCEPT (held since R52+EXT21/22)
**PDF:** /tmp/R53_P4/chirality_catalog_paper.pdf · 23pp · md5 b716a574 · compile 0 undef refs, 0 overfull hbox
**Legs returned:** 3/4 PDF-native (Grok grok-4.3, Gemini gemini-2.5-pro, OpenAI gpt-5-2025-08-07) + Claude/Opus full-read leg.
**Legs failed:** Perplexity (401 insufficient_quota — billing, not a paper issue).

## Net vendor verdicts
- **Gemini:** ACCEPT WITH MINOR CORRECTIONS (no BLOCKER)
- **Grok:** MINOR REVISIONS (no BLOCKER)
- **gpt-5:** MAJOR REVISIONS — but every ESSENTIAL falsified or scope/blocked (below)
- **Claude/Opus leg:** ACCEPT — full arithmetic re-derivation clean (see calibration)

## Verdict-first audit of every finding

### VERIFIED — DO-NOW (closed this round)
- **Gemini P4-N1 (NIT, arithmetic):** Intro/parity text said Shamir exclusion factor "~6–12" but the paper's own stated inputs (0.32% WLS vs 1.7%–4.0%) give 1.7/0.32=5.31 and 4.0/0.32=12.5 → range 5.3–12.5. Lower bound "6" mis-rounds 5.31. **VERIFIED** (self-inconsistency vs own arithmetic). **Closed:** L365 + L754 `$\sim\!6$--$12$` → `$\sim\!5$--$12$` (corrected lower bound; upper 12 retained = conservative rounding of 12.5, understates exclusion). Changelog comment L73 left as historical audit-trail.

### FALSIFIED (false positives — verified against source)
- **gpt-5 P4-E1 / recurring "+3.64σ vs +7.93σ should not shift 2× from NMC":** FALSIFIED. Source declares these are DIFFERENT estimators: +3.64σ = 500-MC direct-MC on the full A_p field; +7.93σ = 10⁴-perm on the canonical-unapodized **A_p/2 half-scaled** field with N_spiral-weighted subtraction (Sec. notation, Table III caption, App. A.a). gpt-5's premise ("mask/field/subtraction identical") is false. Same FP truth-audited in many prior rounds.
- **gpt-5 P4-E6 (Table III z ≠ displayed inputs):** FALSIFIED. Apodized ℓ=1 (24.74−1.93)/3.12 = 7.31 = printed exactly. Canonical ℓ=1 +7.93 requires σ_null=6.70/7.93=0.845, which rounds to displayed 0.84; [2,6] +4.20 consistent with σ=0.205→display 0.20. Caption explicitly states z is from full-precision arrays, not the 2-sig-fig display. Deriving z from rounded display is exactly the artifact the caption preempts.
- **gpt-5 P4-E7 (App A.c 2.30e-5→1.51e-5 "stale"):** FALSIFIED. Those are the +3.64σ 500-MC canonical full-A_p estimator's pre/post-monopole-subtraction C₁ (paragraph explicitly says "(the canonical-mask number)", 500 perm null, seed 42; 1−1.51/2.30=0.343 ✓ "~34%"). Distinct from Table III's 10⁴-perm A_p/2 rows by declared convention — not an inconsistency.
- **gpt-5 P4-E8 ("~12%" unproven):** FALSIFIED. gpt-5's 7.8% uses the label-shuffle null rows in Table III; the 12% is the MASTER-decoupled **monopole-only generative** null mean (artifact master_decoupled_monopole_null.json), a different null. Wrong-null comparison.
- **gpt-5 P4-E4 / n1 (URL "galaxy- chirality- catalog" stray spaces):** FALSIFIED. Source L1010 is clean `galaxy-chirality-catalog`; the spaces are xurl hyphen line-breaks in the rendered PDF, hyperlink target intact.
- **Grok P4-E1 (abstract +0.41σ lacks "not comparable" qualifier):** FALSIFIED. Abstract already contains the verbatim qualifier ("…arise from distinct null procedures and are diagnostic-only, not directly comparable as detection significances").
- **Grok P4-E2 (move 99.32% into abstract):** FALSIFIED. Abstract already states "a monopole-only generative null reproduces 99.32% of the raw pre-MASTER ℓ=1 power."
- **Grok P4-M2 (Table III lacks "not comparable" caption):** FALSIFIED. tab:multipole caption already says "z values are relative to each row's own null and are not comparable across rows, footprints, or with the real-space dipole."
- **Grok P4-N3 ("June 13 2026" is a future date):** FALSIFIED. Today is 2026-06-26; the paper timestamp is in the past. Reviewer knowledge-cutoff artifact.
- **gpt-5 P4-M1 (2.98× suppression ignores sign flip):** FALSIFIED as defect. Signed values shown explicitly (+1.576% → −0.529%; +0.788% → −0.265%); sign reversal is on the page. At most a wording nicety.

### TRULY-BLOCKED (submission-gated; not closeable this round)
- **Gemini P4-M1 / gpt-5 P4-E4 / P4-M8 (Zenodo persistent DOI; baseline-ready release file):** Submission-gated. Paper already discloses the pending-DOI status and the QC-flag filtering instruction transparently. Deferred to journal-submission per directive.
- **Gemini P4-E1 / gpt-5 P4-E5 (finalize commit hash):** 53b41d12 is the real pinned \artifact commit; final hash advances at submission restamp. Blocked.

### OPINION / OUT-OF-SCOPE (no defect)
- gpt-5 E2/E3, Grok N2 (in-body \artifact paths): deliberate reproducibility-hyperlink convention; dispositioned as style across all P4 rounds.
- gpt-5 M2–M7, M9–M12, m1–m15, n2–n3; Grok M1/M3/N1: clarity/enhancement/derivation requests on an already-exhaustively-hedged manuscript. M12 (parity-even derivation) deliberately NOT fabricated — /never-fabricate-derivation; the scoping statement is standard and defensible.

## Claude/Opus leg — independent arithmetic re-derivation (all PASS)
- GZ1 confusion matrix totals 240,919 ✓; row sums 71,615/73,025/96,279 ✓
- Chirality accuracy 81,939/117,205 = 69.91% ✓; per-class CW 67.4% / CCW 72.4% ✓
- 3-class accuracy diagonal 141,438/240,919 = 58.7% ✓; precision/recall all match
- NS triage 27,435/144,640 = 19% ✓
- Catalog C dev (0.497353−0.5)/2.795e-4 = −9.47σ ✓; Raw A +28.7σ ✓
- Asymmetry suppression |1.576/0.529| = 2.98× ✓ (sign-reversed)
- Fisher 2√3·σ(f_CW) = √(3/N) = 9.68e-4 ≈ 9.7e-4 ✓
- f_sky 24,087/49,152 = 0.49005 ✓
- Shamir factor (fixed): 1.7/0.32=5.31, 4.0/0.32=12.5 → "~5–12" ✓

## CONVERGENCE STATEMENT
P4 **HOLDS at ACCEPT.** Three PDF-native vendors converge on no-BLOCKER (Gemini ACCEPT, Grok MINOR, gpt-5 MAJOR-but-all-ESSENTIALs-falsified). All gpt-5 "arithmetic" ESSENTIALs (E1/E6/E7/E8) are the recurring estimator-convention / display-rounding / wrong-null false positives, re-falsified here against source. One genuine NIT-tier self-consistency defect (Shamir factor lower bound 6→5) found by Gemini and independently by Claude-leg arithmetic — closed surgically. Recompile clean: 0 undef refs, 0 overfull hbox >50pt, 23pp unchanged. Remaining open items are all Zenodo/DOI/commit-hash submission-gated (TRULY-BLOCKED). No fabrication, no false-positive "fixes." Convergence achieved — 1 verified MINOR closure, 0 BLOCKERs, paper ready to remain at ACCEPT.
