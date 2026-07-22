# Wave-1 arXiv Submission Kit — P3, P1A, P1B
---

## 2026-07-21 ADDENDUM — P1B superseded to v2B.0.12 (Archive/DOI closure)

Every `v2B.0.11` reference below for **P1B** is superseded by **v2B.0.12**:

- The namaster-proof 0.1.7 software archive is **PUBLISHED**: DOI
  **10.5281/zenodo.21481753** (Houston-authorized 2026-07-21; receipt in
  `SSOT/zenodo/`). v2B.0.12's Archive paragraph cites it — the boards' only
  remaining P1B major (persistent identifier) is closed in-paper.
- Submission tarball: `paper1b_namaster_proof_arxiv_v2B.0.12.tar.gz`
  (commit-bound, isolated recompile pass: 6 pp, 0 errors / 0 undef-ref).
- License (D2, RESOLVED 2026-07-21): **CC-BY-4.0** for P1A + P1B + P5.
- P1A/P1B Zenodo deposits are staged as drafts with prereserved DOIs
  10.5281/zenodo.21481838 (P1A) / …21481842 (P1B, holding the v2B.0.12
  files); publish on Houston's explicit go.
- P1A remains v1A.0.124 exactly as documented below.

## Prepared 2026-07-19 | git HEAD `b680ca1c` | Goal: a minutes-long click session for Houston

> **2026-07-20 update — P3 tarball rebuilt at the DOI-bearing version.** P3's
> `\paperVersion` advanced `v3.2.0-r10` → `v3.2.0-r11` to embed the real minted
> Zenodo archival DOI `10.5281/zenodo.21461888` (concept DOI
> `10.5281/zenodo.21461887`) in the Data Availability section. The submission
> tarball below is rebuilt and standalone-verified at `v3.2.0-r11`
> (`project-context/SSOT/arxiv_tarballs/paper3_apjs_arxiv_v3.2.0-r11.tar.gz`,
> commit-bound to `bdb3d5cceb61096a7ca9aab279e80a2d379ff15c`). P1A and P1B are
> **unchanged** — still `v1A.0.124` / `v2B.0.11`, tarballs as originally
> verified 2026-07-19. See `project-context/SSOT/queue.md` for the closed row.

This kit is the single source for the wave-1 arXiv drop. Everything below is
**verified against the current tex sources** (not the stale 2026-06 runbook,
which describes superseded paper versions and cross-citation structure).

### What changed vs the old `ARXIV_SUBMISSION_RUNBOOK.md`
The 2026-06-20 runbook is **stale** for wave-1 and must not be followed verbatim:
- **P1A was rewritten** from the old "Channel-Level Closure of Four ECH Dark-Energy Routes" (29 pp, 8 figures, `astro-ph.CO`, 4 companion cross-cites) into a **narrow 7-page, 0-figure CQG-style Note** ("Algebraic Cartan Elimination…"). The entire old long version now lives inside `\begin{comment}` blocks and does **not** compile into the PDF. **P1A now has ZERO companion cross-citations** — the runbook's "P1A needs 4 companion bibitem back-patches" no longer applies.
- **P1B identity changed** from the "MCMC companion" (`astro-ph.CO`) to a **software metapaper** for `namaster-proof` (JORS-style, `astro-ph.IM`). New tex: `arxiv/paper1b_namaster_proof.tex`.
- **All three wave-1 papers are fully self-contained** — no `arXiv:XXXX.XXXXX` placeholders in live text, no companion `\bibitem` patches, **no coordinated-drop v2 back-patch needed** for cross-citations. Each can be submitted independently, in any order.

---

## 0. TL;DR click order

```
1. Confirm arXiv account + endorsement for gr-qc and astro-ph.IM (§4 pre-flight)
2. Decide license per paper (§ per-paper "Houston must do" — P1A/P1B unresolved)
3. Upload 3 tarballs, paste 3 metadata blocks (§1, §2), submit
4. (Optional) mint Zenodo DOIs now, or defer to a v2 replacement (§3 presents both)
```

No cross-paper sequencing constraint. Recommended upload order (simplest first):
**P1B → P1A → P3**.

---

## 1. Exact tarballs — VERIFIED (standalone tectonic 0.16.9 compile, isolated temp extract)

| Paper | Version | Tarball (in `project-context/SSOT/arxiv_tarballs/`) | Pages | Figs | Compile | Tarball status |
|-------|---------|------------------------------------------------------|-------|------|---------|----------------|
| **P3**  | v3.2.0-r11 | `paper3_apjs_arxiv_v3.2.0-r11.tar.gz` | **17** | 3 | exit 0, **0 errors / 0 undef-ref**, 1 overfull (max 1.82 pt) | **REBUILT + VERIFIED 2026-07-20** (DOI-bearing version) |
| **P1A** | v1A.0.124  | `paper1a_arxiv_v1A.0.124.tar.gz`      | **7**  | 0 | exit 0, **0 errors / 0 undef-ref**, 34 overfull (max 18.67 pt — cosmetic, see note) | **REBUILT + VERIFIED** (old v1A.0.123 was stale) |
| **P1B** | v2B.0.11   | `paper1b_namaster_proof_arxiv_v2B.0.11.tar.gz` | **6** | 0 | exit 0, **0 errors / 0 undef-ref**, 2 overfull (max 0.43 pt) | **VERIFIED** (existing, matches current) |

Checksums (for provenance / re-verify):

| Paper | tarball sha256 | tarball md5 | bytes |
|-------|----------------|-------------|-------|
| P3  | `365bd34910544ba10e712cf988247c943d7e370be9c5c90baa7e2a6f97ed30f4` | (see `.proof.json`) | 146,315 |
| P1A | `3f56a6bf7452c8574656416e806727d0feaac4b750400d83a00b68bd2771993c` | `85923519615dd1364102135a2126cd6a` | 130,292 |
| P1B | `51f37515c1780ad994cd9594953576d5e8bb43909c47d5c155a40a220b847e97` | `9f640a21561de9d2dc00b2a3964f1105` | 8,822 |

Per-tarball verification receipts written alongside each tarball as
`*.proof.json` (P1A/P1B: 2026-07-19, verifier `wave1-submission-kit`; P3:
rebuilt 2026-07-20 at the DOI-bearing version, verifier `doi-tarball-rebuild`,
receipt `project-context/SSOT/arxiv_tarballs/paper3_apjs_arxiv_v3.2.0-r11.proof.json`).

**Tarball contents (what arXiv receives):**
- **P3**: `paper3_apjs.tex`, `aastex701.cls` (bundled — this is what makes it standalone), `figures/{p3_v320_catalog_overview,p3_v320_r6_chance_control,p3_v320_selection_waterfall}.pdf`
- **P1A**: `paper1a_ech_nogo.tex`, `paper1a_ech_nogo.bbl`, `references.bib` (text-only; 0 figures live)
- **P1B**: `paper1b_namaster_proof.tex` (single file — self-contained `article` with inline `thebibliography`; 0 figures)

> **P1A overfull note (honest disclosure):** 34 overfull hboxes, largest 18.67 pt in a ~246 pt revtex column (~7.6% intrusion). These are long inline-math / `\texttt` lines that reach slightly into the gutter — **no content is lost and there is no column-to-column overlap** (paper is single-flow at these points). arXiv accepts this without issue; it passed prior R-round/latex-audit at this version. Not a submission blocker. If Houston wants them gone, that is a cosmetic D-round micro-pass, not a wave-1 gate.

> **P1A rebuild note:** the previously-staged tarball was `v1A.0.123`; the tex is at `v1A.0.124`. Rebuilt with `tools/build_exact_arxiv_bundle.py --paper P1A --git-commit b680ca1c… --output …paper1a_arxiv_v1A.0.124.tar.gz --write` (deterministic, commit-bound, mtime=0). P3 and P1B tarballs already matched their current tex versions and were re-verified in place.

> **SSOT drift to note (not a blocker):** `project-context/SSOT/index.md` banner shows P1B at `v2B.0.10`; the tex and the built tarball are `v2B.0.11`. The tex/tarball are authoritative. Recommend advancing the SSOT banner to `v2B.0.11` in a housekeeping commit.

---

## 2. Ready-to-paste arXiv metadata

Author (all three): **Houston Golden** — ORCID **0009-0008-3617-8729** — affiliation *Independent Researcher, Los Angeles, California, USA*.

---

### P1A — `paper1a_arxiv_v1A.0.124.tar.gz`

- **Title:** `Algebraic Cartan Elimination in Minimal Einstein–Cartan–Holst Gravity: Spin-Sourced Contact and Zero-Spin Scalar Branches`
- **Primary category:** `gr-qc`  ✅ recommended (pure classical-gravity / torsion-elimination result)
- **Cross-list:** `hep-th`  (four-fermion contact interaction, NJL Fierz projection)
- **Comments field:** `7 pages, no figures. Code and reproducibility artifacts at github.com/Hubify-Projects/bigbounce`
- **License:** ⚠️ **UNRESOLVED — Houston must pick** (see §3). Config `metadata_blocker`: "the live paper declares no license."
- **Abstract (plain-text for webform):**

```
We consolidate two standard consequences of the same algebraic Cartan equation
in minimal Einstein-Cartan-Holst (ECH) gravity. On the spin-sourced branch,
eliminating the non-propagating connection gives the minimal axial-axial contact
interaction -(3 kappa/16)[gamma^2/(1+gamma^2)] J_5^2. A deliberately elevated
homogeneous normalization illustrates only its scale: kappa n_psi^2 / rho_Lambda
~ 3.6e-69 (n_psi/100 cm^-3)^2. This coefficient-one dimensional benchmark omits
the actual contact factor 3/16 and the finite-Holst factor gamma^2/(1+gamma^2);
number density also does not fix the state-dependent renormalized composite
<J_5^I J_{5I}>, a vacuum stress tensor, or an equation of state. In the declared
direct-channel, hard-four-momentum-cutoff, standard mean-field NJL convention,
the scalar Fierz projection is repulsive, G_s = -3 kappa/16, so its real
homogeneous scalar gap equation has no nonzero solution. This conditional sign
result does not exclude other truncations, species structures, non-minimal
couplings, or propagating torsion.

On the zero-spin branch, canonical scalar matter has no Lorentz-connection
source; for an invertible tetrad and real nonsingular constant gamma, the same
algebraic equation gives C = T = 0. After solving that equation, the local
classical reduced action is the Einstein-scalar action because the Holst
contraction vanishes pointwise by the algebraic Bianchi identity. Thus the
classical scalar equations and tensor evolution operators equal their GR
counterparts for matched background, initial, and boundary data with standard
falloff, so the first-order variational surface contribution vanishes. Equality
of right- and left-helicity solutions additionally requires matched
parity-symmetric initial data. This on-connection-shell statement is not an
off-shell equality of the original first-order actions and excludes
quantum/anomaly, non-minimal, propagating-torsion, and nontrivial
global/topological sectors.

The identities used here are standard. The contribution is their
convention-audited consolidation into the two Cartan branches and the sharply
bounded dimensional coefficient benchmark above; no ECH dark-energy or
birefringence prediction is made.
```

---

### P1B — `paper1b_namaster_proof_arxiv_v2B.0.11.tar.gz`

- **Title:** `namaster-proof: Exact pseudo-C_ell window inference and content-bound validation for reproducible spin-2 analyses`
- **Primary category:** `astro-ph.IM`  ✅ recommended (instrumentation & methods — a validation/reproducibility software layer for cut-sky spin-2 / pseudo-C_ell analysis)
- **Cross-list (recommended):** `astro-ph.CO`  (the target audience is CMB/large-scale-structure spin-2 analysts)
- **Cross-list (optional CS visibility):** `cs.MS` (Mathematical Software) is the closest arXiv CS home for a software metapaper; `cs.SE` is defensible but arXiv moderators may reclassify a physics-domain tool. **Recommend NOT adding a cs.* cross-list unless Houston specifically wants CS-community reach** — astro-ph.IM + astro-ph.CO is the honest primary audience.
- **Comments field:** `6 pages, no figures. Software metapaper. Package at github.com/Hubify-Projects/bigbounce/tree/main/packages/namaster-proof; reproducibility artifacts at github.com/Hubify-Projects/bigbounce`
- **License:** ⚠️ **UNRESOLVED — Houston must pick** (see §3). Config `metadata_blocker` also flags: mint a persistent software archive DOI (Zenodo for `namaster-proof 0.1.7`) if he wants it cited.
- **Abstract (plain-text for webform):**

```
namaster-proof is a focused Python verification layer for two error-prone steps
in cut-sky spin-2 analyses. First, it evaluates a uniformly rotated EE, EB, BE,
BB spectrum through the complete NaMaster bandpower-window operator, avoiding
replacement of the operator by bin-centre or effective-multipole templates.
Second, it writes JSON results and content-bound sidecar receipts with atomic
per-file replacement and fails closed when result bytes or caller-asserted
execution metadata change. The package also supplies explicit multipole-support
contracts, fixed-grid rotation-angle recovery, command-line receipt
verification, and compatibility tests against the production helpers from which
it was extracted. The software is intended for method validation and
reproducibility checks; it is not a sky-analysis pipeline, foreground model, or
cosmological inference engine.
```

---

### P3 — `paper3_apjs_arxiv_v3.2.0-r11.tar.gz`

- **Title:** `Public-ID Recovery for a Historical DESI DR1 Anomaly List: 170 High-Coordinate-Consistency Core and 11 Lower-Confidence Positional Associations`
- **Primary category:** `astro-ph.IM`  ✅ **recommended** over `astro-ph.GA`. Rationale: the paper's own stated primary deliverable is *"the reusable, memory-bounded join and provenance/validation machinery itself"* — this is an instrumentation-&-methods / reproducibility paper about a public-identifier recovery pipeline, not a galaxy-astrophysics result. The 181-row catalog is the method's first instance.
- **Cross-list:** `astro-ph.GA` (DESI galaxy/QSO targets, catalog content) and optionally `astro-ph.CO` (DESI is a cosmology survey). Recommend `astro-ph.GA` as the single cross-list; add `astro-ph.CO` only if Houston wants cosmology-list visibility.
- **Comments field:** `17 pages, 3 figures. Prepared in AASTeX (ApJS format). Catalog at huggingface.co/datasets/bamfai/bigbounce-anomaly-catalog (CC-BY-4.0). Code at github.com/Hubify-Projects/bigbounce`
- **License:** config default `cc-by-4.0` (matches the CC-BY catalog/data release). Confirm this is what Houston wants for the manuscript source (§3).
- **Archival DOI:** the manuscript now embeds the real minted Zenodo archival DOI `10.5281/zenodo.21461888` (concept `10.5281/zenodo.21461887`) in the Data Availability section — this is distinct from the AAS journal digital-asset DOI, which the journal assigns during its own publication workflow and remains honestly disclosed as pending in the text (§3.4 below is now historical for P3; no v2 back-patch needed for this DOI).
- **Abstract (plain-text for webform):**

```
Anomaly searches become reusable catalogs only when rows trace public archive
objects and the recovery from a declared input list is reconstructable. The
primary deliverable of this work is that reusable, memory-bounded join and
provenance/validation machinery itself; the 181-row DESI DR1 catalog reported
here is its first instance, produced by applying the machinery to one frozen
historical input list. We recover public identifiers for a frozen historical
DESI anomaly list whose legacy identifiers mixed public-looking values with
internal hashes. We document the available immutable clustering and BigAE
lineage but do not reconstruct the unavailable production normalization or
physical-feature sensitivity. Starting from 190,015 positional clusters
containing a DESI member, we stream all 28,425,963 rows of the public DESI Data
Release 1 (DR1) pixel-based redshift catalog in 200,000-row chunks, read 18
columns, and query a spherical-coordinate k-d tree. The predeclared parent
selection is a 1 arcsec match to a main-survey row carrying at least one LRG,
ELG, QSO, BGS_ANY, or MWS_ANY DESI_TARGET bit. It reproduces exactly 20,299,155
eligible DESI rows and 2,468 positional matches. Requiring the global primary
redshift row leaves 2,448; requiring ZWARN=0 leaves 181 unique public TARGETID
associations. These 181 rows form the v3.2.0-r2 data release audited in this
manuscript: 170 high-coordinate-consistency core associations at or below 0.1
arcsec and 11 lower-confidence positional associations between 0.1 and 1 arcsec.
They comprise 157 Redrock GALAXY, 23 QSO, and one STAR classifications; spectral
type was not a selection cut. A quality-tier column exposes this contract without
silently changing the declared 1 arcsec list; neither tier is a secure
object-identity or purity claim. Every released row and all 18 carried DESI
fields were re-read from their recorded FITS row and compared exactly. The
release includes the Parquet catalog, dictionary, code, waterfall, checksums,
and provenance. A separately released, explicitly secondary table preserves all
2,267 warning-bearing global-primary rows without admitting them to the primary
catalog. Sixteen deterministic 60-120 arcsec local shifts of all 190,015 cluster
positions yield 86.7 +/- 14.4 parent and 76.2 +/- 13.3 warning-free-primary
associations within 1 arcsec, compared with 2,468 and 181 observed. The
corresponding shifted 0.1-1 arcsec annulus contains 75.6 +/- 13.0
warning-free-primary associations versus 11 observed, so the tail is not treated
as secure candidate-level identity. The sub-0.1 arcsec portion of the within-1
arcsec excess is the expected self-recovery of the seed DESI members whose own
coordinates define the cluster centroids; it verifies the recovery end to end
rather than providing independent association evidence, and the local-shift
control is informative only for the 0.1-1 arcsec tail. These are reproducible
follow-up lists, not validated detections or unbiased samples for anomaly-rate
inference.
```

---

## 3. Pre-submission checklist — DONE vs Houston-must-do

### ✅ DONE (verified by this kit, 2026-07-19)
- [x] All 3 tarballs exist at the current versions and **standalone-compile clean** (tectonic 0.16.9, exit 0, 0 errors, 0 undefined references) — receipts in `*.proof.json`.
- [x] P1A stale tarball **rebuilt** to v1A.0.124 (commit-bound, deterministic).
- [x] `\paperVersion` in each tex matches the tarball filename version.
- [x] Every live `\includegraphics` figure is present in its tarball (P1A/P1B have 0 live figures; P3 has 3, all bundled).
- [x] `.bbl` present where needed (P1A external-refs bbl bundled; P1B/P3 inline/aastex bibliography self-resolves).
- [x] **No `arXiv:XXXX.XXXXX` cross-citation placeholders in live text** — none of the three cross-cite each other; **no v2 back-patch step needed.**
- [x] Metadata (title, abstract, author, ORCID) extracted directly from the current tex and plain-text-converted (§2).

### ⚠️ Houston must do (decisions + account state this kit cannot verify)

1. **arXiv account + endorsement.** How to check: log in at `arxiv.org` → *Submit* → start a new submission and look at the category dropdown. First-time submitters to a category may need an **endorsement**.
   - P1A → needs **gr-qc** submission privilege.
   - P1B, P3 → need **astro-ph.IM** submission privilege.
   - If any category shows "you need endorsement," arXiv displays an endorsement code / request path; a colleague already publishing in that category endorses you once. Do this **before** the click session or the upload will stall.

2. **ORCID resolves.** The old runbook flagged `0009-0008-3617-8729` as returning 404. Confirm `https://orcid.org/0009-0008-3617-8729` loads and is linked to the arXiv account before submitting.

3. **License — per paper (P1A & P1B are genuinely unresolved; P3 defaults CC-BY-4.0).** Two honest options:
   - **(a) arXiv.org perpetual, non-exclusive license to distribute** — the default. You keep copyright; no downstream reuse rights granted beyond arXiv distribution. Safest, most conventional for physics preprints. Zero downside if you're unsure.
   - **(b) CC BY 4.0** — permits redistribution/adaptation with attribution. Matches the CC-BY-4.0 data/catalog releases (P3's HF catalog, P2/P4 config). Choose this if you want maximum reuse/openness and consistency with the data license.
   - **Recommendation:** P3 → **CC BY 4.0** (config already sets it; matches the catalog). P1A & P1B → your call; **arXiv non-exclusive (a)** is the safe default if you don't have a reason to prefer CC-BY. This is your authorization — the kit does not pick it for you.

4. **Zenodo / software DOI — mint now (cite in v1) vs add in v2.**
   - **P3 — ALREADY EMBEDDED (2026-07-20), no longer deferred.** The Zenodo archival DOI `10.5281/zenodo.21461888` (concept `10.5281/zenodo.21461887`) is minted and embedded in the manuscript's Data Availability section at `v3.2.0-r11`; the submission tarball is rebuilt at this version (§1). The separate AAS journal digital-asset DOI is still honestly disclosed as "pending" — that one is assigned by ApJS during its own publication workflow and cannot be minted on arXiv day. No v2 back-patch is needed for the Zenodo DOI.
   - **P1A, P1B — still deferred (unchanged).** Neither currently prints a DOI as a live claim (P1B links github/tree/main; P1A cites a reproducibility tree, not a DOI).
     - **Path A — defer (recommended for speed):** submit v1 as-is today. Mint DOIs later and add them in a v2 replacement (arXiv v2 is free and easy). Nothing in v1 becomes wrong — the papers already state DOIs as pending.
     - **Path B — mint first:** if you want a DOI cited in v1, mint before submitting: P1B → Zenodo software DOI for `namaster-proof 0.1.7`. Then insert the DOI in the tex and rebuild that tarball.
     - **Recommendation:** **Path A** for P1A/P1B. Only take Path B for P1B if a citable software DOI in v1 matters to you.

5. **P3 HuggingFace catalog → public.** At the moment P3 posts, flip `bamfai/bigbounce-anomaly-catalog` to public so the CC-BY-4.0 links in the paper resolve. (HF token `HF_TOKEN` in `.env.local`.) Verify the dataset is public before or at posting.

6. **(Housekeeping, non-blocking)** Advance the SSOT `index.md` banner P1B `v2B.0.10` → `v2B.0.11` to match tex/tarball.

---

## 4. Single ordered click-walkthrough (whole wave)

**Pre-flight (once, before clicking):**
1. Log into arxiv.org; confirm endorsement for `gr-qc` and `astro-ph.IM` (§3.1).
2. Confirm ORCID `0009-0008-3617-8729` resolves and is linked (§3.2).
3. Decide license per paper (§3.3) and DOI path (§3.4). Recommended: P3=CC-BY-4.0 (Zenodo archival DOI already embedded — no defer needed), P1A/P1B=arXiv non-exclusive, defer P1A/P1B DOIs to v2.

**Per paper (repeat 3×; order P1B → P1A → P3):**
4. arXiv → *Start New Submission* → license: pick per §3.3.
5. *Upload files* → upload the one tarball from `project-context/SSOT/arxiv_tarballs/`:
   - P1B: `paper1b_namaster_proof_arxiv_v2B.0.11.tar.gz`
   - P1A: `paper1a_arxiv_v1A.0.124.tar.gz`
   - P3: `paper3_apjs_arxiv_v3.2.0-r11.tar.gz`
6. Let arXiv auto-process → **verify the arXiv-side preview PDF page count** matches this kit (P1B 6, P1A 7, P3 17) and that no figures are missing. If arXiv's TeX build errors, the tarball still compiled locally with tectonic — check arXiv's log (it uses a pinned TeXLive; revtex4-2/aastex701 are standard there).
7. *Add/Change Metadata* → paste Title, Abstract from §2; set author "Houston Golden", link ORCID.
8. Set **Primary** + **Cross-list** categories per §2.
9. Set **Comments** field per §2.
10. *Preview* → eyeball the rendered abstract/title → *Submit*.
11. Record the returned submission ID.

**Post (optional, same day or later):**
12. Flip P3's HF catalog to public (§3.5).
13. P3 needs no DOI v2 back-patch (already embedded at v3.2.0-r11, §3.4). For P1A/P1B, if deferring DOIs (recommended): after any DOI is minted, upload a v2 replacement with the DOI inserted — no rush, no live-cross-ID coordination required (papers are independent).
14. Sync SSOT/Convex with the new arXiv IDs (standing directive A).

---

*Kit verified 2026-07-19 against git HEAD `b680ca1c`. Tarballs + `*.proof.json` receipts in `project-context/SSOT/arxiv_tarballs/`. Supersedes the wave-1 portions of `ARXIV_SUBMISSION_RUNBOOK.md` (2026-06-20), which describes superseded paper versions.*
