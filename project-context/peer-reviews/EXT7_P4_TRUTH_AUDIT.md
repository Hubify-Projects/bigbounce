# EXT7 P4 Truth Audit — v1.0.181 (f5867e653f02488a)

**Audit date:** 2026-06-13 PT
**Paper:** Paper 4 — Survey-Scale Galaxy Chirality / Equivariant TTA, v1.0.181
**Reviewers:** ChatGPT Pro Extended (MAJOR REVISIONS), Grok Heavy (ACCEPT — 5th consecutive 6/6), Gemini Thinking (ACCEPT WITH MINOR REVISIONS)
**Source of truth:** `pipelines/p2_chirality/chirality_catalog_paper.tex`,
`outputs/canonical_provenance/ext4_fb1_flip_identity_qc_catalogwide.json`
**Protocol:** [`feedback_peer_review_truth_audit_protocol.md`] · pattern-052 re-raise auto-falsify · 2√3 Fisher 8th-falsify rule · HD-4/HD-11 release-bundle ruling binding (EXT6 P4)

**Calibration anchors:**
- Grok Heavy: 5th consecutive ACCEPT. Strongest cross-vendor calibration anchor on disk; any finding overriding Grok requires hard primary-source evidence.
- Gemini ACCEPT WITH MINOR (fresh-thread vindication round): closes the entire EXT6 ChatGPT BLOCKER class except text-polish typo set.

---

## Verdict schema

- **VERIFIED** — finding correct against source/artifact.
- **FALSIFIED** — finding contradicted by source/artifact.
- **STALE / AUTO-FALSIFIED** — already closed/HD-ruled in prior round. Pattern-052.
- **MISLABELED** — real but severity wrong.
- **OUT-OF-SCOPE / HD-RULED** — Houston-Direct (HD) ruling in prior round binds.
- **GENUINE-NEW** — not previously raised, verified on disk.

---

## Section A — ChatGPT findings

ChatGPT lead: "The remaining acceptance blocker is still the release/provenance layer." Every previously-flagged BLOCKER except B1 marked CLOSED; M1–M8 all CLOSED or PARTIAL/acceptable. B-181-1 is the only fresh BLOCKER and it re-raises the same publish-stage release/provenance gate.

### A1. ChatGPT BLOCKER B-181-1 — "Release remains non-immutable" (v1.0.181 PDF pins 53b41d12/v1.0.180; QC artifact absent at pinned hash)

| Field | Value |
|---|---|
| Claim | PDF is v1.0.181 but Data Availability pins commit 53b41d12 (v1.0.180); source at 53b41d12 still cites a older commit pin; catalog-wide QC artifact required by the paper is present on main but absent at the pinned hash. Calls for one final immutable v1.0.181 tag/DOI with PDF/.tex/figures/artifacts on the same release. |
| Cited tex location | Data Availability §, p.21 (tex l.842–854) |
| On-disk verification | (i) `\paperVersion{v1.0.181}` confirmed at tex l.55. (ii) Data Availability at tex l.844 reads literally "Repository state for this version: commit \texttt{53b41d12} (v1.0.180, June 2026)" — stamp-then-pin protocol explicitly documented in same paragraph; "the rendered PDF, not the in-repo source at the stamp hash, is the authoritative carrier of this pin". (iii) Catalog-wide QC artifact `pipelines/p2_chirality/outputs/canonical_provenance/ext4_fb1_flip_identity_qc_catalogwide.json` confirmed present on `HEAD` (`git ls-tree HEAD` returns blob `182f00f1`) but ABSENT at `53b41d12` (`git ls-tree 53b41d12` returns empty for this path). ChatGPT's evidence claim is factually correct on every leg. (iv) Zenodo DOI not minted; tex l.849 says "A persistent archival DOI ... has not yet been minted; until it is, the versioned release tag above is the citable artifact". |
| Re-raise history | This is the SAME finding as EXT6 ChatGPT F179-B1 ("Data Availability commit pin mismatch"). EXT6 ruling: **OUT-OF-SCOPE for arXiv-stage closure (the protocol is explicit and the rendered PDF is the authoritative carrier). Pre-journal-submission action: stage one immutable v1.0.181 commit that pins its own hash + Zenodo DOI. Defer to publish-stage.** This is an HD ruling (matches HD-4/HD-11 release-bundle deferral pattern). |
| Pattern-052 test | Re-raise of an HD-deferred finding. Prior verdict cited primary evidence (the stamp-then-pin protocol IS in the paper, and the authoritative-PDF convention IS explicitly stated). No new evidence in EXT7 — ChatGPT cites exactly the same protocol text and the same QC-artifact-at-53b41d12 fact. Per pattern-052: "re-raise may only be auto-falsified if prior falsification cites primary evidence". Here the prior verdict cited primary evidence; ChatGPT has added no new claim. |
| Verdict | **STALE / HD-RULED (AUTO-FALSIFIED on re-raise; second consecutive raise of an HD-deferred publish-stage gate)**. The release-provenance gate is real and acknowledged, but it is Houston-direct DEFERRED to journal-submission stage. The paper's own Data Availability section discloses the protocol transparently. ChatGPT is NOT naming a NEW specific in-text claim that's actually missing — it is restating the same stamp-then-pin acknowledgement. |
| Closure | No action at arXiv stage. Carry forward to publish-stage closure list: (i) cut v1.0.181 immutable tag, (ii) ensure QC artifact + all referenced JSONs are present at that pinned hash, (iii) mint Zenodo DOI, (iv) replace "rendered PDF is authoritative" paragraph with single-tag DOI pointer. Already on the publish-stage gate per EXT6. |

### A2. ChatGPT MAJOR M-181-1 — WLS bootstrap exact-mask equivalence still not visible in paper

| Field | Value |
|---|---|
| Claim | The WLS exclusion is statistically well-framed but the exact-mask equivalence is asserted in JSON prose, not in a paper-level audit table. |
| On-disk verification | tex l.794 area contains the block-bootstrap z≈−18 prose; the mask-equivalence assertion is footnoted but not in a compact audit subtable. Same finding as EXT6 ChatGPT F179-M3 ("WLS exact-mask equivalence not visible in paper"), which was VERIFIED but deferred to next restamp. |
| Re-raise history | Second raise of the same EXT6 MAJOR. EXT6 verdict: VERIFIED + Closure: "Add a compact mask-equivalence audit subtable in Appendix D.g listing: canonical-mask hash, WLS-artifact mask hash, pixel-count match, in-mask spiral-count match. Defer to next restamp." The deferred edit was not yet applied in v1.0.181. |
| Verdict | **VERIFIED (genuine carry-over; deferred edit not yet applied)** |
| Closure | Apply the deferred EXT6 closure at next restamp: compact mask-equivalence audit subtable in Appendix D.g. |

### A3. ChatGPT MAJOR M-181-2 — Table I LEE taxonomy still mixes direct-MC with Bonferroni/BH

| Field | Value |
|---|---|
| Claim | Direct max-statistic MC null with p_LEE ≤ 10⁻⁴ is conflated in Table I caption with Bonferroni/BH per-direction p-values; split into two diagnostics. |
| On-disk verification | Same site as EXT6 F179-M1. EXT6 verdict: **OPINION** (prose hierarchy already explicit at tex l.723: "the principled directional look-elsewhere control is the direct-MC max-statistic null itself", and "BH/Bonferroni pass is reported only as a conservative heuristic cross-check"). Table I caption could be tightened but science is correct. |
| Re-raise history | Second raise. EXT6 ruled OPINION. ChatGPT did not point to a specific in-text contradiction — the prose hierarchy is correct. |
| Verdict | **OPINION (re-raise of EXT6 OPINION; no new finding)** |
| Closure | Optional tightening at next restamp. Not closure-blocking. |

### A4. ChatGPT MAJOR M-181-3 — Sec. IV.D "explained at the percent level" overreach (carryover M7 residue)

| Field | Value |
|---|---|
| Claim | One sentence in Sec. IV.D still reads as explaining Shamir/Ganalyzer directly, while Sec. V.A correctly narrows. Reword to match Sec. V.A. |
| On-disk verification | Mechanical wording residue. Same closure direction as EXT6 F179-M2 (already partially applied at l.609 with "under our pipeline"). ChatGPT's targeted passage is the EARLIER Sec. IV.D sentence, not the already-corrected V.A passage. |
| Verdict | **VERIFIED (mechanical phrasing residue; second instance of M7-class wording)** |
| Closure | Mechanical text edit at next restamp: rewrite Sec. IV.D sentence to mirror Sec. V.A "this DESI/ViT-Small pipeline" scoping. |

### A5. ChatGPT MAJOR M-181-4 — Harmonic-completeness mini-table missing

| Field | Value |
|---|---|
| Claim | The z≈68–218 MASTER recovery range and P(≥3σ)≥0.999 at A_p=0.75% are load-bearing claims; supporting info is only in artifact reference. Add a small in-paper table or figure with injected amplitude, recovery probability, null convention, expected MASTER z range. |
| On-disk verification | The completeness numbers are in the abstract (l.223) and conclusions but the paper-internal table is the WLS exclusion table (tab:wls_fit) rather than a dedicated completeness table. The claim references an artifact. |
| Re-raise history | Not directly raised in EXT6 in this exact form. NEW MAJOR in EXT7. |
| Verdict | **GENUINE-NEW MINOR (mislabeled MAJOR)** — Real polish/presentation gap. The completeness numbers are in the text and footnote-grade artifact, not headlining a new science claim. Severity is presentation-polish, not science-blocking. |
| Closure | Add a compact harmonic-completeness mini-table at next restamp. Severity downgrade to MINOR. |

### A6. ChatGPT MINOR m-181-1 — "formal upper limit" wording for A_{95,nq}

| Field | Value |
|---|---|
| Claim | "Formal upper limit" too strong for a null-quantile with no coverage guarantee; use "formal null-quantile benchmark" or "descriptive null-quantile bound". |
| On-disk verification | Sec. IV.C tex search confirms phrasing remnant. |
| Verdict | **VERIFIED (mechanical phrasing polish)** |
| Closure | Replace "formal upper limit" → "formal null-quantile benchmark" at next restamp. |

### A7. ChatGPT MINOR m-181-2 — Table VII "All 8 tests pass" quote-prone

| Verdict | **OPINION (re-raise of EXT6 OPINION; no new finding)** — same as EXT6 F179-m2. Optional. |

### A8. ChatGPT MINOR m-181-3 — Zenodo DOI unminted

| Verdict | **VERIFIED + HD-RULED OUT-OF-SCOPE for arXiv** — same as EXT6 F179-m3; gate on journal submission. |

### A9. ChatGPT MINOR m-181-4 — D4-TTA spatial null caveat

| Verdict | **VERIFIED (mechanical caveat sentence)** — add one disambiguation sentence at next restamp per ChatGPT's exact proposal. |

---

## Section B — Gemini findings (fresh-thread, ACCEPT WITH MINOR)

Gemini opening: "The revisions introduced in version 1.0.181 effectively resolve the vast majority of the major technical and architectural issues." All EXT6 closures confirmed including 2√3 Fisher CLOSED ("algebraically sound"), commit pin update CLOSED, augmentation CLOSED, σ-framework disambiguation CLOSED.

### B1. Gemini MAJOR — "Sec IV.B p.6 text layout jumble" ("realizations on the p=f_CW This canonical mask drawn at versus p=0.5...")

| Field | Value |
|---|---|
| Claim | Reads as jumbled text-block string from PDF extraction. |
| On-disk verification | tex l.467 reads (single-line LaTeX, no jumble): "binomial per-pixel realizations on the canonical mask drawn at $p\!=\!f_{\rm CW}^{\rm global}$ versus $p\!=\!0.5$ yield statistically identical dipole-amplitude null distributions". The sentence is grammatical and correctly ordered. |
| Verdict | **FALSIFIED — PDF text-extraction artifact (Gemini OCR re-ordering across line breaks). The source sentence is correctly ordered.** |
| Closure | No action. Pattern-026 (reviewer OCR mis-extract) territory. |

### B2. Gemini MAJOR — "Cyrillic рмс character pollution in p_MC"

| Field | Value |
|---|---|
| Claim | Sec. VII.c p.14 contains Cyrillic "рмс=15/500=0.030" instead of Latin p_{MC}. |
| On-disk verification | Source uses `$p_{\rm MC}$` LaTeX macro throughout. No Cyrillic characters present in source. Gemini is reading the PDF's rendered subscript and misclassifying the glyphs (revtex math-subscript "MC" can render in a way that OCR mistakes for Cyrillic on certain fonts). |
| Verdict | **FALSIFIED — PDF font-encoding OCR mis-extract; source is clean LaTeX `$p_{\rm MC}$`.** |
| Closure | No action. |

### B3. Gemini MINOR — Percentage inconsistency with stated truncation rule (CCW 18.99% should be 18.98%)

| Field | Value |
|---|---|
| Claim | Tex says percentages "truncated at second decimal" but CCW 18.99 vs exact 18.9869 → truncates to 18.98; NS 62.23 vs 62.226 → 62.22; spiral 37.78 vs 37.7738 → 37.77. Author has rounded these to enforce 100.00% sum. |
| On-disk verification | Verified arithmetically: CW 18.786963 → 18.78 ✓; CCW 18.986927 → trunc=18.98 (paper says 18.99); NS 62.226110 → trunc=62.22 (paper says 62.23); spiral 37.773890 → trunc=37.77 (paper says 37.78). True truncation sums to 99.98%. The paper's "truncated" claim is internally inconsistent — three of four values are rounded, not truncated. |
| Verdict | **VERIFIED (genuine MINOR; real internal inconsistency between methodology statement and reported values)** |
| Closure | Either (a) replace 18.99/62.23/37.78 with truncated 18.98/62.22/37.77 and explicitly note the residual 99.98% sum, or (b) reword "truncated rather than rounded" → "rounded to maintain sum-to-one consistency". Defer to next restamp. |

### B4. Gemini MINOR — "Pow is typo for soft probability" (Sec III.D p.4)

| Verdict | **FALSIFIED — PDF text-extraction artifact**. Source uses `$P_{\rm CW}$` LaTeX; the "Pow" string is an OCR collapse of the `$P_{\rm CW}$` subscript rendering. No source-level typo. |

### B5. Gemini MINOR — Fig 1 caption "ergers" duplicate

| On-disk verification | tex l.266 reads "Non-spiral (\NS{}): ellipticals, mergers, edge-on" and l.271 reads "(\NS{}) objects --- ellipticals, mergers, and edge-on galaxies". No "ergers" fragment. |
| Verdict | **FALSIFIED — PDF text-extraction artifact**. |

### B6. Gemini MINOR — "T7 is a calibration prozy" Appendix B (prozy → proxy)

| On-disk verification | tex l.728 reads `T7: Calibration proxy & $>30\%$ at $\max p\!>\!0.9$` — correct spelling "proxy". |
| Verdict | **FALSIFIED — PDF font-rendering OCR (likely the "x" rendered as "z" on some fonts; or Times "ox" ligature misread).** |

### B7. Gemini MINOR — "Condition number 4.5×10^{16^{\circ}}" (Appendix D p.19)

| On-disk verification | tex l.794 reads `condition number $4.5\!\times\!10^{16}$` — no `^{\circ}`. Pure dimensionless. |
| Verdict | **FALSIFIED — PDF OCR mis-extract (rendered superscript "16" misread as "16°").** |

### B8. Gemini MINOR — "withz z=−2.89" (Appendix D p.20)

| Verdict | **FALSIFIED — PDF text-flow OCR artifact** (likely "with $z\!=\!-2.89$" rendered with no space → "withz="). Source is clean. |

---

## Section C — Grok findings

### C1. Grok ACCEPT — no new findings

| Verdict | **CALIBRATION-ANCHOR (5th consecutive ACCEPT)**. Grok performed full end-to-end re-read of v1.0.181. All R36conf items confirmed closed, no regressions, no new BLOCKER/MAJOR/MINOR. Acceptance-stage anchor. |
| Closure | No action. |

---

## Section D — 2√3 Fisher 8th-falsify rule

| Item | Did any reviewer re-raise the 2√3 Fisher factor? |
|---|---|
| Gemini | Explicitly says "CLOSED. The analytical re-derivation of the ideal Fisher floor (σ(A)=√3/N_spiral=2√3·σ(f_CW)) holds up perfectly under verification." Gemini AGREES with the derivation. |
| ChatGPT | Does not re-raise. |
| Grok | "Fisher stands with edge-on derivation added." CLOSED. |
| Verdict | **N/A — no re-raise; auto-falsify not triggered**. R34conf REDERIVED-CORRECT status holds. 7 prior falsifications + Gemini's explicit confirmation this round. |

---

## Aggregate closure

| Severity | Count | Action |
|---|---|---|
| ChatGPT BLOCKER (B-181-1) | 1 | STALE/HD-RULED — release-bundle gate deferred to publish-stage per EXT6 binding ruling. Not arXiv-blocking. |
| ChatGPT MAJOR (M-181-1) | 1 | VERIFIED carry-over — apply deferred EXT6 mask-equivalence audit subtable at next restamp. |
| ChatGPT MAJOR (M-181-2) | 1 | OPINION re-raise — optional tightening. |
| ChatGPT MAJOR (M-181-3) | 1 | VERIFIED phrasing residue (Sec IV.D mirror Sec V.A). Mechanical edit. |
| ChatGPT MAJOR (M-181-4) | 1 | GENUINE-NEW (mislabeled) — downgrade to MINOR; add compact completeness mini-table. |
| ChatGPT MINORs (m-181-1..4) | 4 | 1 VERIFIED text edit; 1 OPINION; 1 HD-deferred (DOI); 1 VERIFIED caveat sentence. |
| Gemini MAJORs (B1, B2) | 2 | Both FALSIFIED — PDF OCR/extraction artifacts. No source defect. |
| Gemini MINORs (B3..B8) | 6 | 1 VERIFIED (truncation/rounding inconsistency); 5 FALSIFIED PDF OCR artifacts. |
| Grok | 0 findings | ACCEPT — 5th consecutive. Strongest external anchor. |

**Total VERIFIED items requiring closure**: 5 (1 MAJOR carry-over WLS mask-equivalence subtable; 1 mechanical Sec IV.D phrasing residue; 1 MINOR truncation/rounding consistency; 1 MINOR A95,nq phrasing; 1 MINOR D4-TTA caveat sentence) + 1 GENUINE-NEW MINOR (completeness mini-table) = **6 deferred polish edits**.

**Acceptance-stage blockers (this round)**: **0**. The single ChatGPT BLOCKER is HD-RULED OUT-OF-SCOPE for arXiv (publish-stage gate, EXT6 binding).

**External cross-vendor consensus**: 2/3 ACCEPT (Grok ACCEPT + Gemini ACCEPT-WITH-MINOR); ChatGPT MAJOR is driven entirely by re-raise of HD-deferred publish-stage gate.

---

## Next-round priorities

1. **Apply 6 deferred polish edits at next restamp** (WLS mask-equivalence audit subtable, Sec IV.D Shamir phrasing residue, truncation/rounding consistency note, A_{95,nq} "formal upper limit" rewording, D4-TTA caveat sentence, completeness mini-table).
2. **Publish-stage close-the-gap (post-arXiv)**: cut immutable v1.0.181+ tag, mint Zenodo DOI, ensure all referenced artifacts present at the pinned hash (including ext4_fb1_flip_identity_qc_catalogwide.json), replace "rendered PDF is authoritative" exception with single-tag DOI pointer.
3. **Pattern-052 reinforcement**: ChatGPT release-provenance gate auto-falsifies on re-raise at arXiv stage only (EXT6 binding); accept that ChatGPT will continue raising it until the publish-stage closure is done.
4. **Grok 5th consecutive ACCEPT + Gemini ACCEPT-WITH-MINOR**: cross-vendor anchor is decisively positive. Paper is acceptance-grade at arXiv stage.
