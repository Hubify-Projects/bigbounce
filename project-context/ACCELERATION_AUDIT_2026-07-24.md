# Acceleration + journal-route audit — 2026-07-24

**Scope:** read-only audit. One question: *what is the fastest honest path from
today's state to all six papers actually published, and what is currently
getting in the way that nobody has noticed?*

**Method:** every claim below is verified against the artifact on disk or a live
URL fetched during this audit. Where a repo document asserts something that the
artifact does not support, that is stated plainly. Anything not confirmable from
an official source is labelled **UNVERIFIED** with the check that would settle
it. No file other than this one was modified; nothing was submitted, published,
or emailed.

**Pinned state at audit time** (HEAD `344125ce`): P1A v1A.0.126 · P1B v2B.0.15 ·
P2 v1.7.128 · P3 v3.2.0-r13 · P4 v1.0.271 · P5 v0.1.143-2026-07-24. Two parallel
lanes moved P1B and P5 *during* this audit; their in-flight work (P5→P4 Zenodo
back-patch, P5 deposit staging, P1B ORCID/JORS conformance, arXiv endorser
drafts) is treated as done and is **not** re-reported here.

---

## Executive summary

### The single fastest path to first publication

**Two zero-cost submissions can leave this week, and neither needs arXiv.** Rank
them by what you want first:

- **Fastest to a real editor's desk — today, zero blocking edits: P2 →
  Physical Review D.** APS requires **only a PDF** at initial submission
  (*"We only require a PDF file for a new submission"*), arXiv is an optional
  import and not a gate (*"If you do not wish to directly upload from arXiv, you
  will be given the opportunity to provide your arXiv id later"*), and the
  subscription route carries **no APC** ($2910 applies only if CC-BY OA is
  elected). P2's PDF exists, its abstract has no cap to breach, and it has **no
  blocking content defect** — only two quality fixes worth riding along (§1.2).
  SSOT already routes it here: `project-context/SSOT/paper-2/status.md:42` records
  the edit loop as *"EXHAUSTED"* with *"Next gate: Houston venue / human-referee
  decision."* That decision has been the open item; the venue research now says
  go. **This paper has been submittable for some time and nobody noticed.**
- **Lowest editorial bar, therefore fastest to an actual acceptance: P1A →
  Classical and Quantum Gravity, article type "Note".** One agent-executable
  edit stands in the way (§1.1).

Do both. They are independent papers at independent publishers, both free, both
arXiv-free. Detail on P1A, the stronger *publication* bet:

| Gate | P1A / CQG |
|---|---|
| arXiv preprint required? | **No.** IOP: *"our authors are permitted to share a Preprint of their article anywhere at any time"* — permitted, never required ([IOP preprint policy](https://publishingsupport.iopscience.iop.org/preprint-pre-publication-policy/)) |
| Manuscript format | **Format-free at initial submission.** CQG: *"You can format your paper in the way that you choose! It is not necessary to try to produce pages that look like published journal pages."* revtex4-2 ships as-is, zero conversion ([CQG author guidelines](https://publishingsupport.iopscience.iop.org/journals/classical-and-quantum-gravity/)) |
| Cost | **£0.** CQG: *"Publication on a subscription-access basis is free of charge."* Gold OA is optional at £2530 |
| Abstract cap | None published. P1A's live abstract is 268 words — no cap to breach |
| Cross-paper dependency | **Zero.** All 38 `\cite{Golden2026P1b/P2}` uses sit inside `\begin{comment}` blocks and do not compile — verified by `pdftotext`, the 8-page Note's bibliography contains only third-party literature |
| Artifact links | 20 URIs, 0 dangling |
| What blocks it today | One agent-executable edit: the compiled Note has **no** conflict-of-interest, funding, or AI-usage statement, because the whole Acknowledgments block is trapped at `arxiv/paper1a_ech_nogo.tex:4043-4730` inside `\begin{comment}...\end{comment}` |

The remaining four routes each cost money (JORS £824; AAS $1,425–$5,581), need a
content fix (P3/P4 abstracts are 69% and 36% over the AAS 250-word cap), or wait
on a credential (P5's Zenodo deposit is blocked on `ZENODO_TOKEN`). PRD and CQG
are the only two that are free, format-free, arXiv-free, and cap-free.

**Wall-clock estimate:** P2 needs nothing before the click. The P1A fix is ~30
agent-minutes (write a Note-scoped acknowledgments paragraph covering COI +
funding + AI usage, add ORCID, recompile, `/latex-audit`, re-mirror). Both then
need one Houston account and one click each.

### Top 5 ranked actions

| # | Action | Owner | Why it ranks here |
|---|---|---|---|
| 1 | **Purge the "(in preparation)" companion-citation class across P2, P5, and P1A's `.bib`**, replacing each with the companion's published Zenodo DOI | **AGENT-EXECUTABLE** (~30 min) | The programme's own papers currently tell referees that their companions are unpublished — in two cases *in the compiled, publicly-served PDF*. Two of the three also carry the **retracted** `f_NL = −35/8` value that P2 spends an appendix disowning. This is the headline unflagged finding; see §2.1–2.2. It gates nothing formally, which is exactly why it has survived: it is the first thing a referee clicks |
| 2 | **Submit P2 to PRD** | **HOUSTON-ONLY** | Zero blocking edits. PDF-only initial submission, no arXiv, no APC on the subscription route, no abstract cap. SSOT has had this parked behind a "venue decision" that the research now answers. Do action #1 first so the reference list is clean, then click |
| 3 | **Un-comment and Note-scope P1A's acknowledgments** (COI + funding + AI disclosure), add ORCID, recompile, re-mirror | **AGENT-EXECUTABLE** (~30 min) | IOP makes COI and funding declarations *unconditionally mandatory* and AI disclosure mandatory when AI was used. P1A's compiled PDF has **none of the three**, because the whole Acknowledgments block is swallowed by `\begin{comment}` at `arxiv/paper1a_ech_nogo.tex:4043-4730`. This is the only content gate on the lowest-bar venue in the portfolio. Draft text already exists inertly at `:4531-4534` |
| 4 | **Cut P3's abstract 423→250 and P4's 339→250 words** | **AGENT-EXECUTABLE** | Hard, quoted AAS cap (*"a single paragraph of not more than 250 words"*). Two finished papers cannot be cleanly submitted to their declared venue until this lands, and nothing else about the AAS route is blocked. Highest ratio of papers-unblocked to effort in the whole audit |
| 5 | **Repair the "one patch (line) ahead" deposit literals in P2/P3/P4** | **AGENT-EXECUTABLE** | All three compiled, publicly-served PDFs state a factual falsehood: each is *three* patch releases ahead of its Zenodo deposit, not one. This is pattern-047 recurring **after** the 2026-07-23 closure that was supposed to end it — see §3.2. Fix it by computing the value, not by writing a new literal |

**Deliberately not in the top 5: the arXiv endorsement requests** (drafts landed
today at `project-context/SSOT/ENDORSEMENT_REQUEST_DRAFTS_2026-07-24.md`).
Sending them is **HOUSTON-ONLY** and the reply is **EXTERNALLY-BLOCKED**, but
arXiv is on *nobody's* critical path — none of the six declared venues requires a
preprint, and four of the six are now confirmed by direct quotation. Endorsement
buys visibility and the coordinated-posting story, not publication. Run it in the
background; never wait on it.

### The single most important thing nobody had flagged

**The six papers' bibliographies still describe each other as unpublished — in
compiled, publicly-served PDFs — and two of them cite a physics value the cited
paper explicitly retracts.** Concretely:

- `p5_desi_chirality.tex:5497-5500` cites Paper II as *"in preparation; manuscript
  in preparation"* and titles it `f_NL = −35/8`. P2 has a published DOI, and P2's
  own text (`02_full_draft.tex:1106`) reads *"The result corrects the
  unreproduced printed −35/8 literature value."* Its headline is **−35/16**.
- `focused_paper_refs.bib` gives `Golden2026P1a` the journal string
  `"(in preparation)"`; it is cited at `02_full_draft.tex:1192` and prints as
  `[14] … (in preparation)` in P2's compiled PDF. P1A has a DOI.
- `arxiv/references.bib` carries both defects plus `note = "Companion paper,
  posted concurrently on arXiv"` — a claim that can never be made true.

This survived a targeted fix of the identical defect: today's P5 lane
back-patched the *Paper IV* citation to its Zenodo DOI and shipped v0.1.143,
leaving the Paper II citation ten lines below untouched. And it is invisible to
every existing sweep because all instances live in bibliography constructs
(`.bib` fields and `\bibitem` titles) while the claims-sync and referee-bait
greps are scoped to `.tex` bodies.

Underneath it is the pattern that produced it: **closures repair the exact string
a reviewer quoted, and the adjacent literal in the same sentence survives.**
§3.2 shows the same mechanism defeating the 2026-07-23 version-drift closure
within one day. These are documented, `status: active` patterns (047, 053,
002/032) with no executable detector — of ~97 catalogued patterns, roughly **8
have a mechanical check**, and `.git/hooks/pre-push` enforces only site freshness.
That gap, not arXiv, is what will keep putting defects into submitted
manuscripts.

---

## 1. No-arXiv publication routes

Prior work covered **JORS (P1B)** and **ApJS (P3)** in
`project-context/SSOT/JOURNAL_ROUTE_PREP_2026-07-22.md`. This section adds
P1A, P2, P4, P5 and corrects two items that document marked UNVERIFIED.

### 1.0 Cross-venue summary

| | P1A → CQG Note | P1B → JORS | P2 → PRD | P3 → ApJS | P4 → ApJS | P5 → AJ |
|---|---|---|---|---|---|---|
| arXiv required? | **No** (quoted) | **No** (quoted) | **No** (quoted) | **No** | **No** | **No** (quoted) |
| Format accepted as-is? | **Yes** — format-free | template conformance verified by the in-flight lane | **Yes** — PDF only at initial submission | `aastex701` ✔ | `aastex701` ✔ | **Yes** — AAS accepts "other versions of LaTeX" |
| Cost to publish | **£0** (subscription route) | £824 | **$0** (subscription route; $2910 only for CC-BY) | $1,425–$5,581 | $1,425–$5,581 | $1,425–$5,581 |
| Abstract vs cap | 268 w, no cap | 109 w | 185 w, no cap | **423 w vs 250 ✗** | **339 w vs 250 ✗** | 224 w vs 250 ✔ |
| ORCID in manuscript | ✗ | ✔ (landed today) | ✗ (**required by APS at the portal**) | ✗ | ✗ | ✗ |
| COI statement in PDF | ✗ | ✔ | ✗ | ✗ | ✗ | ✗ |
| AI/LLM disclosure in PDF | ✗ (**IOP mandates**) | ✔ | ✗ (APS does not mandate) | **✗ (AAS mandates)** | ✔ | ✔ |
| Companion cite prints "(in preparation)" | in `.bib`, not compiled | — | **yes, renders** | — | — | **yes, renders** |
| Submittable today? | after action #3 | yes (portal + APC) | **YES — no blocking edit** | after abstract cut | after abstract cut | yes (portal + polish) |

Verified counts: abstract word counts computed by stripping `\begin{comment}`
blocks, `%`-lines, math and macros from each canonical `.tex`; COI/AI/ORCID
presence measured against `pdftotext` output of each compiled PDF, not against
source.

### 1.1 P1A → Classical and Quantum Gravity (IOP), article type "Note"

Manuscript `arxiv/paper1a_ech_nogo.tex` / `.pdf`, v1A.0.126, 8 pp,
md5 `6ade40c14049a316eabf21e67dc10072`, `revtex4-2`.

| Requirement | Detail (verbatim where quoted) | Source |
|---|---|---|
| Preprint | *"our authors are permitted to share a Preprint of their article anywhere at any time."* Permitted, never a condition of submission | [IOP preprint policy](https://publishingsupport.iopscience.iop.org/preprint-pre-publication-policy/) |
| Portal | ScholarOne Manuscript Central, `https://mc04.manuscriptcentral.com/cqg-iop` (login-walled; 403 unauthenticated) | [Submission options](https://iopscience.iop.org/journal/0264-9381/page/submission-options) |
| Initial format | *"You can format your paper in the way that you choose! It is not necessary to try to produce pages that look like published journal pages."* Single PDF; `iopart.cls` not required | [CQG author guidelines](https://publishingsupport.iopscience.iop.org/journals/classical-and-quantum-gravity/) |
| "Note" definition | *"brief articles that make a short, interesting point, which would not normally merit publication as a full Paper but still make a useful and novel addition to the literature."* **No numeric word/page limit published by CQG** | [About CQG](https://publishingsupport.iopscience.iop.org/journals/classical-and-quantum-gravity/about-classical-quantum-gravity/) |
| APC | *"Publication on a subscription-access basis is free of charge."* Gold OA optional, £2530/€2905/$3490 +VAT | [About CQG](https://publishingsupport.iopscience.iop.org/journals/classical-and-quantum-gravity/about-classical-quantum-gravity/) |
| ORCID | *"we recommend you supply ORCID identifiers for all authors to avoid ambiguity"* — recommended, not stated mandatory | [CQG author guidelines](https://publishingsupport.iopscience.iop.org/journals/classical-and-quantum-gravity/) |
| Conflict of interest | **Mandatory**: *"All authors and co-authors are required to disclose any potential conflicts of interest when submitting their article."* | [IOP ethical policy](https://publishingsupport.iopscience.iop.org/ethical-policy-journals/) |
| Funding | **Mandatory**: *"IOP Publishing requires all authors to declare any funding they received related to the research article."* | [IOP ethical policy](https://publishingsupport.iopscience.iop.org/ethical-policy-journals/) |
| Generative-AI use | **Mandatory when used**: *"If authors use generative AI tools… they must disclose this usage in the Acknowledgements section… listing the model and version… and how it was used."* | [IOP ethical policy](https://publishingsupport.iopscience.iop.org/ethical-policy-journals/) |
| Data availability | *"The journal encourages authors to include a data availability statement… This is not mandatory."* | [IOP standard data policy](https://publishingsupport.iopscience.iop.org/iop-publishing-standard-data-policy/) |
| Cover letter / suggested referees / institutional email | Not stated on any public page — **UNVERIFIED**. Settled only by opening the logged-in ScholarOne wizard | portal 403 unauthenticated |
| Affiliation / membership gate | None found for an independent researcher | absence across fetched pages |

**READY.** Format needs no conversion. arXiv genuinely irrelevant. Author block
complete (`:1168-1170`). Data & Code Availability renders with live Zenodo DOI
`10.5281/zenodo.21481838` (HTTP 200 this audit) plus frozen commit `7befce143848`.
Compiled bibliography is 11 third-party `\bibitem`s — self-contained. No
`arXiv:XXXX` placeholder in live text. All 20 embedded URIs resolve.

**MISSING**
- **[AGENT-EXECUTABLE, blocking] No COI, funding, or AI-usage statement in the
  compiled PDF.** Root cause: the entire Acknowledgments block sits inside
  `\begin{comment}...\end{comment}` at `arxiv/paper1a_ech_nogo.tex:4043-4730`
  and never compiles. `pdftotext` of the 8-page PDF returns zero hits for
  "acknowledg", "conflict", "funding". Draft text exists inertly at `:4531-4534`
  ("No external funding was received… Computational resources were self-funded";
  "an agentic AI research pipeline…"). Two of the three are unconditionally
  mandatory at IOP. This is the P1A blocker.
- **[AGENT-EXECUTABLE] ORCID absent.** `grep 0009-0008 arxiv/paper1a_ech_nogo.tex`
  → 0 hits.
- **[AGENT-EXECUTABLE, cosmetic] Blank PDF Title/Author metadata** (`pdfinfo`).
- **[AGENT-EXECUTABLE, low] `arxiv/references.bib:1161-1188`** — four
  `Golden2026P1b/P2/P3/P4` entries carry `note = "Companion paper, posted
  concurrently on arXiv"` (a claim that cannot be made true) and a
  `%% TODO-SUBMISSION: insert arXiv ID` marker, and `Golden2026P2`'s title
  carries the **superseded** `$f_{\rm NL} = -35/8$`. These entries are *not*
  cited in the compiled Note (all uses are inside `\begin{comment}`), so they do
  not reach a referee's eyes — but they ship inside the submission source
  bundle. Honest severity: source-hygiene, not a submission blocker.
- **[JUDGMENT, flag not blocker] Note-length fit.** ~3,984 live words over 8
  two-column pages is long against CQG's "brief… short interesting point"
  framing. CQG publishes no numeric cap, so this is an editor-desk risk, not a
  rule violation.
- **[HOUSTON-ONLY]** ScholarOne account + submission click; ORCID into the
  portal's own author fields; subscription-vs-Gold-OA election (subscription is
  free); cover-letter / referee-suggestion fields if the wizard prompts.
- **EXTERNALLY-BLOCKED: none.**

**Verdict: CAN P1A BE SUBMITTED TO CQG TODAY WITHOUT ARXIV? Not today — but the
blocker is entirely inside the manuscript and is agent-fixable in one commit.**
The venue imposes no arXiv gate, no format gate, no fee, and no affiliation gate.

### 1.2 P2 → Physical Review D (APS), Research Article

Manuscript `research/focused_paper_source_integration/02_full_draft.tex`,
v1.7.128, 11 pp, `revtex4-2` `aps,prd`.

**Source-access caveat, stated up front.** `journals.aps.org` serves a live
Cloudflare JS bot-challenge to automated fetch. Per the standing rule against
defeating bot-detection, that challenge was **not** solved. Every APS quote below
comes from Wayback Machine archives of the same official APS URLs, snapshot dates
2025-12 to 2026-07-20 — public unaltered mirrors of the official pages, but not a
same-day read. **UNVERIFIED against today's live pages**; settled by Houston
opening the pages in his own browser.

| Requirement | Detail (verbatim where quoted) | Source |
|---|---|---|
| arXiv posting | **Not required — an optional import convenience only.** *"You will then have the option to add your arXiv number if applicable… **If you do not wish to directly upload from arXiv, you will be given the opportunity to provide your arXiv id later in the process.**"* | [Web submission guidelines](https://web.archive.org/web/20260404113211/https://journals.aps.org/authors/web-submission-guidelines-physical-review) |
| Portal + what it needs | `https://authors.aps.org/Submissions`. **PDF only for initial submission**: *"We only require a PDF file for a new submission and resubmissions."* `.tex` sources requested after acceptance | same page |
| Format | REVTeX preferred; PDF alone suffices for review. Exact `revtex4-2 aps,prd` string not re-confirmed on the archived pages — **UNVERIFIED at version granularity**, consistent with the current APS standard | same page + [PRD authors](https://web.archive.org/web/20260720060036/https://journals.aps.org/prd/authors) |
| **ORCID** | **REQUIRED**: *"ORCID iDs are required for all Corresponding Authors and are strongly encouraged for all other authors."* Golden is sole/corresponding author | [Editorial policies](https://web.archive.org/web/20260711205003/https://journals.aps.org/authors/editorial-policies) |
| APC | Hybrid. **$2910 only if CC-BY open access is elected**; the subscription route carries no APC | [APCs](https://web.archive.org/web/20260710123058/https://journals.aps.org/authors/apcs) |
| Data availability | **REQUIRED**: *"All published articles must include a Data Availability Statement (DAS)."* Built via a submission-server Q&A, separate from the in-paper section | [DAS policy](https://web.archive.org/web/20260404113211/https://journals.aps.org/authors/data-availability-statements) |
| Affiliation / email | No independent-researcher barrier. *"Authors must use the affiliation(s) where the research was conducted."* *"Active email addresses are required for all authors"* — no domain restriction stated; `hubify.com` untested | Editorial policies |
| Referees | Suggested and opposed referees both optional; opposed entered as free text in the editor comments | [Submission FAQ](https://web.archive.org/web/20251205131948/https://journals.aps.org/authors/submission-faq) |
| Cover letter | Folded into the "Editorial Info" step, not a separate mandatory upload — **UNVERIFIED** whether the field is required | Web submission guidelines |
| AI/LLM disclosure | **No in-manuscript disclosure section mandated.** *"Authors and Referees may use AI-based writing tools exclusively to polish, condense, or otherwise lightly edit their writing… authors must take full responsibility for the contents."* | Editorial policies |
| Abstract cap | None found | — |

**READY.** revtex4-2 is native; initial submission needs only the PDF, which
exists (11 pp, md5 `2b8f63bb8221e6f4f783db35c73221eb`, byte-mirrored to
`public/papers/` and `site/public/`). Abstract 185 words, no cap. Author, email,
affiliation present (`:34-36`). Data and Code Availability section present with
live Zenodo DOI `10.5281/zenodo.21461881` (HTTP 200). No affiliation gate. APS
mandates no AI-disclosure section, so P2's absence of one is **not** a gap here.
All 31 embedded URIs resolve; tarball `paper2_arxiv_v1.7.128.tar.gz` current.
Note that SSOT itself already routes P2 here: `paper-2/status.md:42` records the
edit loop as *"EXHAUSTED"* with *"Next gate: Houston venue / human-referee
decision."* That gate is this submission.

**MISSING**
- **[AGENT-EXECUTABLE] ORCID absent from the `.tex`** (`:34-36`). PRD requires it
  for the corresponding author; the binding requirement is at the portal
  (**HOUSTON-ONLY**), but adding `\author[0009-0008-5616-5994]{…}` is free.
- **[AGENT-EXECUTABLE] The companion citation prints as "(in preparation)".**
  `research/focused_paper_source_integration/focused_paper_refs.bib`,
  `@article{Golden2026P1a}` has `journal = "(in preparation)"` and
  `note = "…companion paper, this volume"`. It **is** cited, at `:1192`
  (*"as convention-audited in the companion paper~\cite{Golden2026P1a}"*), and it
  **renders**: `pdftotext` of the compiled PDF gives reference `[14] H. Golden,
  Structural Closure of Einstein–Cartan–Holst … (in preparation) (2026),
  hUBIFY-2026-001A; companion paper`. P1A has carried a published Zenodo DOI
  (`10.5281/zenodo.21481838`) since 2026-07-21. Same class as §2.1 — see §2.2.
- **[AGENT-EXECUTABLE] Stale deposit literal** at `:1346` — see §3.2.
- **[AGENT-EXECUTABLE, recommended] No COI statement** in the compiled PDF —
  §2.3.
- **[HOUSTON-ONLY]** APS account + submission click; ORCID linkage in the portal;
  the DAS submission-server Q&A; cover-letter text and referee suggestions;
  subscription-vs-$2910-CC-BY election.
- **[UNVERIFIED]** Exact class acceptance and non-institutional-email tolerance —
  the Cloudflare gate blocked a same-day live read.

**Verdict: CAN P2 BE SUBMITTED TO PRD TODAY WITHOUT ARXIV? YES.** arXiv is
confirmed to be an optional import, not a gate; only a PDF is required at initial
submission and it exists; the subscription route is free. **P2 has no blocking
content defect** — the two bibliography/DOI items and the ORCID macro are quality
fixes that should ride along, not gates. This is the shortest distance between
today and a real journal desk.

### 1.3 P4 → ApJS (AAS), catalog + methods article

Manuscript `pipelines/p2_chirality/chirality_catalog_paper.tex`, v1.0.271,
32 pp, `\documentclass[twocolumn,linenumbers]{aastex701}`.

Portal, class currency, gold-OA/CC-BY, no-arXiv-requirement and no-membership
findings are inherited from `JOURNAL_ROUTE_PREP_2026-07-22.md` §2 and are not
re-derived. Two of that document's UNVERIFIED items are now **settled**:

- **APC — CORRECTED.** The prior figures ($1,172 / $2,651 / $4,589) came from a
  third-party aggregator and are wrong. AAS's own page states the 2026 schedule,
  identical for ApJ/ApJS/AJ: **≤30 quanta $1,425; 31–50 $3,162; 51–100 $5,581;
  >100 +$250 surcharge**, and *"The charges below are current for the 2026
  calendar year."*
  ([AAS article charges](https://journals.aas.org/article-charges-and-copyright/))
- **AI disclosure — CONFIRMED MANDATORY-ISH.** AAS publishes an **"LLM Usage
  Policy"**: *"Authors are expected to acknowledge and cite the use of any LLM
  used in manuscript preparation. Responsibility for the accuracy of the
  submission remains with the authors."*
  ([Manuscript Preparation](https://journals.aas.org/manuscript-preparation/)).
  This makes **P3's total absence of any AI/LLM mention a live compliance gap** —
  see §2.4.
- **`linenumbers` — CONFIRMED REQUIRED**: *"we now require authors to include
  them in both submission and revision."* P4 already sets it; P3 and P5 should
  be checked at submission time.

**The large-catalog question (highest-value P4-specific answer).** AAS Data
Guide: *"When tables are longer than ~200 data rows or contain critical object
related data, authors are strongly encouraged to deliver their tables at
submission in a machine readable format. Tables that exceed 400 data lines will
only have the full data set appear in machine readable format with a short
example version in the manuscript."* And: *"DbF is not appropriate for all data,
specifically extremely large data sets (> 100 MB) or data that is already
available online"*, with a standing instruction to *contact AAS Journals Data
Editors in advance* where size is a concern
([Data Guide](https://journals.aas.org/data-guide/)). P4's catalog is 8,474,531
rows / ~952 MB — ~9× the stated DbF ceiling, so external hosting with an
abbreviated in-article table is exactly right, which is what P4 already does.
**UNVERIFIED:** AAS names Zenodo (AAS Journals Community) and Harvard Dataverse
as its preferred repositories; Hugging Face is not among them. Whether AAS data
editors accept HF as the primary host is unconfirmed — settled by one
pre-submission email to AAS Data Editors (HOUSTON-ONLY).

**READY.** Correct current class. Catalog externally hosted with live pinned
revisions (three HF revision URLs fetched this audit, all HTTP 200). Data
Availability + Software present with pinned revisions, SHA-256s, receipts.
AI-assisted-methodology paragraph present inside `\begin{acknowledgments}` and
renders in the PDF. **No stale cross-references to any of the other five
papers** — verified; the body states the result *"does not depend on any
unpublished companion work."* All 30 GitHub `/blob/main/` links resolve to
committed files. Tarball `paper4_arxiv_v1.0.271.tar.gz` current.

**MISSING**
- **[AGENT-EXECUTABLE, blocking] Abstract 339 words vs the AAS 250-word cap**
  (`chirality_catalog_paper.tex`, `\begin{abstract}` block) — 36% over.
- **[AGENT-EXECUTABLE] ORCID absent** from the author block
  (`\author{Houston Golden}` + `\affiliation{...}` + `\email{...}`; AASTeX7 wants
  `\author[0009-0008-5616-5994]{...}`).
- **[AGENT-EXECUTABLE] Stale deposit literal.** `chirality_catalog_paper.tex:1907`:
  *"That record archives the reviewed `v1.0.268` PDF and source…; the present
  manuscript is `\paperVersion`, one patch line ahead"* — v1.0.271 is **three**
  releases ahead. See §3.2.
- **[AGENT-EXECUTABLE, low] Deprecated `\keywords` free-text style** rather than
  UAT concepts; AAS collects UAT terms at acceptance, so non-blocking.
- **[HOUSTON-ONLY]** AAS portal account + upload; Zenodo re-stage credentials;
  APC decision; the AAS Data Editors email about HF hosting.

**Verdict: CAN P4 BE SUBMITTED TO ApJS TODAY WITHOUT ARXIV? No — the abstract
cap is a genuine content blocker.** arXiv is not a factor. Everything else is
cheap agent work or a portal step.

### 1.4 P5 → The Astronomical Journal (AAS), observational research article

Manuscript `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex`,
v0.1.143-2026-07-24, 42 pp, `revtex4-2` with `aps,prd` options.

**The class-mismatch premise is false — verified.** P5 is in APS revtex while
targeting an AAS journal, which looked like a hard blocker. AAS's own
Manuscript Preparation page says otherwise: *"Authors are strongly encouraged to
prepare their manuscripts using the most recent version of the AASTeX macro
package… The journals also accept manuscripts prepared using Microsoft Word"*
and *"Authors that use other versions of LaTeX have to include the lineno.sty
package which can be obtained at CTAN."*
([Manuscript Preparation](https://journals.aas.org/manuscript-preparation/)).
AASTeX is encouraged, not mandatory; the only stated obligation for non-AASTeX
LaTeX is line numbers.

**Conversion effort, if wanted for reviewer-expectation polish** (measured, not
estimated): 5,554 lines; class-specific surface is 1 `\documentclass` line with
9 revtex-only options, **1** `\affiliation`, **0** `\preprint`, **0** `\pacs`
(the `showpacs` option is vestigial), **0** `\widetext`, and **27**
`ruledtabular` environments needing a booktabs swap (booktabs already loaded).
27 tables, 9 figures, and an 18-entry manual `thebibliography` are all portable
untouched. Realistically a half-day mechanical pass — **optional, not on the
critical path.**

**AJ scope.** *"The Astronomical Journal publishes significant original research
relevant to all aspects of astronomy and astrophysics. It maintains its
traditional emphasis on scientific results that are derived from observations…"*
([Scope statements](https://journals.aas.org/scope-statements/)). A DESI
void-environment observational analysis is squarely in scope. Abstract cap,
portal, and gold-OA terms are identical to ApJS; charges are the same
$1,425–$5,581 schedule confirmed in §1.3.

**READY.** Abstract 224 words — under the cap, unlike P3/P4 (but with only 26
words of headroom, so any added DOI sentence needs a re-count). AI-assisted
disclosure present inside the acknowledgments and renders. Data-and-code
availability section present with DESI DR1, DESIVAST VAC, and the Paper IV
catalog. Paper IV dependency now back-patched to the published Zenodo DOI
`10.5281/zenodo.21461899` (v0.1.143, commit `eecec167`). 48 GitHub links, all
resolving to committed files. Tarball current.

**MISSING**
- **[AGENT-EXECUTABLE, blocking-quality] The Paper II citation** — see §2.1.
  This is the finding of this audit.
- **[AGENT-EXECUTABLE] ORCID absent** — 0 hits for the ORCID string anywhere in
  the file.
- **[AGENT-EXECUTABLE] No UAT/AAS keywords block** — 0 hits for `\keywords`,
  "Key words", "Subject headings".
- **[AGENT-EXECUTABLE, optional] revtex→AASTeX conversion** — not required by
  AAS policy; half-day if elected.
- **[HOUSTON-ONLY, in flight] P5's own Zenodo DOI.** `git log` shows
  `344125ce chore(P5): stage Zenodo deposit at v0.1.143 (draft blocked on
  ZENODO_TOKEN)` — the deposit is staged and blocked on a credential Houston
  holds. Receipt at `project-context/SSOT/zenodo/P5_zenodo_staged_receipt_2026-07-24.json`.
- **[HOUSTON-ONLY]** AAS portal account + upload; APC decision.

**Verdict: CAN P5 BE SUBMITTED TO AJ TODAY WITHOUT ARXIV? On format and venue
policy, yes.** The class is not a gate and the abstract is under cap. What
stops a clean click is content hygiene — the Paper II citation, ORCID, and
keywords, all same-day agent edits — plus P5's own DOI, which is
credential-blocked, not agent-blocked.

---

## 2. Hidden blockers — verified, with evidence

Every item below was confirmed against the compiled artifact or a live fetch.
Items that looked like blockers and turned out clean are listed in §2.6 so the
next agent does not re-hunt them.

### 2.1 P5 cites Paper II as "in preparation", by a retracted value, ten lines below a citation that was fixed today

**File:** `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex:5497-5500`

```
\bibitem{golden_fnl_2026}
H.~Golden,
\emph{$f_{NL} = -35/8$ Forecast: SPHEREx Discrimination of Bounce vs.\
Inflation}, companion paper (Paper~II), in preparation; manuscript in preparation.
```

Three defects in one entry:

1. **It cites P2 as unpublished.** P2 has a published Zenodo version DOI
   `10.5281/zenodo.21461881` (concept `10.5281/zenodo.21461880`), minted
   2026-07-20, receipt at
   `project-context/SSOT/zenodo/P2_zenodo_receipt_2026-07-20.json`. Both DOIs
   returned HTTP 200 during this audit. This is documented
   **pattern-053 (companion-in-prep-citation leak)**, `status: active`,
   `papers_observed: [P1A, P1B, P5]` — recurring in the exact paper the pattern
   already names.
2. **It titles P2 by a value P2 explicitly retracts.** P2's own text
   (`research/focused_paper_source_integration/02_full_draft.tex:1106`) reads:
   *"The result corrects the unreproduced printed $-35/8$ literature value"*, and
   `:1120` adds: *"Appendix… documents why the separately printed $-35/8$ is not
   reproduced."* P2's headline is **−35/16**. P5's bibliography therefore
   advertises its own companion under a number that companion spends an
   appendix disowning. A referee who follows the citation finds an internal
   contradiction across the programme. This violates the standing
   `/bigbounce-claims-table-sync` rule ("grep every .tex … zero stale instances
   allowed") — it escaped because the sweep greps `.tex` bodies, and this
   instance is a bibliography title (and its twin, §2.2, lives in a `.bib`).
3. **It survived the fix for its own sibling.** The bibitem immediately above
   (`golden_chirality_2026`) was back-patched *today* to Paper IV's published
   Zenodo DOI with an explicit "not an arXiv preprint and not peer reviewed"
   qualifier (commit `eecec167`, v0.1.143). The template for the correct fix is
   literally ten lines above the defect.

**It renders.** `pdftotext pipelines/p5_desi_chirality/paper/p5_desi_chirality.pdf`
→ reference `[4]`: *"H. Golden, fNL = −35/8 Forecast: SPHEREx Discrimination of
Bounce vs. Inflation, companion paper (Paper II), in preparation; manuscript in
preparation."* And it is load-bearing enough to be cited in the body at `:956`.
Confirmed still present in the v0.1.143 PDF after today's bump.

**Fix (AGENT-EXECUTABLE, ~10 min):** mirror the `golden_chirality_2026`
treatment — correct the title to −35/16, cite version DOI
`10.5281/zenodo.21461881` and concept `10.5281/zenodo.21461880`, and keep the
honest "not an arXiv preprint and not peer reviewed" qualifier. Then re-run the
§2.2 sweep across `.bib` files.

### 2.2 The same class is in P2's bibliography — and P2's *renders*

**File:** `research/focused_paper_source_integration/focused_paper_refs.bib`

```
@article{Golden2026P1a,
    author = "Golden, Houston",
    title  = "{Structural Closure of Einstein--Cartan--Holst Dark Energy: ...}",
    journal = "(in preparation)",
    year = "2026",
    note = "HUBIFY-2026-001A; companion paper, this volume"
}
@article{Golden2026P2,
    title  = "{$f_{\rm NL} = -35/8$ Forecast: SPHEREx Discrimination of Bounce vs.\ Inflation}",
    journal = "(in preparation)",
    ...
}
```

`Golden2026P1a` **is cited and does render.** `02_full_draft.tex:1192` reads
*"as convention-audited in the companion paper~\cite{Golden2026P1a}"*, and
`pdftotext` of the compiled P2 PDF returns reference `[14] H. Golden, Structural
Closure of Einstein–Cartan–Holst … **(in preparation)** (2026),
hUBIFY-2026-001A; companion paper`. P1A has carried a published Zenodo DOI
`10.5281/zenodo.21481838` since 2026-07-21 (HTTP 200 this audit). So **P2's
compiled, publicly-served PDF tells a PRD referee that its load-bearing
convention audit lives in an unpublished manuscript** — when that manuscript has
a citable DOI. Second live instance of pattern-053, in the paper this audit
recommends submitting first.

The sibling `Golden2026P2` entry in the same file is P2's own self-reference,
uncited, and carries the third instance of the retracted **−35/8** title.

**Also: `arxiv/references.bib` (P1A's database)**

```
@article{Golden2026P2,
    author = "Golden, Houston",
    title = "{$f_{\rm NL} = -35/8$ Forecast: SPHEREx Discrimination of Bounce vs.\ Inflation}",
    year = "2026",
    note = "Companion paper, posted concurrently on arXiv"
}
```

and the sibling `@unpublished{Golden2026P1b, … note = "Companion paper, posted
concurrently on arXiv"}`.

**Honest scoping:** these entries are **not** cited in the compiled P1A Note —
all 38 non-`%`-comment lines referencing `Golden2026P1b` / `Golden2026P2` fall
inside `\begin{comment}` ranges `(1213,1333) (1389,1724) (1847,2616)
(2720,3815) (4043,4730) (4871,5060)`, verified programmatically, and `pdftotext`
of the 8-page PDF contains neither "35/8" nor "concurrently on arXiv". So this is
**not** a referee-visible defect today. It is a source-bundle hygiene item: the
`.bib` ships inside the submission tarball, the "posted concurrently on arXiv"
note is a claim that cannot be made true, and the stale −35/8 is the second
instance of a value the claims-sync rule says must have zero stale instances.

**Why it escaped.** Tally the retracted `−35/8` across the repo: three live
instances, in `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex:5499`
(a `\bibitem` title), `arxiv/references.bib` (a `.bib` title field), and
`research/focused_paper_source_integration/focused_paper_refs.bib` (a `.bib`
title field). **Not one of them is in a `.tex` body paragraph** — which is
exactly the scope of the `/bigbounce-claims-table-sync` sweep ("grep every .tex
AND every HTML/TSX page"). Bibliography titles and `.bib` databases are outside
it. **The sweep's file scope is the bug**, and it is a one-line fix.

Same story for "(in preparation)": three instances, two of which render in
compiled PDFs (P5 §2.1, P2 above), all in bibliography constructs rather than
prose — which is why the body-text referee-bait grep in §2.6 came back almost
clean while the reference lists did not.

### 2.3 Conflict-of-interest statements are absent from five of six compiled PDFs

Measured on `pdftotext` output, not source:

| | P1A | P1B | P2 | P3 | P4 | P5 |
|---|---|---|---|---|---|---|
| Conflict-of-interest | **✗** | ✔ | **✗** | **✗** | **✗** | **✗** |
| Funding statement | **✗** | ✔ | ✔ | ✔ | ✔ | ✔ |
| Acknowledgments section at all | **✗** | ✔ | ✔ | ✔ | ✔ | ✔ |

P1A has none of the three (root cause in §1.1). The other four have
acknowledgments and funding but no COI declaration. IOP makes COI mandatory
(quoted, §1.1). Whether APS and AAS require an explicit COI statement at
submission rather than collecting it as a portal field is **UNVERIFIED** —
settled by reading the logged-in submission wizards. Regardless, a one-sentence
"The author declares no competing interests." is free insurance and is
**AGENT-EXECUTABLE** across all five.

### 2.4 P3 has no AI/LLM disclosure, and AAS requires one

`grep -inE "^[^%]*(AI-assisted|large language model|agentic|LLM)"
pipelines/p3_anomaly_engine/paper3_apjs.tex` → **zero hits**. `pdftotext` of the
compiled P3 PDF likewise returns nothing for AI/LLM/Claude/GPT. Its
acknowledgments section is DESI-collaboration boilerplate only.

AAS's Manuscript Preparation page carries an **LLM Usage Policy**: *"Authors are
expected to acknowledge and cite the use of any LLM used in manuscript
preparation."* P3 is bound for ApJS. P4 and P5 (also AAS-bound) both carry an
AI-assisted-methodology paragraph; P3 does not. The repo's own practice
elsewhere is to disclose. **AGENT-EXECUTABLE**, one paragraph.

P2 (`02_full_draft.tex`) has the same absence — zero AI/LLM hits in source or
PDF. Whether APS mandates disclosure is covered in §1.2.

### 2.5 Site alias `site/public/p1a-ech-nogo.pdf` serves a stale 37-page P1A

md5 `ba0e829fd2b88ac4e6405081ac22b878`, 37 pages, ModDate 2026-07-07 — against
the canonical 8-page v1A.0.126 (`6ade40c14049a316eabf21e67dc10072`). The
equivalent aliases for P1B, P2, P3, P5 do not exist at all; P4's is byte-current.

**Honest severity: low.** `site/src/data/papers.ts` routes every P1A button to
`/papers/paper1a_ech_nogo_v1A.0.126.pdf`, which is current, so nothing links to
the stale file. But it is a live, publicly-reachable URL serving a superseded
37-page manuscript — the exact shape of `spattern-pdf-404-or-old-version`. Delete
it or re-mirror. **AGENT-EXECUTABLE.**

### 2.6 Checked and clean — do not re-hunt these

Verified during this audit, all passing:

- **Artifact-link integrity (AGENT_RULES §4.7.1).** Extracted every `/URI` from
  all six compiled PDFs including compressed streams: 192 URIs, **90 distinct
  `github.com/Hubify-Projects/bigbounce/{blob,tree}/main/` targets, 0 dangling**
  against the working tree, and **0 untracked in git HEAD** (checked with
  `git ls-files --error-unmatch` plus a `git ls-tree` fallback for directories).
  The `/artifact-link-verify` discipline is working.
- **Submission tarballs.** All six current: `paper1a_arxiv_v1A.0.126`,
  `paper1b_namaster_proof_arxiv_v2B.0.15`, `paper2_arxiv_v1.7.128`,
  `paper3_apjs_arxiv_v3.2.0-r13`, `paper4_arxiv_v1.0.271`,
  `paper5_arxiv_v0.1.143-2026-07-24`. (The older `paper1b_arxiv_v1B.0.109` and
  `paper3_arxiv_v3.1.113` names are superseded manuscripts, not stale bundles.)
- **PDF mirrors.** Canonical PDF byte-matches `public/papers/` and
  `site/public/papers/` for all six. Only exception in §2.5.
- **External anchors.** Six Zenodo DOIs (`21481838`, `21481753`, `21481842`,
  `21461881`, `21461888`, `21461899`) and three HF repos plus three pinned HF
  revision URLs — **all HTTP 200** this audit. No `pattern-026` 404s.
- **Referee-bait string sweep** across all six `.tex`, non-comment lines, for
  "in preparation / in prep / forthcoming / to appear / arXiv:XXXX / in press /
  will be presented elsewhere / future work": exactly **two** hits in `.tex`.
  `arxiv/paper1a_ech_nogo.tex:4191` ("deferred to future work and would not
  change…") is inside a comment block and does not compile — benign. The other
  is §2.1. **Caveat: this sweep is `.tex`-only.** Extending it to `.bib`
  immediately surfaced two more live instances (§2.2). Body prose is clean; the
  bibliographies are not.
- **`tools/bigbounce_preflight.py run`** → `verdict: PASS`, 0 findings, core
  sha256 `9a533244…`.
- **`tools/check_new_patterns.sh`** → 2 low-grade p038 caption flags on P4
  (`:1233`, `:1304`; both captions define their own σ formula, so the "different
  nulls" concern does not apply) and 3 p039 prose-table-reference flags on P1A,
  all inside suppressed comment blocks. No real hits.
- **P1A's compiled Note is genuinely standalone** — zero live companion
  citations, confirming it can be submitted alone without a coordinated-posting
  story.
- **P3's HuggingFace catalog is already live** at the pinned revision cited in
  the paper. See §4.3 — SSOT still lists this as an open pre-submission gate.

---

## 3. Self-improvement loop health

`project-context/plan.md:60` flags the 2026-07-15 finding — *"70+ documented
review patterns but only a handful enforced by `tools/check_new_patterns.sh`"* —
and calls for *"one executable HubStack learning-loop engine, one BigBounce
adapter, packet-bound preflight receipts, and measured known-pattern
escape/closure-regression rates before another review wave."* (task PUB-007).

### 3.1 Current state — measured, not asserted

**The engine was built.** `tools/bigbounce_preflight.py` (351 lines) exists,
consumes `project-context/pre-review-rules.json`
(`schema: hubstack.paper-pre-review-rules/v1`), emits a hash-bound receipt
(HEAD + registry + rules + source + PDF), and fails closed on staleness. Running
it today: **PASS, 0 findings.** So the architectural half of PUB-007 is closed.

**The catalog did not follow.** Counting what is actually executable:

| | Count |
|---|---|
| Pattern files in `project-context/review-patterns/` (excl. INDEX, CANDIDATE-CLUSTERS) | **97** |
| Of those, still marked `-DRAFT` | 14 |
| Generic rules in `pre-review-rules.json` | **9** |
| Portfolio validators registered | 6 |
| Numbered patterns with a genuine mechanical detector | **≈8** — 017/055 (two compiled-prose regexes), 026/046 (`artifact_crosscheck.py`), 037 (twice: rule + script), 038, 039, 040, 041 |
| Enforcement rate | **≈8%** |

**Nothing runs automatically on the patterns.** `.git/hooks/pre-push` invokes
only `tools/site_freshness_check.sh` — site staleness, not manuscript defects —
and honours a `FRESHNESS_SKIP=1` bypass. `tools/check_new_patterns.sh` is
referenced by exactly one file in the whole repo:
`tools/tests/test_proactive_sweep_tools.py:52`, which reads its *source text* as
a fixture. **The pattern detector is never invoked by any hook, CI workflow, or
by the preflight engine itself.** The three GitHub workflows (`build-data.yml`,
`namaster-proof.yml`, `p1b-runpod-watchdog.yml`) do not touch it.

So the honest state of PUB-007: **engine yes, coverage no, automation no.** The
gap plan.md flagged nine days ago is materially unchanged in coverage terms.

### 3.2 Was the 2026-07-23 class preventable? Yes. Is it now enforced? No — and it is already leaking again

The re-sweep's one genuinely-new-real class was
(`project-context/peer-reviews/INT_v3/TRUTH_AUDIT_RESWEEP_2026-07-23.md:9-15`):

> **Version-stamp drift in Data-Availability prose** — "the present manuscript
> is v1.7.126 / v3.2.0-r11 / v1.0.269" vs current … Root cause: the
> self-reference is a hardcoded literal the version-bump flow doesn't touch.

**Preventable by an existing rule: yes, exactly.**
`project-context/review-patterns/pattern-047-version-pin-staleness-on-bump.md`,
`status: active`, `first_seen: EXT1 (2026-06-10)`,
`papers_observed: [P1A, P1B, P2, P3, P4, P5]`:

> **Description**: Data Availability commit hashes, bundle metadata, and DOI
> placeholders go stale across version bumps
> **Prevention**: … Gate added to `/bigbounce-version-bump` — every bump must
> update Data Availability hash, bundle metadata labels, and release manifests
> in the same commit.

A documented, active pattern with a documented prevention recurred six weeks
later, simultaneously on three papers. The "prevention" was prose inside a
skill, not an executable detector — so it did not fire. **That is a measured
known-pattern escape.**

**Is it now enforced so it can never recur? No.** The closure bound the
*manuscript* version to `\paperVersion`, which does make that half drift-proof
by construction. But the **same sentence** carries two more hardcoded literals —
the deposit version and the relationship phrase — and both are **false right
now, in all three papers, in compiled and publicly-served PDFs**:

| Paper | File:line | Prose (renders in PDF) | Deposit | Manuscript | Truth |
|---|---|---|---|---|---|
| P2 | `research/focused_paper_source_integration/02_full_draft.tex:1346` | *"archives the reviewed `v1.7.125` release … the present manuscript is `\paperVersion`, **one patch line ahead**"* | v1.7.125 | v1.7.128 | **three** ahead |
| P3 | `pipelines/p3_anomaly_engine/paper3_apjs.tex:944-947` | *"archives the reviewed `v3.2.0-r10` bytes exactly; the present manuscript is `\paperVersion`, **one patch ahead**"* | r10 | r13 | **three** ahead |
| P4 | `pipelines/p2_chirality/chirality_catalog_paper.tex:1907` | *"archives the reviewed `v1.0.268` PDF and source …; the present manuscript is `\paperVersion`, **one patch line ahead**"* | v1.0.268 | v1.0.271 | **three** ahead |

Confirmed rendered: `pdftotext` on P2 → *"archives the reviewed v1.7.125
release"*; on P3 → *"reviewed v3.2.0-r10 bytes exactly"*.

`JOURNAL_ROUTE_PREP_2026-07-22.md:106` already noticed the P3 instance ("the gap
is now two patch releases, not one") — and it was still not fixed, and has since
widened to three. **The class is open, not closed.**

**The generalisable lesson:** the closure loop repairs the exact string a
reviewer quoted, and the adjacent literal in the same sentence — the one no
reviewer happened to name — survives. That is the mechanism behind both §2.1 and
§3.2. It is the meta-pattern worth minting.

### 3.3 Which unenforced patterns to make executable, ranked by payoff

Ranked by (frequency of real escapes observed) × (cheapness of a deterministic
detector) × (referee visibility if it ships).

| # | Pattern | Detector (all are ~20–60 lines of Python/grep) | Why it ranks here |
|---|---|---|---|
| 1 | **047 — version-pin staleness**, generalised to *any* hardcoded version/relationship literal | For each paper, parse the Data-Availability paragraph; extract every `vX.Y.Z`-shaped literal; assert each is either `\paperVersion` or matches the paper's actual Zenodo deposit version from `project-context/SSOT/zenodo/*_receipt_*.json`; assert any "N patch(es) ahead" phrase equals the true delta | Live in 3 of 6 papers *right now*, after being "closed" yesterday. Perfectly deterministic — the receipt JSON already holds ground truth |
| 2 | **053 — companion in-prep citation leak**, extended to `.bib` files and `\bibitem` titles | Grep every `.tex` **and** `.bib` for "in preparation / in prep / forthcoming / to appear / posted concurrently / this volume"; for each hit, cross-check the referenced paper against the DOI registry in `project-context/SSOT/zenodo/*_receipt_*.json`; fail if the cited paper has a published DOI | **Three live instances today** — P5 (§2.1), P2 and P1A `.bib` (§2.2) — two of which render in compiled PDFs. Catches exactly the class the P5 back-patch lane was created to fix, before the next one is missed |
| 3 | **Cross-paper claim consistency** (002 / 032 / claims-table-sync), **scope widened to `.bib` and bibliography titles** | Maintain a small ledger of retracted-vs-current headline values (e.g. `−35/8 → −35/16`); grep all `.tex`, `.bib`, `.tsx`, `.html` for retracted values; fail on any hit | **Three live instances of one retracted value** (§2.1, §2.2) got through because the existing sweep's file scope excludes `.bib` and bibliography titles. One scope change plus a small ledger file |
| 4 | **Venue-bound abstract word cap** (new; would have caught P3 and P4 months ago) | Read the paper's declared venue from `project-context/paper_registry.json`, look up the cap in a small venue table (AAS 250, RNAAS 150, …), strip LaTeX, count, fail over cap | P3 is 69% over and P4 36% over their venue's hard, quoted limit. This is the *only* content blocker standing between two finished papers and a real submission, and it is trivially machine-checkable |
| 5 | **Submission-compliance presence check** (new; COI / funding / AI-disclosure / ORCID) | For each paper, assert the compiled PDF's text contains a COI sentence, a funding sentence, an AI/LLM disclosure, and the ORCID string; venue-parameterised for which are mandatory | 5 of 6 papers lack COI; 3 lack AI disclosure; 5 lack ORCID (§2.3, §2.4). P1A's absence is caused by a `\begin{comment}` swallowing the whole block — a source-only grep would have *passed*, which is exactly why this check must read the **compiled PDF** |
| 6 | **045 — abstract-body drift** | Extract each quantitative sentence from the abstract; require a body sentence with a matching number and qualifier | `papers_observed: [all six]`, high referee visibility, no detector. Harder than 1–5 (needs fuzzy matching), so ranked below them |

**Two structural fixes worth more than any single detector:**

- **Wire `check_new_patterns.sh` and the ranked detectors into
  `tools/bigbounce_preflight.py`** so they ride the existing hash-bound receipt,
  and **invoke the preflight from `.git/hooks/pre-push`** alongside the freshness
  gate. Today the engine exists and the detectors exist and nothing connects
  them.
- **Retire or promote the 14 `-DRAFT` patterns.** A catalog where 14% of entries
  are permanently draft trains agents to treat the catalog as documentation
  rather than as a contract.

**Measured known-pattern escape rate:** of the patterns this audit could test
against current artifacts, **047 escaped (3 papers), 053 escaped (2 papers), and
the claims-sync class escaped (2 files)** — while every pattern that *does* have
an executable detector (017/026/037/038/039/040/046) shows zero real hits. The
correlation is not subtle: **the enforced patterns do not recur; the documented
ones do.**

---

## 4. Acceleration opportunities

### 4.1 Circular dependencies — one broken, two still live, one dissolved

The P5/Paper-IV loop ("P5 can't cite P4 until P4 is posted; P4 can't post
without endorsement") was broken today by citing P4's Zenodo DOI instead of an
arXiv ID. **Siblings of that exact shape:**

- **LIVE — P5 → Paper II.** Identical shape, identical fix available, not done
  (§2.1). P5's bibliography still treats P2 as an unpostable future object even
  though P2 has a published DOI. *Break it the same way.*
- **LIVE — P2 → Paper I(a).** Same shape again, and it renders in P2's compiled
  PDF as `[14] … (in preparation)` (§2.2), in the very paper this audit
  recommends submitting first. P1A has had a DOI since 2026-07-21. *Break it the
  same way.*
- **DISSOLVED but still asserted — P1A → "coordinated submission".** P1A's
  suppressed prose builds a story in which the companions "are all posted
  concurrently in the coordinated submission, which fixes only the citable arXiv
  identifiers", and treats companion numbers as unciteable "until Paper I(b) is
  publicly posted". Both premises are obsolete: four companions carry published
  Zenodo DOIs, and the compiled Note cites none of them anyway. The dependency
  is already dissolved in the compiled artifact — but `arxiv/references.bib`
  still encodes it (§2.2). *Delete the assumption from the source bundle.*
- **STALE — P3's "HF catalog flip at time of arXiv submission."**
  `project-context/SSOT/paper-3/status.md:469` files publishing the anomaly
  catalog to HuggingFace as a pre-arXiv gate, and `:81` lists "HF catalog flip at
  time of arXiv submission" as a final gate. The catalog **is already live** —
  `bamfai/bigbounce-anomaly-catalog` and the exact pinned revision
  `cdaaa03a72c69d86f011be128d93f261dc5b39a8` cited at `paper3_apjs.tex:204` both
  returned HTTP 200 this audit. This gate is done and should be closed in SSOT so
  it stops appearing on the critical path.

**The general test to keep applying:** any gate phrased *"…at time of arXiv
submission"* or *"…before arXiv submission"* is a candidate circular dependency,
because arXiv is the one externally-blocked node. Grepping SSOT for that phrasing
returns three real gates: `paper-3/status.md:81` and `:469` (both the HF catalog
flip, both already satisfied — see above) and `paper-4/status.md:613`, already
struck through as DONE with the Zenodo DOI since minted. The only genuinely
arXiv-owned rows left are `queue.md:905-906` (`P-ARXIV-P4` / `P-ARXIV-P3`), which
are Houston-owned by definition. **No science or packaging work is actually
waiting on arXiv.**

### 4.2 Work currently on the critical path that is actually optional

- **arXiv endorsement (D4) itself.** It is described throughout the repo as *the*
  structural blocker. It is not a blocker to **publication**: CQG, JORS, PRD,
  ApJS, and AJ each accept submissions without a preprint — **five of the five
  distinct venues, four of them confirmed by direct quotation from the
  publisher's own policy page** (§1). Endorsement should be reclassified from
  *blocking* to *parallel, value-adding* — chase it, but never wait on it. The
  drafts landed today; sending them is Houston's, and the reply is a third
  party's.
- **The revtex→AASTeX conversion for P5.** Looked mandatory, is not (§1.4). A
  half-day of work that buys presentation polish, nothing else. Do it after
  submission, or not at all.
- **`P3-SDSS-LAMOST-EROSITA-FULL-SCAN`, `P3-E`, `P3-F`** (`queue.md:863-871`) —
  multi-day pod work, budgeted in fractions of a percent of readiness, aimed at
  extending catalog coverage. None of it is required for the ApJS submission of
  the catalog *as published*. Explicitly park it.
- **Further review waves.** Directive P defines convergence as "0
  genuinely-new-real findings outstanding across ACTIVE legs", and the
  2026-07-23 re-sweep reached it after the three stamp closures. `queue.md:810`
  still carries `R9-P2-VERIFY-V143`, a June row asking for another clean
  cross-vendor round on v1.7.43. Reviewer-word churn on converged content is
  measured referee variance (pattern-066), not progress. Every hour spent there
  is an hour not spent on the abstract cuts that actually gate two submissions.

### 4.3 Repo-hygiene items that are silently costing wall-clock

- **`project-context/NEEDS_HOUSTON.md` is ~2 months stale.** Header: *"Last
  updated: 2026-05-29 PDT — SHIP-READY"*. It tells Houston to upload
  `p1a_v1A.0.36_arxiv.tar.gz` and `p4_v1.0.139_arxiv.tar.gz` — versions 90 and
  132 releases behind — and lists readiness figures (P1B 78, P2 81, P3 85, P5 82)
  superseded by directive P's 95×6. This is *the* file named for Houston's own
  work queue, and following it today would produce a wrong submission.
  **AGENT-EXECUTABLE:** rewrite it as the partition table this audit produces.
- **`project-context/SSOT/queue.md` carries April-era rows** referencing drive-to-100
  fire numbers, superseded versions, and `Houston BLOCKING` P3 items
  (`:973`, `:974`, `:977`) whose subject matter has been through many rounds
  since. Un-triaged, they make the Houston-only list look far longer than it is.
  **AGENT-EXECUTABLE:** one triage pass marking each row current / superseded /
  moot with evidence.
- **The stale `site/public/p1a-ech-nogo.pdf`** (§2.5).

### 4.4 The recommended sequence

Nothing below weakens a scientific gate; every item is packaging, compliance, or
bookkeeping on already-converged science.

**Wave A — one agent bundle, today (~2–3 hours, all AGENT-EXECUTABLE):**
1. **Bibliography purge across all three files** — `p5_desi_chirality.tex`
   (`golden_fnl_2026`), `focused_paper_refs.bib` (`Golden2026P1a`,
   `Golden2026P2`), `arxiv/references.bib` (all four `Golden2026*`). Replace
   "(in preparation)" / "posted concurrently on arXiv" with the companion's
   published Zenodo version + concept DOI and the honest "not an arXiv preprint
   and not peer reviewed" qualifier, using the `golden_chirality_2026` entry as
   the template. Correct every `−35/8` title to `−35/16`.
2. P1A: un-comment + Note-scope acknowledgments (COI + funding + AI disclosure),
   add ORCID, recompile, `/latex-audit`, `/artifact-link-verify`, re-mirror, bump.
3. P5: add ORCID; add UAT keywords.
4. P3 + P4: cut abstracts to ≤250 words; add ORCID; add P3's AI-usage disclosure.
5. P2/P3/P4: repair the deposit-version and "one patch ahead" literals (§3.2),
   binding to a computed value rather than a new literal.
6. Add a one-sentence COI statement to P1A, P2, P3, P4, P5.
7. Delete or re-mirror `site/public/p1a-ech-nogo.pdf`.
8. Rewrite `NEEDS_HOUSTON.md` from this audit's partition.

Every item recompiles two or more papers, so run directive-G hygiene once at the
end of the bundle rather than per edit.

**Wave B — enforcement, same day or next (AGENT-EXECUTABLE):**
Implement detectors 1–5 from §3.3, wire them into `tools/bigbounce_preflight.py`,
and invoke the preflight from `.git/hooks/pre-push`. Then re-run against all six
papers and confirm the Wave-A fixes are held by machine, not by memory.

**Wave C — HOUSTON-ONLY, in this order:**
1. **APS account + P2 submission to PRD.** Free on the subscription route,
   PDF-only, no arXiv. Fastest thing in the portfolio to reach a real editor.
   Needs Wave A item 1 first so the reference list is clean, and the ORCID linked
   in the portal (APS requires it of corresponding authors).
2. **CQG ScholarOne account + P1A submission.** Free, no arXiv, no format work.
   Lowest editorial bar in the portfolio.
3. `ZENODO_TOKEN` for the staged P5 deposit (`344125ce`).
4. JORS account + P1B submission (£824, or a waiver request in the cover letter).
5. AAS portal account; then P3, P4, P5 in whichever order suits — plus the one
   email to AAS Data Editors about Hugging Face as P4's catalog host (§1.3).
6. Send the endorsement requests. Background, non-blocking.

**Wave D — EXTERNALLY-BLOCKED, nothing to do but wait:** endorser replies,
editorial desks, AAS Data Editors' answer, referee reports.

---

*Prepared 2026-07-24. Read-only audit; this file is the only artifact written.
No submission, account creation, deposit, or email was performed. Every claim is
bound to a file:line, a compiled-PDF text extraction, or a URL fetched during
the audit; unconfirmed items are marked UNVERIFIED with the check that settles
them.*
