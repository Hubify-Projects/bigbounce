# PRD Submission Kit — P2 → *Physical Review D* (APS), article type **Research Article**

**Prepared 2026-07-24** · git HEAD at prep time `ef9993f2` · venue requirements
**re-fetched live from APS's own pages on 2026-07-24**. This kit does **not**
inherit the acceleration audit's APS quotes: that audit read APS through Wayback
Machine snapshots because `journals.aps.org` serves a bot challenge. This session
retrieved the *live* pages through a text-reader proxy that reports the origin
URL, and **three of the audit's APS conclusions are corrected below** (§1.1).

**Goal:** an 11pm click session. §3–§6 is everything you paste. §8 is the one
place a name could embarrass you. §9.1 and §9.2 were the two pre-click items and
**both are closed** — updated 2026-07-24 against **v1.7.130**.

> ### ✅ NO BLOCKING CONTENT DEFECT. This is the shortest distance to a real editor's desk.
> PDF-only initial submission. arXiv irrelevant. No APC on the subscription
> route. Abstract 208 words against a 500-word cap. The PDF exists and compiles
> clean.
>
> ### ✅ BOTH PRE-CLICK ITEMS CLOSED 2026-07-24 in **v1.7.130**
> 1. **AI-usage disclosure — DONE.** A `\section*{AI Usage Disclosure}` now sits
>    in the body immediately after Data and Code Availability (page 8), naming
>    the actual models and versions used on *this* paper, what they did, and
>    what the author retained and verified. See **§9.1**.
> 2. **The deposit self-reference — DONE, and made structurally unable to drift.**
>    The "one patch line ahead" literal is gone; the whole relationship clause,
>    including its tense, is now computed from the two version macros. It renders
>    today as *"the present manuscript is v1.7.130, 5 patch releases ahead, and
>    will be added to the same Zenodo record as a new version on the next
>    re-stage."* See **§9.2**.
>
> Also landed in the same bump: **ORCID `0009-0008-5616-5994` is now in the
> manuscript's author block** (was §9 item 3).
>
> **Current bytes: v1.7.130, md5 `f7116fe3e2541d6f649876f2ec7789ee`, 12 pages**
> (was 11 — the new disclosure section added one; PRD Research Articles have no
> length limit). Mirrored byte-identical to 19 served paths; Convex
> `paperVersions` row `k5713b3bdee7b7my9c2jc32nah8b7xdc`. **The abstract was not
> touched.**

---

## 0. TL;DR

```
1. AI-disclosure + deposit-reference fixes already landed in v1.7.130 (§9.1, §9.2)
2. Create an account at authors.aps.org/Submissions/               (§2)
3. New submission → Physical Review D → Research Article
4. Upload ONE PDF: research/focused_paper_source_integration/02_full_draft.pdf (§4)
5. Paste §3 metadata; ORCID is REQUIRED and gets a verification email (§3)
6. Fill the Data Availability Statement Q&A — MANDATORY for PRD           (§6)
7. Cover letter (§5) — it is also where suggested/excluded referees go    (§8)
8. Do NOT elect the $2910 CC-BY option unless you want to pay it          (§7)
9. Submit. First decision before review: ~3 days (PRD 2025 median).
```

---

## 1. The venue's actual requirements — verified live 2026-07-24

**Retrieval note, stated plainly.** `journals.aps.org` returns HTTP 403 to
automated fetch (Cloudflare). That challenge was **not** solved. Every quote below
was retrieved through a text-reader proxy that returns the page body together
with a `URL Source:` header confirming the origin URL — i.e. the live page, not a
Wayback snapshot. Two APS URLs that other documents cite,
`journals.aps.org/authors/submit-manuscript` and `journals.aps.org/prd/apc`,
**return "Not Found"** — do not use them.

| Requirement | Verbatim governing sentence | Source URL |
|---|---|---|
| **Portal** | *"To resubmit or transfer your paper, go to the APS Submission Server"* → `https://authors.aps.org/Submissions/login/new`. The footer "Submit a Manuscript" link points to `https://authors.aps.org/Submissions/`. **It is the APS Submissions Server, not Editorial Manager.** | https://journals.aps.org/prd/authors |
| **Initial files — PDF is enough** | *"A PDF version of your paper is all that's needed for it to be sent for peer review. However, submitting properly formatted source files in LaTeX (preferred) or Microsoft Word simplifies peer-review… Source files will be converted to a PDF on submission."* | https://journals.aps.org/prd/authors |
| **Nothing else needed** | *"Physical Review D does not require additional materials beyond what is mentioned above."* | https://journals.aps.org/prd/authors |
| **arXiv** | **Not required and not mentioned as a submission requirement on any PRD author page.** It matters only for free OA via SCOAP³: *"All high-energy physics articles published in PRD since January 1, 2018, and that are posted on arXiv under one of the four "hep" primary designations, are made open access under a Creative Commons Attribution license under the auspices of SCOAP 3."* | https://journals.aps.org/prd/about |
| **Article type / length** | *"Research Articles (no length limit)"*; Letters are capped at 4500 words; Comments/Replies at 3500. **P2 is a Research Article — no length constraint.** | https://journals.aps.org/prd/authors |
| **Abstract cap** | *"Length should be about 5% of the article and less than 500 words."* | https://journals.aps.org/authors/style-basics |
| **Cost — subscription** | **$0.** No submission fee and no publication fee is published for the subscription route. | absence across /prd/authors and /authors/apcs |
| **Cost — optional gold OA** | PRD row in the APC table: *"\| Physical Review D \| hybrid \| $2910 \|"* under the header *"\| Journal Title \| Journal Type \| 2026 APC (USD) \|"*. Explicitly labelled **2026**. | https://journals.aps.org/authors/apcs |
| **Colour figures** | *"The charge is US$1090 for a single color figure in print and $595 for each additional color figure."* — a **print** charge. See §7 for why this almost certainly does not apply to you. | https://journals.aps.org/prd/authors |
| **⭐ ORCID — REQUIRED** | *"ORCID iDs are required for all Corresponding Authors and are strongly encouraged for all other authors. APS requires authors to authenticate their identifiers via the ORCID verification process. Verification requests are sent shortly after submission…"* | https://journals.aps.org/authors/editorial-policies |
| **⭐ Data Availability Statement — MANDATORY for PRD** | *"All published articles must include a Data Availability Statement (DAS)… Authors are asked to enter a complete data availability statement during the submission process, including relevant citations."* And: *"Authors submitting to Physical Review journals on or after Dec. 11, 2024 (Sept. 4, 2024, for Physical Review D and PRX Energy) are **required** to have a Data Availability Statement"* | https://journals.aps.org/prd/authors ; https://journals.aps.org/authors/editorial-policies |
| **Data citation** | *"Publicly shared data and software must be cited in the reference list, and the citation must be included in the data availability statement."* | https://journals.aps.org/authors/data-availability-statements |
| **Conflict of interest — encouraged, not mandatory** | *"Authors should alert editors to any potential conflict of interest such as sources of funding, condition of employment… Authors are encouraged to declare any conflict of interest within the paper itself using a Conflict of Interest statement."* | https://journals.aps.org/authors/editorial-policies |
| **⭐ AI / LLM — disclosure required for substantive use** | *"An AI program cannot be held accountable and cannot be listed as an author."* · *"Authors must keep a record of any AI use and disclose any substantive uses in the submitted paper"* · *"Authors should state: AI tool name and version · How the AI assisted · How the authors directed and verified the AI output"* · *"Authors are not required to disclose the use of AI to polish, condense, or otherwise lightly edit the text."* · *"Any AI used to conduct the actual research (e.g., data analysis) must, like any tool, be disclosed within the paper's methods section."* | https://journals.aps.org/authors/appropriate-use-ai-tools |
| **Referees** | *"The cover letter… should include the following: … Any recommended or excluded referees"* and *"Authors are encouraged to suggest suitable reviewers. They may also inform editors of experts who have a potential conflict of interest and who might provide a biased recommendation. However, the editors are not bound by these suggestions and will exercise their best judgment."* | https://journals.aps.org/prd/authors ; https://journals.aps.org/authors/editorial-policies |
| **Cover letter** | *"The cover letter is an opportunity to explain why the manuscript is appropriate for the journal."* Framed as an opportunity; **no page states it is mandatory.** | https://journals.aps.org/prd/authors |
| **Classification — PhySH, not PACS** | *"PhySH is a replacement for an older physics classifiation known as PACS. APS used alpha-numeric PACS codes for about 40 years to classify journal content… PACS ceased development in 2010"* (sic — APS's typo) | https://physh.org/about |
| **Review model** | *"All APS journals follow the single-anonymized peer review procedures"* | https://journals.aps.org/prd/authors |
| **Integrity screening** | *"Manuscripts submitted to APS journals may be submitted to third-party services for integrity checks, including plagiarism, and other content analysis."* | https://authors.aps.org/Submissions/ |
| **⭐ Speed — PRD 2025 medians** | Row: *"\| PRD \| Physical Review D \| 3 \| 41 \| 86 \| 115 \|"* under *"1st decision before review (days) \| 1st decision after review (days) \| Submission to acceptance (days) \| Submission to publication (days)"*, preamble *"All metrics are from 2025."* | https://journals.aps.org/metrics |
| **Independent / unaffiliated author** | *"Authors must use the affiliation(s) where the research was conducted. Current affiliations where research was not conducted can be included as byline footnotes."* No rule about having none; no membership requirement found. | https://journals.aps.org/authors/editorial-policies |
| **Payment platform** | SciPris™; link sent on acceptance | https://journals.aps.org/prd/authors |

### 1.1 Three corrections to the acceleration audit's APS section

The audit read APS through Wayback snapshots and marked its APS findings
UNVERIFIED against live pages. Now checked live:

| Audit said | Live pages say |
|---|---|
| *"AI/LLM disclosure: **No in-manuscript disclosure section mandated**"* — quoting the one-line editorial-policies sentence about polishing | **Incomplete.** APS's dedicated page requires disclosure of *substantive* AI use in the submitted paper, with tool name, version, how it assisted, and how the authors verified the output — and requires research-conducting AI to be disclosed **in the methods section**. Only *light editing* is exempt. See §9.1. |
| *"Abstract cap: None found"* | **There is one: <500 words** (APS Style Basics). P2's 208 words are comfortably under, so the conclusion "not a blocker" survives — but the cap exists. |
| Portal quoted as `https://authors.aps.org/Submissions` | Confirmed correct; the new-submission entry point is `https://authors.aps.org/Submissions/login/new`. Two URLs cited elsewhere in the repo (`/authors/submit-manuscript`, `/prd/apc`) are **404**. |

The audit's core finding — **arXiv is not a gate, PDF alone suffices, subscription
route is free, no blocking content defect** — is confirmed against the live pages.

### 1.2 Items I could NOT verify — stated plainly

All five require an authenticated portal session, which this kit does not open:

1. **Whether creating an account is mandatory before starting a submission.**
   The login/new URL exists; the form text could not be retrieved. **UNVERIFIED.**
   Settled by: open `https://authors.aps.org/Submissions/login/new` in your browser.
2. **The literal PRD subject-area / PhySH picker values in the portal.**
   **UNVERIFIED.** §3 gives the published PRD scope list as the proxy and tells
   you what to choose against any plausible dropdown.
3. **Whether the cover-letter field is technically required to submit.**
   **UNVERIFIED.** Irrelevant in practice — §5 supplies one, and APS says the
   cover letter is where referee suggestions go, so you want it regardless.
4. **Whether an empty affiliation field blocks submission.** **UNVERIFIED.**
   Irrelevant in practice — you have an affiliation string (§3).
5. **Whether PRD still offers a print edition to which the colour-figure charge
   could attach.** **UNVERIFIED.** See §7 — the safe behaviour is simply not to
   opt into anything that mentions print.

---

## 2. Portal + account

1. Go to **https://authors.aps.org/Submissions/** (or straight to
   **https://authors.aps.org/Submissions/login/new** for a new account).
2. Create an APS account if you do not have one. APS accounts are shared across
   *Physical Review* journals.
3. **Link ORCID `0009-0008-5616-5994`.** It is *required* for the corresponding
   author (§1) and APS sends an ORCID **verification request shortly after
   submission** — watch `houston@hubify.com` for it. An unverified ORCID will
   generate chasing email.
4. Start a new submission → journal **Physical Review D** → article type
   **Research Article**.

---

## 3. Paste-ready metadata

**Journal:** `Physical Review D` · **Article type:** `Research Article` (no length limit)

**Title:**

```
The Exact Matter-Contraction Non-Gaussian Amplitude: Four-Vertex Derivation and Conditional Large-Scale-Structure Mapping
```

**Author:** `Houston Golden` (sole author, corresponding author)
**Affiliation:** `Independent Researcher, Los Angeles, California, USA`
**Email:** `houston@hubify.com`
**ORCID:** `0009-0008-5616-5994` — **REQUIRED, not optional, for the
corresponding author.**
 · VERIFIED public 2026-07-24 — `pub.orcid.org/v3.0/0009-0008-5616-5994` returns
 HTTP 200, record name "Houston Golden".

**Subject area.** PRD uses **PhySH (Physics Subject Headings)**; PACS is retired
and should not be entered anywhere. The exact portal picker is UNVERIFIED (§1.2),
but PRD's published scope list is verbatim:

> Particle physics experiments · Electroweak interactions · Strong interactions ·
> Lattice field theories, lattice QCD · Beyond the standard model physics ·
> Phenomenological aspects of field theory, general methods · **Gravity,
> cosmology, cosmic rays** · Astrophysics, astronomy, and astroparticle physics ·
> General relativity · Formal aspects of field theory, field theory in curved
> space · String theory, quantum gravity, gauge/gravity duality

- **Primary section: `Gravity, cosmology, cosmic rays`** ✅ recommended. P2's
  headline is a primordial non-Gaussianity amplitude from a contracting
  cosmological phase — this is the section that owns it.
- **Secondary, if offered: `Astrophysics, astronomy, and astroparticle physics`**
  (the SPHEREx multi-tracer bispectrum mapping is the observational half).
- When the portal asks for **PhySH concepts** (a type-ahead search, not a code
  list), search and select terms along these lines, taking whatever PhySH
  actually offers: `Cosmology`, `Primordial non-Gaussianity`, `Early universe`,
  `Cosmological perturbation theory`, `Large-scale structure of the universe`,
  `Bouncing cosmology` (if it exists — if not, `Cosmological models`).
  **Do not invent a PhySH term; pick from what the widget returns.**

**Keywords.** P2's `.tex` carries no `\keywords` macro. If the portal asks for
free keywords, use:

```
primordial non-Gaussianity; matter bounce; contracting universe; cubic action; bispectrum; SPHEREx; scale-dependent bias; cosmological perturbation theory
```

### Abstract — plain text, ready to paste

**Word count: 208.** Cap is **<500** (§1). Comfortable.

**Provenance:** transcribed verbatim from the compiled PDF
`research/focused_paper_source_integration/02_full_draft.pdf`, **v1.7.130**, md5
`f7116fe3e2541d6f649876f2ec7789ee`, 12 pages, dated "July 24, 2026, 18:35 PDT".
Math ASCII-ified for a web form; no wording changed.

> **NOTE — this differs from `WAVE2_P5_SUBMISSION_KIT_2026-07-20.md`.** That kit
> quotes v1.7.126, whose sentence read *"the corresponding rounded arithmetic map
> is 2.63 sigma"*. The current text reads *"the corresponding arithmetic map,
> recomputed with the adopted r = 0.84 convention, is 2.63 sigma"*. **Use the
> block below, not the wave-2 kit's.**
>
> **The v1.7.130 submission-gate bump did NOT touch the abstract.** The block
> below was re-diffed against the v1.7.130 PDF on 2026-07-24 and is the same text
> as under v1.7.129; only the md5, the page count (11 → 12), and the title-block
> stamp moved.
>
> **RE-VERIFY BEFORE PASTING** if P2 moves again — parallel lanes are active. Run
> `md5 -q research/focused_paper_source_integration/02_full_draft.pdf`; if it is
> no longer `f7116fe3e2541d6f649876f2ec7789ee`, re-read the abstract with
> `pdftotext -f 1 -l 1 … - | head -30` and diff against this block.

```
A matter-dominated contracting phase gives a local-type non-Gaussian amplitude
f_NL^local = -35/16 = -2.1875 before the nonsingular transition. We derive this
contraction-phase coefficient for the stated epsilon = 3/2 background and cubic
action by re-summing all four cubic vertices, re-expand the result in the
ordered symmetric basis, and obtain the unique coefficients (3, 1, -9, 5, -33,
9); independent checks use Cai et al.'s order-grouped expressions and Li et
al.'s general-c_s formula. The result corrects the unreproduced printed -35/8
literature value. For orientation only, and conditional on faithful cubic-order
transmission through a specified bounce completion, we map the published
Heinrich et al. SPHEREx multi-tracer bispectrum sensitivity through the exact
shape. Its flat-grid amplitude recovery is r = 0.8354 and shape cosine is
r_cos = 0.9817; the corresponding arithmetic map, recomputed with the adopted
r = 0.84 convention, is 2.63 sigma before additional nuisance marginalization.
A channel-native surrogate-covariance check spans 3.5 sigma with nuisances
fixed, 3.1 sigma after marginalizing the relativistic-projection amplitude
A_GR, 2.3 sigma with an explicit 30% theory prior on the PNG bias-response
coefficient b_phi, and 0.4 sigma when b_phi is free. These values are
illustrative conditional diagnostics, not an observational headline, a new
joint-covariance forecast, or a detection forecast. The primary contribution is
the exact contraction-phase amplitude derivation.
```

---

## 4. What to upload

**One file.**

| Field | Value |
|---|---|
| Path | `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/research/focused_paper_source_integration/02_full_draft.pdf` |
| Version | `v1.7.130` |
| md5 | `f7116fe3e2541d6f649876f2ec7789ee` |
| Pages | **12** (11 before the AI Usage Disclosure section was added; PRD Research Articles have no length limit) |
| Figures | 2 (`fig1_shape_function.png`, `fig5_inflation_comparison.png`) |
| Size | 604,293 bytes |
| Class | `revtex4-2` with `aps,prd` options — **already the journal's own class** |

**Optional but genuinely useful:** APS says LaTeX source *"simplifies
peer-review"* and is preferred. A verified standalone bundle now exists **at the
current version** — `research/focused_paper_source_integration/paper2_arxiv_v1.7.130.tar.gz`,
md5 `dae645a40332d48bb1bbd2124dbe8455`, rebuilt 2026-07-24 and verified by
extract-and-compile in an isolated `/tmp` dir at 0 errors / 0 undefined refs /
12 pages. The version-mismatch objection is gone. **Recommendation is still:
upload the PDF only** — it is explicitly sufficient, it is one less step, and
APS requests source after acceptance anyway. The tarball is there if you want it
or when acceptance comes.

PDF document properties are blank (`pdfinfo` shows empty Title/Author). Cosmetic;
the portal takes metadata from the form.

---

## 5. Cover letter draft

Not stated as mandatory (§1), but **APS says the cover letter is where
recommended and excluded referees go** — so you want one. Paste:

```
Dear Editors,

I am submitting "The Exact Matter-Contraction Non-Gaussian Amplitude:
Four-Vertex Derivation and Conditional Large-Scale-Structure Mapping" as a
Research Article for Physical Review D.

The paper's primary contribution is an exact derivation. For a matter-dominated
contracting phase with epsilon = 3/2, re-summing all four cubic vertices and
re-expanding in the ordered symmetric basis gives the unique coefficients
(3, 1, -9, 5, -33, 9) and the local-type amplitude f_NL^local = -35/16
= -2.1875. This corrects the printed value of -35/8 in the literature, which I
was unable to reproduce. I want to be direct about this: the value being
corrected is from Cai, Xue, Brandenberger and Zhang (JCAP 0905:011,
arXiv:0903.0631), a paper this work otherwise relies on heavily and whose
order-grouped expressions I use as one of two independent checks; the second
check uses the general-c_s formula of Li, Quintin, Wang and Cai
(arXiv:1612.02036). The correction is a coefficient discrepancy, and the
derivation is laid out vertex by vertex so it can be checked line by line.

The observational content is deliberately secondary and is labelled as such
throughout. The mapping of the published Heinrich, Dore and Krause SPHEREx
multi-tracer bispectrum sensitivity through the exact shape is conditional on
faithful cubic-order transmission through a specified bounce completion, and the
paper states plainly that the resulting sigma values are illustrative
conditional diagnostics rather than an observational headline, a new
joint-covariance forecast, or a detection forecast. The per-triangle covariance
of Heinrich et al. is external to this project and unavailable to me; only their
published scalar sensitivity is used. No new observational data are introduced.

RECOMMENDED REFEREES:
1. [Name] — [institution] — [email]
2. [Name] — [institution] — [email]
3. [Name] — [institution] — [email]

EXCLUDED REFEREES: none. I recognise that the natural experts on this amplitude
are the authors of the paper whose coefficient I am correcting, and I have
deliberately neither suggested nor excluded them. If the editors consider them
the right referees, I have no objection.

I am an independent researcher with no institutional affiliation, no grant
funding, and no collaboration behind this work. The manuscript has not been
submitted elsewhere and is not under consideration at another journal. It has
not been posted to arXiv. A permanent public archive of the manuscript, its
exact source, and the analysis scripts is deposited on Zenodo under DOI
10.5281/zenodo.21461881 (concept DOI 10.5281/zenodo.21461880); I mention it for
transparency, as it is a public record of the same text.

Thank you for your consideration.

Houston Golden
Independent Researcher, Los Angeles, California, USA
ORCID 0009-0008-5616-5994
houston@hubify.com
```

**Why the "excluded referees: none" paragraph is there, and why you should keep
it.** The obvious referees for this paper are Cai and Brandenberger, whose
printed coefficient you correct. Excluding them would look like you are avoiding
scrutiny; suggesting them would be strange. Saying out loud that you have done
neither, and that you do not object, is the strongest position available and it
costs nothing. See §8.

**Do not** claim an institution, grant, collaborator, or endorsement. There is
none.

---

## 6. Data Availability Statement — MANDATORY, entered at the portal

PRD has required a DAS since **4 September 2024**, and it is entered as a
**submission-server Q&A**, separate from the in-paper section (§1). Also note:
*"Publicly shared data and software must be cited in the reference list, and the
citation must be included in the data availability statement."*

Paste this into the DAS field:

```
No new observational or experimental data were generated in this study. All
results are analytic or derived from published values. The analysis code and
numerical artifacts supporting the findings are openly available in the project
repository at https://github.com/Hubify-Projects/bigbounce. An immutable
versioned archival deposit of the reviewed release -- the manuscript PDF, the
LaTeX source, the submission bundle, a tracked-provenance archive, and
SHA-256 checksums -- is published on Zenodo under DOI
10.5281/zenodo.21461881 (concept DOI 10.5281/zenodo.21461880, which resolves to
the latest deposited version). Specifically: the exact vertex certification is
implemented in scripts/p2_vertex_check.py; the exact shape and overlap artifact
is generated by scripts/exact_shape_analysis.py; the real- and redshift-space
Fisher checks are in scripts/c13_independent_bounce_fisher.py and
scripts/c14_rsd_multipole_fisher.py; and the channel-native nuisance ladder is
generated by scripts/c15_channel_native_fisher.py. The per-triangle covariance
of Heinrich et al. [Phys. Rev. D 109, 123511 (2024)] is external to this project
and is not available here; only its published scalar sensitivity is used in the
illustrative mapping.
```

**DOI verified this session:** `https://doi.org/10.5281/zenodo.21461881` follows
to `https://zenodo.org/records/21461881` with final **HTTP 200**.

> **One thing to check in the portal.** APS requires that shared data/software
> *"be cited in the reference list"*, not only linked. P2's compiled reference
> list does not currently carry a `\bibitem` for its own Zenodo deposit (the
> deposit appears in the Data and Code Availability prose). This is a
> copy-editing-stage matter, not a submission blocker, but if the DAS form has a
> "data citation" sub-field, put the full Zenodo citation there:
> *H. Golden, "The Exact Matter-Contraction Non-Gaussian Amplitude" (dataset and
> software), Zenodo (2026), doi:10.5281/zenodo.21461881.*

---

## 7. Cost — what you will actually be charged

| Item | Cost |
|---|---|
| Account | $0 |
| **Submission** | **$0** — no submission fee published |
| **Publication, subscription route** | **$0** |
| Publication, optional CC-BY gold OA | **$2,910 USD** (APS's table, explicitly labelled *2026 APC (USD)*) |
| Colour figures **in print** | $1,090 first + $595 each additional |
| Free OA via SCOAP³ | Applies only to hep-primary arXiv postings — **not this paper** (P2 would be `astro-ph.CO`/`gr-qc`, and it is not on arXiv) |

**Recommendation: take the subscription route. $0.** The manuscript is already
permanently and freely readable under its Zenodo DOI, so $2,910 buys visibility
you largely have. If open access matters to you for this paper specifically, that
is a real preference — but decide it deliberately, not at a payment screen.

**Watch for this at the portal:** APS will present the CC-BY election during
submission and again after acceptance (payments run through SciPris™, with a link
sent on acceptance). Declining OA is not a downgrade and does not affect review.

**On the colour-figure charge:** the quoted charge is for colour **in print**.
P2 has two colour figures. Whether PRD still has a print edition that could
trigger this is **UNVERIFIED** (§1.2). **Practical rule: do not opt into anything
labelled "print" or "colour in print." If a charge appears anywhere on the
confirmation screen, stop and read it before submitting** — an unexpected $1,090
is exactly the surprise this section exists to prevent.

---

## 8. Suggested and excluded referees — and the endorser conflict

APS takes both **in the cover letter** (§1), and is *"not bound by these
suggestions."*

### The conflict, and why P2 is the sharp case

`project-context/SSOT/ENDORSER_SHORTLIST_2026-07-22.md` names people being
approached separately for **arXiv endorsement**. Two of them —
**Yi-Fu Cai** (Tier 1, clears all four codes) and **Robert Brandenberger**
(Tier 2) — together with **Wei Xue** are the authors of arXiv:0903.0631, **the
paper whose printed coefficient P2 corrects**, and they are the single most
natural referee pool for this manuscript.

**That collision is real and it is specific to P2.** Three separate hazards:

1. **Endorser-and-referee.** If Houston asks Cai to endorse him on arXiv *and*
   names Cai as a suggested PRD referee, the endorsement becomes leverage and the
   referee report becomes compromised. Both are on the record in writing.
2. **Suggesting the author you are correcting.** Even setting the endorsement
   aside, naming as your preferred referee the person whose number you say is
   wrong is a strange move — it either reads as naive or as an attempt to force a
   confrontation the editor should be choosing.
3. **Excluding the author you are correcting.** Equally bad in the other
   direction: it reads as avoiding the one person best placed to check you, on a
   paper whose entire claim is "this published coefficient is wrong."

### Recommendation — and it is a firm one

**Name none of Cai, Brandenberger, or Xue in either box, and say so explicitly in
the cover letter (§5 already does).** Neither suggest nor exclude them; state
that you have deliberately done neither and have no objection if the editors
choose them. This is honest, it is defensible if anyone ever compares the two
paper trails, and it leaves the editor's judgment intact — which is where the
decision belongs.

**Keep Cai and Brandenberger in the endorser lane only.** Under the acceleration
audit's own finding, arXiv is not on the critical path for any of these six
papers — so if you ever had to choose, the referee lane is worth more than the
endorsement. But you do not have to choose: the recommendation above costs you
nothing in either lane.

**Sequencing note.** If you have already sent an endorsement request to Cai or
Brandenberger, nothing above changes — you still name neither here. If you have
*not* yet sent one, there is no reason to hold it up on P2's account; the two
processes stay clean as long as no name appears in both.

### Suggested referees — candidates drawn from P2's own reference list

Grounded in the manuscript's own bibliography, so their relevance is a matter of
record. **I did not verify any individual's current affiliation, email, or
availability** — check each on their institutional page. **None is on the
endorser shortlist**; re-check before you paste.

| Candidate | Why they fit | Basis | Conflict check |
|---|---|---|---|
| **David Wands** | Wrote the duality-invariance result that underpins scale-invariant contracting-phase spectra, and a review of local non-Gaussianity from inflation — spans both halves of P2 | P2 refs. [5], [9] | Not on the endorser shortlist. Independent of arXiv:0903.0631. |
| **Edward Wilson-Ewing** | *"The matter bounce scenario in loop quantum cosmology"* — a matter-bounce expert with no stake in the corrected coefficient | P2 ref. [12] | Not on the shortlist. Clean. |
| **Leonardo Senatore** | Non-Gaussianity in single-field inflation and its optimal observational limits — strong on the cubic-action machinery and on what a σ number does and does not mean | P2 ref. [16] | Not on the shortlist. Clean. |
| **Jérôme Quintin** | Co-author of the general-c_s formula P2 uses as its second independent check — arguably the best-placed person alive to check the re-derivation | P2 ref. [8] | Not on the shortlist — **but he is a co-author with Cai on ref. [8].** That is not a conflict with *you*, but it sits adjacent to the corrected paper. **Rank him third or fourth, not first.** |

**Recommendation:** suggest **Wands, Wilson-Ewing, Senatore** — three names, all
on-topic, all independent of both the endorser shortlist and the corrected paper.
Three is the right number; a longer list looks like you are trying to steer.

### Excluded referees

**Recommendation: none, stated explicitly** (§5's letter does this). You have no
adversary, and the one exclusion you might be tempted to make is precisely the one
that would look worst.

---

## 9. Pre-submission checklist

| # | Must be true | Status 2026-07-24 |
|---|---|---|
| 1 | Compiled PDF exists, clean | ✅ **v1.7.130**, md5 `f7116fe3e2541d6f649876f2ec7789ee`, **12 pp** (was 11; the AI Usage Disclosure section added one — PRD Research Articles have no length limit), 2 figures. 0 undefined refs, **0 overfull hboxes**; page 1 and the changed pages 7–8 rendered and visually checked for revtex column overflow — clean. |
| 2 | ORCID resolves publicly (**required by APS**) | ✅ **VERIFIED 2026-07-24** — HTTP 200, "Houston Golden" |
| 3 | ORCID in the manuscript | ✅ **NOW PRESENT** in v1.7.130 — `\altaffiliation` footnote on the author block, rendering as "ORCID: 0009-0008-5616-5994" beside the email footnote on page 1. Still enter it at the portal as well; that is the binding requirement. |
| 4 | Abstract under 500 words | ✅ **208 words** |
| 5 | Zenodo DOI 10.5281/zenodo.21461881 resolves | ✅ **VERIFIED 2026-07-24** — HTTP 200 at `zenodo.org/records/21461881` |
| 6 | DAS text prepared for the portal Q&A | ✅ §6 |
| 7 | Companion citation no longer prints "(in preparation)" | ✅ **FIXED.** The compiled reference [14] now reads *"H. Golden, Algebraic Cartan Elimination in Minimal Einstein–Cartan–Holst Gravity…, Zenodo 10.5281/zenodo.21481838 (2026), Companion paper (Paper I A), publicly archived on Zenodo… it is not an arXiv preprint and the paper is not peer reviewed."* Honest and current. |
| 8 | **AI-usage disclosure present** | ✅ **CLOSED in v1.7.130 — see §9.1** for the text that shipped. Verify: `pdftotext research/focused_paper_source_integration/02_full_draft.pdf - \| grep -c "AI USAGE DISCLOSURE"` → 1. |
| 9 | **Deposit-lag sentence factually correct** | ✅ **CLOSED in v1.7.130 — see §9.2.** Fixed by computation, not by a new literal, so it cannot go stale again. |
| 10 | Zenodo deposit cited in the reference list | ⚠️ Not as a `\bibitem`; it appears in the DAS prose. APS asks for a reference-list citation of shared data. Copy-editing-stage item; §6 tells you where to put it at submission. |
| 11 | Cover letter with referee paragraph drafted | ✅ §5 — **fill in three referee lines before pasting** |
| 12 | No name appears in both the endorser shortlist and the referee box | ✅ by construction (§8) — re-check before pasting |
| 13 | APS account exists, ORCID linked | ⬜ **HOUSTON-ONLY** — this kit creates no accounts |
| 14 | Subscription-vs-$2910-CC-BY decision made | ⬜ **HOUSTON-ONLY** — recommendation: subscription ($0), §7 |
| 15 | Not under consideration elsewhere | ✅ P2 has been submitted nowhere |
| 16 | Source-file upload decision | ✅ recommendation: PDF only (§4). The tarball has been rebuilt at the current version — `research/focused_paper_source_integration/paper2_arxiv_v1.7.130.tar.gz`, md5 `dae645a40332d48bb1bbd2124dbe8455`, extract-and-compile verified in an isolated `/tmp` dir at 0 errors / 0 undefined refs / 12 pages — so it is no longer behind the PDF if APS asks for source post-acceptance. |

### 9.1 The AI-disclosure item — CLOSED in v1.7.130

**What APS actually requires** (re-verified live 2026-07-24 by the lane that made
the fix, through the same origin-reporting text proxy; `journals.aps.org` returns
HTTP 403 to direct automated fetch and that Cloudflare challenge was **not**
solved). From `https://journals.aps.org/authors/appropriate-use-ai-tools`:

- *"Authors must keep a record of any AI use and disclose any substantive uses in
  the submitted paper"*
- disclosure should state *"AI tool name and version · How the AI assisted · How
  the authors directed and verified the AI output"*
- *"Any AI used to conduct the actual research (e.g., data analysis) must, like
  any tool, be disclosed within the paper's methods section."*
- *"Authors are not required to disclose the use of AI to polish, condense, or
  otherwise lightly edit the text."* — the only exemption
- *"An AI program cannot be held accountable and cannot be listed as an author."*

**What shipped.** A `\section*{AI Usage Disclosure}` placed immediately after
Data and Code Availability — deliberately in the body rather than after the
appendices, because APS wants research-conducting AI disclosed in the methods,
not in a back-matter note. It renders on **page 8** of the v1.7.130 PDF. Two
paragraphs: the first says what the AI did, the second says what stayed with the
author.

The disclosure is **deliberately full rather than minimised.** An understated
disclosure that a referee could disprove from this repository's public commit
history would be far worse than a complete one. The model names and versions are
the ones actually on the record for *this* paper — Claude Opus-4 family; Grok-4
and Grok-4.3 and Gemini 2.5 Pro / 3.1 Pro from
`project-context/peer-reviews/INT_v3/ROUND_*-P2-*`; ChatGPT from
`project-context/peer-reviews/EXT_real/P2_*chatgpt*` — not copied from a sibling
paper. Tone and specificity match P1B's existing `\section{AI Usage Disclosure}`
and P3/P4/P5's AI-assisted-methodology paragraphs, so the six papers now read as
one consistent disclosure practice.

**Verify:**
```bash
pdftotext research/focused_paper_source_integration/02_full_draft.pdf - \
  | grep -c "AI USAGE DISCLOSURE"        # → 1
```

### 9.2 The "one patch line ahead" misstatement — CLOSED in v1.7.130

**What it said** (v1.7.129, Data and Code Availability):

> *"That deposit archives the reviewed v1.7.125 release PDF and source (the exact
> bytes reviewed); the present manuscript is v1.7.129, **one patch line ahead**;
> current and subsequent versions will be added to the same Zenodo record on the
> next re-stage."*

v1.7.125 → v1.7.129 is **four** patch releases, not one — the sentence
contradicted itself in the same clause, printing both version numbers and then
mis-stating their difference. This was the acceleration audit's action #5
(pattern-047, "closures repair the exact string a reviewer quoted, and the
adjacent literal survives") recurring in P2 *after* the 2026-07-23 closure meant
to end it: that closure bound the **manuscript** half to `\paperVersion` but left
the **relationship** as a hardcoded English literal.

**How it was fixed — by computation, not by a new literal.** Writing "four patch
releases ahead" would have been the same bug with a different number. Instead:

- `\paperVersion` and `\depositVersion` are the only two places a version string
  is written (`\depositVersion`'s ground truth is `.deposit-staging/P2/v1.7.125/`);
- `\patchOf{}` parses the trailing patch integer out of each;
- `\depositRelation` computes the delta with `\numexpr` and emits the **entire
  clause, including its tense** — with zero / singular / plural branches, so
  "will be added on the next re-stage" cannot survive the re-stage that fulfils
  it, and a zero delta prints "the present manuscript is that same archived
  release" instead of a lag.

This is **the same construction P3 already uses**
(`pipelines/p3_anomaly_engine/paper3_apjs.tex`), adopted rather than reinvented,
so there is one pattern across the portfolio and not two.

**What it renders as today** (v1.7.130 PDF, pages 7–8):

> *"That deposit archives the reviewed v1.7.125 release PDF and source (the exact
> bytes reviewed at that release); the present manuscript is v1.7.130, 5 patch
> releases ahead, and will be added to the same Zenodo record as a new version on
> the next re-stage."*

A stale literal is now unrepresentable in this paragraph.

---

## 10. What happens after you click

**Timeline (APS's own 2025 medians for PRD, §1):**

| Milestone | PRD median, 2025 |
|---|---|
| First decision **before** review (desk) | **3 days** |
| First decision **after** review | **41 days** |
| Submission → acceptance | 86 days |
| Submission → publication | 115 days |

So: about **three days** to know whether it reached referees, and about **six
weeks** to a first substantive report. That is fast, and it is the strongest
practical argument for putting P2 in first.

**Immediately after submitting:** watch `houston@hubify.com` for the **ORCID
verification request** — APS sends it *"shortly after submission"* and it is a
required step, not a courtesy. Also expect automated integrity/plagiarism
screening (§1); nothing to do, but do not be alarmed by a notice about it.

**Review model:** single-anonymized — the referees know who you are, you do not
know them.

**When the decision arrives — what to update in the repo:**

| Outcome | Repo surfaces to update |
|---|---|
| **Any decision** | `project-context/SSOT/paper-2/status.md` — venue, submission date, APS manuscript number, decision verbatim. This closes the file's long-standing *"Next gate: Houston venue / human-referee decision"* line. Add a `reviewTimeline.ts` entry under `site/src/data/` **in the same commit** (standing directive: review-round site sync). Update `project-context/SSOT/index.md` and `queue.md`. |
| **Referee reports** | Save each report's complete raw text under `project-context/peer-reviews/` **before** recording any verdict, and truth-audit every finding with a source-cited disposition before closing it. These are real human referees at the venue the paper was written for — their findings outrank every LLM verdict in the programme's history, and they should be handled with more care, not less. |
| **Revision requested** | Revise `research/focused_paper_source_integration/02_full_draft.tex` under directive G: bump `\paperVersion`, recompile 0-undef-ref, re-mirror the PDF to `public/papers/` and `site/public/` byte-identically, bump Convex `paperVersions` with the real new md5/page count, and re-stage the Zenodo deposit so §9.2's lag sentence becomes true rather than being reworded again. |
| **Accept** | APS requests **source files** post-acceptance (§1) — rebuild the bundle at the accepted version. Add the journal reference to the Zenodo record metadata. Sync Convex (`activityFeed:add`, `papers:*`) — static `papers.ts` alone does not reach the live site (standing directive A). Under directive P this closes a *publishing-phase* row and does not move a readiness score. |
| **Reject** | Record the reason verbatim; do not soften it. If it is scope rather than correctness, the natural sibling venues are *JCAP* (where both arXiv:0903.0631 and arXiv:1612.02036 were published — arguably the paper's true home community) or *Physical Review D* as a Letter after compression. Open it as a queue row; a PRD rejection is a routing outcome, not a science failure, and must not lower a readiness figure. |

---

*Kit prepared 2026-07-24 against git HEAD `ef9993f2`. Every venue requirement
re-fetched live from APS this session through an origin-reporting text proxy;
the Cloudflare bot challenge on `journals.aps.org` was not solved and no
bot-detection was bypassed. Items that could not be confirmed from an official
page are labelled UNVERIFIED in §1.2 with the check that would settle them.
Nothing was submitted, no account was created, and no email was sent.*
