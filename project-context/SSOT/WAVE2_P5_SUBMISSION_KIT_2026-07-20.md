# Wave-2 + P5 arXiv Submission Kit — P2, P4, P5

> **⚠️ SUPERSEDED / HISTORICAL — DO NOT USE FOR SUBMISSION (2026-08-04).**
> This kit is retained for provenance only. The current authoritative source
> is `project-context/SSOT/FINAL_APPROVAL_SUBMISSION_BOARD_2026-08-03.md`,
> together with the 2026-07-24 per-paper kits (`PRD_SUBMISSION_KIT_P2_2026-07-24.md`
> for P2) and the current P4/P5 portal kits
> (`pipelines/p2_chirality/APJS_PORTAL_KIT_v1.0.274.md`,
> `pipelines/p5_desi_chirality/paper/AJ_PORTAL_KIT_v0.1.147-2026-08-03.md`).

## Prepared 2026-07-20 | git HEAD `f9c25de6` | Goal: a minutes-long click session for Houston

> **2026-07-22 ADDENDUM — pre-arXiv confirmation wave; P2 → v1.7.128, P4 →
> v1.0.271, P5 → v0.1.142-2026-07-22.** The 2026-07-22 pre-arXiv confirmation
> wave (18 exact-PDF INT legs: 6 papers × Grok-API + Gemini-API + Claude-Opus
> subagent) truth-audited every wave-2/P5 paper and closed all genuinely-new-
> real findings same-day. Every tarball reference below is superseded:
> **P2 tarball is now `paper2_arxiv_v1.7.128.tar.gz`** (11 pp, md5
> 2b8f63bb8221e6f4f783db35c73221eb; 5 genuinely-new-real closures — a σ
> reff-rounding precision fix, a Planck-consistency σ rounding fix, the
> real-space baseline corrected 0.687→0.688 with an explicit
> bounce-template bias-marginalized-baseline label, and a "rounded to
> 2.63σ" wording fix). **P4 tarball is now `paper4_arxiv_v1.0.271.tar.gz`**
> (32 pp, md5 80eda096226540d8a44d5f1b3202798f; 3 genuinely-new-real
> closures — excluded-rows label, epoch wording, parity-bound hardening).
> **P5 tarball is now `paper5_arxiv_v0.1.142-2026-07-22.tar.gz`** (42 pp,
> md5 a70307b01058d3688bc69758847d414f; 2 genuinely-new-real
> presentation/transparency closures). All three re-verified by standalone
> recompile (0 undef-refs); no science number changed on any paper;
> readiness caps hold (80/80/74). Full verdict matrix, truth audits, and
> Convex sync details: `project-context/SSOT/index.md` CONFIRMATION-WAVE
> 2026-07-22 banner and `project-context/peer-reviews/INT_v3/ROUND_2026-07-22-
> <P>-*-CLAUDESTACK-CONFIRM/` per paper. The hard sequencing constraint below
> (P5 depends on P4's arXiv ID) is unaffected by this wave.

> **2026-07-20 later update — P2 and P4 tarballs rebuilt at the DOI-bearing
> versions.** Both papers' `\preprint`/`\paperVersion` advanced to embed their
> real minted Zenodo archival DOIs: P2 `v1.7.125` → `v1.7.126` (DOI
> `10.5281/zenodo.21461881`, concept `10.5281/zenodo.21461880`); P4 `v1.0.268`
> → `v1.0.269` (DOI `10.5281/zenodo.21461899`, concept `10.5281/zenodo.21461898`).
> The submission tarballs below are rebuilt and standalone-verified at these
> versions, commit-bound to `bdb3d5cceb61096a7ca9aab279e80a2d379ff15c`:
> `paper2_arxiv_v1.7.126.tar.gz`, `paper4_arxiv_v1.0.269.tar.gz`. **P5 is
> unchanged** — still gets its own back-patch (§4) at submit time, per this
> kit's original plan; P5's tarball/version below remain as originally built.
> See `project-context/SSOT/queue.md` for the closed row.

This kit is the single source for the wave-2 (P2, P4) + P5 arXiv drop. Everything
below is **verified against the current tex sources at build commit `f9c25de657d1bcbc3ef0ba729133a00019d71fa3`**
(titles, abstracts, versions, categories extracted directly from the live `.tex`).
Format mirrors `WAVE1_SUBMISSION_KIT_2026-07-19.md`.

> **HEAD note:** the tarballs are commit-bound to build commit `f9c25de6`. Repo
> HEAD has since advanced (`395a6a85` committed the P2/P4 tarballs, `397671bf`
> closed consistency-audit items); **no paper source (tex/figures/config) changed
> between `f9c25de6` and current HEAD**, so all three tarballs remain current. The
> P2 and P4 tarballs are already committed (in `395a6a85`); this kit commit adds
> the P5 tarball, all three `*.proof.json` receipts, and the kit itself.

### The one hard sequencing constraint (read this first)
**P5 depends on both wave-2 papers.** P5's reference list contains a companion
citation to **Paper IV = P4** and a (currently uncited, dangling) companion
citation to **Paper II = P2**. Therefore:

> **Submit P2 and P4 FIRST (any order between them), capture both returned arXiv
> IDs, back-patch them into the P5 source (§4), rebuild + re-verify the P5
> tarball, THEN submit P5.** Do not submit P5 before P2 and P4 have IDs.

P2 and P4 are mutually independent and self-contained — no cross-citation between
them, submit in either order.

---

## 0. TL;DR click order

```
1. Confirm arXiv account + endorsement for astro-ph.CO, astro-ph.GA, astro-ph.IM, gr-qc (§3.1)
2. Decide license per paper (§3.3) — P2/P4 default CC-BY-4.0; P5 unresolved (Houston picks)
3. Submit P2 tarball + metadata (§1, §2)  -> record arXiv ID  = <P2_ARXIV_ID>
4. Submit P4 tarball + metadata (§1, §2)  -> record arXiv ID  = <P4_ARXIV_ID>
5. Back-patch <P2_ARXIV_ID> + <P4_ARXIV_ID> into P5 tex (§4), rebuild + re-verify P5 tarball
6. Submit patched P5 tarball + metadata (§1, §2)
```

---

## 1. Exact tarballs — VERIFIED (standalone tectonic compile, isolated temp extract)

Built with `tools/build_exact_arxiv_bundle.py --paper <P> --git-commit f9c25de6… --write`
(deterministic, commit-bound, mtime=0). Every bundle asset was confirmed
tracked-and-clean at HEAD before the build. Each tarball was then extracted into
an isolated temp dir and compiled with **tectonic** (`--keep-logs`), page count
read with `pdfinfo`.

| Paper | Version | Tarball (in `project-context/SSOT/arxiv_tarballs/`) | Pages | Figs | Compile | Status |
|-------|---------|------------------------------------------------------|-------|------|---------|--------|
| **P2** | v1.7.126 | `paper2_arxiv_v1.7.126.tar.gz` | **11** | 2 | exit 0, **0 err / 0 undef-ref**, 0 overfull | **REBUILT + VERIFIED 2026-07-20** (DOI-bearing version) |
| **P4** | v1.0.269 | `paper4_arxiv_v1.0.269.tar.gz` | **32** | 9 | exit 0, **0 err / 0 undef-ref**, 1 overfull (64.4 pt — cosmetic, see note) | **REBUILT + VERIFIED 2026-07-20** (DOI-bearing version) |
| **P5** | v0.1.141-2026-07-16 | `paper5_arxiv_v0.1.141-2026-07-16.tar.gz` | **42** | 9 | exit 0, **0 err / 0 undef-ref**, 0 overfull | **BUILT + VERIFIED** (pre-back-patch; rebuild after §4) |

Checksums (for provenance / re-verify):

| Paper | tarball sha256 | tarball md5 | bytes |
|-------|----------------|-------------|-------|
| P2 | `b37819ab6fa95dd6024680918b8e952a2c8d413c50d56cd6c669cd8749b20f6d` | `69dea2b63cca7ba8e3f2d8638f64044d` | 222,261 |
| P4 | `bfd3fc2c251096bdb3f73daae2e623f363f19df98a8fa263101af4de0781c695` | `83653ccf9e7339709d8c89896cba8429` | 27,128,713 |
| P5 | `1640ee67ccf7e103c329cb3a3eace3d4bd4214eefd24724dc270a3e16735574e` | `f3b62504c501e64828ae7601a3d38d8d` | 1,028,887 |

Per-tarball verification receipts written alongside each tarball as `*.proof.json`
(schema `bigbounce-standalone-arxiv-proof/v1`). P2/P4: rebuilt 2026-07-20 at the
DOI-bearing versions, verifier `doi-tarball-rebuild`, commit-bound to
`bdb3d5cceb61096a7ca9aab279e80a2d379ff15c` — `paper2_arxiv_v1.7.126.proof.json`,
`paper4_arxiv_v1.0.269.proof.json`. P5: original 2026-07-20 build, verifier
`wave2-p5-submission-kit` — `paper5_arxiv_v0.1.141-2026-07-16.proof.json`.

**Tarball contents (what arXiv receives):**
- **P2**: `02_full_draft.tex`, `02_full_draft.bbl` (bundled — arXiv uses it directly, no bibtex needed), `focused_paper_refs.bib`, `fig1_shape_function.png`, `fig5_inflation_comparison.png`. Class: `revtex4-2` (in arXiv's TeXLive — not bundled).
- **P4**: `chirality_catalog_paper.tex`, `chirality_catalog_paper.bbl`, **`aastex701.cls`** (bundled — this is what makes it standalone), and 13 figure files (`fig_raw_vs_eq.png`, `fig_harmonic_completeness.pdf`, `fig_class_pie.png`, `fig_spiral_density.png`, `fig_confidence_dist.png`, `fig_sky_map.png`, `fig_bootstrap_null.png`, `fig_gallery_cw.png`, `fig_equivariance_demo.png`, `fig_gallery_ccw.png`, `fig_gallery_notspi.png`, `fig_multipoles.png`). All 13 figures confirmed bundled and rendered in the 32-pp compile.
- **P5**: `p5_desi_chirality.tex`, `p5_desi_chiralityNotes.bib` (**inert** — a BibDesk notes sidecar; P5's printed bibliography is a manual inline `\begin{thebibliography}` block, so arXiv runs no bibtex/biber for P5), and 9 figure PNGs. Class: `revtex4-2` (in arXiv's TeXLive).

> **P4 overfull note (honest disclosure):** exactly 1 overfull hbox, 64.4 pt, at
> lines 1650–1651 — a long inline `\texttt{}` file path (`build_dataset/…`) that
> reaches into the gutter. No content is lost, no column-to-column overlap. arXiv
> accepts this. Not a submission blocker; if Houston wants it gone it is a
> one-line cosmetic `\allowbreak`/`\path` micro-fix, not a wave-2 gate.

> **P5 rebuild note:** the P5 tarball above is the **pre-back-patch** build (Paper
> IV/II still read "in preparation"). After inserting the real P2 + P4 arXiv IDs
> (§4) you MUST rebuild and re-verify the P5 tarball; its checksums will change.
> The build command is in §4.

---

## 2. Ready-to-paste arXiv metadata

Author (all three): **Houston Golden** — ORCID **0009-0008-5616-5994** —
affiliation *Independent Researcher, Los Angeles, California, USA*.

---

### P2 — `paper2_arxiv_v1.7.126.tar.gz`

- **Title:** `The Exact Matter-Contraction Non-Gaussian Amplitude: Four-Vertex Derivation and Conditional Large-Scale-Structure Mapping`
- **Primary category:** `astro-ph.CO`  ✅ **recommended.** Rationale: the paper's headline products are a **primordial non-Gaussianity amplitude** (f_NL local-type from a matter-contraction phase, correcting a literature value) and a **SPHEREx multi-tracer bispectrum detectability forecast** — the exact keyword/audience space (f_NL, bispectrum, SPHEREx, PNG bias b_phi) is astro-ph.CO. The paper explicitly states "the primary contribution is the exact contraction-phase amplitude derivation," a cosmological-perturbation-theory result.
- **Cross-list:** `gr-qc`  (the derivation is set in a nonsingular bouncing/contracting early-universe GR background; the bounce-cosmology community lives on gr-qc).
- **Honest alternative:** `gr-qc`-**primary** with `astro-ph.CO` cross is fully defensible if Houston wants the formal-bounce/early-universe-gravity audience as the front door rather than the LSS-forecast audience. The science is identical either way; this is an audience-routing choice. **Recommendation stands at astro-ph.CO primary** because the observable forecast (SPHEREx) and the f_NL correction are what readers will search for.
- **Comments field:** `11 pages, 2 figures. Prepared in REVTeX (PRD format). Code and reproducibility artifacts at github.com/Hubify-Projects/bigbounce`
- **License:** config default `cc-by-4.0` (matches the CC-BY reproducibility artifacts). Confirm in §3.3 or switch to arXiv non-exclusive.
- **Archival DOI:** the manuscript now embeds the real minted Zenodo archival DOI `10.5281/zenodo.21461881` (concept `10.5281/zenodo.21461880`) in the Data and Code Availability section — no longer deferred to camera-ready (§3.4).
- **Abstract (plain-text for webform):**

```
A matter-dominated contracting phase gives a local-type non-Gaussian amplitude
f_NL^local = -35/16 = -2.1875 before the nonsingular transition. We derive this
contraction-phase coefficient for the stated epsilon = 3/2 background and cubic
action by re-summing all four cubic vertices, re-expand the result in the ordered
symmetric basis, and obtain the unique coefficients (3, 1, -9, 5, -33, 9);
independent checks use Cai et al.'s order-grouped expressions and Li et al.'s
general-c_s formula. The result corrects the unreproduced printed -35/8 literature
value. For orientation only, and conditional on faithful cubic-order transmission
through a specified bounce completion, we map the published Heinrich et al. SPHEREx
multi-tracer bispectrum sensitivity through the exact shape. Its flat-grid amplitude
recovery is r = 0.8354 and shape cosine is r_cos = 0.9817; the corresponding rounded
arithmetic map is 2.63 sigma before additional nuisance marginalization. A
channel-native surrogate-covariance check spans 3.5 sigma with nuisances fixed, 3.1
sigma after marginalizing the relativistic-projection amplitude A_GR, 2.3 sigma with
an explicit 30% theory prior on the PNG bias-response coefficient b_phi, and 0.4 sigma
when b_phi is free. These values are illustrative conditional diagnostics, not an
observational headline, a new joint-covariance forecast, or a detection forecast. The
primary contribution is the exact contraction-phase amplitude derivation.
```

---

### P4 — `paper4_arxiv_v1.0.269.tar.gz`

- **Title:** `An Observed-Label Chirality-Dipole Null in 890,069 Quality-Controlled High-Confidence DESI Spirals and an 8.5-Million-Galaxy Catalog`
  - *(Note: this is the current tex title. The stale `paper_deposit_config.json` metadata still reads "…949,584 High-Confidence DESI Spirals…"; the tex is authoritative — 949,584 is the pre-QC start count, 890,069 the post-QC primary sample. Use the tex title above.)*
- **Primary category:** `astro-ph.GA`  ✅ recommended (galaxy morphology / chirality catalog; DESI spirals).
- **Cross-list:** `astro-ph.IM`  (the release is as much about the content-addressed catalog machinery, injection–recovery calibration, NaMaster-complete covariance, and reproducer as about the galaxy result).
- **Comments field:** `32 pages, 9 figures. Prepared in AASTeX (ApJS format). Catalog and weights at huggingface.co/datasets/bamfai/galaxy-chirality-catalog and huggingface.co/bamfai/galaxy-chirality-v2 (CC-BY-4.0). Code at github.com/Hubify-Projects/bigbounce`
- **License:** config default `cc-by-4.0` (matches the CC-BY-4.0 catalog + weights). Confirm in §3.3.
- **Archival DOI:** the manuscript now embeds the real minted Zenodo archival DOI `10.5281/zenodo.21461899` (concept `10.5281/zenodo.21461898`) in the abstract, Data Availability paragraph, and catalog itemize — the "DOI-backed archive remain open" caveat is closed; no longer deferred (§3.4).
- **Abstract (plain-text for webform):**

```
We release observed chirality labels for 8,474,531 DESI Legacy DR8 galaxies and
test one primary high-confidence observed-label dipole. Starting from 949,584
high-confidence spirals, we exclude 59,515 rows marked raw_flip_qc_unsafe, leaving
890,069 quality-controlled rows; 887,472 enter the supported-pixel fit and
fixed-occupancy label-randomization null. The result is consistent with zero
(z_mom = +0.635, one-sided rank p = 0.23768). A coverage-calibrated observed-label
injection-recovery on this primary channel places a 95% sensitivity upper limit
A_95^obs ~ 0.98% (full-amplitude); this is an observed-label sensitivity floor, not
a physical parity-amplitude bound, which remains gated on the morphology transfer
function. The content-addressed release includes the science catalog, unsafe-row
quarantine, retained primary-null array, schema, checksums, and reproducer. WLS and
harmonic analyses use different supports or nulls and are retained only as
systematics diagnostics. A shared block-bootstrap covariance of the primary
estimators, now NaMaster-complete with the MASTER-decoupled l=1 leg, shows the
monopole to be a statistically distinct mode nearly uncorrelated with any
dipole/harmonic estimator. A classifier-injection forward model over 1.7x10^7 banked
network passes excludes classifier confusion as the source of that monopole (0.0% of
the observed value) and localizes its origin upstream of the classifier, without
resolving whether that origin is a true sky asymmetry or a DESI imaging systematic.
A from-scratch, manifest-retained retrain of the GZ1-core classifier component --
retaining every object, split index, and random seed -- validates on a provably
training-disjoint high-confidence GZ1 sample (Cohen's kappa = 0.97). The CE-ResNet
catalog has since been re-provisioned and the full historical composition
regenerated under seeded assembly, reproducing the 6,637 GZ1 and 17,153 CE-spiral
counts exactly and isolating the historical 826-vs-846 record conflict to a seeded
non-spiral subsample crossmatch (reproducible count 819); but a composition-faithful
CE-included retrain collapses to chance on chirality, so the historical CE-included
accuracy is not reproducible under honest ingestion, and the released catalog labels
are unchanged. Spatial transfer calibration, a full joint likelihood, an independent
matched-footprint estimator and a complete systematics-metadata sidecar remain open;
the reviewed release is archived under a minted Zenodo DOI. The parity-even
morphology observable supports no primordial-parity bound.
```

---

### P5 — `paper5_arxiv_v0.1.141-2026-07-16.tar.gz` (submit LAST, after §4 back-patch + rebuild)

- **Title:** `A Catalog-Native DESIVAST Test of Classifier-Labelled Spiral Chirality in DESI DR1`
  - *(The tex title carries a footnote clarifying all environment labels are in DESI DR1 redshift coordinates with no real-space reconstruction. arXiv title field takes the plain title above; the footnote renders in the PDF.)*
- **Primary category:** `astro-ph.GA`  ✅ recommended (galaxy spiral chirality vs. cosmic-web environment).
- **Cross-list:** `astro-ph.CO`  (void/non-void environment, DESIVAST, large-scale-structure context).
- **Comments field:** `42 pages, 9 figures. Prepared in REVTeX. Companion to arXiv:<P4_ARXIV_ID> (Paper IV). Code and reproducibility artifacts at github.com/Hubify-Projects/bigbounce`  *(insert the real P4 arXiv ID at submit time)*
- **License:** ⚠️ **UNRESOLVED — Houston must pick** (see §3.3). Config `metadata_blocker`: "Houston manuscript/source license authorization is absent." Recommend CC-BY-4.0 for consistency with the CC-BY-4.0 catalog P5 consumes, but arXiv non-exclusive is the safe default.
- **Abstract (plain-text for webform):**

```
We test whether classifier-labelled spiral chirality differs between released
DESIVAST void and non-void environments in DESI Data Release 1. The focal hybrid
released-parent descriptive estimate intersects the companion Paper IV catalog with
the released DESIVAST GALZONE TARGET universe (694,642 unique TARGETIDs), yielding
145,789 joined rows. We retain the 145,766 rows with OUT = 0 as the quality parent
and define the two arms by exact membership in the union of released VoidFinder
holes: 31,937 void and 113,829 non-void. We standardize for redshift, imaging leg,
magnitude, size, morphology, extinction, classifier confidence, and the GALZONE edge
flag, with coarse sky blocks used as clusters. The focal adjusted non-void-minus-void
contrast from a 13-column linear nuisance model is Delta f_CW = +0.00145442; a coarse
HEALPix NSIDE = 4 cluster-sandwich calculation gives SE = 0.00331502, 95% CI
[-0.00504290, +0.00795174], and two-sided normal p = 0.66085. A null-imposed
99,999-draw Rademacher wild-cluster efficient-score test gives p = 0.67345. Overlap
weighting gives the same qualitative result. The author-constructed VoidFinder
any-hole sample (N_void = 57,081) and the T-Web, Tempel, and ASTRA analyses are
sensitivity or secondary diagnostic paths rather than parallel focal measurements.
This hierarchy was changed after review and after inspecting the data; the study
remains exploratory, post-hoc, and not preregistered. T-Web intervals omit cosmic
variance and spatial covariance, and all environment assignments remain in redshift
space. The result is therefore a catalog-specific non-detection for classifier
labels, not a physical-handedness, real-space, or cosmological constraint.
```

---

## 3. Pre-submission checklist — DONE vs Houston-must-do

### ✅ DONE (verified by this kit, 2026-07-20)
- [x] All 3 tarballs built commit-bound at HEAD `f9c25de6` and **standalone-compile clean** (tectonic, exit 0, 0 errors, 0 undefined references) — receipts in `*.proof.json`.
- [x] `\preprint`/`\paperVersion` in each tex matches the tarball filename version (P2 v1.7.126, P4 v1.0.269, P5 v0.1.141-2026-07-16).
- [x] Every live `\includegraphics` figure present in its tarball (P2 2/2, P4 13 files/9 figure envs, P5 9/9); P4's `aastex701.cls` bundled.
- [x] `.bbl` bundled where used (P2, P4). P5 uses a manual inline bibliography — no bibtex dependency.
- [x] Titles + abstracts extracted directly from the current tex and plain-text-converted (§2).
- [x] P5 Paper-IV (and Paper-II) back-patch sites located and exact patch instructions written (§4) — **tex NOT modified in this kit.**

### ⚠️ Houston must do (decisions + account state this kit cannot verify)

1. **arXiv account + endorsement.** Log in at `arxiv.org` → *Submit* → start a submission and check each category dropdown for an endorsement prompt.
   - P2 → `astro-ph.CO` (primary) + `gr-qc` (cross).
   - P4 → `astro-ph.GA` (primary) + `astro-ph.IM` (cross).
   - P5 → `astro-ph.GA` (primary) + `astro-ph.CO` (cross).
   - Wave-1 already sought `gr-qc` + `astro-ph.IM` endorsements; the **new** categories to confirm are `astro-ph.CO` and `astro-ph.GA`. Resolve any "needs endorsement" before the click session.

2. **ORCID resolves + linked.** Confirm `https://orcid.org/0009-0008-5616-5994` loads and is linked to the arXiv account.

3. **License — per paper.** Two honest options (same as wave-1):
   - **(a) arXiv.org perpetual non-exclusive license** — default, safest, keeps copyright, no downstream reuse granted. Zero downside if unsure.
   - **(b) CC BY 4.0** — redistribution/adaptation with attribution; matches the CC-BY-4.0 catalog/data/weights releases.
   - **Recommendation:** P2 → CC-BY-4.0 (config default). P4 → CC-BY-4.0 (config default; matches catalog+weights). P5 → your call — CC-BY-4.0 is consistent with the catalog it consumes, but arXiv non-exclusive (a) is the safe default. **This is your authorization; the kit does not pick it for you.**

4. **Zenodo / software DOI.**
   - **P2 — ALREADY EMBEDDED (2026-07-20), no longer deferred.** Zenodo archival DOI `10.5281/zenodo.21461881` (concept `10.5281/zenodo.21461880`) is minted and embedded in the Data and Code Availability section at `v1.7.126`; the submission tarball is rebuilt at this version (§1).
   - **P4 — ALREADY EMBEDDED (2026-07-20), no longer deferred.** Zenodo archival DOI `10.5281/zenodo.21461899` (concept `10.5281/zenodo.21461898`) is minted and embedded in the abstract, Data Availability paragraph, and catalog itemize at `v1.0.269`; the submission tarball is rebuilt at this version (§1).
   - **P5 — still deferred (unchanged).** No DOI printed as a live claim (P5 links HF catalogs). Submit v1 today; mint a DOI later and add in a free v2 replacement if it matters to Houston.

5. **HuggingFace catalogs → public.** At P4/P5 post time, confirm `bamfai/galaxy-chirality-catalog` and `bamfai/galaxy-chirality-v2` are public so the CC-BY-4.0 links resolve. (`HF_TOKEN` in `.env.local`.)

6. **P5 Paper-II bibitem stale value (recommended non-blocking fix).** P5's reference list contains an **uncited** companion bibitem for Paper II (`\bibitem{golden_fnl_2026}`) whose title still reads `f_{NL} = -35/8` — the **superseded** value. P2's corrected headline is **-35/16**. Because P5 uses a manual `thebibliography`, this uncited entry still **prints** in P5's references with the wrong number. Fix it in the same edit pass as the §4 Paper-II back-patch (patch **P5-II** below already corrects the value). Not a hard blocker, but it is a visible internal inconsistency across the two wave papers.

---

## 4. P5 back-patch instructions (Paper IV = P4, Paper II = P2) — apply at submit time, NOT now

The P5 source declares Paper IV via a single controlling macro plus three
hard-coded prose sentences, and carries an uncited Paper II bibitem. After P2 and
P4 have real arXiv IDs, apply the patches below to
`pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex`, then rebuild + re-verify.

**Placeholders — replace before running:** `2607.XXXXX_P4` → the real P4 arXiv ID
(e.g. `2607.01234`); `2607.XXXXX_P2` → the real P2 arXiv ID. (Do NOT leave the
literal `XXXXX` — `tools/prepare_paper_deposit.py` and arXiv both reject
placeholder identifiers.)

### 4a. Paper IV (P4) — REQUIRED before P5 submits

The macro drives all 8 `\paperIVarxiv{}` usages (including the bibitem at line 5448).
Three prose sentences assert "no arXiv identifier" and are NOT macro-driven — patch
each. Verified current strings at HEAD `f9c25de6`:

```bash
T=pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex

# (1) controlling macro — line 19 — updates every \paperIVarxiv{} usage + the Paper IV bibitem
sed -i '' 's|\\newcommand{\\paperIVarxiv}{companion manuscript in preparation}|\\newcommand{\\paperIVarxiv}{arXiv:2607.XXXXX_P4}|' "$T"

# (2) Limitations sentence — line ~4673-4674: "...whose arXiv identifier is\ninserted here on posting."
sed -i '' 's|inserted here on posting\.|\\texttt{arXiv:2607.XXXXX_P4}.|' "$T"

# (3) Data-availability sentence — line ~5137: "Paper~IV remains a companion manuscript in preparation; no arXiv identifier"
sed -i '' 's|Paper~IV remains a companion manuscript in preparation; no arXiv identifier|Paper~IV is posted as \\texttt{arXiv:2607.XXXXX_P4}; no Zenodo|' "$T"
#   NOTE: this rewrites the clause head; verify the resulting sentence reads cleanly
#   ("...is posted as arXiv:...; no Zenodo DOI is asserted here."). Adjust by hand if needed.

# (4) Provenance sentence — line ~5308: "Paper~IV has no verified arXiv identifier at this stage."
sed -i '' 's|Paper~IV has no verified arXiv identifier at this stage\.|Paper~IV is posted as \\texttt{arXiv:2607.XXXXX_P4}.|' "$T"
```

Optional (LaTeX comments only, do not affect the PDF): lines 17-18 (`% Paper IV has
no verified arXiv identifier…`) can be updated for honesty but need not be.

### 4b. Paper II (P2) — recommended in the same pass (fixes the stale value too)

Paper II's bibitem is **uncited** but still prints. Patch it to carry the real P2
arXiv ID **and** correct the superseded `-35/8` → `-35/16`. Verified current string
(lines 5452-5455):

```bash
# fix stale f_NL value AND the in-prep string in one bibitem
sed -i '' 's|\$f_{NL} = -35/8\$ Forecast|$f_{NL} = -35/16$ Forecast|' "$T"
sed -i '' 's|companion paper (Paper~II), in preparation; manuscript in preparation\.|companion paper (Paper~II), \\texttt{arXiv:2607.XXXXX_P2}.|' "$T"
```

### 4c. Rebuild + re-verify the P5 tarball after patching

```bash
cd /Users/houstongolden/Desktop/CODE_YOU/bigbounce
# commit the patched tex first (build tool requires clean-at-commit inputs), then:
NEWHEAD=$(git rev-parse HEAD)
# bump the output filename if you also bump \paperVersion; otherwise remove the old tarball first:
rm -f project-context/SSOT/arxiv_tarballs/paper5_arxiv_v0.1.141-2026-07-16.tar.gz
python3 tools/build_exact_arxiv_bundle.py --paper P5 --git-commit "$NEWHEAD" \
  --output project-context/SSOT/arxiv_tarballs/paper5_arxiv_<NEWVERSION>.tar.gz --write
# then extract to a temp dir + `tectonic --keep-logs p5_desi_chirality.tex`, confirm
# 42 pp (or new count), 0 errors, 0 undef-refs, and that the Paper IV/II lines now
# render the real arXiv IDs (grep the compiled text or eyeball the references page).
```

> **Sequencing reminder:** §4 runs **only after** P2 and P4 are live. If Houston
> prefers, P5 can post first as-is (macro reads "companion manuscript in
> preparation", which is honest and self-consistent) and the IDs added in a free
> P5 v2 replacement — but the coordinated path (patch, then submit) is cleaner and
> is the recommended order.

---

## 5. Single ordered click-walkthrough

**Pre-flight (once):**
1. Log into arxiv.org; confirm endorsement for `astro-ph.CO`, `astro-ph.GA`, `astro-ph.IM`, `gr-qc` (§3.1).
2. Confirm ORCID `0009-0008-5616-5994` resolves + is linked (§3.2).
3. Decide license per paper (§3.3) and DOI path (§3.4). Recommended: P2/P4 = CC-BY-4.0 (Zenodo archival DOIs already embedded — no defer needed), P5 = your call, defer P5's DOI to v2.

**Step 1 — P2 (`paper2_arxiv_v1.7.126.tar.gz`):**
4. Start New Submission → license per §3.3.
5. Upload the P2 tarball → let arXiv auto-process → **verify preview PDF = 11 pages, 2 figures**, no missing figures. (If arXiv's TeX build errors, it uses a pinned TeXLive; revtex4-2 is standard there — check its log.)
6. Metadata: paste Title + Abstract (§2 P2); author "Houston Golden", link ORCID.
7. Primary `astro-ph.CO`, cross `gr-qc`; Comments per §2.
8. Preview → Submit → **record the arXiv ID = `<P2_ARXIV_ID>`.**

**Step 2 — P4 (`paper4_arxiv_v1.0.269.tar.gz`):**
9. Repeat 4-8 with the P4 tarball. **Verify preview PDF = 32 pages, 9 figures.** Primary `astro-ph.GA`, cross `astro-ph.IM`; Title + Abstract (§2 P4). **Record `<P4_ARXIV_ID>`.**
10. Confirm HF catalog + weights are public (§3.5).

**Step 3 — back-patch P5 (§4):**
11. Apply §4a (P4 ID) + §4b (P2 ID + stale-value fix) to the P5 tex. Commit. Rebuild + re-verify the P5 tarball (§4c). Confirm 0 errors / 0 undef-refs and the real IDs render.

**Step 4 — P5 (patched tarball):**
12. Repeat 4-8 with the patched P5 tarball. **Verify preview PDF = 42 pages, 9 figures**, and that the references show `arXiv:<P4_ARXIV_ID>` / `arXiv:<P2_ARXIV_ID>`. Primary `astro-ph.GA`, cross `astro-ph.CO`; Title + Abstract (§2 P5); Comments with the real P4 ID. Confirm HF catalog public.
13. Preview → Submit → record the P5 arXiv ID.

**Post (optional):**
14. P2/P4 need no DOI v2 back-patch (already embedded at v1.7.126/v1.0.269, §3.4). For P5, if deferring its DOI: after it is minted, upload a free v2 replacement with it inserted.
15. Sync SSOT / Convex / review-timeline with the new arXiv IDs (standing directive A).

---

*Kit verified 2026-07-20 against git HEAD `f9c25de657d1bcbc3ef0ba729133a00019d71fa3`.
Tarballs + `*.proof.json` receipts in `project-context/SSOT/arxiv_tarballs/`.
Do NOT submit or push from this kit — it is the click-ready reference for Houston.*
