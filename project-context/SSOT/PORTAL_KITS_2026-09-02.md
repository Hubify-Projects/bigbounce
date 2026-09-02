# Portal kits — 2026-09-02 lineup (CQG / ApJS / PRD Letters / JCAP)

## CLICK-LIST (ordered) — everything Houston must click/send, nothing agent-doable left

1. **ECH Note → CQG** (§1): confirm the Zenodo DOI is minted (see
   `ENDORSER_OUTREACH_2026-09-02.md` click-list step 1) and the gr-qc
   endorsement has cleared, then create a ScholarOne account at
   `https://mc04.manuscriptcentral.com/cqg-iop` and paste the fields in §1
   below — Article type **Paper** (not Note; the ≤2500-word Note form does
   not fit the manuscript, per the final-review recommendation), title and
   abstract already final (v1N.0.4).
2. **P4′ → ApJS** (§2): confirm the P5 Zenodo DOI is minted (see
   `ENDORSER_OUTREACH_2026-09-02.md` click-list step 2) and the
   astro-ph.GA endorsement has cleared, then submit at
   `journals.aas.org/submission/` and paste the fields in §2 below — title
   and abstract already final (v4P.0.4); abstract runs over the 250-word
   AAS working cap and needs a portal-side length check before pasting.
3. **P2′**: no action — DEFERRED, no submission planned (§3).
4. **A3 → PRD Letters / JCAP** (§3a note below): wait for the PBH
   compaction-function row + pending INT board to close before doing
   anything in this section; not yet actionable.
5. **arXiv form fields** (§4): use once each paper's endorsement clears.
6. **Post-approval Zenodo/tarball commands** (§5): the exact commands are
   documented; run only after Houston's explicit go-ahead per manuscript.

---

Field-by-field paste sheets for the near-term works
(`INTENT.md` Track A1/B1/C1): the **ECH Note** (v1N.0.4, APPROVE, readiness
95) → CQG, **P4′** (v4P.0.4, APPROVE, readiness 95, P5 folded in) → ApJS.
**P2′ is DEFERRED** (archived theory record, folded into the A3 paper) — no
PRD Letters / JCAP submission is planned for it. **A3**
(`research/track_a3_multichannel/paper/main.tex` v3M.0.2) is the paper that
would eventually use the PRD Letters / JCAP venue rows below, but it is
**not yet reviewable** (PBH compaction-function row pending, then one INT
board) — §3/§3b below are retained as a venue-mechanics reference for A3,
not as an active P2′ submission plan. Reuses and re-labels verified facts
already on file (`CQG_SUBMISSION_KIT_P1A_2026-07-24.md`,
`PRD_SUBMISSION_KIT_P2_2026-07-24.md`, `pipelines/p2_chirality/APJS_PORTAL_KIT_v1.0.274.md`)
where those facts are archive-level and still current; adds fresh fetches
(2026-09-02) for ApJS and JCAP specifics not covered by the existing kits.
This is a paste-sheet for when each manuscript is ready — not a submission
record.

---

## 1. ECH Note → Classical and Quantum Gravity (IOP), article type **Paper**

Source: `CQG_SUBMISSION_KIT_P1A_2026-07-24.md` §1 (live-fetched 2026-07-24,
6 weeks old — IOP policy pages change rarely; re-fetch only if Houston wants
a hard re-check before clicking submit). Reused verbatim below; the manuscript
target is now the final `arxiv/paper1bc_ech_note/main.tex` v1N.0.4
(APPROVE, readiness 95), submitted as a **Paper** not a Note (per the
2026-09-02 final-review recommendation — the manuscript exceeds the Note
form).

| Field | Value to paste | Source |
|---|---|---|
| Portal | `https://mc04.manuscriptcentral.com/cqg-iop` (ScholarOne) | iopscience.iop.org/journal/0264-9381/page/submission-options |
| Account | New ScholarOne account required (first-time author) | publishingsupport.iopscience.iop.org how-to-submit page |
| Article type | **Paper** (not Note — the final v1N.0.4 manuscript exceeds the ≤2500-word Note form; per the 2026-09-02 final-review recommendation, submit as a regular CQG Paper) | Final-review recommendation, `FINAL_REVIEW_RECOMMENDATIONS_2026-09-02.md` |
| Length limit | N/A for Paper article type (Note's implicit length cap no longer applies) | — |
| Title | **"What Minimal Einstein–Cartan Torsion Does for the Bounce and Cannot Do for Dark Energy"** (FINAL — `arxiv/paper1bc_ech_note/main.tex` v1N.0.4) | arxiv/paper1bc_ech_note/main.tex |
| Abstract cap | **300 words hard cap** — "we may rescind the manuscript and ask you to re-write it" if over | CQG guidelines page |
| Abstract | Final v1N.0.4 abstract, verbatim — see `ENDORSER_OUTREACH_2026-09-02.md` §1 for the full text (word-count check before pasting: the compiled abstract runs close to 300 words; trim if the ScholarOne counter flags it over) | arxiv/paper1bc_ech_note/main.tex |
| Keywords | Free-text, no PACS required. Use: Einstein–Cartan gravity, Holst action, torsion bounce, Popławski cosmology, four-fermion interaction, dark energy, no-go (verbatim `\keywords{}` from v1N.0.4) | CQG guidelines page + arxiv/paper1bc_ech_note/main.tex |
| Author/ORCID | Houston Golden, Independent Researcher, Los Angeles, CA, USA; `houston@hubify.com`; ORCID `0009-0008-5616-5994` (recommended, not mandatory) | CQG guidelines page |
| Data-availability statement text | No dedicated data-availability section exists in v1N.0.4 (theory/no-go paper, not a data release) — use: "This paper derives analytic results; no new observational or simulation data were generated. All derivations, symbolic cross-checks, and the theory-audit machine-checkable assertions are available at the pinned commit `\repoSHA` (`research/theory_audit/p1n_r3_checks_2026_09_02.py`) in the public repository https://github.com/Hubify-Projects/bigbounce." | arxiv/paper1bc_ech_note/main.tex (repoSHA macro + acknowledgments) |
| Suggested reviewers | Endorser candidates NOT approached for the gr-qc endorsement (§1 of `ENDORSER_OUTREACH_2026-09-02.md` lists 6; only Popławski + one of Iosifidis/Agullo are asked to endorse) — suggest the remaining confirmed-eligible names: **Jérôme Quintin** (ÉTS/McGill, jquintin@physics.mcgill.ca), **Edward Wilson-Ewing** (UNB), **Christian Böhmer** (UCL), plus whichever of Iosifidis/Agullo was not the endorser | `ENDORSER_OUTREACH_2026-09-02.md` §1 table |
| Cover letter draft | "Dear Editors, I submit 'What Minimal Einstein–Cartan Torsion Does for the Bounce and Cannot Do for Dark Energy' for consideration as a CQG Paper. The manuscript derives a channel-level no-go result for minimal Einstein–Cartan–Holst gravity as a dark-energy source, complementing the published Einstein–Cartan bounce literature (Popławski et al.) that CQG regularly publishes. I am an independent researcher and the sole author; there are no conflicts of interest and no external funding. Thank you for your consideration. — Houston Golden" | drafted this session from the final abstract |
| Format at initial submission | Single PDF only — "You can format your paper in the way that you choose" | publishingsupport how-to-submit page |
| Source files | Required only **at revision** (TeX + figures) | publishingsupport "what files to submit at revision" page |
| arXiv/preprint | Permitted anywhere/anytime, **never required**, no declaration needed | IOP preprint policy page |
| Cost | **£0** on subscription route; optional gold OA **£2530 / €2905 / $3490** (no effective-date label found) | CQG About page |
| COI declaration | **MANDATORY** — in an Acknowledgements section | IOP ethical policy page |
| Funding declaration | **MANDATORY** — "declare any funding they received related to the research article" | IOP ethical policy page |
| Generative-AI disclosure | **MANDATORY if used** — must name model + version + how used, in Acknowledgements | IOP ethical policy page |
| Data-availability statement | Encouraged, not mandatory; placement: dedicated "Data availability" section immediately after Acknowledgements | IOP standard data policy page |
| Suggested/opposed reviewers | Optional field in ScholarOne; IOP not obliged to use them | how-to-submit page |
| Cover letter | Optional — "any pertinent information that could affect the way the manuscript is handled" | how-to-submit page |
| Speed (2026-07-24 metrics) | First decision before review ~6 days; after review ~54 days; desk-reject 63%; acceptance 21% | iopscience.iop.org About-the-journal page |

**Pre-submission checklist specific to the Note merge:**
1. Confirm the merged P1A+P1C manuscript compiles with the Acknowledgements
   block intact (COI + funding + AI-use — all three IOP-mandatory; the
   old P1A had them accidentally commented out until v1A.0.127 — do not
   repeat that failure mode in the merge).
2. Confirm ORCID is in the author block (was fixed in v1A.0.127 for the
   standalone P1A — verify it survives the merge).
3. Re-read the CQG "Research data" heading for a named DAS form variant
   before writing a fresh data-availability paragraph (unverified in the
   2026-07-24 kit — item 4 there).
4. `arxiv/main.tex` (the stale v2.3.18 monolith some reviewer prompts
   mistakenly cited as "P1A") is retired to `arxiv/_retired/` per the
   2026-09-02 decision — confirm the CQG upload comes from the merged
   P1A+P1C source, not that retired file.

---

## 2. P4′ → The Astrophysical Journal Supplement Series (ApJS), AAS eJournalPress

**Existing staging sheet:** `pipelines/p2_chirality/APJS_PORTAL_KIT_v1.0.274.md`
(prepared 2026-08-03) already has field values for the **pre-merge, P4-only**
version — title, abstract, UAT concepts, upload inventory. It predates the
P5-fold-in decision (2026-09-02 Track C1) and needs a title/abstract update
once P5 becomes a section of P4′ rather than a standalone paper. Reused facts
below; new facts are from fresh 2026-09-02 fetches of AAS journal policy
pages (`journals.aas.org`), since the existing kit did not cite live AAS
guideline URLs.

| Field | Value to paste | Source |
|---|---|---|
| Portal | AAS journals general submission system (eJournalPress) at `journals.aas.org/submission/`; select ApJS at manuscript-type step | journals.aas.org/manuscript-preparation/ (fetched 2026-09-02) |
| Article type | Regular Article — **confirm current label in the live portal**, unverified this session (existing kit flags the same) | pipelines/p2_chirality/APJS_PORTAL_KIT_v1.0.274.md |
| Title | **FINAL — "The Largest Test of a Preferred Galaxy-Spin Axis: An 8.47-Million-Galaxy DESI Chirality Catalog, a Void-Environment Contrast, and a Sensitivity Confrontation with the Rotating-Black-Hole-Universe Prediction"** (`pipelines/p4prime_chirality_test/paper/main.tex` v4P.0.4 — P5 folded in as the void-environment contrast) | pipelines/p4prime_chirality_test/paper/main.tex |
| Abstract | Final v4P.0.4 abstract, verbatim — see `ENDORSER_OUTREACH_2026-09-02.md` §2 for the full text | pipelines/p4prime_chirality_test/paper/main.tex |
| Abstract cap | **250 words** for standard AAS-journal articles (general AASTeX guideline; ApJS-specific page did not publish a different number this session — treat 250 as the working cap and confirm on ApJS's own About page before finalizing) | journals.aas.org/manuscript-preparation/ (fetched 2026-09-02) — **the final v4P.0.4 abstract (≈330 words) runs over 250 words; trim for the portal field or confirm the "extended abstract" convention before pasting as-is** |
| Data-availability statement text | Verbatim from the manuscript's `Data Availability` section: "The 8,474,531-row catalog, quarantine, exact null arrays, generator scripts, and full provenance register are archived under Zenodo DOI 10.5281/zenodo.21461899 (concept DOI 10.5281/zenodo.21461898), published under CC-BY-4.0, and mirrored at huggingface.co/datasets/bamfai/galaxy-chirality-catalog. The black-hole-universe exclusion analysis is fully reproducible from the committed script `research/bh_universe_dipole/poplawski_dipole_exclusion_2026_09_02.py` and its output JSON. The catalog is a single Apache Parquet file (952,115,239 bytes) with one row per DESI Legacy DR8 galaxy... This manuscript is served alongside its git-tracked source at github.com/Hubify-Projects/bigbounce." (full text, pipelines/p4prime_chirality_test/paper/main.tex `\section*{Data Availability}`) — **P5's own Zenodo DOI is still pending (residual item, click-list step 2); add it to this statement once minted.** | pipelines/p4prime_chirality_test/paper/main.tex |
| Software/facilities line (for ApJS) | Verbatim: "Software: NumPy, healpy, HEALPix, NaMaster (pymaster), PyTorch, pandas, SciPy. Facilities: DESI Legacy Imaging Surveys DR8 (data products); no proprietary telescope time was used in this analysis, which is entirely based on public archival imaging and catalog data." | pipelines/p4prime_chirality_test/paper/main.tex `\section*{Software, Facilities, and Acknowledgements}` |
| Suggested reviewers | Endorser candidates NOT approached for the astro-ph.GA endorsement (§2 of `ENDORSER_OUTREACH_2026-09-02.md` lists 6; only Desmond + Smethurst are asked to endorse) — suggest: **Karen Masters** (Haverford, Galaxy Zoo PI), **Brooke Simmons** (Lancaster), **Mike Walmsley** (Toronto/Dunlap, Zoobot) | `ENDORSER_OUTREACH_2026-09-02.md` §2 table |
| Cover letter draft | "Dear Editors, I submit '[final title above]' for consideration in ApJS. We release the largest chirality catalog to date (8.47M DESI Legacy DR8 galaxies) and confront the rotating-black-hole-universe spin-axis prediction, confirming the independent non-detections of Iye et al. (2021) and Patel & Desmond (2024) at higher statistical power than any prior sample except Shamir (2022). The catalog, quarantine set, and full provenance are Zenodo-archived under CC-BY-4.0. I am an independent researcher and sole author; no conflicts of interest, no external funding. Thank you for your consideration. — Houston Golden" | drafted this session from the final abstract |
| Running head | ≤44 characters | journals.aas.org/manuscript-preparation/ |
| Keywords | Unified Astronomy Thesaurus (UAT) concepts, 1–12 per the 2026-08-03 kit's own list: Spiral galaxies; Catalogs; Galaxy classification systems; Galaxy properties; Large-scale structure of the universe; Observational cosmology; Astrostatistics techniques; Sky surveys — **add "Galaxy dynamics" or similar if the merged version foregrounds the spin-axis prediction test more explicitly** | pipelines/p2_chirality/APJS_PORTAL_KIT_v1.0.274.md |
| ORCID | Not mandated by the fetched general guideline; AASTeX 7+ supports it — **enter it anyway** (`0009-0008-5616-5994`) since ApJS's own submission form commonly requests it | journals.aas.org/manuscript-preparation/ |
| Author info | Houston Golden, Independent Researcher, Los Angeles, CA, USA; `houston@hubify.com` | — |
| Data availability | AAS "encourages" data/digital-materials enrichment; no single mandated wording found this session — cite the Chen et al. 2022 "Best Practices for Data Publication" convention (doi:10.26132/NED7) and, since P4′ IS a large catalog release, be maximally explicit: name the HuggingFace dataset + model repos, CC-BY-4.0 license, and machine-readable-table convention (encouraged for >200 rows, which the catalog vastly exceeds) | journals.aas.org/data-guide/ (fetched 2026-09-02) |
| Machine-readable tables | Encouraged for tables with >200 rows — the 8.47M-row catalog should be released as a machine-readable table / linked dataset, not an inline table | journals.aas.org/data-guide/ |
| License / OA | AAS journals are open-access (moved to full OA per `aas.org/press/aas-journals-open-access` — confirm current APC amount live in the portal at submission time; not independently re-verified this session) | WebSearch result, 2026-09-02, unconfirmed against the primary page — **treat as directional, re-check `journals.aas.org` OA/APC page before relying on a dollar figure** |
| Cover letter | Not flagged as required by the fetched pages; the 2026-08-03 kit includes one anyway (reusable, needs title/journal-fit sentence updated for the merged framing) | pipelines/p2_chirality/APJS_PORTAL_KIT_v1.0.274.md |
| Suggested reviewers | Portal has a reviewer-suggestion field per the 2026-08-03 kit's checklist; format not independently verified this session | pipelines/p2_chirality/APJS_PORTAL_KIT_v1.0.274.md checklist |
| Upload format | AASTeX (currently `aastex701.cls`/`aastex702.cls` per the two source `.tex` files — **confirm both P4 and P5 sources are on the same AASTeX version before merging**, and that the merge doesn't silently mix class versions) | repo grep, `pipelines/p2_chirality/` + `pipelines/p5_desi_chirality/paper/` |

**Open item before this kit is submission-ready:** the title and abstract
above are now FINAL (v4P.0.4, P5 folded in as the void-environment
cross-check section) — the remaining open item is the **word-count trim**
against the 250-word AAS abstract cap (current abstract ≈330 words) and
minting P5's Zenodo DOI (click-list step 2). Do not paste the abstract into
the live portal without a portal-side length check.

---

## 3. P2′ Letter → Physical Review D Letters (primary) or JCAP (alternate) — **DEFERRED; retained as A3's venue reference**

**Status:** P2′ is not being submitted (archived theory record, folded into
the A3 multi-channel paper per the 2026-09-02 final-review recommendation).
The venue-mechanics rows below (portal, length limits, ORCID/DAS
requirements, arXiv-first gate for JCAP) remain valid and reusable for
**A3** (`research/track_a3_multichannel/paper/main.tex` v3M.0.2) once it
clears its remaining PBH compaction-function row and pending INT board —
A3 would submit as a PRD Letter or Research Article (confirm article type
once final) rather than a standalone P2′ Letter. Do not act on this section
as a live P2′ submission plan.

### 3a. PRD Letters (APS)

Source: `PRD_SUBMISSION_KIT_P2_2026-07-24.md` §1 (live-fetched 2026-07-24 via
text-reader proxy, since `journals.aps.org` blocks automated fetch directly).
The existing kit is bound to P2 as a full **Research Article** (no length
cap); P2′ under the 2026-09-02 decision is a **Letter**, a different article
type with different limits — pulling those rows out below.

| Field | Value to paste | Source |
|---|---|---|
| Portal | `https://authors.aps.org/Submissions/` (APS Submissions Server, not Editorial Manager) | journals.aps.org/prd/authors (fetched 2026-07-24) |
| Article type | **Letter** (not Research Article — P2′ is explicitly a Letter per Track A1) | — |
| Length limit | **4,500 words** for Letters (vs. no limit for Research Articles) | journals.aps.org/prd/authors, fetched 2026-07-24 |
| Abstract cap | ~5% of article length, **under 500 words** (general APS style rule; for a 4,500-word Letter, aim well under 250 words in practice) | journals.aps.org/authors/style-basics |
| Initial files | PDF only is sufficient for review; LaTeX preferred but not required at submission | journals.aps.org/prd/authors |
| arXiv | Not required; matters only for SCOAP³ free-OA eligibility on hep-designated arXiv categories (P2′'s astro-ph.CO cross-listed gr-qc likely does not qualify — confirm if OA route matters) | journals.aps.org/prd/about |
| ORCID | **REQUIRED** for corresponding author, with a post-submission verification email | journals.aps.org/authors/editorial-policies |
| Data Availability Statement | **MANDATORY** for PRD submissions since 2024-09-04 | journals.aps.org/prd/authors + editorial-policies |
| Cost | $0 subscription route; optional CC-BY OA **$2,910** (2026 APC table) | journals.aps.org/authors/apcs |
| Color figures (print) | $1,090 first figure / $595 each additional — almost certainly N/A for an electronic-only Letter | journals.aps.org/prd/authors |
| Cover letter | Where suggested/excluded referees go | existing PRD kit §8 |
| Author info | Houston Golden, Independent Researcher, Los Angeles, CA, USA; ORCID `0009-0008-5616-5994` (required, verification email will fire) | — |

**Gate — superseded:** P2′ itself will not be submitted (DEFERRED). The
independent second-method f_NL derivation gate that used to block P2′ is
inherited by A3's own remaining board work (PBH compaction-function row +
pending INT board) — do not treat this row table as actionable until A3
clears those and Houston confirms its target venue/article type.

### 3b. JCAP (SISSA) — alternate route

Fetched 2026-09-02 (`jcap.sissa.it` help pages via search; SISSA's own
domain blocked direct WebFetch this session — facts below are from search
summaries, **lower confidence than the CQG/PRD/ApJS rows above; re-verify by
logging into `jcap.sissa.it` directly before relying on any limit number**):

| Field | Value to paste | Source / confidence |
|---|---|---|
| Portal | `jcap.sissa.it` (SISSA's own submission system; all-electronic, "from submission to publication is automatic") | jcap.sissa.it help pages, 2026-09-02 search — **confirmed the portal exists and is self-hosted; specific field labels not independently fetched** |
| Registration | All users (authors, referees, editors) must register on the JCAP site itself — separate account from arXiv or APS | same, search-derived |
| **arXiv ID — REQUIRED at submission** | "It is required to provide an ArXiv id to submit an article to the journal." **This is the decisive fact for the PRD-vs-JCAP choice**: JCAP submission is gated on an arXiv posting existing first, so if Houston wants to submit P2′ to a journal before or independent of the arXiv drop, PRD Letters (arXiv not required) is the faster path; JCAP requires arXiv first. | jcap.sissa.it help pages, 2026-09-02 search — **medium confidence; verify on the live `jcap.sissa.it/jcap/help/helpLoader.jsp?pgType=author` page before treating as final**, but this is consistent with JCAP's known SISSA/arXiv-overlay publishing model |
| LaTeX class | JCAP house style class published at `jcap.sissa.it/jcap/help/JCAP_TeXclass.jsp`, with an author's manual PDF | jcap.sissa.it, 2026-09-02 |
| Article types / length limits | **Not independently confirmed this session** — JCAP traditionally does not publish a strict page cap for regular Papers but has historically supported shorter formats; do not assume a specific word count without checking the live author-help page | unresolved — flag for a follow-up live fetch before finalizing a JCAP submission |
| Cost | JCAP/SISSA journals have historically been open-access with author-side page charges funded via SCOAP³ for HEP-designated arXiv categories — **not independently confirmed this session for astro-ph.CO/gr-qc cross-listed content specifically** | unresolved |

**Recommendation given the two options:** PRD Letters is the better-verified
and faster path (arXiv not required, ORCID + DAS requirements already fully
mapped from the 2026-07-24 kit). JCAP requires an arXiv ID first, which
ties its timeline to the endorsement-gated arXiv submission
(`ENDORSER_OUTREACH_2026-09-02.md` §3) — only worth pursuing if Houston
specifically wants the JCAP venue for scope/audience reasons once arXiv is
live.

---

## 4. arXiv form fields (all three works, once each is submission-ready)

| Field | Value |
|---|---|
| ECH Note primary category | gr-qc |
| ECH Note cross-list | astro-ph.CO |
| P4′ primary category | astro-ph.GA |
| P4′ cross-list | astro-ph.CO |
| P2′ primary category | astro-ph.CO |
| P2′ cross-list | gr-qc |
| License | CC BY 4.0 (matches the Zenodo deposits and the lab's stated open-reproducibility policy per `CLAUDE.md` Q2) |
| Comments line | Free text — state page/figure count and, for P4′, the HuggingFace dataset URL(s) per the existing P4/P5 kit convention (`WAVE2_P5_SUBMISSION_KIT_2026-07-20.md` line 181: `"32 pages, 9 figures. ... Catalog and weights at huggingface.co/... Code at github.com/Hubify-Projects/bigbounce"`) |
| Report number | Blank (no internal report-number scheme in use) |
| Journal-ref | **Blank at initial submission** — filled in only after journal acceptance, never pre-filled |

---

## 5. Post-approval staging — commands documented, NOT executed

**Houston-only gate.** Per `INTENT.md` "Houston-only acts": minting a Zenodo
DOI and clicking submit are his acts. Nothing below has been run this
session; these are the exact commands to run once he says go.

### 5a. Zenodo new-version DOIs

`tools/zenodo_deposit.py` exists and is the fail-closed deposit tool
(confirmed present, `--help` inspected 2026-09-02). It reads `.zenodo.json` +
staged files from a `--staging-dir`, creates a **draft** deposition, uploads,
MD5-verifies every file, and only publishes with `--publish --confirm
PUBLISH`. Token comes from `$ZENODO_TOKEN` or repo `.env.local`, never
printed.

- **P4′ new version** (concept DOI `21461898` per Houston's brief — confirm
  this is the correct concept ID for the P4/P5-merged record before running,
  since the existing Zenodo reference table in
  `ENDORSEMENT_REQUEST_DRAFTS_2026-07-24.md` lists P4's concept-adjacent DOI
  as `10.5281/zenodo.21461899`, which is the *version* DOI of the same record; see the DOI note below):
  ```bash
  python3 tools/zenodo_deposit.py \
    --staging-dir <path-to-staged-P4-prime-files> \
    --paper P4prime \
    --receipt-out project-context/SSOT/zenodo/P4prime_zenodo_receipt_<date>.json \
    --deposition-id 21461898
  # verify the draft in the Zenodo web UI, THEN, only with explicit go-ahead:
  python3 tools/zenodo_deposit.py \
    --staging-dir <path-to-staged-P4-prime-files> \
    --paper P4prime \
    --receipt-out project-context/SSOT/zenodo/P4prime_zenodo_receipt_<date>.json \
    --deposition-id 21461898 \
    --publish --confirm PUBLISH
  ```
- **ECH Note new version** (concept DOI `21481837` per Houston's brief —
  cross-check against `ENDORSEMENT_REQUEST_DRAFTS_2026-07-24.md`'s P1A row,
  `10.5281/zenodo.21481838`, its version DOI; see the DOI note below):
  ```bash
  python3 tools/zenodo_deposit.py \
    --staging-dir <path-to-staged-ECH-note-files> \
    --paper ECHNote \
    --receipt-out project-context/SSOT/zenodo/ECHNote_zenodo_receipt_<date>.json \
    --deposition-id 21481837
  # verify draft, then --publish --confirm PUBLISH only on explicit go-ahead
  ```

**DOI note (resolved by the orchestrator, 2026-09-02):** there is no
discrepancy. `21461898` (P4) and `21481837` (P1A) are the Zenodo *concept*
DOIs; `21461899` and `21481838` are the *version* DOIs of the archived
releases (both pairs recorded in `SSOT/index.md`, DOI-COMPLETE 2026-07-21).
`tools/zenodo_deposit.py --deposition-id` takes a *draft deposition id*, not a
concept id: the new-version flow is (1) Houston clicks **New version** on the
published record (21461899 / 21481838) in the Zenodo UI, (2) copy the new
draft's deposition id from the URL, (3) run the commands above with that id.
Never pass the concept id.

### 5b. arXiv tarballs via bib-tarball-rebuild

Skill at `~/.claude/scistack/hubstack/publishing/bib-tarball-rebuild/SKILL.md`.
For each of the three works, once its manuscript is final:
1. Confirm the registered `.tex` stem in `project-context/paper_registry.json`
   (do not hardcode `main` — the retired `arxiv/main.tex` monolith is exactly
   the file this convention exists to avoid).
2. Parse `\cite{}` keys from the `.tex` and reconcile against the `.bbl`
   (catches the "stale .bbl" arXiv-submission failure mode).
3. Rebuild the tarball from scratch in `/tmp` with only referenced figures.
4. Smoke-test: re-extract + recompile standalone, 0 undef-refs.
5. Only then hand the tarball to Houston for the arXiv upload click.

Not run this session — no merged manuscript exists yet for any of the three
works.

---

## 6. What is NOT done here

- ECH Note (v1N.0.4) and P4′ (v4P.0.4) manuscripts ARE compiled, merged
  where applicable, APPROVE at agent gates, readiness 95 — titles/abstracts
  above are final, not draft.
- No Zenodo deposit command was run (draft or publish) this session — both
  new-version mints (ECH Note theory-audit artifacts; P5 under P4) are
  click-list items, not yet executed.
- No arXiv tarball upload was clicked — tarballs are built and
  standalone-recompile-verified on disk (sha256 in §1/§2 above); the
  upload click itself is Houston's.
- No endorsement email was sent (see `ENDORSER_OUTREACH_2026-09-02.md`).
- P2′ is DEFERRED — no submission planned; its content lives in A3, which
  is not yet reviewable.
- The JCAP field table (§3b) is search-derived, not independently
  live-fetched from `jcap.sissa.it` itself — treat as directional and
  re-verify before relying on any specific limit; also not yet actionable
  since it is retained only as A3's future venue reference.
