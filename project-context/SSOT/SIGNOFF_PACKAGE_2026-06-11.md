# Houston Sign-Off Package — 2026-06-11

**Decision document for the 6-paper arXiv publish push.** Every number below traces to a committed source (cited inline). Sources: SSOT/index.md + paper-N/status.md · EXT1/EXT2/EXT3_BROWSER_MANIFEST.md · EXT3_P*_TRUTH_AUDIT.md · EXT1_HOUSTON_DECISIONS.md · COMPUTE_QUEUE.md · review-patterns/INDEX.md · ZENODO_RELEASE_CHECKLIST.md (P2) · DATA_RELEASE_MANIFEST.md (P3).

---

## 1. One-screen summary

**Campaign arc:** R23conf internal 5-vendor confirmation (2026-06-09) → **EXT1** browser-tier external round (2026-06-10; ChatGPT GPT-5.5 Pro Extended · Grok Heavy · Gemini 3.5 Thinking; 18 threads, all six papers) → R29 internal + closure wave → **EXT2** in-thread delta (2026-06-10) → R31/R31conf + closure wave → **EXT3** in-thread delta (2026-06-11). Three full external cycles in ~36 hours.

- **Gap metric (genuinely-new substantive findings per cycle): 60 → ~32 → ~27** (index.md exit-criterion note; per-paper EXT3 audits sum P1A ~2.5 · P1B ~3 · P2 ~4–5 · P3 5 · P4 6 · P5 6).
- **Grok Heavy: clean external round, 6/6 ACCEPT at EXT3** (EXT3_BROWSER_MANIFEST.md).
- **Zero substantive physics blockers remain** — every EXT3 truth-audit's exit-criterion assessment states no new physics/math/statistics blocker on any paper; no headline number, null, Fisher form, or NANOGrav statistic was challenged. ChatGPT's residual MAJORs are wording/figure/policy class (§4); Gemini's EXT3 MAJORs are falsified stale-reads/extraction artifacts on every paper it regressed.
- **EXT3 closure waves already landed** (commits 5fdddaba/f5617bce/79eecc0d/73b532dc/53b41d12+7e473380/4f20efcc; final mirror bundle c38e2a87). All six compile clean, latex-audit PASS, artifact_crosscheck PASS.

**Current versions (EXT3-closed, mirrored, tarballed):** P1A **v1A.0.61** · P1B **v1B.0.58** · P2 **v1.7.53** · P3 **v3.1.93** · P4 **v1.0.175** · P5 **v0.1.65-2026-06-11**.

**Readiness per SSOT** (queue.md header, 2026-06-11): P1A 95 · P1B 94 · P2 94 · P3 95 · P4 95 · P5 95 — held at the 95-cap per `feedback_99_pct_readiness_cap`/`feedback_readiness_oscillation`. Index.md exit-criterion note: *"All six papers at exit-criterion modulo Houston sign-off + Zenodo batch + P3 TARGETTYPE recount."*

**What the final 1% means:** the cap structure reserves 95→99 for a clean external round + your sign-off, and 99→100 for your explicit quote in SSOT. Grok's 6/6 ACCEPT plus the truth-audited discount of the ChatGPT/Gemini MAJORs is the campaign's case that the external gate is effectively met; **the remaining gate is you** — the per-paper sign-off lines below, plus the small open-decision lists, the Zenodo batch, and two queued compute items (P3 recount, P1B SN-overlap chains).

---

## 2. Per-paper state

### P1A — ECH structural constraints (arxiv/paper1a_ech_nogo.tex, v1A.0.61, 27 pp)

| Provider | EXT1 | EXT2 | EXT3 |
|---|---|---|---|
| ChatGPT Pro Ext | REJECT | MAJOR ("moved substantially toward publishability") | MAJOR (0 fresh blockers; audit: "zero substantive physics/math blockers… severity-momentum on wording residue") |
| Grok Heavy | MAJOR | ACCEPT | ACCEPT |
| Gemini Thinking | MAJOR | MINOR | MAJOR — **100% falsified** (stale read; G1–G4 all FALSIFIED) |

Headline campaign closures: confabulated Ref[22] Mercuri–Capozziello → Shapiro & Teixeira 2014 CQG 31 185002 (externally verified); pair-exchange sign-error chain deleted — §X.B vanishing now proved Bianchi-only; App C WKB recomputed 10⁻⁶³→10⁻³⁵ eV (~30 orders, not ~60); v1A.0.61 fixed the ALP achromatic-vs-spectral contradiction + β=(α/2M)Δϕ=(αf_a/2M)Δθ mapping + "ECH-independent class tests" retitle + EB photon-coupling conditional + bundle scoping; repro docs harmonized (frozen chains ARE committed, ~257 MB).

OPEN HOUSTON-DECISIONS (EXT3 audit §c + EXT1 ledger carry-forward):
1. Companion-import anchors (Table I, §III, App A) + arXiv IDs at upload (K1/K6, standing) — **default: keep with disclaimers; insert real IDs on submission day**.
2. Bundle tag: tex now scopes "v1A.0.59-bundle unchanged (text-only restamp)"; option to mint a v1A.0.61 tag instead — **default: clause suffices; tag with the Zenodo batch**.
3. Fig. 4 caption "unique surviving minimal-ECH channel under the stated ansätze" — delete vs keep (C6) — **default: keep the R31 qualified phrasing**.
4. PACS retention (C9/HD-3, 3rd raise) — **default: keep for PRD target**.
(HD-1 title "Closure" + HD-2 abstract length: ruled all-default at EXT1, applied.)

Queued compute: none (COMPUTE_QUEUE.md lists no P1A item).

**[ ] Houston approves P1A v1A.0.61 for arXiv**

### P1B — MCMC companion (arxiv/paper1b_mcmc_companion.tex, v1B.0.58, 18 pp)

| Provider | EXT1 | EXT2 | EXT3 |
|---|---|---|---|
| ChatGPT Pro Ext | MAJOR | MAJOR | MAJOR (both fresh "blockers" = 1 falsified soft-wrap + 1 wording/policy; audit: "no substantive physics/statistics blocker") |
| Grok Heavy | MINOR | ACCEPT | ACCEPT (one DOI over-credit discounted) |
| Gemini Thinking | MINOR | MAJOR | **ACCEPT** |

Headline campaign closures: sample count 176,840→176,240 chain-confirmed from raw line-counts; ΔN_eff/H₀ rebooked +0.058±0.179 / 67.78±1.09 after independent chain recompute; v1B.0.58 regenerated parameter_summary_CORRECTED.json from raw chains with S₈=0.8141±0.0085 (all 7 Table I params); "Quintom-B empirical anchor" → "Exploratory w₀wₐ cross-check" pending control chains; 3 live HF dataset URLs into App A + DOI language corrected; root CHANGELOG.md version→commit pin; export-script off-by-one root-caused (column permutation).

OPEN HOUSTON-DECISIONS:
1. DOI/Zenodo minting + clean tagged release (HD-4 + HD-11) — **default: submission day, one sitting (ruled at EXT1)**.
2. Parked disclosures: pairing-swap test not run (G1) + live Planck-only chain mentions (G2) — both ruled adequate-disclosure 3 rounds running — **default: keep parked; optional one-line abstract trim**.
3. Abstract f_a∼M_Pl accommodation-vs-prediction framing (EXT1-F3 lineage) — **default: keep current wording**.

Queued compute: **SN-overlap control chains** (COMPUTE_QUEUE.md §3: DESI DR2+NPIPE+Pantheon+ only and +DES-SN5YR only, to R̂−1<10⁻², on the dedicated MPI pod; the one substantive P1B residual). EXT3 audit recommendation: sign-off can proceed on the demoted "exploratory" framing; fold (w₀,wₐ) shifts into §III/Table II when converged.

**[ ] Houston approves P1B v1B.0.58 for arXiv** (option: hold for control-chain fold-in)

### P2 — f_NL forecast (research/focused_paper_source_integration/02_full_draft.tex, v1.7.53)

| Provider | EXT1 | EXT2 | EXT3 |
|---|---|---|---|
| ChatGPT Pro Ext | MAJOR | MAJOR | MAJOR — the one substantively-earned MAJOR (stale figures + Addis attribution); **all items landed in v1.7.53** |
| Grok Heavy | MINOR | MINOR | ACCEPT |
| Gemini Thinking | MINOR | MINOR | MAJOR — **100% falsified** (G0 stale read; manifest logs its P2 submission silently failed first attempt) |

Headline campaign closures: realistic-range headline honestly rebooked **3–5σ → 2.6–5σ at all 15 sites** + cross-paper sweeps; v1.7.53 regenerated both stale figure assets to template-corrected values (fig2 + bphi_sensitivity — the EXT3 C1 blocker); **Addis σ_GR attribution fixed after ChatGPT's 3-round persistence was vindicated by source fetch** (pattern-052 born here — two prior audit falsifications overturned); Li −35/16 demoted everywhere to single-time-ordering stress test; BF rebooked ~9–14 with r→1 endpoint labeled; SY τ_NL non-sequitur rewritten.

OPEN HOUSTON-DECISIONS:
1. Anomaly-tracer/SDB section placement (C8, 3rd raise, OPINION) — **default: keep current placement**.
2. Zenodo DOI (HD-11, ruled) — checklist prepped at `research/focused_paper_source_integration/ZENODO_RELEASE_CHECKLIST.md`; release tag becomes **paper2-v1.7.53**.
3. EXT3 audit recommends one targeted ChatGPT delta-confirm on the regenerated figures before calling the round clean — **default: run it in-thread on submission day (cheap)**.

Queued compute: none.

**[ ] Houston approves P2 v1.7.53 for arXiv**

### P3 — Multi-survey anomaly catalog (pipelines/p3_anomaly_engine/paper3_draft.tex, v3.1.93)

| Provider | EXT1 | EXT2 | EXT3 |
|---|---|---|---|
| ChatGPT Pro Ext | MAJOR | MAJOR | MAJOR (reduces, after Houston-ruled/stale re-raises, to the queued recount + FM1–FM4 — FM2–FM4+Cm1/Cm4/Gf3/B3 landed in v3.1.92) |
| Grok Heavy | MAJOR | MINOR | ACCEPT |
| Gemini Thinking | MAJOR | MINOR | MAJOR — escalation falsified (4 FALSIFIED + 1 STALE; effective ≈MINOR) |

Headline campaign closures: count correction — catalog-grade **269,317** promoted to abstract lead (HD-7 default applied; prior 264,938 double-removal fixed); "203 novel" → "203 SIMBAD-unmatched" everywhere; eROSITA de-scoped to membership-only n=298 (score axis irreproducible, §II.B/§III.E now consistent — FM3); Planck train/score overlap disclosed with artifact (152/200 training); LAMOST denominator 11,334,161 + 84,433-loss disclosure; "pass every validation test" → enumerated checks; DATA_RELEASE_MANIFEST.md frozen with SHA-256s + per-survey score-schema flags.

OPEN HOUSTON-DECISIONS (EXT3 audit Houston queue):
1. **Title**: plural "Novelty Fractions" + 378,280 lead (NB2/B1, multi-round) — **default on file: singular retitle; recommended: rule now**.
2. **S_BigAE column strip** (Table III/tab:erosita_top still prints the irreproducible scores under a bold do-not-use warning) — now 3-reviewer/2-round consensus to strip — **recommended: YES, strip** (audit recommendation).
3. Ruled-and-standing (no action): Gaia in catalog-grade (HD-8 keep), NANOGrav placement (HD-9 keep), correction-note retention (HD-6 keep), DOI timing (HD-11 submission day).
4. EXT1 ledger carry: LAMOST_DR10 + eROSITA_DR1 citation spot-checks still open for you (or a Perplexity live-fetch leg).

~~Queued compute~~ **RECOUNT LANDED 2026-06-11 (v3.1.93)**: the thrice-flagged DESI TARGETTYPE-restricted recount is computed and disclosed at 5 tex sites — **2,468 science-class matches (1.3% of clusters) → restricted catalog ≈0.9× Liang 2023, NOT 73×; ~98.7% of DESI anomaly clusters on sky/secondary/filler spectra** (artifact `ext3_b2_targettype_recount.json`; control match 99.8%). Remaining queued compute: FM1 scaler-refit robustness check only (pod-side tables; paper states the assumption explicitly with this test queued).

**[ ] Houston approves P3 v3.1.93 for arXiv** (the recount gate you set is now closed)

### P4 — Galaxy chirality catalog (pipelines/p2_chirality/chirality_catalog_paper.tex, v1.0.175, 22 pp)

| Provider | EXT1 | EXT2 | EXT3 |
|---|---|---|---|
| ChatGPT Pro Ext | MAJOR | MAJOR | MAJOR (rests on provenance-gate design + 4 NF majors, all bounded; **NF-M1 closed with compute in v1.0.175**) |
| Grok Heavy | MINOR | ACCEPT | ACCEPT (over-credited on links/tags; hallucinated "v2026.06" — real tag v2026.04) |
| Gemini Thinking | MINOR | ACCEPT | MINOR — demotion **100% extraction-artifact-driven**; true posture ≈ ACCEPT |

Headline campaign closures: NF-M1 flip-identity QC executed (2.9% violations root-caused to raw/eq pipeline-pass mismatch, NOT float32; HC dipole unchanged after QC exclusion: **z=+0.48 vs +0.52 baseline**; 2 artifacts committed); HC stale-label sweep (Fig 7 / conclusion / App E now all carry the p_eq>0.6, N=949,584 qualifier); A95∈(1.0%,1.5%] falsification boundary honest; Data Availability hash two-step stamp→pin per pattern-047. **No reviewer in any of the 3 cycles challenged the headline HC null (+0.41σ), the WLS exclusion (z≈−18), or any committed artifact number** (EXT3 audit).

OPEN HOUSTON-DECISIONS (EXT3 audit Houston queue):
1. Provenance-gate design: keep the two-step stamp→pin convention (with the one-commit self-reference lag) vs cite the pin commit — **default: keep two-step + disclosure clause**.
2. `\artifact` links re-point from mutable `blob/main/` to the pinned commit or DOI — **default: do at submission with the Zenodo DOI** (real reproducibility fix, ChatGPT first to flag).
3. D4 spatial stratification scope (M6) — enhancement, not error — **default: out of scope for v1**.

Queued compute (COMPUTE_QUEUE.md §4): HF model-repo version tag on `bamfai/galaxy-chirality-v2` matching catalog tag **v2026.04** (5 min, HF write token; Grok EF16, confirmed EXT3).

**[ ] Houston approves P4 v1.0.175 for arXiv** (first in submission queue)

### P5 — DESI chirality environment (pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex, v0.1.65-2026-06-11, 30 pp)

| Provider | EXT1 | EXT2 | EXT3 |
|---|---|---|---|
| ChatGPT Pro Ext | MAJOR | MAJOR | MAJOR (reduces to B1+NM2 once triple-falsified k=20 re-raise + Houston-ruled framing removed — **both landed: artifact 29 + Δ-statistics in v0.1.65**) |
| Grok Heavy | MINOR | ACCEPT | ACCEPT |
| Gemini Thinking | MAJOR | MAJOR | MAJOR — **100% unsupported** (Gf1–Gf5 all extraction artifacts; 10-of-12 across EXT2+EXT3) |

Headline campaign closures: thrice-flagged DESIVAST footprint retabulation **executed** (Δf_CW=+0.0018, z=+0.78, p=0.43 — clean null, artifact 29; COMPUTE_QUEUE marks ✅ DONE); Δf_CW/SE/z/p/CI contrast statistics added to Tables VI/X + Bonferroni-5 family re-anchored on the declared primary estimand (|z_Δ|≤1.12, p_Δ≥0.26 all three algorithms); dark-split co-reporting added (void 0.4584 n=469 vs non-void 0.5056 n=5,845, nominal ≈2σ pre-multiplicity); T-Web (Hahn 2007) title nomenclature fix; dual-parent sample ledger 678,945 vs 783,820; ChatGPT's k=20 re-raise closed-with-prejudice (exact k-unbounded rerun in-paper, conclusions invariant).

OPEN HOUSTON-DECISIONS (EXT3 audit Houston queue):
1. **NM1 title count** — title still reads "Across 791,635 DR1 Matched Spirals" but the T-Web cross-check operates on 783,820 env-matched (791,635 − 7,815). Options: "783,820 Environment-Matched DR1 Spirals" or keep 791,635 with "chirality-relevant matched sample" phrasing — **recommended default: 783,820 env-matched**. **Blocks Fig 3 title regen** (COMPUTE_QUEUE.md §5 — minutes of local work after the ruling).
2. Body-prose V-Web→T-Web rename scope (M1; title done, body keeps "V-Web" for HF-slug back-compat) — **default: keep back-compat note, rename at journal stage**.
3. EFT appendix length (M9) — **default: keep (labeled heuristic)**.
4. Paper IV companion dependency + DOI — submission-day (insert P4's real arXiv ID).

Queued compute (COMPUTE_QUEUE.md §5): Fig 3 baked-title regen — blocked solely on decision 1.

**[ ] Houston approves P5 v0.1.65 for arXiv** (after NM1 ruling + Fig 3 regen)

---

## 3. Submission-day runbook

**Order (SSOT/PUBLISH_PLAN.md): P4 → P1A+P1B → P3 → P2 → P5.** P4 first (cleanest external posture, companion anchor for P1A/P5); P1A+P1B same-day pair; P5 last (needs P4's arXiv ID).

**Per-paper common steps:** (1) create the GitHub release tag at the submission version → (2) Zenodo auto-imports via webhook; edit metadata; publish; copy DOI → (3) replace every "DOI inserted at submission"/"pending DOI assignment" placeholder in the tex → (4) populate the `%\preprint{arXiv:XXXX.XXXXX}` marker → (5) recompile + `/latex-audit` + `/artifact-link-verify` → (6) rebuild tarball → (7) upload; after each posting, insert the real arXiv ID at the companion-reference placeholders of the not-yet-submitted papers (the R23conf-noted TODO-SUBMISSION companion placeholders, "posted concurrently on arXiv").

| Step | Paper | Tarball | Specifics |
|---|---|---|---|
| 1 | P4 | `pipelines/p2_chirality/paper4_arxiv_v1.0.175.tar.gz` | Mint Zenodo DOI; re-point `\artifact` blob/main → pinned commit/DOI (open decision §2-P4); HF model tag v2026.04 (COMPUTE_QUEUE §4); recompile+verify |
| 2 | P1A | `arxiv/paper1a_arxiv_v1A.0.61.tar.gz` | Insert P4 arXiv ID at companion anchors; preprint marker `arxiv/paper1a_ech_nogo.tex` L410; mint bundle tag w/ Zenodo batch |
| 3 | P1B | `arxiv/paper1b_arxiv_v1B.0.58.tar.gz` | Insert P1A arXiv ID; App A HF "pending DOI assignment" → minted DOIs; marker `arxiv/paper1b_mcmc_companion.tex` L750; if SN-overlap chains converged, fold (w₀,wₐ) shifts into §III/Table II first |
| 4 | P3 | `pipelines/p3_anomaly_engine/paper3_arxiv_v3.1.93.tar.gz` | TARGETTYPE recount ✅ LANDED (v3.1.93); **flip HF dataset `bamfai/bigbounce-anomaly-catalog` STAGED → public on arXiv posting** + insert Zenodo DOI in DATA_RELEASE_MANIFEST.md header + tex; marker `paper3_draft.tex` L44 |
| 5 | P2 | `research/focused_paper_source_integration/paper2_arxiv_v1.7.53.tar.gz` | ZENODO_RELEASE_CHECKLIST.md steps 1–6 (tag paper2-v1.7.53); replace "DOI inserted at submission"; marker `02_full_draft.tex` L17; optional in-thread ChatGPT figure delta-confirm |
| 6 | P5 | `pipelines/p5_desi_chirality/paper/paper5_arxiv_v0.1.65.tar.gz` | NM1 title ruling → Fig 3 regen (COMPUTE_QUEUE §5) → restamp; insert P4 arXiv ID; mint DOI |

All six tarballs verified on disk at the versions above. Per HD-11 (ruled): mint all Zenodo DOIs in one sitting on submission day.

---

## 4. Standing risks

1. **ChatGPT's residual MAJORs are wording/policy class, not physics** — each EXT3 audit's exit-criterion assessment states this explicitly: P1A "zero substantive physics/math blockers… ChatGPT itself states 'no new fatal error'"; P1B "no substantive physics/statistics blocker is newly identified"; P2 "zero of its residual findings is a physics/derivation blocker"; P3/P4/P5 "no new blockers from any reviewer." The EXT3 closure waves (commits in §1) landed the same-day items; risk is reputational (a 4th ChatGPT MAJOR on momentum), not scientific.
2. **P1B SN-overlap control chains still converging on the pod** (COMPUTE_QUEUE §3; SSOT queue.md "P1B SN-overlap control chains (MPI pod)"). Paper is honest without them ("Exploratory w₀wₐ cross-check," caveat (e) full disclosure) — but submitting P1B before fold-in leaves the one compute-bound residual external.
3. **P3 TARGETTYPE recount not yet run** (thrice-flagged; the only catalogue-definition item not Houston-ruled). Disclosed in-paper as queued, but submitting without it ships a known-stale ~73× benchmark scoping.
4. **Gemini EXT3 is unreliable as a verdict source** — stale reads + extraction artifacts dominate (P1A 4/4 falsified; P2 G0 confabulated version label; P3 escalation rationale fully falsified; P5 10-of-12 artifacts over two rounds; manifest logs silent submission failures). Per the audits: weight Gemini regressions at zero unless source-confirmed.
5. **Closure-introduced regression (pattern-051)** — ~40% of EXT2's genuinely-new findings were our own closure regressions; the EXT3 closure wave is externally unreviewed. Mitigation: pattern-051 5-point self-check ran on the bundle; optional targeted delta-confirms (P2 figures explicitly recommended).
6. **Audit over-falsification (pattern-052)** — the Addis vindication shows a re-raised FALSIFIED finding can be right; re-raise vindication test now mandatory before re-falsifying.
7. **Grok over-credits release/DOI artifacts** (P1B DOI closure falsified two rounds running; P4 "v2026.06" hallucinated tag) — on submission day, verify tags/DOIs at artifact level, never from reviewer text.

---

*Prepared 2026-06-11 from committed sources only. Sign-off lines in §2; readiness moves 95→99 per paper on your check, 99→100 on your quote in SSOT.*
