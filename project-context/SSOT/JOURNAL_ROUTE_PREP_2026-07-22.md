# Journal Route Prep — JORS (P1B) + ApJS (P3), no-arXiv-required tracks

**Date:** 2026-07-22 (research completed 2026-07-23)
**Scope:** Research + repo-doc only. No submission, no account creation, no emails were performed by this worker. Every requirement claim below is source-cited; anything not confirmed from an official source is marked **UNVERIFIED**.

---

## 1. JORS (Journal of Open Research Software) — P1B `namaster-proof` software metapaper

**Manuscript:** `arxiv/paper1b_namaster_proof.pdf` / `.tex`, v2B.0.14 (2026-07-22)
**Software:** `namaster-proof` 0.1.7, MIT License, `packages/namaster-proof/`
**DOIs:** software 10.5281/zenodo.21481753 (archived source, commit `0a587b58`); manuscript 10.5281/zenodo.21481842 (CC-BY-4.0)

### Confirmed current (2026) requirements, with sources

| Requirement | Detail | Source |
|---|---|---|
| Submission portal | Web-based portal at `account.openresearchsoftware.metajnl.com`, submission wizard | [Submission Guidelines](https://openresearchsoftware.metajnl.com/about/submissions) |
| Manuscript format | Software Metapapers must conform to JORS's own template, submitted as **.docx or LaTeX (+ PDF for LaTeX)** | [Submission Guidelines](https://openresearchsoftware.metajnl.com/about/submissions) |
| Structure | No more than 3 heading levels; JORS's own model is 3 top sections — Overview (title/authors/abstract), Availability, Reuse Potential — but "authors should structure the article as they see fit" | [Submission Guidelines](https://openresearchsoftware.metajnl.com/about/submissions); [About](https://openresearchsoftware.metajnl.com/about) |
| Repository requirement | Software must be in a public repository under an OSI-approved or CC0 license; repo must be sustainable, support long-term preservation, and provide a **persistent identifier (DOI/handle)** | [About](https://openresearchsoftware.metajnl.com/about) |
| Qualifying repositories | GitHub + Zenodo explicitly named as acceptable (Zenodo supports automated GitHub import and mints the DOI) | [About](https://openresearchsoftware.metajnl.com/about) |
| Peer review model | Single-anonymous (single-blind); reviewers may optionally sign | [Editorial Policies](https://openresearchsoftware.metajnl.com/about/editorialpolicies) |
| Review depth | Journal aims for 1–2 review rounds to reach a publishable metapaper | [Editorial Policies](https://openresearchsoftware.metajnl.com/about/editorialpolicies) |
| Typical timeline | ~21 weeks average from submission to publication (third-party aggregator, not the journal's own page) | [journalseeker.com aggregator](https://journalseeker.com/journal.php?q=journal+of+open+research+software) — **UNVERIFIED against the journal's own published stats page** |
| APC / fee | **£824.00** for Software Metapapers (+ tax where applicable); fee waivers/discounts available if requested in the cover letter at submission | [Submission Guidelines](https://openresearchsoftware.metajnl.com/about/submissions) |
| Article license | CC-BY 4.0, authors retain copyright | [About](https://openresearchsoftware.metajnl.com/about) |
| Software license | OSI-approved license recommended (MIT/GPL/Apache-2.0/BSD); less restrictive = higher reuse-potential score | [About](https://openresearchsoftware.metajnl.com/about) |
| Preprint / arXiv | **Not required.** Prior posting to preprint servers, personal sites, or conference presentation is explicitly *not* deemed prior publication | [Submission Guidelines](https://openresearchsoftware.metajnl.com/about/submissions) |
| ORCID | **Not mentioned** anywhere in JORS's public submissions/about/editorial-policy pages — no confirmed requirement either way | UNVERIFIED (absence across all 3 fetched JORS policy pages) |
| Author affiliation | Not specified as a requirement | UNVERIFIED (absence in fetched pages) — unaffiliated/independent-researcher authorship is not flagged as an issue anywhere in JORS's guidelines |
| Post-acceptance obligation | Authors must copy the final article citation back into the software repository | [About](https://openresearchsoftware.metajnl.com/about) |

### READY / MISSING checklist — JORS / P1B

**READY**
- [x] Software openly licensed: MIT (`packages/namaster-proof/LICENSE`) — matches JORS's OSI-approved requirement.
- [x] Software in a public repo with a persistent identifier: GitHub (`Hubify-Projects/bigbounce/tree/main/packages/namaster-proof`) + Zenodo DOI `10.5281/zenodo.21481753` for the exact 0.1.7 / commit-`0a587b58` archive — satisfies the repository + PID requirement directly.
- [x] `CITATION.cff` and `codemeta.json` present and populated (`packages/namaster-proof/CITATION.cff`, `codemeta.json`) — supports the "copy citation back to repo" post-acceptance step and general metadata completeness JORS reviewers check.
- [x] Manuscript maps onto JORS's Overview / Availability / Reuse Potential model: Introduction + Statement of Need ≈ Overview; explicit `\section{Availability}` (license, archive DOIs, install instructions, validation-artifact SHA-256s); explicit `\section{Reuse Potential}`. Extra sections (Implementation, Exact-Window Inference, Content Validation, Quality Control, Worked Examples, Limitations, AI Usage Disclosure) are additive and within JORS's "structure as you see fit, ≤3 heading levels" latitude.
- [x] Compiled PDF exists and is current: `arxiv/paper1b_namaster_proof.pdf`, **v2B.0.15** (2026-07-24, closes below).
- [x] Manuscript itself separately archived with its own DOI (10.5281/zenodo.21481842, CC-BY-4.0) — exceeds what JORS asks for (JORS only requires the *software* PID).
- [x] No arXiv posting needed — confirmed not required by JORS.
- [x] No author-affiliation barrier — Houston Golden, independent researcher, is not disqualifying per any fetched JORS page.
- [x] Software's test contract is honestly stated in-paper (39 run + 2 monorepo-coupled skips) — relevant to JORS's "correctness of metadata / accessibility of software" review criterion.
- [x] **ORCID now embedded in the manuscript (CLOSED 2026-07-24).** `arxiv/paper1b_namaster_proof.tex` author block now reads `Houston Golden\\Independent researcher\\[2pt]\href{https://orcid.org/0009-0008-5616-5994}{ORCID: 0009-0008-5616-5994}` — Houston's verified ORCID `0009-0008-5616-5994` (the older `...3617-8729` iD found in some historical docs is confirmed WRONG and was not used). No house style existed across the other five papers' *current* `.tex` sources (grep of `arxiv/*.tex`, `pipelines/*/*.tex`, `research/*/*.tex` for `orcid` returned zero hits in the canonical files); a stale legacy P2 draft at `research/focused_paper_source_integration/arxiv_package/main.tex` has an unlinked `\orcidicon` placeholder with no numeric ID rendered, so it was not treated as an established precedent. A clean `\href` to `orcid.org` was used per the task spec's fallback instruction. Verified rendering on the recompiled page 1 (`pdftoppm` render, read visually — clickable blue "ORCID: 0009-0008-5616-5994" line under the affiliation, no overflow).

**JORS TEMPLATE CONFORMANCE — RESOLVED (2026-07-24), template IS required at initial submission**
- [x] **Authoritative answer obtained.** Fetched `https://openresearchsoftware.metajnl.com/about/submissions` directly (raw HTML, not just the AI-summarized fetch) and located the journal's own **"Submission Preparation Checklist"** section (`#submission-checklist`), which states: *"All submissions must meet the following requirements... For Software Metapapers: ... The submission conforms to the article template. For LaTex submissions, a PDF should be provided along with the original LaTex file(s). Submissions in .docx format are also acceptable."* This is a self-certified checklist item **gating the submission itself** (an OJS-standard "Submission Preparation Checklist" ticked at the point of upload) — i.e. **(a) template conformance is required AT INITIAL SUBMISSION, not deferred to camera-ready.** Source: [Submission Guidelines — Submission Preparation Checklist](https://openresearchsoftware.metajnl.com/about/submissions#submission-checklist), fetched 2026-07-24.
- [x] **Downloaded and inspected the actual LaTeX template** (linked from the same page's "Templates" list as "LaTex Template" → `https://account.openresearchsoftware.metajnl.com/index.php/up-j-jors/libraryFiles/downloadPublic/3`, filename `JORS_Template.zip`). Contents: `jors.cls` (`\ProvidesClass{josr}`, a thin wrapper — `\LoadClass[a4paper]{article}` plus `xcolor`/`sectsty`/`enumitem`/`hyperref`/`fancyhdr`/`titlesec`, 1.2in margins, 12pt default, no-indent paragraphs) and `jors_template.tex` (`\documentclass{jors}`), with a mandated exact heading sequence: `(1) Overview` → `Title` / `Paper Authors` / `Paper Author Roles and Affiliations` / `Abstract` / `Keywords` / `Introduction` / `Implementation and architecture` / `Quality control` → `(2) Availability` → `Operating system` / `Programming language` / `Additional system requirements` / `Dependencies` / `List of contributors` / `Software location` / `Language` → `(3) Reuse potential` → `Acknowledgements` / `Funding statement` / `Competing interests`.
- [ ] **GENUINE, NOT YET CLOSED: manuscript does not use `jors.cls` or the mandated heading sequence.** `arxiv/paper1b_namaster_proof.tex` is `\documentclass[11pt]{article}` with its own section structure (Introduction, Statement of Need, Implementation, Exact-Window Inference, Content Validation, Quality Control, Worked Examples, Availability, Reuse Potential, Limitations, AI Usage Disclosure) — substantively equivalent content, mapped onto JORS's 3-part model, but not the literal template file or its exact subsection headers (`Title`/`Paper Authors`/`Paper Author Roles and Affiliations` as separate `\section*` blocks; `Operating system`/`Programming language`/`Additional system requirements`/`Dependencies`/`List of contributors`/`Software location` as separate headers under Availability). **Per task instruction this agent is NOT auto-restructuring the manuscript** — that is a real, nontrivial rewrite (new class file + heading reorganization + re-verification of the whole `\section{Availability}`/`\section{Reuse Potential}` content against the template's granular subsections) that should be scoped as its own closure pass, not folded silently into an ORCID/hygiene patch. Flagged for Houston/next P1B-lane agent: adopt `jors.cls` + `jors_template.tex`'s heading skeleton, port the existing prose into the mandated subsections, recompile, re-run directive-G hygiene. The downloaded template is staged for reuse at `/private/tmp/claude-501/-Users-houstongolden-Desktop-CODE-YOU/f7fc5dec-47e4-4a55-a3c8-f7744dff894f/scratchpad/jors_template_extract/JORS_Template/` (session-scratchpad only — not committed; re-download from the URL above when the restructuring pass runs).
- [ ] **JORS account + submission click** (account.openresearchsoftware.metajnl.com) — explicitly out of scope for this worker (no account creation). Genuine next human step.
- [ ] **APC £824.00** — either budget for it or draft a waiver request for the cover letter at submission time; not verified whether Houston/BAMF has a standing waiver arrangement.

**Verdict (updated 2026-07-24):** ORCID item CLOSED (real edit, verified in the recompiled v2B.0.15 PDF). Template-conformance item is now a **CONFIRMED, cited requirement** (no longer UNVERIFIED) but remains a genuine open MISSING item — the manuscript must be ported onto JORS's own `jors.cls`/heading skeleton before a clean submission click. The APC and account creation remain Houston's own next actions.

---

## 2. ApJS (The Astrophysical Journal Supplement Series) — P3 DESI catalog paper

**Manuscript:** `pipelines/p3_anomaly_engine/paper3_apjs.pdf` / `.tex`, v3.2.0-r12 (2026-07-22)
**Zenodo archival DOI (of the reviewed v3.2.0-r10 bytes):** 10.5281/zenodo.21461888 (version) / 10.5281/zenodo.21461887 (concept)

### LaTeX class check (explicit verification requested)

`pipelines/p3_anomaly_engine/paper3_apjs.tex` line 8: `\documentclass[twocolumn]{aastex701}`.

`aastex701.cls` **is** the current AAS class file — despite the "701" filename, it is **AASTeX v7.0.1**, the newest major AASTeX release (announced March 2025, class file dated 2025-05-09), replacing the older `aastex631`/`aastex63` lineage. Confirmed via the AAS's own GitHub repo and journals.aas.org's own hosted copy of the file:
- [AASJournals/AASTeX7 — aastex701.cls on GitHub](https://github.com/AASJournals/AASTeX7/blob/main/aastex701.cls)
- [journals.aas.org hosted aastex701.cls](https://journals.aas.org/wp-content/uploads/2025/05/aastex701.cls)
- [AAS Nova: "A New AASTeX Has Dropped!" (2025-03-04)](https://aasnova.org/2025/03/04/aas-publishing-news-a-new-aastex-has-dropped/)
- [AASTeX v7.0 Author Guide](https://journals.aas.org/aastexguide/)

**No class conversion is needed.** P3 is already on the current required class and already framed for ApJS (`twocolumn`, correct AAS journal macros).

### Confirmed current (2026) requirements, with sources

| Requirement | Detail | Source |
|---|---|---|
| Submission portal | Single portal for AJ/ApJ/ApJL/ApJS/PSJ/RNAAS at `aas.msubmit.net/cgi-bin/main.plex` ("Submit a manuscript") | [Manuscript Submission](https://journals.aas.org/submission/) |
| AASTeX version | AASTeX v7 (`aastex701.cls`) is current; v6+ still explicitly accepted for some features (e.g. `linenumbers`), but v7 is the actively promoted current package | [Manuscript Preparation](https://journals.aas.org/manuscript-preparation/); [AASTeX Package page](https://journals.aas.org/aastex-package-for-manuscript-preparation/) |
| Abstract limit | "a single paragraph of not more than 250 words" (AJ/ApJ/ApJL/ApJS/PSJ; Research Notes is 150) | [Manuscript Preparation](https://journals.aas.org/manuscript-preparation/) |
| ORCID | AASTeX7's peer-review system "will also extract affiliations, e-mails, and ORCIDs to help identify authors already in our peer review system" — ORCID is *used/read* by the system; **no page states it is mandatory for submission to proceed** | [Manuscript Preparation](https://journals.aas.org/manuscript-preparation/) — mandatoriness **UNVERIFIED** |
| Data-behind-figures / digital assets | AAS *encourages* (does not universally mandate) enriching articles with data; offers data review, archiving data behind figures, linking to outside repositories; recommends **Zenodo (AAS Journals Community)** or Harvard Dataverse for deposits | [Data Guide](https://journals.aas.org/data-guide/) |
| Digital-asset DOI minting | AAS does **not mint its own DOI at submission** — it accepts/prefers external repository DOIs (e.g. Zenodo); the AAS *journal* digital-asset DOI is a separate thing the journal assigns during its own production workflow, after acceptance | [Data Guide](https://journals.aas.org/data-guide/); P3's own honest in-text framing (`paper3_apjs.tex` lines 933-941) matches this |
| Machine-readable tables | MRTs strongly encouraged for tables >~200 rows or with critical object data; **required** in machine-readable format (with only an abbreviated example in-text) once a table exceeds 400 lines | [Data Guide](https://journals.aas.org/data-guide/) |
| AAS membership | **No mention found on any fetched AAS author/policy/submission page** that membership is required to submit or publish | UNVERIFIED (absence-based only — checked `/submission/`, `/policies/`, `/manuscript-preparation/`, `/author-resources/`) |
| Publication charges (APC) | Tiered by "digital quanta" as of 2026: ApJS **$1,172** (≤30 quanta), **$2,651** (31–50), **$4,589** (51–100), +$250 long-article surcharge (>100 quanta) | [manusights.com ApJ APC summary, third-party aggregator](https://manusights.com/blog/astrophysical-journal-apc-open-access) — **UNVERIFIED against AAS's own official rate-schedule page** (not independently fetched this pass) |
| Open access / license | All AAS journals are Gold OA since 1 Jan 2022; articles published CC-BY 4.0, authors retain copyright | [AAS OA transition](https://journals.aas.org/oa/) |
| arXiv / preprint requirement | **Not required.** No AAS page states arXiv posting is a prerequisite for submission; posting before, during, or after is author's choice | Confirmed by absence across [FAQ](https://journals.aas.org/faq-accessible/), [Manuscript Preparation](https://journals.aas.org/manuscript-preparation/), and general search — **UNVERIFIED as an explicit "not required" statement**, but no source states otherwise |

### READY / MISSING checklist — ApJS / P3

**READY**
- [x] **Correct LaTeX class already in use** — `aastex701` (AASTeX v7.0.1), the current required class. No conversion work needed.
- [x] Author block has full name, affiliation, and email: `Houston Golden`, `Independent Researcher, Los Angeles, California, USA`, `houston@hubify.com` (`paper3_apjs.tex` lines ~66-69).
- [x] Data Availability (`\section*{Data Availability}`) and Software (`\section*{Software}`) sections present, with exact software versions, catalog release paths, checksums, and license terms (CC BY 4.0 for data).
- [x] Full 181-row / 43-column MRT-style catalog (`tab3.tsv`) plus column dictionary and SHA-256 manifest already staged in `pipelines/p3_anomaly_engine/aas_submission_v3.2.0-r4/` — exceeds the AAS machine-readable-table bar even though the row count (181) is under the "strongly encouraged" 200-row trigger.
- [x] Zenodo archival DOI for the reviewed manuscript bytes embedded in-text and honestly scoped: `10.5281/zenodo.21461888` (version) / `10.5281/zenodo.21461887` (concept), with an explicit, non-fabricated statement that the AAS journal digital-asset DOI is a separate, still-open, publication-workflow gate (not claimed).
- [x] Keywords use AAS-style Unified Astronomy Thesaurus format: `catalogs --- surveys --- methods: data analysis --- methods: statistical --- galaxies: spectra --- quasars: general`.
- [x] No AAS membership barrier identified in any current policy page.
- [x] No arXiv preprint required or expected as a gate.
- [x] Software/build environment fully version-pinned in-text (Python 3.9.6, NumPy 1.26.4, pandas 2.1.4, SciPy 1.13.1, fitsio 1.3.0, PyArrow 21.0.0) with `PROVENANCE.json` cross-reference.

**MISSING / BLOCKING**
- [ ] **Abstract is far over the AAS 250-word limit.** Word-counted the current `\begin{abstract}…\end{abstract}` block in `pipelines/p3_anomaly_engine/paper3_apjs.tex` at **~415 words** (raw word-split; LaTeX-markup-adjusted count is still well north of 300). AAS's own Manuscript Preparation page states the abstract must be "a single paragraph of not more than 250 words." **This is a genuine, concrete blocker to a clean ApJS submission click** — the abstract needs a ~40%+ cut before submission, independent of any other gate.
- [ ] **ORCID not embedded in the manuscript.** Same issue as P1B — `\author{Houston Golden}` carries no `\author[ORCID]{}` binding. AASTeX7's system reads ORCIDs from the peer-review system/author profile rather than strictly requiring an in-text macro, so this is not confirmed as a hard blocker, but it should be added to `\author[0009-0008-5616-5994]{Houston Golden}` (standard AASTeX7 syntax) before submission for correctness and to pre-populate the portal's author-identity fields.
- [ ] **Zenodo archival DOI is one point release stale relative to the current manuscript.** The in-text DOI paragraph (lines ~933-941) honestly states the archive pins the reviewed `v3.2.0-r10` PDF while the manuscript was `v3.2.0-r11` at the time ("one patch ahead ... will be added to the same Zenodo concept record on the next re-stage"). The manuscript has since advanced to **v3.2.0-r12** — the gap is now two patch releases, not one. Not a submission blocker (the DOI paragraph is honestly scoped either way and doesn't claim r12 coverage), but the "one patch ahead" wording will read as stale/inaccurate once someone checks it against the live `\paperVersion` macro — worth a one-line re-stage/reword before the actual submission.
- [ ] **AAS submission-portal account + manuscript upload** (`aas.msubmit.net`) — explicitly out of scope for this worker (no account creation). Genuine next human step.
- [ ] **APC budgeting** — tiered $1,172–$4,589+ depending on final "digital quanta" count; the rate-schedule figure above is from a third-party aggregator, not AAS's own official page, so **UNVERIFIED** — should be confirmed against AAS's own current fee schedule before submission (not confirmed as blocking the submission click itself; AAS typically invoices post-acceptance).
- [ ] **No AI Usage Disclosure section in P3** (P1B has one; P3 does not, per section-heading grep of `paper3_apjs.tex`). Whether AAS mandates an AI-disclosure statement is **UNVERIFIED** — no AAS-specific policy page was found confirming or denying this; general 2026 academic-publishing trend leans toward requiring one. Recommend adding a short disclosure section preemptively given the AI-assisted development already disclosed for P1B and the rest of the repo's practice.

**Verdict:** Real, concrete blocker exists: the abstract is roughly 165 words (66%) over the AAS 250-word cap and must be shortened before a clean submission. Everything else (class, author metadata, data/DOI framework, no-membership, no-arXiv-requirement) is either already satisfied or a routine portal-entry/account step outside this worker's scope.

---

## 3. Summary table

| | JORS / P1B | ApJS / P3 |
|---|---|---|
| Correct format already in repo? | Plain `article` class — JORS template conformance **CONFIRMED required at submission** (Submission Preparation Checklist, fetched 2026-07-24), NOT yet ported to `jors.cls` — genuine open item | ✅ `aastex701` (current AASTeX v7.0.1) — no conversion needed |
| arXiv required? | ❌ Not required (confirmed) | ❌ Not required (no source states otherwise) |
| AI usage disclosure present? | ✅ Yes (`\section{AI Usage Disclosure}`) | ❌ Missing |
| ORCID embedded in manuscript? | ✅ **Closed 2026-07-24** — v2B.0.15, `0009-0008-5616-5994` | ❌ Missing (same value) |
| Persistent software/data identifier? | ✅ Zenodo DOI 10.5281/zenodo.21481753 | ✅ Zenodo DOI 10.5281/zenodo.21461888 |
| Concrete content blocker? | **`jors.cls`/heading-skeleton porting still open** (see §1) | **Abstract ~415 words vs. 250-word AAS limit** |
| Fee | £824.00 (Software Metapaper) | $1,172–$4,589+ tiered (UNVERIFIED vs. AAS's own page) |
| Membership/affiliation gate? | None found | None found |
| Account creation (human step, out of scope here) | account.openresearchsoftware.metajnl.com | aas.msubmit.net |

---

*Prepared by the journal-route-prep worker, 2026-07-22/23. No arXiv submission, no journal account creation, and no emails were performed. All claims above are source-linked; items without an authoritative citation are explicitly marked UNVERIFIED.*
