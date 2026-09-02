# Portal kits — 2026-09-02 lineup (CQG / ApJS / PRD Letters / JCAP)

Field-by-field paste sheets for the three near-term works
(`INTENT.md` Track A1/B1/C1): the **ECH Note** → CQG, **P4′** → ApJS, **P2′
Letter** → PRD Letters (primary) or JCAP (alternate). Reuses and re-labels
verified facts already on file (`CQG_SUBMISSION_KIT_P1A_2026-07-24.md`,
`PRD_SUBMISSION_KIT_P2_2026-07-24.md`, `pipelines/p2_chirality/APJS_PORTAL_KIT_v1.0.274.md`)
where those facts are archive-level and still current; adds fresh fetches
(2026-09-02) for ApJS and JCAP specifics not covered by the existing kits.
**None of these manuscripts exist in their new (merged/condensed) form yet.**
This is a paste-sheet for when they do — not a submission record.

---

## 1. ECH Note → Classical and Quantum Gravity (IOP), article type **Note**

Source: `CQG_SUBMISSION_KIT_P1A_2026-07-24.md` §1 (live-fetched 2026-07-24,
6 weeks old — IOP policy pages change rarely; re-fetch only if Houston wants
a hard re-check before clicking submit). Reused verbatim below; the only
change from the 2026-07-24 kit is the manuscript target (merged P1A+P1C
Note, not standalone P1A) and title.

| Field | Value to paste | Source |
|---|---|---|
| Portal | `https://mc04.manuscriptcentral.com/cqg-iop` (ScholarOne) | iopscience.iop.org/journal/0264-9381/page/submission-options |
| Account | New ScholarOne account required (first-time author) | publishingsupport.iopscience.iop.org how-to-submit page |
| Article type | **Note** — "brief articles that make a short, interesting point... not normally merit publication as a full Paper but still make a useful and novel addition" | CQG About page |
| Length limit | **None published** for Note (verified-by-absence); target ≤12 pp per `INTENT.md` Track B1 self-imposed cap | CQG About/guidelines pages |
| Title | *Minimal Einstein–Cartan–Holst gravity: what spin-torsion does for the bounce and cannot do for dark energy* (working — pending merged manuscript's actual title) | — |
| Abstract cap | **300 words hard cap** — "we may rescind the manuscript and ask you to re-write it" if over | CQG guidelines page |
| Keywords | Free-text, no PACS required | CQG guidelines page |
| Author info | Houston Golden, Independent Researcher, Los Angeles, CA, USA; `houston@hubify.com`; ORCID `0009-0008-5616-5994` (recommended, not mandatory) | CQG guidelines page |
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
| Title | *[UPDATE FOR MERGE]* — the 2026-08-03 kit's title is P4-only ("An Observed-Label Chirality-Dipole Null in 890,069 Quality-Controlled High-Confidence DESI Spirals and an 8.5-Million-Galaxy Catalog"); per Track C1 framing this should foreground the rotating-black-hole-universe spin-axis test and note P5's environment cross-check is folded in | INTENT.md Track C1 |
| Abstract cap | **250 words** for standard AAS-journal articles (general AASTeX guideline; ApJS-specific page did not publish a different number this session — treat 250 as the working cap and confirm on ApJS's own About page before finalizing) | journals.aas.org/manuscript-preparation/ (fetched 2026-09-02) — **existing kit's abstract (§ above, 890,069/8,474,531 language) runs well over 250 words; it will need cutting or the portal's "extended abstract" convention confirmed** |
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

**Open item before this kit is submission-ready:** the 2026-08-03 kit's
abstract, title, and UAT list all need a pass reflecting P5 as a folded-in
section (void/non-void environment cross-check) rather than a separate
paper, and a word-count check against the 250-word AAS cap (the current
abstract text is materially longer). Do not paste the 2026-08-03 abstract
into the live portal unverified against that cap.

---

## 3. P2′ Letter → Physical Review D Letters (primary) or JCAP (alternate)

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

**Gate before this section is actionable:** P2′ does not exist as a
condensed ≤4,500-word Letter yet — the current source
(`research/focused_paper_source_integration/02_full_draft.tex`) is a full
Research Article, and per the portfolio decision an **independent
second-method f_NL derivation** (Salopek–Bond or δN) must land before any
submission regardless of venue.

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

- No manuscript was compiled, merged, or condensed.
- No Zenodo deposit command was run (draft or publish).
- No arXiv tarball was built.
- No endorsement email was sent (see `ENDORSER_OUTREACH_2026-09-02.md`).
- The JCAP field table (§3b) is search-derived, not independently
  live-fetched from `jcap.sissa.it` itself — treat as directional and
  re-verify before relying on any specific limit.
