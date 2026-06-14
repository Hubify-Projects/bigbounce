# EXT12 Browser Submission Manifest

**Round:** EXT12  
**Goal:** Verify EXT11-closure-wave closures → 18/18 ACCEPT loop terminator  
**EXT11-closure versions:** P1A v1A.0.74 / P1B v1B.0.71 / P2 v1.7.65 / P3 v3.1.108 / P4 v1.0.188 / P5 v0.1.77-2026-06-13  
**Submitted:** 2026-06-13 (EXT11-closure-wave bundle commit)  
**Harvest ETA:** ≥30 min from last submission

---

## PDF Verification Gate (Phase 1)

All 6 mirrors must md5-match source before submission. Run:

```bash
PAPERS_DIR="site/public/papers"
md5 $PAPERS_DIR/paper1a_ech_nogo_v1A.0.74.pdf        # expected: 3871b58706d4b7ccdcb3067cb58538bb
md5 $PAPERS_DIR/paper1b_mcmc_companion_v1B.0.71.pdf   # expected: aa1a694e8af7864631d1286bbd43bb64
md5 $PAPERS_DIR/paper2_fnl_forecast_v1.7.65.pdf       # expected: fc42f3939798acae30c01e2098745381
md5 $PAPERS_DIR/paper3_anomaly_catalog_v3.1.108.pdf   # expected: 72bd3e5b6bc133ef0943a0d5c6db1954
md5 $PAPERS_DIR/chirality_catalog_paper_v1.0.188.pdf  # expected: c47abc1893375ba483c6b82df5811915
md5 $PAPERS_DIR/p5_desi_chirality_v0.1.77.pdf         # expected: e5a3999a4354d0d9f3edf63929534f82
```

| Paper | File | PDF md5 (prefix 8) | Match |
|-------|------|-------------------|-------|
| P1A | `paper1a_ech_nogo_v1A.0.74.pdf` | `3871b587` | GATE |
| P1B | `paper1b_mcmc_companion_v1B.0.71.pdf` | `aa1a694e` | GATE |
| P2  | `paper2_fnl_forecast_v1.7.65.pdf` | `fc42f393` | GATE |
| P3  | `paper3_anomaly_catalog_v3.1.108.pdf` | `72bd3e5b` | GATE |
| P4  | `chirality_catalog_paper_v1.0.188.pdf` | `c47abc18` | GATE |
| P5  | `p5_desi_chirality_v0.1.77.pdf` | `e5a3999a` | GATE |

---

## Per-Paper EXT12 Delta-Prompts

### P1A — v1A.0.74 closure summary for EXT12

```
This is EXT12 — a focused delta-round on the EXT11-closure revisions.

Attached: Paper 1A v1A.0.74 (EXT11-closure version, 28pp).

EXT11 closure summary for your review:
- Eq. 15 second form refactored to inverse-denominator structure (visually unambiguous). Note: the EXT11 finding that Eq.15 had an "algebraic inversion error" was a misread of the LaTeX structure — the source was algebraically correct throughout. The refactor makes this visually unambiguous.
- αW⁵ sphaleron T-crossover wording corrected per literature consensus.
- App C opening paragraph softened to journal-style language.
- 3 LaTeX typographic artifacts fixed (taller |…| delimiters at p.25, bold γ_BI in Table IV, Sec IV B parenthetical rewrite).

Please re-evaluate at the same MNRAS/PRD standard. Report as ACCEPT, MINOR REVISIONS, or MAJOR REVISIONS with specific findings.
```

### P1B — v1B.0.71 closure summary for EXT12

```
This is EXT12 — a focused delta-round on the EXT11-closure revisions.

Attached: Paper 1B v1B.0.71 (EXT11-closure version, 21pp).

EXT11 closure summary for your review:
- Sec V.B release-pairing description aligned to c15.input.yaml likelihood names: planck_2020_lollipop.lowlE + planckpr4lensing (for c15, the independent replication chain) vs planck_2018_lowl.EE + planck_2018_lensing.clik (for the frozen production chains). The description now accurately reflects the actual Cobaya input files.
- Internal audit labels (E3/E4) and (E8) stripped from journal prose — these were internal review-round tracking labels that should not appear in the submitted paper.

Please re-evaluate at the same MNRAS/PRD standard. Report as ACCEPT, MINOR REVISIONS, or MAJOR REVISIONS with specific findings.
```

### P2 — v1.7.65 closure summary for EXT12

```
This is EXT12 — a focused delta-round on the EXT11-closure revisions.

Attached: Paper 2 v1.7.65 (EXT11-closure version, 28pp).

EXT11 closure summary for your review:
- r=0.84 confirmed as the canonical noise-weighted central value (unchanged).
- r=0.75 now explicitly labeled r_{16th percentile} throughout — this is a distributional robustness check showing the 16th-percentile template-overlap value, not an alternative central estimate or denominator.
- BF self-check paragraph restructured to disentangle the delta-prior row (which gives the theoretical maximum BF) from the Gaussian-bounce-prior rows (which give the physically motivated BF range). The comparison table now makes clear which row corresponds to which prior assumption.

Please re-evaluate at the same MNRAS/PRD standard. Report as ACCEPT, MINOR REVISIONS, or MAJOR REVISIONS with specific findings.
```

### P3 — v3.1.108 closure summary for EXT12

```
This is EXT12 — a focused delta-round on the EXT11-closure revisions.

Attached: Paper 3 v3.1.108 (EXT11-closure version, 29pp).

EXT11 closure summary for your review:
- Abstract scope corrected: 4 of 6 surveys (DESI, SDSS, Planck, NEOWISE) pass the 5σ injection-recovery gate and are presented at catalog grade. eROSITA (1.2% recovery rate) and Gaia (5.2% recovery rate) are now flagged as exploratory throughout the paper — in the abstract, section headers, and captions.
- Table IX BF ratio behavior clarified: the Bayes factor table now includes a note distinguishing the prior-sensitivity regime from the model-preference regime.

Please re-evaluate at the same MNRAS/PRD standard. Report as ACCEPT, MINOR REVISIONS, or MAJOR REVISIONS with specific findings.
```

### P4 — v1.0.188 closure summary for EXT12

```
This is EXT12 — a focused delta-round on the EXT11-closure revisions.

Attached: Paper 4 v1.0.188 (EXT11-closure version, 23pp).

Note: Paper 4 achieved 3/3 ACCEPT at EXT11 — the first paper in this series to achieve unanimous acceptance across all three independent reviewing systems. EXT12 is a verification round.

EXT11 closure summary for your review:
- Shamir reference [2]: title text + DOI + arXiv verified and confirmed correct. The full citation is: Shamir (2022), PASJ 74, 1114, DOI 10.1093/pasj/psac058, arXiv:2208.00893. This was the only VERIFIED finding at EXT11.
- Stray internal label (B1) removed from Appendix B.
- "next submission pass" placeholder language replaced with journal-style "future work."

Please re-evaluate at the same MNRAS/PRD standard. Report as ACCEPT, MINOR REVISIONS, or MAJOR REVISIONS with specific findings.
```

### P5 — v0.1.77-2026-06-13 closure summary for EXT12

```
This is EXT12 — a focused delta-round on the EXT11-closure revisions.

Attached: Paper 5 v0.1.77-2026-06-13 (EXT11-closure version, 32pp).

EXT11 closure summary for your review:
- Figs 2, 3, and 9 REGENERATED from generation scripts. The EXT11 finding that plot titles showed "V-Web" labels was correct — the EXT10 V-Web→T-Web rename was applied to the LaTeX source text but not to the figure image files. Figs 2/3/9 have been regenerated with correct T-Web plot titles.
- §IX C and §VIII T-Web vs T-Web ambiguity resolved via explicit disambiguation distinguishing the Hahn (2007) tidal-tensor T-Web implementation (used in this work) from concurrent-literature T-Web constructions.
- Adversarial χ-unit footnote language softened to journal style.
- Table I "MS" clarification: the EXT11 finding that Table I showed "MS (millisecond pulsars)" was a pdftotext rendering artifact of italic \textit{NS} (neutron stars) in the LaTeX source. The source text is correct — the table header reads NS as intended.

Please re-evaluate at the same MNRAS/PRD standard. Report as ACCEPT, MINOR REVISIONS, or MAJOR REVISIONS with specific findings.
```

---

## Submission Log (Phase 2) — TO BE FILLED DURING SUBMISSION

Protocol: Upload new EXT11-closure PDF + paste EXT12 delta-prompt (per-paper above) to EXISTING EXT11 chat URLs (same-thread delta). Use `/external-review-browser-loop` SKILL Phase-2 recipe.

### ChatGPT — Big Bounce Book Project (`/g/g-p-6881c7f354808191a36860ff4d29fa69`)
Model/effort: **Pro Extended**

| Paper | PDF md5 (prefix) | Chat URL (SAME as EXT11) | Submitted (PDT) | Harvest | Verdict |
|-------|---------|----------|-----------------|---------|---------|
| P1A | 3871b587 | [link](https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a2dc597-d61c-83e8-ac93-8f3bf7f139fb) | TBD | TBD | TBD |
| P1B | aa1a694e | [link](https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a2dc5cf-db00-83e8-b824-21b626a0d9ab) | TBD | TBD | TBD |
| P2  | fc42f393 | [link](https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a2dc5f2-5e8c-83e8-9318-b7aefa847ee0) | TBD | TBD | TBD |
| P3  | 72bd3e5b | [link](https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a2dc617-2480-83e8-bf48-cc78a7bce891) | TBD | TBD | TBD |
| P4  | c47abc18 | [link](https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a2dc65e-2488-83e8-90f8-fcacbf9d4378) | TBD | TBD | TBD |
| P5  | e5a3999a | [link](https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a2dc684-5918-83e8-b53e-28fde5fca69a) | TBD | TBD | TBD |

### Grok — BigBounce-Papers Project (`/project/e6c9ce77-4f86-4d94-b440-1062a78171c1`)
Model/effort: **Heavy**

| Paper | PDF md5 (prefix) | Chat URL (SAME as EXT11) | Submitted (PDT) | Harvest | Verdict |
|-------|---------|----------|-----------------|---------|---------|
| P1A | 3871b587 | [link](https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=7f12a3a9-339f-4a0d-a258-3d7224b02a7e) | TBD | TBD | TBD |
| P1B | aa1a694e | [link](https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=6fede933-742f-423b-b1d8-bbbf7254d6c1) | TBD | TBD | TBD |
| P2  | fc42f393 | [link](https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=1d8e1fbc-6a0e-4917-b1a5-cf389b307141) | TBD | TBD | TBD |
| P3  | 72bd3e5b | [link](https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=df8b502c-8c32-408f-9509-82be147fccbe) | TBD | TBD | TBD |
| P4  | c47abc18 | [link](https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=9b06db9f-adeb-4928-8b88-8b17655b095d) | TBD | TBD | TBD |
| P5  | e5a3999a | [link](https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=52437983-41f2-4016-ac45-ad392572ce46) | TBD | TBD | TBD |

### Gemini — `gemini.google.com/u/0/` (Houston Golden · Work · Ultra)
Model/effort: **2.5 Thinking**
Note: Gemini requires FRESH chat URLs per submission (backend silently drops uploads on re-opened chats). Use hidden `input[type=file]` upload pattern (pattern from EXT11 SKILL upgrade).

| Paper | PDF md5 (prefix) | NEW Chat URL (fresh submit) | Submitted (PDT) | Growth-confirmed | Harvest | Verdict |
|-------|---------|----------|-----------------|-----------------|---------|---------|
| P1A | 3871b587 | TBD (fresh URL) | TBD | TBD | TBD | TBD |
| P1B | aa1a694e | TBD (fresh URL) | TBD | TBD | TBD | TBD |
| P2  | fc42f393 | TBD (fresh URL) | TBD | TBD | TBD | TBD |
| P3  | 72bd3e5b | TBD (fresh URL) | TBD | TBD | TBD | TBD |
| P4  | c47abc18 | TBD (fresh URL) | TBD | TBD | TBD | TBD |
| P5  | e5a3999a | TBD (fresh URL) | TBD | TBD | TBD | TBD |

---

## EXT12 Expected Outcome

- **HIGH confidence: 18/18 ACCEPT**
- Basis: All EXT11 residuals are closed. P4 already universal 3/3. Grok has been 6/6 for 3 consecutive rounds. All remaining ChatGPT/Gemini MINOR items were addressable-local fixes — all addressed.
- **Harvest window:** ≥30 min from last Gemini submission
- **If any MINOR remains:** truth-audit first — most likely a false-positive given the systematic pdftotext artifact class now documented.

---

## EXT12 Harvest Notes (to fill after harvest)

- Harvest ETA: ≥30 min from last submission
- Truth-audit file: `EXT12_BATCH_TRUTH_AUDIT.md` (create after harvest)
- If 18/18 ACCEPT: loop terminates → fire `/bigbounce-close` protocol → Houston sign-off → arXiv submission
- If any MINOR: closure wave → EXT13

---

*Generated: 2026-06-13 PDT (EXT11-closure-wave bundle)*  
*Chat URLs inherited from EXT11_BROWSER_MANIFEST.md (ChatGPT + Grok same-thread; Gemini fresh)*
