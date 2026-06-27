# R52 P5 — Peer-Review Truth Audit (Opus judgment leg)

**Paper:** P5 — "Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with T-Web (Hahn 2007) Tidal-Tensor Cross-Check."
**Reviewed PDF:** `p5_desi_chirality_v0.1.82-2026-06-18.pdf` (md5 401a73f9, 32 pp).
**Source .tex:** `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex` — now at **v0.1.83-2026-06-19** (one patch AHEAD of the reviewed PDF; v0.1.83 = D-round visual polish, "no science change" per changelog line 37). Findings are judged against v0.1.82 content but two are already STALE-closed by the in-tree v0.1.83.
**Date / calibration:** June 2026. arXiv 25xx/26xx valid; deliberate companion placeholders allowed; extraction-mangled math is not a real defect; catalog/methodology extensiveness is not a defect.

---

## 0. Reviewer recommendations — AS ACTUALLY WRITTEN IN-TEXT

The dispatch brief mislabeled OpenAI and Gemini as "accept." Their in-text Recommendation lines say otherwise:

| Reviewer | Brief label | **Actual in-text Recommendation** |
|----------|-------------|-----------------------------------|
| Claude_subagent | MINOR | **MINOR REVISIONS** (line 3) |
| Grok_brutal | REJECT | **REJECT** (line 46) |
| OpenAI_methodology | accept | **MAJOR REVISIONS** (line 126) |
| Gemini_cosmology | accept | **MAJOR REVISIONS** (line 92) |
| Perplexity_citations | accept | **CALL FAILED** — 401 insufficient_quota; no review produced |

Real distribution: 1 MINOR, 2 MAJOR, 1 REJECT, 1 dead. The two MAJORs + REJECT **converge on one ESSENTIAL**: the Paper IV dependence. That convergence — not Grok's REJECT — is the substantive signal of this round.

---

## 1. Net verdict

**P5 HOLDS. No BLOCKER. No fatal finding.** The science conclusion (environment-independence of spiral chirality, carried by the monopole-independent cross-class Δf_CW contrast, n=56,981, z=+0.31, p=0.76) is intact, reproducible (Claude leg reconciled Tables III/IV/V/VIII/X/XII/XVI/XVII to committed JSON), and the lone small-N weakness (n=428 T-Web void) is explicitly superseded by the 56,981 DESIVAST anchor.

The round's real work is **two MAJOR DO-NOW items** (Paper IV reframing; density-metric definition reconciliation) plus a handful of MINOR presentation polish. Grok's REJECT is a **false positive** built on a primary/secondary inversion.

### VERIFIED counts by tier
- **BLOCKER: 0**
- **MAJOR: 2** — (V1) Paper IV framing / self-containedness; (V2) Table V density-metric ρ̄ log10-vs-linear definitional mismatch (OpenAI E6).
- **MINOR: ~7** (presentation cluster) — version-history strings in body; σ-comparability caveat consolidation; membership-count footnote; ASTRA n≥100 filter clarity; k=20-vs-exact count labels; design-effect CI justification; assorted caption pointers.
- **DO-NOW-at-submission (deliberate placeholder): 1** — archival DOI (OpenAI E2).
- **STALE (already fixed in in-tree v0.1.83): 2** — Fig 8 colorbar overlap (Claude M5); Table VII dagger undefined (OpenAI M2).

---

## 2. Deduped findings — verdict each

### VERIFIED

**V1 — Paper IV dependence / framing.** (OpenAI E1 ESSENTIAL, Gemini E1 ESSENTIAL, Claude M2 MINOR, Grok N1 MINOR.)
The Δf_CW = −0.0026 catalog-wide monopole subtracted in every σ_pred is sourced from Paper IV ("in preparation"), and the per-galaxy CW/CCW labels themselves come from Paper IV's catalog. Three reviewers flag it; two call it publication-blocking.
*Adjudication:* VERIFIED as a real **framing / self-containedness** weakness, **MAJOR**, **DO-NOW** — but NOT a science BLOCKER, for two source-grounded reasons: (a) the headline lives in the cross-class **two-sample Δf_CW contrast, which is mathematically monopole-independent** (.tex line 1114: "the void-vs-non-void contrast Δf_CW, whose two-sample [SE]…"); the monopole only enters the interpretive σ_pred. (b) The **internal matched-sample monopole is already computed and displayed in-paper** — fP5CW = 0.49719 on 812,793 rows, residuals in Table XII (OpenAI E1 itself notes this). So the dependence is removable by reframing with zero new computation.
*Gemini's stronger claim* ("cannot be published until Paper IV is accepted") is OVER-STRICT / OPINION: calibration permits a deliberate companion, and the internal monopole already removes the load-bearing reliance.

**V2 — Table V density metric: log10 vs linear (OpenAI E6 ESSENTIAL→treat MAJOR).**
Caption (line 1443-1444) and §IV A step 12 (line 904) state ρ̄ = quartile mean of **log10(1+δ_smooth)**. The displayed values — cluster Q1/Q4 = 1.55/2.21, filament Q1/Q4 = 0.90/1.86 (lines 1459-1466) — are physically consistent with **linear (1+δ)** at 25 Mpc/h Gaussian smoothing (δ ≈ −0.1…+1.2), not log10 (which would imply δ ≈ 7…160, implausible at that smoothing). The body's class-overlap argument (lines 1491-1494) uses these magnitudes directly.
*Adjudication:* VERIFIED — a genuine internal **definition-vs-displayed-value** contradiction. **MAJOR** (correctness-of-record; a PRD referee correctly caught it), but **DO-NOW trivial** and **changes no conclusion** (stratification ordering is invariant). Fix = state explicitly whether ρ̄ is linear (1+δ) or log10(1+δ), and reconcile step-12 wording with the table.

**V3 — Version-history strings in scientific body (OpenAI E3, partial).** "Paper IV's current headline (v1.0.166)" (lines 686, 691); "earlier preprint versions used 'V-Web'" (title footnote, lines 437, 815). VERIFIED present. **MINOR** — PRD prefers stable cites; scrub companion version strings from narrative (the `\paperVersion` use in Appendix C reproducibility note, lines 3591/3630, is an allowed release note). Non-load-bearing.

**V4 — σ-from-half non-comparability caveat repeated inconsistently (Claude M7).** Caveat genuinely appears in Tables III/V/VI/IX/XIII captions + §V. VERIFIED **MINOR** — consolidate to one canonical §V statement + cross-refs. (NB: directly contradicts Gemini m3, which wants it removed as confusing — see OPINION.)

**V5–V8 — OpenAI pass-2 presentation MINORs.** Two membership-count layers footnote (Claude M6); ASTRA n≥100 filter made explicit in Table XIV (OpenAI M5); k=20-vs-exact count labels in Table VIII (OpenAI M6); Jeffreys-CI design-effect justification on duplicate rows (OpenAI M7). All VERIFIED **MINOR**, DO-NOW caption/footnote edits; none alters a conclusion.

### DO-NOW-AT-SUBMISSION (deliberate placeholder)

**D1 — Archival DOI (OpenAI E2).** Line 3605: "A DOI-minted archival snapshot … accompanies journal submission." No DOI yet. Paper is pre-submission; this is a deliberate placeholder (the ASTRA companion already carries a real Zenodo DOI 10.5281/zenodo.19358024, line 3048). Mint + insert the P5 DOI at submission. Not a current science defect.

### STALE (fixed in in-tree v0.1.83, post-PDF)

**S1 — Fig 8 colorbar collision (Claude M5).** v0.1.83 changelog: "Fig 8 healpix skymap → 2-panel (count + sigma) with separate colorbars (overlap fixed)." CLOSED.
**S2 — Table VII dagger undefined (OpenAI M2).** v0.1.83 changelog: "Table VII caption dagger defined." CLOSED.

### FALSIFIED

**F1 — Grok E1 (ESSENTIAL): title "56,981 Void Spirals" misleading; real test is n=428.** FALSIFIED. 56,981 is the **DESIVAST VoidFinder primary void-spiral sample** (.tex lines 401, 444, 517; Table X row line 2283: VoidFinder n=56,981, f_void=0.4964, Δf_CW=+0.0007, z=+0.31). The n=428 is the T-Web **secondary** bin. Grok inverted primary and secondary; the title accurately names the primary sample.

**F2 — Grok E2 (ESSENTIAL): headline carried by n=428 (1σ floor ≈2.4pp).** FALSIFIED. The headline is the 56,981 DESIVAST contrast; the 428 bin is explicitly superseded (Claude leg; .tex §VIII). Same inversion as F1.

**F3 — Grok E3 (ESSENTIAL): no "not directly comparable" σ qualifier at every juxtaposition.** FALSIFIED. Qualifier appears in Tables III/V/VI/IX/XIII captions and §V text; Gemini m3 even argues it is OVER-stated. At most a polish nit (→ V4), not a missing control.

**F4 — OpenAI E4 (ESSENTIAL): Clopper-Pearson "1 − 0.05 1/6 = 39%" algebra wrong.** FALSIFIED — PDF extraction artifact. Source line 2098 reads `$1 - 0.05^{1/6} = 39\%$` with correct braces (1 − 0.6070 = 0.393 ≈ 39%). Identical false positive adjudicated in R34 (documented .tex lines 191-194).

**F5 — Gemini m1 (MINOR): Table IV Quintile-3 residual sign error (+1.87 should be −1.87).** FALSIFIED. Table IV column is explicitly `$|\sigma_{\rm obs}-\sigma_{\rm pred}|$` (line 1397), an absolute value; |−3.94 − (−2.07)| = 1.87 is correct. Gemini misread an abs-value column as signed.

**F6 — Gemini m2 (MINOR): Table VIII sign convention inconsistent with Table X.** FALSIFIED. Both use the same explicitly-stated convention Δf_CW ≡ f_non-void − f_void (lines 544-545, 2270, Table X row 2283: 0.4971 − 0.4964 = +0.0007). The paper even warns against the opposite sign (lines 2385-2387). Convention is uniform and stated.

**F7 — Grok M2 (MAJOR): RSD makes the DESIVAST flagship weaker than claimed.** FALSIFIED / OUT-OF-SCOPE. DESIVAST VoidFinder holes are defined by the void-finder directly and do **not** use the tidal field; the RSD caveat applies to the T-Web path and is carried prominently (Claude M1). For a null, RSD dilutes rather than manufactures signal → the bound is conservative.

**F8 — Grok M3 (MAJOR): Fig 3 over-weights the void bin.** FALSIFIED/OPINION. Non-comparability is flagged and the Jeffreys CI is shown honestly bracketing parity; nothing treats the 428 bin as decisive.

### OPINION / OUT-OF-SCOPE (editorial; no edit required)

- **Length, 32 pp for a null** (Grok M1 MAJOR, Gemini M2 MAJOR, OpenAI z1 NIT): OPINION. Calibration: catalog/methodology extensiveness is not a defect. Condensation optional, not required.
- **Restructure to present DESIVAST primary first** (Gemini M1 MAJOR): OPINION — legitimate editorial preference; current order (T-Web context → DESIVAST primary) is defensible. Not a correctness issue.
- **Abstract should lead with χ²=3.00 unique-spiral / compress** (Gemini m4, Claude M3): OPINION — both statistics are reported; lead choice is editorial.
- **Remove/keep σ-comparability sentence** (Gemini m3 vs Grok E3): reviewers directly contradict; resolved by V4 (consolidate, don't delete).
- **OpenAI M1 (h⁻¹Mpc vs Mpc/h), M3 (preprint-softening), E5 (pre-registration wording), n1–n12 NITs**: low-severity presentation; fold into the MINOR polish pass at author discretion.

---

## 3. Grok REJECT adjudication — reason by reason

| Grok reason | Tier claimed | Verdict | Basis |
|-------------|--------------|---------|-------|
| E1 title misleading (56,981 vs 428) | ESSENTIAL | **FALSIFIED** | 56,981 = DESIVAST primary (lines 401/444/2283); 428 = secondary |
| E2 headline carried by n=428 | ESSENTIAL | **FALSIFIED** | headline = 56,981 contrast; primary/secondary inverted |
| E3 σ-comparability qualifier absent | ESSENTIAL | **FALSIFIED** | qualifier present in 5 table captions + §V |
| M1 32-page length | MAJOR | **OPINION** | extensiveness not a defect (calibration) |
| M2 RSD weakens flagship | MAJOR | **FALSIFIED/OOS** | VoidFinder holes don't use tidal field; RSD dilutes |
| M3 Fig 3 over-weights void | MAJOR | **OPINION** | non-comparability flagged; CI honest |
| N1 Paper IV recap | MINOR | **VERIFIED** (→V1) | real, but Grok itself ranks it only MINOR |
| N2 over-precise digits | MINOR | **OPINION/NIT** | cosmetic |
| NIT1-3 typos / "the the" | NIT | cosmetic | low priority |

**Disposition: FALSE-POSITIVE REJECT.** Every ESSENTIAL and MAJOR reason is FALSIFIED or OPINION. The verdict rests entirely on a **primary/secondary inversion** — Grok treated the n=428 T-Web void bin as the paper's headline when the paper's headline is the n=56,981 DESIVAST cross-class contrast. Consistent with the prior P1A/P5 Grok-outlier pattern. The only load-bearing concern Grok raises (Paper IV, N1) it ranks merely MINOR — i.e., even Grok's own report does not support REJECT.

**Strongest single falsifying evidence:** `.tex` line 401 (title) + line 444 ("DESIVAST primary: 56,981 k=20 VoidFinder void spirals") + Table X row line 2283 (VoidFinder n=56,981, Δf_CW=+0.0007, z=+0.31, p=0.76) jointly establish that 56,981 is the primary headline sample, not a "secondary re-projection."

---

## 4. CLOSURE PLAN

### MAJOR — DO-NOW

**C1 (V1, Paper IV framing).** §II + §V + Abstract.
- *Current:* "the known Paper IV catalog-wide classifier-monopole systematic of ≈0.26 pp … is subtracted"; "Paper IV establishes the catalog-wide CW-fraction monopole as a classifier-residual bias."
- *Proposed:* Lead with the **internal** matched-sample monopole fP5CW = 0.49719 (Δf = −0.0026 on 812,793 rows; residuals already in Table XII) as the reference subtracted in σ_pred; demote Paper IV to corroborating context ("consistent with the independent estimate of [3]"). Add one sentence: "The environment-independence headline is the two-sample Δf_CW contrast, which is invariant under any catalog-wide monopole; if the Paper IV (or internal) monopole value shifts, the σ_pred rows (Tables IV/V/XII) move with it while the Δf_CW null does not." Remove "known … classifier systematic" framing unless peer-reviewed-citable.
- Tier: **MAJOR**, DO-NOW. No new computation (internal monopole already in-paper).

**C2 (V2, density metric).** Table V caption (line 1443-1444) + §IV A step 12 (line 904).
- *Current:* "ρ̄ is the quartile mean of log10(1+δ_smooth)."
- *Proposed:* Confirm against the pipeline which quantity the displayed ρ̄ values are. The magnitudes (0.90–2.21) indicate **linear (1+δ_smooth)**; if so, relabel ρ̄ as the quartile mean of (1+δ_smooth) and note that stratification was performed on log10(1+δ_smooth) while the table reports linear means (or recompute log-means to match the stated definition). Reconcile step-12 wording.
- Tier: **MAJOR** (definitional correctness-of-record), DO-NOW, **conclusion unchanged**.

### MINOR — DO-NOW (single polish pass)

- **C3 (V3):** scrub "Paper IV v1.0.166" / "earlier preprint" version strings from body (lines 686, 691, 437, 815); keep only the Appendix C reproducibility tag.
- **C4 (V4):** one canonical σ-comparability statement in §V; cross-ref from Tables III/V/VI/IX/XIII captions; delete the redundant restatements (resolves Gemini m3's "confusing" complaint by consolidation, not deletion).
- **C5 (V5):** Table X membership-count footnote (sphere-PIS vs catalog-native GALZONE) pointing to §VIII D.
- **C6 (V6):** Table XIV — make the n≥100 filter explicit and exclude/annotate the 1-2-object classes (OpenAI M5).
- **C7 (V7):** Table VIII — per-row label of membership basis ("k=20" vs "exact k-unbounded"); reconcile 621,964 vs 621,864 (OpenAI M6).
- **C8 (V8):** Fig 3 / §VI A — either plot Jeffreys CIs on the 783,820 unique-TARGETID parent, or justify the sqrt(N) design-effect approximation (OpenAI M7).
- **C9:** fold OpenAI M1/M3/E5/n1-n12 caption + unit + hyphenation NITs into the same pass at author discretion.

### DO-NOW-AT-SUBMISSION
- **C10 (D1):** mint and insert the P5 archival DOI (Zenodo/equivalent) for tag v0.1.82/v0.1.83 in Appendix C + data-availability line.

### TRULY-BLOCKED
- **None.** Every VERIFIED item is closeable with in-tree material; no missing hardware/data.

### NO ACTION
- All FALSIFIED (F1-F8), all OPINION/length/structure items, and the two STALE items (already closed in v0.1.83). Do **not** "fix" the Clopper-Pearson line, Table IV residual, or Table VIII sign — they are correct in source.

---

*Verdict rationale (honest calibration): MNRAS/PRD rigor applied. No unsupported load-bearing claim, no missing critical control, full reproducibility. Two genuine MAJOR DO-NOW presentation/definition items (Paper IV reframing; ρ̄ definition) + a MINOR polish pass bring P5 to submission standard. Grok REJECT = false positive (primary/secondary inversion). Net: P5 HOLDS; readiness consistent with MINOR-to-MAJOR REVISIONS, not REJECT and not BLOCKER.*
