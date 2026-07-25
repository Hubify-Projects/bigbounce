# JORS Submission Kit — P1B → *Journal of Open Research Software* (Ubiquity Press), article type **Software Metapaper**

**Prepared 2026-07-24** · git HEAD at prep time `ef9993f2` · venue requirements
**re-fetched live from JORS's own pages on 2026-07-24** (every page returned HTTP
200; nothing below is inherited second-hand from the acceleration audit or from
`JOURNAL_ROUTE_PREP_2026-07-22.md`).

**Goal:** an 11pm click session. §3–§6 is everything you paste. §7 is the money.
§8 is the one thing that needs 20 minutes of your own judgment before you start.

> ### ✅ NO CONTENT GATE. The manuscript artifact is finished.
> `arxiv/jors_submission/` already holds a JORS-template-conforming rendering on
> the official `jors.cls`, content-equivalence-gated against the canonical
> v2B.0.15 manuscript, compiling clean at 8 pages A4. Nothing in the paper needs
> to change.
>
> ### ⚠️ BUT: two things must be ready BEFORE you open the wizard
> 1. **Five reviewer names *with email addresses*.** JORS's submission checklist
>    makes this a self-certified requirement (§1). You cannot improvise it at
>    11pm. §8 gives candidates and where to find their real emails — **do not
>    guess an email address.**
> 2. **The £824 decision.** Pay it, or request a waiver — and the waiver request
>    must be *in the cover letter at the moment of submission*. There is no later
>    opportunity (§7).

---

## 0. TL;DR

```
1. Decide: pay £824, or request a waiver in the cover letter    (§7)  ← DO THIS FIRST
2. Assemble 5 reviewer names + real email addresses             (§8)  ← AND THIS
3. Register at account.openresearchsoftware.metajnl.com         (§2)
4. Start the submission wizard → Software Metapaper
5. Upload 3 files: the JORS .tex, jors.cls, the JORS .pdf       (§4)
6. Paste §3 metadata; paste §5 cover letter into "Comments to the Editor"
   — the cover letter must ALSO carry the 5 reviewers, the waiver request,
   and the preprint declaration. One box, four jobs.              (§5)
7. Tick the Submission Preparation Checklist. Submit.
```

**arXiv: not required — JORS actively encourages preprints.**
**Cost: £824 + tax, invoiced only on acceptance, waivable.**

---

## 1. The venue's actual requirements — verified live 2026-07-24

Canonical domain confirmed: **openresearchsoftware.metajnl.com** (Ubiquity Press,
E-ISSN 2049-9647). The submission portal is a *separate host*:
`account.openresearchsoftware.metajnl.com`.

| Requirement | Verbatim governing sentence | Source URL |
|---|---|---|
| **Account** | *"To submit online, and to check the status of your submission, you need to have an account."* | https://openresearchsoftware.metajnl.com/about/submissions |
| **Submit URL** | `https://account.openresearchsoftware.metajnl.com/index.php/up-j-jors/submission/wizard` (linked from the home page and `/about/submissions`) | same |
| **Registration fields** | Retrieved live from `.../up-j-jors/user/register`: **Given Name\*, Affiliation\*, Country\*, Email\*, Username\*, Password\*, Repeat password\***, a privacy-statement consent box, and a reCAPTCHA. Family Name is not starred. Password rules: *"be at least 12 characters long / contain an alphabetic character / contain a numeric character / contain an uppercase character / contain a lowercase character / contain a non-alphanumeric character"* | https://account.openresearchsoftware.metajnl.com/index.php/up-j-jors/user/register |
| **Template conformance — required at submission** | *"The submission conforms to the article template. For LaTex submissions, a PDF should be provided along with the original LaTex file(s). Submissions in .docx format are also acceptable."* | https://openresearchsoftware.metajnl.com/about/submissions#submission-checklist |
| **Metapaper structure** | Mandated headings, verbatim from the official template: **(1) Overview** — Title; Paper Authors; Paper Author Roles and Affiliations; Abstract; Keywords; Introduction; Implementation and architecture; Quality control. **(2) Availability** — Operating system; Programming language; Additional system requirements; Dependencies; List of contributors; Software location:; Language. **(3) Reuse potential**; then Acknowledgements (Optional); Funding statement (Optional); Competing interests; References. | `JORS_Template.zip` / `jors_sw_paper_template_0-2.docx`, linked from /about/submissions |
| **Software location — Archive block** | *"Archive (e.g. institutional repository, general repository) (required – please see instructions on journal website for depositing archive copy of software in a suitable repository) / Name: … / Persistent identifier: e.g. DOI, handle, PURL, etc. / Licence: … / Publisher: Name of the person who deposited the software / Version published: … / Date published: dd/mm/yy"* | official template |
| **Abstract length** | *"A short (ca. 100 word) summary of the software being described…"* | official template |
| **Paper word limit** | **None published for metapapers.** The only cap on the site applies to a different section: *"Submissions should be no longer than 3000 - 4000 words"* (Issues in Research Software). Verified-by-absence for metapapers. | /about/submissions |
| **APC** | Publication Fees table as displayed 2026-07-24: **"Software Metapapers £824.00"** (and "Issues in Research Software £891.00"). Charged post-acceptance: *"Articles accepted for publication will be asked to pay an Article Publication Charge (APC)…"* and *"Tax will be added to all fees charged, when applicable"*. No submission fee found. | /about/submissions |
| **⭐ WAIVER — how to request** | *"If you need to request an APC waiver, please outline this in your cover letter."* And: *"If you do not have funds available to pay the APC (e.g., because your institution/funder will not cover the fee) then we may be able to offer a discount or full waiver. Should you need to discuss waiver options or the APC in general, please ensure that you contact the editor as early as possible. Editorial decisions are made independently from the ability to pay the APC. Waiver requests must be received as part of the submission information (e.g. in the cover letter)."* Checklist form: *"Any waiver request must be made at the time of submission in the Comments to the Editor section. Unless a waiver is granted by the journal, in writing, the author(s) accepts that an Article Processing Charge (APC) will be invoiced if the manuscript is accepted."* | /about/submissions |
| **⭐ FIVE reviewers — required** | Checklist item: *"Names and email addresses of five potential peer-reviewers have been provided in the 'Comments for the Editor' box below."* | /about/submissions#submission-checklist |
| **Excluded reviewers** | *"Authors are invited to recommend or ask for the exclusion of specific individuals from the peer review process. The journal does not guarantee to follow these suggestions."* | https://openresearchsoftware.metajnl.com/about/editorialpolicies |
| **Cover letter — REQUIRED** | Checklist item: *"A cover letter has been provided in the Comments to the Editor."* | /about/submissions#submission-checklist |
| **Preprint policy** | *"Yes. We encourage people to submit preprint servers such as arXiv at time of submission to JORS. JORS does not require the removal of preprints…"* and *"The author declares that a preprint is available within the cover letter presented during submission. This must include a link to the location of the preprint."* | /about ; /about/editorialpolicies |
| **Archive persistent identifier — mandatory** | Reviewer form: *"If the Archive section is filled out, is the link in the form of a persistent identifier (e.g. a DOI)? Can you download the software from this link?"* Journal requirement: *"We require that the version of software described in your software is available in at least one repository that satisfies the criteria below"*, and repositories must *"Provide persistent identifiers (e.g. DOI, handle, ARC etc.)"* | /about/editorialpolicies ; /about |
| **Licence** | *"Authors retain copyright and grant the journal right of first publication with the work simultaneously licensed under a Creative Commons Attribution License…"* — CC BY 4.0 | /about/submissions Copyright Notice |
| **Peer review model** | *"Peer review is typically single anonymous, however reviewers may sign their reviews."* | /about/editorialpolicies |
| **ORCID** | *"The journal strongly recommends that all authors submitting a paper register an account with… ORCID"* / *"encourages all corresponding authors to include an ORCID within their submitting author data"* — recommended, not required | /about/submissions |
| **Competing interests** | Checklist: *"Where relevant, competing interests have been declared."* Template: *"If there are no competing interests, please add the statement: 'The authors declare that they have no competing interests.'"* Funding statement is marked **"Optional"** in the metapaper template. | /about/submissions ; official template |
| **Figures** | *"All figures must be uploaded separately as supplementary files during the submission process, if possible in colour and at a resolution of at least 300dpi. Each file should not be more than 20MB… JPG, TIFF, GIF, PNG, EPS."* — **P1B has zero figures**, so this step is skipped entirely | /about/submissions |
| **Journal statistics (2025 volume)** | Submissions 98; Acceptances 45; *"Acceptance rate 33%"*; *"Time from submission to publication 495 days"* (mean) | /about |
| **Independent / unaffiliated author** | No affiliation requirement in any editorial policy. The only friction is the starred **Affiliation** box on the registration form. *"Editorial decisions are made independently from the ability to pay the APC."* | /about/editorialpolicies ; registration form |

### Items I could NOT verify — stated plainly

1. **Time to *first decision*. UNVERIFIED — no public figure exists.** JORS
   publishes only submission-to-*publication* mean (495 days, 2025 volume), which
   includes revision rounds and production. Settled by: ask the Editor-in-Chief
   directly, or ask in the cover letter. **Plan for this being slow.**
2. **Citation-style conflict — needs an editor to resolve.** The official
   template says *"Please enter references in the Harvard style … citing them in
   the text with a number in square brackets"*, while /about/submissions says
   *"This journal uses the Vancouver numbered system."* and *"Citations must be
   as parenthetical citations according to a numerical system."* These are not
   the same instruction. **UNVERIFIED which governs.** P1B currently uses
   numbered square-bracket citations `[1]–[4]`, which satisfies *both* documents'
   numeric-in-text requirement; only the reference-list formatting is ambiguous.
   **Not a blocker** — this is a copy-editing matter, and §5's cover letter
   mentions it so the editor can rule. Do not restructure the bibliography over it.
3. **Whether the APC table is current.** The Publication Fees table carries no
   date stamp; a nearby "APC cost breakdown" element is labelled *"2023 data"*.
   The **£824.00** figure is what the live page displays on 2026-07-24.
   **UNVERIFIED as a 2026-effective rate.** Settled by: the invoice, or by asking
   the editor when you request the waiver. Ask in the same message — §5 does.
4. **Whether the wizard's "Comments to the Editor" box has a length limit.**
   Unknown. §5's text is ~500 words; if it truncates, the priority order is
   waiver request → five reviewers → preprint declaration → the rest.

---

## 2. Portal + account

1. **https://openresearchsoftware.metajnl.com/about/submissions** — read the
   Submission Preparation Checklist once, in full, before starting. It is
   self-certified and it is where the five-reviewer and cover-letter requirements
   live.
2. Register: **https://account.openresearchsoftware.metajnl.com/index.php/up-j-jors/user/register**
   - Given Name: `Houston` · Family Name: `Golden`
   - **Affiliation (required field):** `Independent Researcher`
   - Country: `United States`
   - Email: `houston@hubify.com`
   - Password: 12+ chars with upper, lower, digit, and a symbol
   - There is a reCAPTCHA on this form. That is yours to complete — I neither can
     nor will.
3. Add ORCID **0009-0008-5616-5994** to the profile / submitting-author data.
4. Submit at
   **https://account.openresearchsoftware.metajnl.com/index.php/up-j-jors/submission/wizard**
   → section **Software Metapapers**.

---

## 3. Paste-ready metadata

**Article type / section:** `Software Metapaper`

**Title** (paste exactly; if the field is plain-text-only, the subscript ell
renders as written):

```
namaster-proof: Exact pseudo-C_ell window inference and content-bound validation for reproducible spin-2 analyses
```

**Author:** `Houston Golden` (sole author, corresponding author)
**Affiliation:** `Independent Researcher, Los Angeles, California, USA`
 — the manuscript's own author-roles line reads *"Independent researcher
 (unaffiliated), Los Angeles, California, USA"*; use either, they agree.
**Email:** `houston@hubify.com`
**ORCID:** `0009-0008-5616-5994`
 · VERIFIED public 2026-07-24 — `pub.orcid.org/v3.0/0009-0008-5616-5994` returns
 HTTP 200, record name "Houston Golden".

**Keywords** (verbatim from the manuscript's Keywords section):

```
Python; cosmology; pseudo-C_ell; NaMaster; reproducibility; provenance
```

**Suggested subject/discipline tags,** if the wizard asks for a free-text
discipline rather than a fixed list: `Astronomy and Astrophysics`; `Cosmology`;
`Research Software Engineering`; `Reproducible Research`. JORS publishes no fixed
subject taxonomy on its public pages — **UNVERIFIED**; take whatever the wizard
offers that is closest to astronomy/physics software.

### Abstract — plain text, ready to paste

**Word count: 113** against the template's guidance of *"ca. 100 word"*. That is
guidance, not a cap. Leave it as is.

**Provenance:** pulled verbatim from the compiled JORS PDF
`arxiv/jors_submission/paper1b_namaster_proof_jors.pdf`, rendering of manuscript
**v2B.0.15**, PDF md5 `51e302e6746ef9d67e3bde9265b1ec91`, 8 pages A4.

> **RE-VERIFY BEFORE PASTING** if a parallel lane has bumped P1B since: run
> `md5 -q arxiv/jors_submission/paper1b_namaster_proof_jors.pdf`; if it is no
> longer `51e302e6746ef9d67e3bde9265b1ec91`, re-read the abstract out of the new
> PDF and diff it against the block below.

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

### Software-location metadata — the fields JORS will ask for

These are already written into §(2) Availability of the submitted PDF, but the
wizard may also ask for them as form fields. Copy from here:

| Field | Value |
|---|---|
| **Archive — Name** | `namaster-proof 0.1.7` — commit-pinned archive of the `packages/namaster-proof` source tree (repository commit `0a587b583f8e86c4ce1ee4a20526fcdcd8035fe6`), with its license, citation metadata, and checksums |
| **Archive — Persistent identifier** | `doi:10.5281/zenodo.21481753` ✅ **VERIFIED 2026-07-24, resolves HTTP 200 → zenodo.org/records/21481753** |
| **Archive — Licence** | `MIT License` |
| **Archive — Publisher** | `Zenodo` |
| **Archive — Version published** | `0.1.7` |
| **Archive — Date published** | `21/07/26` (21 July 2026) — note the template's `dd/mm/yy` format |
| **Code repository — Name** | `Hubify-Projects/bigbounce — packages/namaster-proof` |
| **Code repository — Identifier** | `https://github.com/Hubify-Projects/bigbounce/tree/main/packages/namaster-proof` |
| **Code repository — Licence** | `MIT License` |
| **Code repository — Date published** | `16/07/26` (16 July 2026) |
| **Operating system** | Linux and Windows where Python and NumPy are available; CI covers Linux (Python 3.10–3.13) and Windows (Python 3.12). macOS expected to work but **not exercised in CI and listed as untested** |
| **Programming language** | Python; version 0.1.7 requires Python ≥ 3.10 |
| **Dependencies** | NumPy ≥ 1.24 (only required runtime dependency). PyMaster optional, user-supplied; the retained physical validation used PyMaster 2.6 and healpy 1.19.0 |
| **List of contributors** | Houston Golden — sole author and contributor (design, implementation, tests, examples, documentation, packaging), consistent with `CITATION.cff` and `codemeta.json`, which each list a single author. AI coding and review agents assisted under the author's supervision; see the AI usage disclosure section |
| **Language** | English |

---

## 4. What to upload

**Three files, all from `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/arxiv/jors_submission/`.**

| Role | Path | md5 | Notes |
|---|---|---|---|
| **Main LaTeX source** | `arxiv/jors_submission/paper1b_namaster_proof_jors.tex` | `9d378c5c143931b1989e5721ce08c71d` | 27,192 bytes; `\documentclass{jors}` |
| **Class file** | `arxiv/jors_submission/jors.cls` | `fa935958e955a7eb9ca010c69c479148` | **byte-identical to the copy in JORS's own `JORS_Template.zip`** — upload it so the editor can compile without hunting for it |
| **Compiled PDF** | `arxiv/jors_submission/paper1b_namaster_proof_jors.pdf` | `51e302e6746ef9d67e3bde9265b1ec91` | **8 pages, A4**, 280,105 bytes, **0 figures** |

**Do not upload:**
- `paper1b_jors_submission_v2B.0.15.tar.gz` (md5 `4e68a042f7386d292dd9ad5720957038`) — that is the provenance bundle, not a submission file. The portal wants individual files.
- `JORS_template_reference.tex` — JORS's own template, kept locally for reference.
- The canonical `arxiv/paper1b_namaster_proof.pdf` (6 pp, US Letter, md5 `e1a80ef5c6078b7fd93d036ff719bbd0`). **That is the wrong file for this venue** — it is the non-JORS rendering. This is the easiest mistake to make in the whole submission: the two PDFs have near-identical names and sit two directories apart. **Check for "(1) Overview" on page 1 before you upload.** If page 1 starts with a two-column REVTeX title block instead, you have the wrong file.

There is no `.bbl` or `.bib`: the bibliography is an inline `thebibliography`, so
the source compiles standalone with `pdflatex` alone. Verified in an isolated
extract: 0 errors, 0 undefined references, 0 overfull hboxes, 8 pages.

No figure uploads (§1) — P1B has zero figures.

---

## 5. Cover letter — REQUIRED, and it carries four payloads

JORS funnels the cover letter, the five reviewers, the waiver request, and the
preprint declaration into **one "Comments to the Editor" box** (§1). Miss any one
and you fail a checklist item you have already ticked.

**Before pasting, fill in the five reviewer lines from §8. Do not submit with the
placeholder text in place.**

```
Dear Editors,

I am submitting "namaster-proof: Exact pseudo-C_ell window inference and
content-bound validation for reproducible spin-2 analyses" for consideration as
a Software Metapaper.

namaster-proof is a small Python verification layer for two steps that are easy
to get wrong in cut-sky spin-2 power-spectrum analyses: evaluating a rotated
EE/EB/BE/BB spectrum through the complete NaMaster bandpower-window operator
rather than through bin-centre or effective-multipole stand-ins, and binding
result files to their execution metadata so that a silent change in either fails
closed rather than propagating. It is deliberately narrow. The paper states
plainly what the package is not: it is not a sky-analysis pipeline, a foreground
model, or a cosmological inference engine, and its recovery checks are software
validation, not measurements or detection significances. It is an independent
downstream verification layer and is not an official release of, or affiliated
with, the NaMaster project.

The software is openly licensed (MIT) and permanently archived: version 0.1.7,
pinned to repository commit 0a587b583f8e86c4ce1ee4a20526fcdcd8035fe6, is
deposited on Zenodo under DOI 10.5281/zenodo.21481753, with the live repository
at https://github.com/Hubify-Projects/bigbounce/tree/main/packages/namaster-proof.
CITATION.cff and codemeta.json are included in the package.

PREPRINT DECLARATION. This manuscript has not been posted to arXiv. A permanent
public archive of the manuscript and its exact source is deposited on Zenodo
under DOI 10.5281/zenodo.21481842 (CC-BY-4.0), available at
https://doi.org/10.5281/zenodo.21481842. I declare it here because it is a
publicly readable copy of substantially this text, and I would rather over-
disclose than under-disclose. That deposit archives an earlier revision of the
manuscript (v2B.0.13); the version submitted here is v2B.0.15, rendered onto the
JORS article template.

APC WAIVER REQUEST. I am an independent researcher with no institutional
affiliation, no grant funding, and no institution or funder able to cover an
article publication charge. I am therefore requesting a full waiver of the
GBP 824.00 Software Metapaper APC, under the journal's stated waiver policy. I
would be glad to discuss a partial discount if a full waiver is not available. I
would also be grateful if you could confirm the current APC figure, as the fee
table on the submissions page carries no effective date.

SUGGESTED REVIEWERS (five, per the submission checklist):
1. [Name] — [institution] — [email]
2. [Name] — [institution] — [email]
3. [Name] — [institution] — [email]
4. [Name] — [institution] — [email]
5. [Name] — [institution] — [email]
I have no reviewers I wish to exclude.

COMPETING INTERESTS. The author declares that they have no competing interests.

One small clarification I would welcome guidance on: the JORS metapaper template
asks for Harvard-style references cited with numbers in square brackets, while
the submissions page states the journal uses the Vancouver numbered system. The
manuscript uses numbered square-bracket in-text citations, which satisfies both;
I am happy to reformat the reference list to whichever style you prefer.

I confirm this work has not been published elsewhere and is not under
consideration at another journal.

Thank you for your consideration.

Houston Golden
Independent Researcher, Los Angeles, California, USA
ORCID 0009-0008-5616-5994
houston@hubify.com
```

**On the waiver paragraph — do not soften it and do not embellish it.** The
policy says waivers exist precisely for authors whose institution or funder will
not cover the fee, and it says *"Editorial decisions are made independently from
the ability to pay the APC."* The honest statement — no affiliation, no funder —
is exactly the case the policy describes. Never invent an institution to look
more fundable; it would be false and it would make you *less* eligible for the
waiver.

---

## 6. Data / code availability answer

JORS's whole subject *is* the code, so this is already the spine of the paper
(§(2) Availability). If a separate portal field asks for a data/code availability
statement, paste:

```
The software described in this metapaper, namaster-proof version 0.1.7, is
released under the MIT License. The reviewed version is permanently archived on
Zenodo under DOI 10.5281/zenodo.21481753, pinned to repository commit
0a587b583f8e86c4ce1ee4a20526fcdcd8035fe6, together with its license, citation
metadata, and checksums. The live source, issue tracker, installation
instructions, API documentation, tests, and examples are at
https://github.com/Hubify-Projects/bigbounce/tree/main/packages/namaster-proof.
The manuscript itself, with its exact source and provenance manifest, is
separately archived under DOI 10.5281/zenodo.21481842 (CC-BY-4.0). The two
validation artifacts referenced in the paper are content-bound by SHA-256
(745b0a2f060773ce69c005ea84b74b305ec26a85f6aaafe58f0b3244b7f39914 and
b00f850e338007caea6af76f4e9305ab6b54a68e6799efd450bc76f1c325f331). No
observational data are introduced by this work.
```

**DOIs verified this session** (both follow to HTTP 200):
- `10.5281/zenodo.21481753` (software 0.1.7) → `zenodo.org/records/21481753` ✅
- `10.5281/zenodo.21481842` (manuscript) → `zenodo.org/records/21481842` ✅

---

## 7. Cost — read this before you start

| Item | Cost |
|---|---|
| Registration | £0 |
| Submission | **£0** — no submission fee found on any page |
| **Article Publication Charge, Software Metapaper** | **£824.00 + tax where applicable** |
| When charged | **Only on acceptance.** *"Articles accepted for publication will be asked to pay an Article Publication Charge"* |
| Waiver | Full waiver or discount available — **must be requested in the cover letter at submission** |
| Article licence you get | CC BY 4.0, you retain copyright |

**There is no payment screen at submission.** Nothing will ask for a card. The
invoice only appears if the paper is accepted. What you *are* doing at submission
is agreeing to the checklist line: *"Unless a waiver is granted by the journal,
in writing, the author(s) accepts that an Article Processing Charge (APC) will be
invoiced if the manuscript is accepted."*

**Recommendation: request the full waiver.** You genuinely meet the stated
criterion (no institution, no funder). Requesting it costs nothing, cannot
prejudice the editorial decision by the journal's own written policy, and there
is **no second chance** — waivers must be requested at submission. Worst case you
are told no and you decide then whether £824 is worth it, with a real
acceptance in hand rather than a hypothetical one.

**Judgment call that is genuinely yours:** if the waiver is refused and the paper
is accepted, is £824 worth it for a software metapaper? Honest framing — the
software is already permanently citable via its Zenodo DOI, so the £824 buys peer
review and a journal-of-record citation, not availability. Decide that *after* an
acceptance, not now.

---

## 8. Five suggested reviewers — required, and where the endorser conflict sits

**This is the one part of the JORS submission you cannot do at 11pm.** The
checklist requires **five names *and* email addresses**. Budget 20 minutes.

### Rule 1 — never guess an email address
Take each address from the person's own published paper (corresponding-author
footnote) or their institutional staff page. A bounced or wrong address in a
reviewer suggestion is worse than one fewer suggestion.

### Rule 2 — no one from the arXiv endorser shortlist
`project-context/SSOT/ENDORSER_SHORTLIST_2026-07-22.md` lists people being
approached separately to endorse arXiv submissions. **Do not name any of them
here.** An endorsement is a personal favour you asked for; a referee suggestion
asserts independence. Doing both to the same person compromises the review and
makes the endorsement look transactional — and both are in writing.

**For P1B this costs you nothing.** The endorser shortlist is DESI/cosmology and
galaxy-chirality people (Cai, Noriega, Brandenberger, Xue, Shamir, Martini,
Gonzalez-Perez, Lamman, Elbers, Suárez-Pérez). The right reviewers for a
pseudo-C_ell *software* metapaper are CMB/LSS software and
research-software-engineering people. The two sets barely intersect — the natural
candidates below are none of them. Check each name against the shortlist anyway
before you paste.

### Candidate pool

**Group A — the pseudo-C_ell / NaMaster / HEALPix software community.** Grounded
in P1B's own four-reference bibliography, so their relevance is a matter of
record rather than my guess.

| Candidate | Basis |
|---|---|
| **David Alonso** | First author of *"A unified pseudo-C_ell framework"* — the NaMaster paper. P1B ref. [2]. The single most domain-expert reviewer available. |
| **Anže Slosar** | Co-author of the same NaMaster paper. P1B ref. [2]. Long track record in open cosmology software. |
| **Javier Sanchez** | Co-author of the same NaMaster paper. P1B ref. [2]. |
| **Eric Hivon** | First author of the MASTER method paper, P1B ref. [1]; also a HEALPix author. Reviews the pseudo-C_ell foundations the package validates against. |
| **Martin Reinecke** | HEALPix co-author (P1B ref. [4]) and a maintainer of the underlying spherical-harmonic software stack — a strong *software-quality* reviewer as opposed to a method reviewer. |

> **Judgment call, flagged explicitly.** Alonso / Sanchez / Slosar are NaMaster's
> authors, and P1B is an *independent verification layer for NaMaster* that
> explicitly states it "is not an official release of, or affiliated with, the
> NaMaster project." That could cut either way: they are the best-qualified
> reviewers alive for this, and they may also feel proprietary about an external
> tool that checks theirs. **Recommendation: include one or two of them, not all
> three, and balance the list with reviewers who have no NaMaster stake.** JORS
> review is single-anonymous, so they will know it is your paper but you will not
> know who reviewed.

**Group B — research-software / reproducibility reviewers.** JORS's own review
form scores metadata correctness, installability, documentation and reuse
potential — not cosmology. At least two of your five should be people who assess
*software*, not spectra. Good sources for real, current names with public
contact details:
- The **JORS editorial board** — https://openresearchsoftware.metajnl.com/about/editorialteam
  (do not suggest the handling editor; do use it to see who the journal already
  trusts, and to identify their community).
- **JOSS** (Journal of Open Source Software) reviewers who have handled
  astronomy/Python submissions — the reviewer list and every review are public at
  `github.com/openjournals/joss-reviews`.
- Maintainers of adjacent astronomy Python packages (`healpy`, `pixell`,
  `astropy` affiliated packages) whose GitHub profiles carry institutional
  contact details.

I have deliberately **not** invented five specific names with email addresses
here. Doing so would be exactly the kind of plausible-looking fabrication this
kit exists to prevent. Pick from the grounded Group A list, add two from Group B
after five minutes on those pages, and verify every address at its source.

### Excluded reviewers
**Recommendation: exclude no one, and say so.** §5's letter states *"I have no
reviewers I wish to exclude."* You have no adversary here, and an unexplained
exclusion request invites the editor to wonder why.

---

## 9. Pre-submission checklist

| # | Must be true | Status 2026-07-24 |
|---|---|---|
| 1 | JORS-conforming manuscript exists on the official `jors.cls` | ✅ `arxiv/jors_submission/` — 8 pp A4, 0 errors, 0 undef-refs, 0 overfull hboxes, verified in an isolated extract |
| 2 | `jors.cls` byte-identical to JORS's own distributed copy | ✅ md5 `fa935958e955a7eb9ca010c69c479148` |
| 3 | All mandated template headings present in the required order | ✅ (1) Overview / (2) Availability / (3) Reuse potential + Acknowledgements, Funding statement, Competing interests |
| 4 | Content equivalent to the canonical v2B.0.15 manuscript | ✅ 50 of 53 prose blocks byte-verbatim; the 3 exceptions are exactly the blocks JORS mandates be split into granular Availability fields, each reconciled fact-by-fact. No claim, number, caveat, or citation lost |
| 5 | ORCID in the manuscript | ✅ present in the author-roles line, `0009-0008-5616-5994` |
| 6 | ORCID resolves publicly | ✅ **VERIFIED 2026-07-24** — HTTP 200, "Houston Golden" |
| 7 | Software archived with a persistent identifier | ✅ Zenodo DOI `10.5281/zenodo.21481753` — **verified resolves HTTP 200** |
| 8 | Manuscript archive DOI resolves | ✅ `10.5281/zenodo.21481842` — **verified resolves HTTP 200** |
| 9 | Software under an OSI-approved licence | ✅ MIT (`packages/namaster-proof/LICENSE`) |
| 10 | `CITATION.cff` + `codemeta.json` present | ✅ both in `packages/namaster-proof/` |
| 11 | Competing-interests statement present | ✅ in the manuscript; repeated in the cover letter |
| 12 | AI usage disclosed | ✅ dedicated `AI usage disclosure` section in the submitted PDF |
| 13 | Abstract ≈ 100 words | ✅ 113 — guidance, not a cap |
| 14 | Zero figures (so no separate figure uploads) | ✅ confirmed |
| 15 | **Five reviewer names + real email addresses ready** | ⬜ **NOT READY — HOUSTON-ONLY, §8.** Hard checklist requirement. |
| 16 | **Cover letter with waiver request drafted** | ✅ drafted in §5 — **you must fill in the five reviewer lines before pasting** |
| 17 | **£824 decision made** (pay vs waiver) | ⬜ **HOUSTON-ONLY** — recommendation: request the full waiver, §7 |
| 18 | JORS account created | ⬜ **HOUSTON-ONLY** — this kit creates no accounts |
| 19 | Preprint declaration decided | ✅ §5 declares the Zenodo manuscript deposit with its link, per JORS's preprint policy. Recommended: leave it in. |
| 20 | Not under consideration elsewhere | ✅ P1B has been submitted to no journal |

---

## 10. What happens after you click

**Timeline — set expectations low.** JORS publishes **no time-to-first-decision
figure** (UNVERIFIED, §1). The only public number is a **495-day mean from
submission to publication** across the 2025 volume, and an acceptance rate of
**33%** (45 of 98). Editorial policy states the journal *"aims for 1–2 review
rounds"*. Treat this as a slow venue: months, not weeks. If speed matters more
than the JORS byline, note that the software is already permanently citable via
its Zenodo DOI today — nothing about the package's availability is waiting on
this.

**If the editor replies about the waiver before review:** answer promptly and
plainly. Do not negotiate by inventing hardship you do not have; "no institution,
no funder" is the whole case and it is true.

**When the decision arrives — what to update in the repo:**

| Outcome | Repo surfaces to update |
|---|---|
| **Any decision** | `project-context/SSOT/paper-1/status.md` (P1B section) — venue, submission date, manuscript ID, decision verbatim. Add a `reviewTimeline.ts` entry under `site/src/data/` **in the same commit** (standing directive: review-round site sync). Update `project-context/SSOT/index.md`. |
| **Reviewer reports** | Save every report's complete raw text under `project-context/peer-reviews/` **before** recording a verdict, and truth-audit each finding with a source-cited disposition before closing it. The integrity rules that govern INT/EXT rounds apply with more force to real human referees, not less. |
| **Revision requested** | Revise the **JORS rendering** (`arxiv/jors_submission/paper1b_namaster_proof_jors.tex`) and decide deliberately whether each change should also propagate to the canonical `arxiv/paper1b_namaster_proof.tex`. **They are two renderings of one manuscript — letting them diverge silently is the failure mode this arrangement is designed to avoid.** If the canonical changes, directive G applies: bump `\paperVersion`, recompile, re-mirror every served PDF path, sync Convex with real md5/page counts. |
| **Accept** | Post-acceptance JORS requires the published citation be copied back into the software repository — update `packages/namaster-proof/CITATION.cff` and `README`. Add the journal reference to both Zenodo records' metadata. Sync Convex (`activityFeed:add`) so the live site shows it; static `papers.ts` alone does not reach the site (standing directive A). Under directive P this closes a *publishing-phase* row and does not move a readiness score. |
| **Reject** | Record the reason verbatim. The natural next venue for a software metapaper of this shape is **JOSS** (Journal of Open Source Software) — free, fast, and openly reviewed — which would need a much shorter `paper.md`, not this metapaper. Open that as a queue row rather than treating a rejection as terminal. |

---

*Kit prepared 2026-07-24 against git HEAD `ef9993f2`. Every venue requirement
re-fetched live from openresearchsoftware.metajnl.com this session; items that
could not be confirmed from an official page are labelled UNVERIFIED in §1 with
the check that would settle them. Nothing was submitted, no account was created,
no email was sent, and no reviewer was contacted.*
