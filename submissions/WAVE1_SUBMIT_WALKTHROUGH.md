# WAVE-1 arXiv Submission Walkthrough — P4 → P3 → P2

**Order matters:** submit **P4 first, then P3, then P2.** (P4 is the input catalog P5
cites as a companion; P3 and P2 are independent. This order keeps the wave-2
cross-references clean.)

**Verified:** 2026-07-11 (program-exit restamp — all 5 papers re-stamped to today's date + a fresh patch version, no content change). Every bundle below is rebuilt from the current source at the exit versions and standalone re-extract+compile-verified (0 errors, 0 undefined refs; the .tex inside each tarball matches the repo source; page 1 shows "July 11, 2026"). All 5 wave bundles (P4/P3/P2/P5/P1U) rebuilt 2026-07-11 at the restamp versions.
- P4 `arxiv_p4_v1.0.236.tar.gz` — **rebuilt 2026-07-11** at v1.0.236 (restamp) — standalone exit 0, 0 undef, **35 pages**; page 1 "July 11, 2026". Served-PDF md5 `fd34a3ed45cd0425dd984aee03d97041`; tarball md5 `2742b0dd8bc7af4bbe83f0b287e0bc96`. 20 bare-filename entries. Grok EXT literal ACCEPT + Claude INT ACCEPT.
- P3 `arxiv_p3_v3.1.153.tar.gz` — **rebuilt 2026-07-11** at v3.1.153 (restamp) — standalone exit 0, 0 undef, **37 pages**; page 1 "July 11, 2026". Served-PDF md5 `9b7391ed5438f43d7f2a1499567902e8`; tarball md5 `af0045ac92d796341ee756f012b59ab9`. Subdir prefix `arxiv_p3_v3.1.153/`.
- P2 `arxiv_p2_v1.7.113.tar.gz` — **rebuilt 2026-07-11** at v1.7.113 (restamp; .bbl regenerated via bibtex) — standalone exit 0, 0 undef, **37 pages**; page 1 shows "July 11, 2026". Served-PDF md5 `de34d7ac50d3f1f3cc3d2ef35f3b409b`; tarball md5 `33dfb04a55b2c2a96412acf632d664bd`. `./`-prefixed (`02_full_draft.tex` + `.bbl` + `focused_paper_refs.bib` + revtex `02_full_draftNotes.bib` control file + 5 figs + `bphi_sensitivity.pdf`).
- Placeholder scans: all three CLEAN (only commented-out `%\preprint{arXiv:XXXX.XXXXX}` lines, which never render). No dangling companion-paper placeholders. P3 still carries one optional `\emph{DOI inserted at submission}` Zenodo sentence (see P3 note below).
- Abstracts: the paste blocks below are the arXiv-form-safe (<1920 chars) versions; the H17→W-wave convergence tail changed **no headline number** (−35/16 unchanged in P2 final tex; all counts stable — "0 genuinely-new findings"), so the science text in every wave-1 abstract remains valid at the final versions. (P4 abstract 1583 chars, P3 1559 chars, P2 1583 chars — all ≤1920, re-checked against final source.)

**Wave-2 bundles (rebuilt 2026-07-11 to exit versions, for the P5+P1U wave):**
- P5 `arxiv_p5_v0.1.121.tar.gz` — **rebuilt 2026-07-11** at v0.1.121-2026-07-11 (restamp), standalone exit 0, 0 undef, **45 pages**; page 1 "July 11, 2026". Served-PDF md5 `6422770cccbd81a8c7c35375b9781840`; tarball md5 `7ec341c5fa9932be0f855325fbd37aca`. Subdir prefix `p5_arxiv_v0.1.121/`. Inline `thebibliography` (no bibtex pass; .bbl carried from source; revtex `p5_desi_chiralityNotes.bib` control file included). First EXT ACCEPT of the program (Grok, v0.1.117) + Claude INT ACCEPT.
- P1U `arxiv_p1_unified_v1U.0.13.tar.gz` — **rebuilt 2026-07-11** at v1U.0.13 (restamp; .bbl regenerated via bibtex), standalone exit 0, 0 undef, **60 pages**; page 1 "July 11, 2026". Served-PDF md5 `7ba02c4a178f5de0dc6332bd7265a228`; tarball md5 `5a06e6b9385425827959122aca8415bb`. `./`-prefixed; includes both `.bib` files + `scripts/*.py` (P1A+P1B merged; there is NO standalone P1B submission).

---

## STEP 0 — Endorsement / submit-rights pre-check (do ONCE, before P4)

1. Go to **https://arxiv.org/user** (log in as the submitter — houston@hubify.com is the account on file).
2. Confirm you can **start a new submission** and that **astro-ph** appears in your allowed categories.
   - If arXiv shows an **endorsement required** notice for astro-ph.CO / astro-ph.IM / astro-ph.GA / gr-qc: request endorsement from a qualifying author (someone who has recently submitted to that archive) before proceeding. First-time submitters to a category often need this; it can take a day, so check now.
3. Confirm your **name + affiliation** on the account: `Houston Golden`, Independent Researcher, Los Angeles, California, USA.

If Step 0 is clean (astro-ph enabled, no endorsement block), proceed. If blocked, resolve endorsement first — nothing below works until you can submit to astro-ph.

---

## PAPER 1 — P4 (submit FIRST)

**Upload:** `submissions/P4/arxiv_p4_v1.0.236.tar.gz`
(Full paste-ready field text also lives in `submissions/P4/ARXIV_METADATA.txt`.)

### 1. Start submission → upload the tarball
arxiv.org/submit → "Start a new submission" → upload `arxiv_p4_v1.0.236.tar.gz`.
Let arXiv run AutoTeX. It should compile to **35 pages**.

### 2. Metadata — paste these blocks

**Title:**
```
A Null Chirality Dipole in 8.5 Million DESI Galaxies from Equivariant Deep Learning
```

**Authors:**
```
Houston Golden
```
(Affiliation "Independent Researcher, Los Angeles, California, USA" goes in the affiliation field, not the author name. Submitter email is on the account, not the authors field.)

**Abstract** (1583 chars, arXiv-safe — paste exactly):
```
We measure the large-scale chirality dipole of spiral galaxies and find it consistent with null. Our primary estimator, a real-space dipole fit to the high-confidence equivariant sample (N ~ 9.5x10^5 spirals), gives +0.41 sigma (moment-z against an isotropic pixel-permutation null; empirical-rank p = 0.31); a block-bootstrap template fit disfavors a clean cosmological dipole at the 1.7% reference amplitude (lower end of Shamir's 1.7%-4.0% range) at z ~ -18. This ell=1 observable is parity-even, not a direct parity-violation test. The measurement rests on the largest chirality-labeled galaxy catalog to date: 8,474,531 DESI Legacy DR8 galaxies classified by a flip-equivariant Vision Transformer (3,201,160 spirals), released publicly with model weights and reproducibility scripts. The p_eq > 0.6 cut is pre-specified: the null is robust across the high-confidence regime while the low-confidence tail (p_eq <= 0.5) carries a systematics-attributed excess. Two limitations are explicit. First, the MASTER pseudo-C_ell channel on this patchy footprint is a systematics diagnostic, not an independent null: a monopole-only generative null reproduces 99.32% of the raw pre-MASTER ell=1 power, and residuals after deconvolution are attributed to survey systematics via an eight-anchor battery, not claimed as detections. Second, the quoted sigma values come from distinct null procedures and are not directly comparable as detection significances. Falsification: a future real-space dipole at >= 5 sigma with amplitude A >~ A_95 in (1.0%, 1.5%] would be in tension with this null.
```

**Primary category:** `astro-ph.CO`
**Cross-list:** `astro-ph.GA`

**Comments:**
```
35 pages, 12 figures; data + code at https://github.com/Hubify-Projects/bigbounce
```

**License:** **CC BY 4.0** (recommended — consistent with the public data + weights
release). Conservative alternative: arXiv's standard perpetual non-exclusive license.
→ **Houston decision:** confirm CC BY 4.0 at upload time.

### 3. Preview checks (before hitting Submit)
- Open the arXiv-generated PDF preview.
- **Page 1** shows version/date consistent with v1.0.236 (title-block emits the timestamp; no stray version tag).
- **Figures render** — spot-check that figure pages show images, not blank boxes (the tarball is ~25 MB precisely because the figures are heavy; if a figure is missing, do NOT submit — reping the loop).
- Title, authors, abstract, categories match the blocks above.

### 4. Submit → record the ID
Submit. arXiv assigns `arXiv:25XX.XXXXX`. **Write it here:**
```
P4 arXiv ID: __________________
```

---

## PAPER 2 — P3 (submit SECOND)

**Upload:** `submissions/P3/arxiv_p3_v3.1.153.tar.gz`
(Paste-ready fields also in `submissions/P3/ARXIV_METADATA.txt`.)

> **BEFORE UPLOAD — one optional Houston-gated edit (Zenodo DOI):**
> The paper body (`pipelines/p3_anomaly_engine/paper3_draft.tex`, ~line 1542) has the
> sentence `\emph{DOI inserted at submission}` reserving a spot for a Zenodo DOI.
> - If you want the DOI in v1: mint the Zenodo DOI for the HF dataset, replace that
>   sentence, recompile, and rebuild the tarball as `arxiv_p3_v3.1.153.tar.gz` before upload.
> - If you'd rather ship now and add the DOI in a v2: the current bundle is submittable
>   as-is (the sentence reads cleanly; it is not a broken placeholder). Your call.

### 1. Start submission → upload
Upload `arxiv_p3_v3.1.153.tar.gz`. Compiles to **37 pages**.

### 2. Metadata — paste these blocks

**Title:**
```
A Multi-Survey Autoencoder Anomaly-Candidate Catalog: 268,519 Reconstruction-Outlier Sources from a Native-Trained Scan of 37.3 Million Spectra and Map Patches
```

**Authors:**
```
Houston Golden
```

**Abstract** (1559 chars, arXiv-safe — paste exactly):
```
We present a multi-survey autoencoder anomaly catalog produced by applying the BigAE framework to 37.3 million sources and CMB map patches across six archives (DESI DR1, SDSS DR18, LAMOST DR10, eROSITA DR1, Planck, NEOWISE; ACT DR6 quarantined). The primary deliverable is a validated subset of 268,519 unique anomaly candidates (a process-volume figure, i.e. candidates surviving per-survey validation gates, not confirmed physical detections); its like-for-like science-target benchmark is 2,468 DESI anomaly clusters (~0.92x the largest published single-survey catalog). The full inclusive Path-C catalog contains 377,482 anomalies; the validated subset excludes a LAMOST exploratory tier (98% blue-excess training-bias artifact), eROSITA (irreproducible score axis), and synthetic Gaia. DESI clears three independent gates: 5-fold cross-validation Jaccard 0.862, OOD Jaccard 0.732, and injection-recovery 99-100% at 5 sigma for the broad/extended class; SDSS and Planck likewise pass injection-recovery gates. An archival cross-match of DESI top-1,000 anomalies against 18 all-sky catalogs yields a genuine novelty fraction of 17.8% +/- 1.2%. Two cosmological applications are secondary demonstrations: a multi-tracer f_NL bias measurement yields sigma(f_NL) = 8.14 (envelope [3.92, 8.98]), and a NANOGrav 15-yr KDE MCMC yields gamma = 2.567 +/- 0.382, placing the matter-bounce prediction gamma = 3.0 at +1.13 sigma. The catalog, model weights, and reproducibility scripts are released at https://huggingface.co/datasets/bamfai/bigbounce-anomaly-catalog.
```

**Primary category:** `astro-ph.IM`  (instrumentation/methods — this is a catalog + ML-methods paper)
**Cross-list:** `astro-ph.CO`, `astro-ph.GA`

**Comments:**
```
37 pages, 12 figures; data + code at https://github.com/Hubify-Projects/bigbounce
```

**License:** **CC BY 4.0** (recommended). Conservative alt: arXiv non-exclusive.

### 3. Preview checks
- Page 1 shows July 11, 2026 / v3.1.153.
- Figures render (12 figures, mix of PNG + PDF).
- Title/authors/abstract/categories match.

### 4. Submit → record the ID
```
P3 arXiv ID: __________________
```

### P3 DATA DEPENDENCY — HF dataset (already public, NO flip needed)
The paper promises a public HF dataset `bamfai/bigbounce-anomaly-catalog` (weights +
reproducibility scripts + parquets). **Checked via the HF API on 2026-07-09: it is
already PUBLIC** (`private: false`, `gated: false`) — **no visibility flip is
required at submission time.** File listing was inspected: data parquets, dedup
JSONs, README, and result dirs only — no secrets.

*If it is ever found private again, the staged flip command (Houston runs it; token
read from `.env.local`, never printed) is:*
```bash
HF_TOKEN=$(grep -m1 '^HF_TOKEN=' .env.local | cut -d= -f2-)
curl -s -X PUT -H "Authorization: Bearer $HF_TOKEN" -H "Content-Type: application/json" \
  https://huggingface.co/api/datasets/bamfai/bigbounce-anomaly-catalog/settings \
  -d '{"private": false}'
```

---

## PAPER 3 — P2 (submit THIRD)

**Upload:** `submissions/P2/arxiv_p2_v1.7.113.tar.gz`
(Paste-ready fields also in `submissions/P2/ARXIV_METADATA.txt`.)

### 1. Start submission → upload
Upload `arxiv_p2_v1.7.113.tar.gz`. Compiles to **37 pages**.
(Note: the source `\date{}` reads "July 11, 2026"; the real version is v1.7.113.
arXiv shows its own submission date, so this is cosmetic.)

### 2. Metadata — paste these blocks

**Title:**
```
Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook
```

**Authors:**
```
Houston Golden
```

**Abstract** (1583 chars, arXiv-safe — paste exactly):
```
A matter-dominated contracting phase preceding a nonsingular bounce predicts a minimally parameterized local-type non-Gaussianity f_NL^local = -35/16 = -2.1875, opposite in sign and ~2 orders of magnitude larger than the single-field slow-roll value. Our central contribution resolves the long-standing eight-year Cai-Li factor-of-two discrepancy (Cai et al. -35/8 vs. Li et al. -35/16) in favour of -35/16: re-summing Cai et al.'s own four cubic-action vertices at epsilon = 3/2 gives -35/16 in the squeezed limit, matching Li et al.'s independent general-c_s result at c_s = 1, while the published -35/8 traces to a spurious +(99/128) sum_i k_i^3 term in Cai et al.'s final combined polynomial (both share the identical f_NL = 10A/(3 sum k_i^3) convention, so it is an arithmetic error, not a convention difference). We then recast published SPHEREx and MegaMapper forecasting power onto this prediction: this is a sensitivity recast of a single external forecast, not an independent one. After template-mismatch correction the SPHEREx bispectrum significance for f_NL = -35/16 is ~2.6-2.75 sigma optimistic, reducing to a realistic ~1.3-2.75 sigma after the full systematic budget. A closed-form Bayesian comparison, validated across three 10^5-realization Monte Carlo ensembles, gives illustrative (prior-dependent) Bayes factors favouring the bounce over tuned multifield competitors. The forecast is conditional on faithful cubic-order bispectrum transmission through the bounce (derived here to a bounded ~10^-3 systematic via single-clock LQC superhorizon zeta-conservation).
```

**Primary category:** `astro-ph.CO`
**Cross-list:** `gr-qc`
→ **Houston decision:** `hep-th` is a defensible *additional* cross-list (bounce
cosmology has hep-th readership). Task spec is CO + gr-qc; add hep-th only if you want
the extra reach.

**Comments:**
```
38 pages, 6 figures; data + code at https://github.com/Hubify-Projects/bigbounce
```

**License:** **CC BY 4.0** (recommended). Conservative alt: arXiv non-exclusive.

### 3. Preview checks
- Figures render (6 figures; verify fig1/fig4 show the corrected `-35/16` labeling,
  not the retracted `-35/8`).
- Title/authors/abstract/categories match.

### 4. Submit → record the ID
```
P2 arXiv ID: __________________
```

---

## AFTER ALL THREE — wrap-up

### Zenodo DOI note
No DOI is required to submit. Mint a Zenodo DOI (for the GitHub repo and/or the HF
dataset) at your convenience and add it as a **journal-ref/DOI** on the arXiv abstract
page, or in a v2. For P3 specifically, minting it *before* upload lets you fill the
reserved `\emph{DOI inserted at submission}` sentence (see P3 note above); otherwise
add in v2.

### Post-assignment cleanup (each paper, optional v2)
Once arXiv assigns each ID, you may uncomment and fill the `%\preprint{arXiv:XXXX.XXXXX}`
line in each source `.tex` for the version-of-record, then rebuild. Not required for v1.

### Wave-2 handoff (P5 + P1U)
**Paste the three assigned arXiv IDs (P4, P3, P2) — plus P1B's, if a standalone P1B is
ever posted — back to the loop; wave-2 insertion is automated by
`tools/insert_arxiv_ids.sh` (REPO path corrected to CODE_YOU 2026-07-10; dry-run
green).** Wave-2 papers are **P5** (`arxiv_p5_v0.1.121.tar.gz`, v0.1.121, 45 pp) and the
**unified Paper 1 P1U** (`arxiv_p1_unified_v1U.0.13.tar.gz`, v1U.0.13, 60 pp — P1A+P1B
merged; there is NO standalone P1B submission). Both cross-cite the wave-1 IDs:
- **P5**: the `\paperIVarxiv` macro (`p5_desi_chirality.tex:24`, currently
  `arXiv:XXXX.XXXXX`) resolves to **P4's** assigned ID.
- **P1U**: five `%% TODO-SUBMISSION` companion bib entries in `arxiv/references.bib`
  (see the list below) get the wave-1 IDs; regenerate the `.bbl` and recompile so the
  IDs render.

### Only-remaining manual fills (everything else is automated)
These are the **sole** placeholders a human/loop must fill at submission — all others in
the sources are commented-out `%\preprint{...}` lines that never render:

| # | File / location | Placeholder | Fill with |
|---|---|---|---|
| 1 | `arxiv/references.bib` L1114–1118 `Golden2026P1a` | `[arXiv:XXXX.XXXXX --- ID inserted at coordinated submission]` | **P1U's OWN** forward-ref — **LEAVE AS-IS** (P1U's ID doesn't exist until P1U itself is assigned; fill at P1U v2 or leave) |
| 2 | `arxiv/references.bib` L1130 `Golden2026P1b` | `note = "Companion paper, posted concurrently on arXiv"` | P1B's ID if a standalone P1B is posted; else leave (P1B folded into P1U) |
| 3 | `arxiv/references.bib` L1138 `Golden2026P2` | same companion note | **P2** wave-1 ID |
| 4 | `arxiv/references.bib` L1146 `Golden2026P3` | same companion note | **P3** wave-1 ID |
| 5 | `arxiv/references.bib` L1154 `Golden2026P4` | same companion note | **P4** wave-1 ID |
| 6 | `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex:24` | `\newcommand{\paperIVarxiv}{arXiv:XXXX.XXXXX}` | **P4** wave-1 ID |
| 7 (optional) | `pipelines/p3_anomaly_engine/paper3_draft.tex` (~L1654) | `\emph{DOI inserted at submission}` | Zenodo DOI (mint-before-upload or add in v2) |
| 8 (optional) | `research/.../02_full_draft.tex` (comment L644) | Zenodo `(DOI inserted at submission)` note | Zenodo DOI (optional) |

Fills 3–6 are exactly what `tools/insert_arxiv_ids.sh --p4 … --p3 … --p2 …` performs
(it also regenerates the `.bbl`, mirrors PDFs, and rebuilds the bundle). Fill 1 stays as
the self-placeholder; fill 2 is inert while P1B is folded into P1U.

---

## Program-exit state — honest snapshot (2026-07-11)

**All five papers are past the directive-K two-clean-waves convergence bar.** The
edit-loop program has EXITED. Clean-wave streaks at exit: **P1U 2 · P2 3 · P3 4 · P4 4 ·
P5 2**. The H17 base wave *did* surface real errors (P4 Shamir factor-of-2, P2
vertex-sign, P3 k-fold/37.3M bookkeeping, P5 primary-estimand seam, P1U Check-D sign),
and **each was closed by a real, source-cited edit** at the versions bundled here; the
subsequent W-waves surfaced **0 genuinely-new real findings** — every remaining MAJOR/
MINOR is a source-cited re-flag of already-disclosed content (pattern-066 referee
variance). Verdict highlights (literal, read from raw text in `project-context/peer-reviews/`):
- **Two literal EXT ACCEPTs — the program's first two:** Grok EXT `VERDICT: ACCEPT` on
  **P5** (v0.1.117, `EXT_real/H17_2026-07-10/final/P5_grok_final.md`) and on **P4**
  (v1.0.235, W1-EXT).
- **Claude-subagent INT ACCEPTs:** **P4 and P5** on retest after closures. P1U/P2/P3
  stay at MINOR/MAJOR — **no third Claude ACCEPT was recorded**; do not claim one.
  OpenAI's INT verdict on **P5 moved REJECT → MAJOR** on native-PDF v0.1.120 — its first
  non-REJECT on that paper.
- **Remaining below-ACCEPT verdicts are pattern-066 oscillation**, not correctable
  errors: ChatGPT holds a structural REJECT on P1U/P2/P3/P4 — recorded verbatim,
  dispositioned (never flipped) in `project-context/peer-reviews/DISPOSITIONS/P{1U,2,3,4,5}.md`.
- **Convex honest caps (2026-07-11):** P1A/P1U 62, P1B 56, P2 74, P3 62, P4 74, P5 68 —
  **not 96/98/99.**

**Two-clock note.** There are two independent completion clocks. The **arXiv clock** is
now Houston-gated only: the kit is rebuilt + standalone-verified at the exit versions, so
it is one set of **Houston submission clicks** away (minutes). The **journal clock** runs
on **human referees** (months, external) and is the only remaining path to lift the
LLM-referee scope items — no further autonomous editing clears them.

---

## Decisions Houston must make (flagged)
1. **License** for all: CC BY 4.0 (recommended) vs arXiv non-exclusive. Default CC BY 4.0.
2. **P2 hep-th** cross-list: add as a second cross-list, or keep CO + gr-qc only.
3. **P3 Zenodo DOI timing**: mint-before-upload (fills the reserved sentence, needs a
   `.153` rebuild) vs ship-now-add-in-v2.
