# R32conf — Paper 3 — Claude_brutal referee report

- **Reviewer:** Claude_brutal (in-session Opus leg, API-credit fallback for failed Anthropic-API leg)
- **Round:** R32conf
- **Paper:** P3 — Spectrally Unusual Sources at Scale (paper3_draft.pdf)
- **Version:** v3.1.93 (28 pages)
- **PDF md5:** a3504a9b6d4e46e254d151a7364c5719 (verified locally; matches header "a3504a9b")
- **Date:** 2026-06-11 PT
- **Mode:** brutal journal-style referee, recount-consistency-priority sweep
- **Recount artifact verified on disk:** `pipelines/p3_anomaly_engine/ext3_b2_targettype_recount.json` present and consistent with the disclosure numbers (1″=2,468 / 2″=2,531 / 5″=3,390 / denom=20,299,155 / SPECTYPE 2371/95/2).

(Earlier stub from the failed Anthropic-API leg overwritten in this file per task instructions; original credit-balance failure logged at request_id req_011Cbx9mPqnXXryNXjN9XcJv.)

---

## VERDICT — preliminary (will be finalized at bottom after full read)

To be tallied after full read; recount-consistency sweep first.

---

## Section 1 — RECOUNT CONSISTENCY SWEEP (priority 1)

Target numbers (must match across all 5 disclosure sites):
- `2,468` (1″ science-class match)
- `2,531` (2″)
- `3,390` (5″)
- `190,015` (DESI anomaly cluster total used in recount)
- `20,299,155` (broader bitmask denominator)
- `≈0.9×` (recount multiplier vs Liang 2023's 2,685)
- `~98.7%` (non-primary-class fraction)
- `86%` (DESI_TARGET==0 fraction)
- `2,685` (Liang 2023 benchmark anomaly count)
- `2,371 / 95 / 2` (SPECTYPE GALAXY/QSO/STAR of the 1″ matches)
- Retained-elsewhere full-stream numbers: `195,829`, `0.87%`, `141×` point-source tier, `73×` as full-stream DESI-only inflation.

### Site 1 — Abstract (p.1) — PASS

Quote: *"the DESI-only subset (195,829 anomalies) is a ~73× increase on the same benchmark (not a like-for-like comparison: the DESI count is a top-1% cut of the full 22.5M-spectrum scan, not restricted to validated science targets, while the benchmark accounting is science-target-only; the completed science-class-restricted recount finds only 2,468 DESI anomaly clusters coincide at 1″ with a main-survey spectrum carrying a primary science-class target bit — ≈0.9× the benchmark's 2,685, not 73× — so ~98.7% of DESI anomaly clusters fall on sky-fiber, secondary-target, or filler spectra"*

Numbers present: 195,829 / 73× / 2,468 / 1″ / ≈0.9× / 2,685 / ~98.7%. Internally consistent with target list. Missing from abstract (acceptable in abstract): 190,015 / 20.3M / 2″ / 5″ / 86%. No "queued" / "will be performed" language remains. PASS.

### Site 2 — §IV.A DESI DR1 subsection (p.5) — PASS (with caveat M1)

Quote: *"A positional recount against the DR1 redshift catalog (zall-pix; 28,425,963 rows) quantifies the scope claim directly: of the 190,015 deduplicated DESI anomaly clusters, only 2,468 (1.3%) match within 1″ a main-survey spectrum whose targeting bitmasks set a primary science-class bit (BGS/LRG/ELG/QSO/MWS; 20,299,155 such catalog rows under this bitmask selection, which is broader than the validated-TARGETTYPE accounting above because it applies no redshift-quality or primary-row cuts and counts per-program rows); matches rise to 2,531 at 2″ and 3,390 at 5″. By Redrock SPECTYPE the 1″ matches are 2,371 GALAXY, 95 QSO, 2 STAR. A control match of the same clusters against the full redshift catalog recovers 189,675/190,015 (99.8%) at 1″, confirming the positional join is sound; the conclusion is that ~98.7% of DESI anomaly clusters coincide with spectra carrying no primary science-class target bit (86% have DESI_TARGET = 0 outright — sky fibers and secondary/ToO programs). Restricted to validated science targets, the DESI anomaly catalog is therefore ≈0.9× the size of the Liang et al. benchmark (2,468 vs. 2,685), not 73×: the 73× figure is a statement about the full spectra stream, dominated by non-science-target spectra (recount artifact: pipelines/p3_anomaly_engine/ext3_b2_targettype_recount.json)."*

Numbers present: 190,015 / 2,468 / 1.3% / 1″ / 20,299,155 / 2,531 / 2″ / 3,390 / 5″ / 2,371 GALAXY, 95 QSO, 2 STAR / 189,675/190,015 / 99.8% / ~98.7% / 86% / 0.9× / 2,685 / 73×. All 11 target numbers present and consistent. PASS.

### Site 3 — §IV.A broader-bitmask vs ~6.5M coherence — PASS (see M1)

Quote (p.5 earlier): *"all 22,504,897 coadded spectra from the Main Survey through the DESI-trained BIGAE model, of which ~6.5 million carry a validated science TARGETTYPE in the five primary classes — … The headline 195,829 DESI anomaly count is the top-1% score-cut of the full 22.5-M-spectrum scan and is not restricted to the validated-TARGETTYPE subset; per-class anomaly rates and SIMBAD-novelty fractions reported below refer to the ~6.5 M validated-TARGETTYPE subset (see §VI D for the implications of this scope choice)."*

The recount paragraph DOES explicitly distinguish its 20,299,155 denominator from the "~6.5 M validated-TARGETTYPE" denominator with the parenthetical *"which is broader than the validated-TARGETTYPE accounting above because it applies no redshift-quality or primary-row cuts and counts per-program rows"*. Explanation present and coherent. PASS — but see M1 for residual reader-confusion risk.

### Site 4a — §VI.A The LAMOST Training-Bias Lesson (p.18) — PASS

Quote: *"DESI anomalies (0.87%, multi-band, 0% artifact rate in top 200) pass each of the internal checks applied to them … no independent architecture was applied to DESI, and the completed science-class recount shows ~98.7% of DESI anomaly clusters fall on non-primary-class spectra, §III A) while LAMOST anomalies (0.39%, 98% blue-excess) fail the simplest check"*

Phrasing "completed science-class recount" + "~98.7%" matches Site 1/2 exactly. No "queued"/"will be performed"/"pending" language. Cross-ref §III A is the same anchor used by the abstract, internally consistent. PASS.

### Site 4b — §VI.E Comparison with Prior Work (p.19) — PASS (see M2)

Quote: *"Our DESI anomaly rate of 0.87% is numerically close to the 1.07% rate reported by Liang et al. [11] … but the science-class-restricted recount (§III A) shows the two rates are measured on different populations: our 0.87% is a full-spectra-stream rate, while Liang et al.'s 1.07% is a science-target rate. Restricted to main-survey primary-class targets — the population Liang et al. actually scanned — our catalog contains 2,468 anomalies (≈0.9× their 2,685; restricted rate 0.012% at the same S > 5 threshold), so the rate agreement across the two populations is partly coincidental and the like-for-like statement is the ≈0.9× absolute count."*

Numbers: 0.87% / 1.07% / 2,468 / 0.9× / 2,685 / 0.012%. ALL consistent. Note: 2,468/20,299,155 = 0.01216% which rounds to 0.012% — arithmetic spot-check PASSES. PASS, modulo M2 below (the 0.012% denominator subtlety).

### Site 5 — §VII Conclusions, Scale item (p.20) — PASS

Quote: *"This is ~141× the largest prior single-survey catalog [11] (~100× on the catalog-grade point-source subset alone); DESI-only is a ~73× increase on the same benchmark (full-scan count vs. a science-target-only benchmark catalog — not like-for-like: the science-class-restricted recount gives 2,468 anomalies, ≈0.9× the benchmark; §III A)."*

Retains the 141× / 73× full-stream numbers without contradiction, AND immediately co-locates the ≈0.9× / 2,468 recount disclaimer in the same bullet. No site still presents an unqualified 73× claim. PASS.

### Arithmetic spot-checks

- `2,468 / 190,015 = 0.012988…` → paper writes `1.3%` (p.5). PASS.
- `2,468 / 2,685 = 0.9192…` → paper writes `≈0.9×`. PASS.
- `1 − 2,468 / 190,015 = 0.98701…` → paper writes `~98.7%`. PASS.
- `2,371 + 95 + 2 = 2,468`. PASS.
- `189,675 / 190,015 = 0.99821…` → paper writes `99.8%`. PASS.
- `2,468 / 20,299,155 = 0.0001216 = 0.01216%` → paper writes `0.012%` in §VI.E. PASS.
- `195,829 / (22.5e6) ≈ 0.871%` → paper writes `0.87%`. PASS.
- `195,829 / 2,685 = 72.93` → paper writes `~73×`. PASS.

**RECOUNT CONSISTENCY SWEEP RESULT: PASS — all 5 sites consistent, all arithmetic checks pass, no residual "queued" language, no unqualified 73× claim, no contradiction with the 6.5M denominator (explicitly explained), and the 195,829 / 0.87% / 141× full-stream values are retained without conflict.**

---

## Section 2 — Abstract-vs-body drift (rule 15) — PASS

Abstract recount clause ("≈0.9× the benchmark's 2,685, not 73×") matches §III A body precisely. The abstract omits the 2″/5″ numbers and the 20.3M denominator detail, which is appropriate compression. No drift detected.

---

## Section 3 — Closure-introduced regression check (pattern-051)

I read the §III A paragraphs around the recount edit and the §VI / §VII cross-refs. No dangling references, no duplicated clauses, no obvious neighboring-sentence breakage. Several minor stylistic regressions noted below (M3, m4).

---

## Section 4 — Standard brutal pass — additional findings beyond recount

See findings list below.

---

## Findings (final)

### MAJOR

**MAJOR-1 (M1) — Triple denominator presented within four pages without a comparison table.**
Location: §III intro (~p.5 col.1, "~6.5 million carry a validated science TARGETTYPE"), §III A recount paragraph (p.5 col.2, "20,299,155 such catalog rows under this bitmask selection"), §III A pre-recount ("22,504,897 coadded spectra"). The recount paragraph DOES disclose that its 20.3M denominator is "broader than the validated-TARGETTYPE accounting above" but a journal referee will still flag the three coexisting DESI denominators (22.5M / ~20.3M / ~6.5M) as a clarity hazard. **Recommendation:** add a one-line bracketed table or two-row summary somewhere (caption of Table I or a footnote under §III A) listing the three denominators and what each accounts for. Currently the reader has to assemble the relationship from prose. Not blocking, but the recount story is the paper's headline reframing and deserves a visual anchor.

**MAJOR-2 (M2) — "0.012%" rate quote in §VI.E uses the broader 20.3M denominator while the body's 1.3% rate uses the 190,015 anomaly-cluster denominator — same numerator (2,468), different rates.**
Location: §VI.E p.19 *"restricted rate 0.012% at the same S > 5 threshold"*. The 0.012% is `2,468 / 20,299,155` (a rate of science-class spectra that landed in the anomaly catalog), whereas §III A's `1.3%` is `2,468 / 190,015` (a fraction of anomaly clusters that hit a science-class target). Both numbers are correct under their respective denominators but the reader is given two ostensibly comparable "rates" without disambiguation. **Recommendation:** in §VI.E, rephrase to *"restricted rate 0.012% over the 20.3M-row science-class spectra denominator"* or footnote-link to §III A. A referee will object that "the same S > 5 threshold" implies the same rate-basis as 0.87%, which it does not.

**MAJOR-3 (M3) — §III A inline parenthetical contains a recount paragraph that mixes "DESI anomaly clusters" with "DESI anomalies" in adjacent sentences without flagging that the cluster count (190,015) is the post-FoF-dedup count, not the raw 195,829.**
Location: §III A p.5 *"of the 190,015 deduplicated DESI anomaly clusters, only 2,468 (1.3%) match within 1″"*. Earlier in the same column the headline number is `195,829`. The relationship 195,829 → 190,015 (via 7-way 5″ FoF dedup with 5,814 collapsed counterparts, ≈3%) is consistent with Table I footnotes and §IV.C, but the recount paragraph never says "post-dedup". Combined with the LAMOST/SDSS-rate references that quote pre-dedup anomaly counts, this is a real referee hazard. **Recommendation:** insert "(post-FoF dedup; cf. §IV.C)" after the first mention of `190,015` in §III A.

### MINOR

**m4** — §III A "control match … recovers 189,675/190,015 (99.8%)" — the `99.8%` rounds 189,675/190,015 = 0.99821; reads more naturally as "99.82%" or "≥ 99.8%". Cosmetic.

**m5** — Abstract: "the completed science-class-restricted recount finds only 2,468 DESI anomaly clusters coincide at 1″…" — "only" is editorial in the abstract. A referee will read "only" as authorial framing and flag it; recount narratives are stronger with the bare number. Cosmetic.

**m6** — §VI.A: the LAMOST lesson bullet ends *"… completed science-class recount shows ~98.7% of DESI anomaly clusters fall on non-primary-class spectra, §III A) while LAMOST anomalies (0.39%, 98% blue-excess) fail the simplest check"* — the parenthesis open/close pair around `§III A)` is unbalanced (the open paren is missing). Minor LaTeX-edit regression around the recount insertion. **Confirm:** the sentence as printed reads "checks applied to them (5-fold Jaccard stability, OOD-holdout Jaccard, and top-200 visual inspection; no independent architecture was applied to DESI, and the completed science-class recount shows ~98.7% of DESI anomaly clusters fall on non-primary-class spectra, §III A) while LAMOST…". Reading it as a single parenthetical that closes at `§III A)`, the syntax is valid — but the semicolon-paren mid-sentence is awkward. Cosmetic.

**m7** — §III A: "broader than the validated-TARGETTYPE accounting above because it applies no redshift-quality or primary-row cuts and counts per-program rows" — the phrase "per-program rows" is undefined for a reader who hasn't seen DESI's targeting-bit tables. Add a half-sentence gloss or pointer to the bitmask reference.

**m8** — §VII Conclusions item 1 says "~141× the largest prior single-survey catalog" but the abstract says "~141× the size of the largest prior single-survey anomaly catalog [11]". Consistent; flag only because the abstract uses `141.5×` style precision at p.1 ("the point-source tier is ~141× the size of the largest prior single-survey anomaly catalog"). Cosmetic.

**m9** — §VI.E p.19: *"our 0.87% is a full-spectra-stream rate, while Liang et al.'s 1.07% is a science-target rate. Restricted to main-survey primary-class targets — the population Liang et al. actually scanned — our catalog contains 2,468 anomalies (≈0.9× their 2,685; restricted rate 0.012% at the same S > 5 threshold), so the rate agreement across the two populations is partly coincidental"* — the framing "partly coincidental" is slightly weak. The honest statement is that the two rates are NOT comparable because the denominators differ by ~3× (22.5M vs ~6.5M, and ~250K Liang EDR scope vs DR1 full scope), and the numerator-denominator coincidence is fortuitous. Consider strengthening to "is a coincidence of unrelated rate definitions". Stylistic.

**m10** — §III A: the 99.8% control-match number is asserted as evidence the positional join is sound, but the failure of 0.2% (340 clusters) to match the *full* zall catalog is unexplained. 340 clusters out of 190,015 missing from a 28.4M-row catalog is plausibly a small-fraction near-edge-of-fiber or coadd-vs-zall-pix mismatch issue, but a referee will ask. **Recommendation:** one-line footnote.

### Non-recount findings (standard brutal pass)

**MAJOR-4 (M4) — Abstract §V SMBHB-vs-bounce framing is over-precise about a "decisive" Bayes factor that the paper itself walks back.**
Location: abstract: *"SMBHB γ = 4.33 at +4.61σ (Savage-Dickey B_MB/SMBHB = 7.14×10³ under the flat γ ∈ [0,7] prior; prior-sensitive by construction, and the SMBHB γ = 4.33 is a population-mean reference value rather than a sharp prediction; environmentally modified SMBHB models with eccentric binaries or stellar-scattering-driven hardening can produce γ ~ 2.5–3, so this Bayes factor is decisive only against the idealized circular-orbit reference"*. The 4.61σ + log B = 3.85 "decisive" language followed by self-cancellation in the same sentence is rhetorically unstable. A statistics referee will demand the abstract either drop the σ-figure or quote the environmentally-modified comparison directly. Recommend: in the abstract, replace the bracketed sentence with *"decisive only against the idealized circular-orbit SMBHB reference; not a cosmological detection."* (You already say this in §V.A — port it to the abstract.) Severity MAJOR because the abstract is the most-cited surface and currently overpromises.

**MAJOR-5 (M5) — Spatial χ² result withdrawn in §IV.B but the abstract has no spatial-uniformity claim either way.**
Location: §IV.B p.13 *"the significant χ²ᵥ = 15.7 is dominated by the inhomogeneous footprints of the seven retained archives rather than intrinsic astrophysical clustering"* — this is the right disclosure and correctly walks back the earlier 38,330-pixel figure. **However** the §IV.B paragraph also says *"shows the combined anomaly distribution is strongly non-uniform (χ² = 376,713, dof = 24,048, χ²ᵥ = 15.7)"* and only then walks it back. The reader gets one sentence presenting a 5,000σ-equivalent statistic followed by one sentence saying it is uninterpretable. Recommend either (a) prefix the χ² with "uncorrected" and the walk-back with "after footprint correction would be required" or (b) move the χ² number into the caveat. Severity MAJOR because the χ²ᵥ = 15.7 is exactly the kind of number a reviewer extracts without context.

**MINOR-11 (m11) — §V Fisher forecast phrasing of "(no improvement at current S/N)" is correct but the abstract says "central forecast σ(f_NL) = 8.14 with 1σ envelope [3.92, 8.98] (the central 9.4% improvement is a noise-driven forecast pending higher-S/N follow-up, not a detection)". The 1σ envelope including 3.92 (a 55% improvement) while the central is 8.14 (9.4% improvement) reads to a Fisher-forecast referee as a 1σ band that is highly asymmetric and prior-driven — which the paper acknowledges, but the abstract should also state that the lower edge is the convex-mapping image of α̂ + σ_α and not a likelihood-asymmetry estimate. Cosmetic.

**m12** — §VI.D residual caveat (b) "DESI OOD: training-pool cut flags 52.8% of OOD (61× headline)" — the parenthetical "61× headline" is internal shorthand that a reader hasn't been primed for. Add a half-line gloss.

**m13** — p.10 §III.E "eROSITA Path-C ranking is the n = 298 membership list (ranked by the committed raw score artifact)" — the membership-list-only framing is repeated five times across the paper (Table I caveat, §III E, Table IV row (f), Appendix A, Conclusions). One coherent treatment instead of five would tighten the paper.

**m14** — §VI.E "Restricted to main-survey primary-class targets — the population Liang et al. actually scanned" — Liang et al. [11] is a DESI EDR paper (~250,000 spectra) whereas this work is DR1 (~22.5M coadded). Strictly "the population Liang scanned" is the DESI EDR Bright Galaxy Survey subset, not the DR1 primary-class. The 2,685 number is from a different DR/scope than the 2,468. The recount is still the right like-for-like measure (both are "anomalies in primary-science-class spectra"), but the wording should clarify that the scope is matched on selection class, not DR. **Recommendation:** add half-sentence "(Liang scanned the DESI EDR BGS sample; we restrict our DR1 catalog to the same target-class selection for the like-for-like comparison)".

**m15** — Reference list: refs [39]–[41] (Bonvin & Durrer, Challinor & Lewis, Di Dio et al.) appear at the end of the .bib but I don't see them cited in body text (the §V GR-projection caveat mentions "general-relativistic projection corrections" without numbered cites; the Heinrich et al. [33] cite carries that block). Verify these refs are actually invoked or remove. Cosmetic but the kind of thing a Phys. Rev. D copy-editor will flag.

**m16** — Figure 5 caption claims "no prior SIMBAD entry within 5″" but §IV.A says NEOWISE SIMBAD-unmatched is 45%, so the 0% novelty rate of the top-100 NEOWISE selection is not separately stated as an empirical fact in the caption. Cosmetic.

**m17** — Table V row for ACT DR6: "Cross-transfer fully connected baseline (Appendix F); ACT DR6 was not native-retrained under Path-C and is dropped from the main per-survey block (formally quarantined). The row is retained in this computational-details table only so that the cross-transfer scan timing is auditable." OK, but the row is now redundant with Appendix F prose. Either keep the table row OR delete and rely on §F. Cosmetic.

**m18** — §VI Limitations point (4): *"the empirical α_jk = 0.19±0.65 is < 1σ from null, so the 9.4% improvement is a central-value forecast pending higher-S/N follow-up"* — the 9.4% number contradicts the abstract's "central 9.4% improvement" only in that the abstract says "central forecast σ(f_NL) = 8.14" → 8.98 - 8.14 = 0.84 → 0.84 / 8.98 = 9.4%. Consistent; flag only because the abstract uses "9.4%" without showing the arithmetic. Cosmetic.

---

## VERDICT — final

**Verdict: ACCEPT with MINOR REVISIONS — recount sweep PASSES cleanly; all 5 disclosure sites internally consistent; arithmetic spot-checks all PASS; no residual "queued"/"73× unqualified" language anywhere. Issues identified are clarifications, not science blockers.**

- **ESSENTIAL findings:** **0**
- **MAJOR findings:** **5** (M1 triple-denominator clarity hazard; M2 dual-rate-basis "0.012%" ambiguity in §VI.E; M3 unflagged 195,829→190,015 dedup in recount paragraph; M4 abstract overpromises "decisive" Bayes factor; M5 abstract-vs-§IV.B χ² walk-back imbalance)
- **MINOR findings:** **13** (m4–m18; cosmetic + stylistic + one stale-ref check)

The recount disclosure is the paper's central reframing and it lands clean across all five surfaces — that was the round's purpose and it succeeded. The MAJORs are all clarity/framing issues, not arithmetic or scope errors. M1 and M2 are the two most worth fixing before submission: a small denominator table and one rephrase in §VI.E would close them.

Recommend re-stamp + restamp-bundle commit, then close the round.

---

## Sign-off

Claude_brutal — in-session Opus 4.7 [1M] fallback for failed Anthropic-API leg
R32conf, P3 v3.1.93, PDF md5 a3504a9b6d4e46e254d151a7364c5719
2026-06-11 PT
