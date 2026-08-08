# CQG Submission Kit — P1A → *Classical and Quantum Gravity* (IOP), article type **Note**

**Prepared 2026-07-24** · git HEAD at prep time `ef9993f2` · venue requirements
**re-fetched live from IOP's own pages on 2026-07-24** (not inherited from the
acceleration audit — every quote below was independently retrieved this session).

**Goal:** an 11pm click session. Everything you must type or paste is in §3–§6.
Everything you must *decide* is called out with a recommendation.

> ### ✅ GATE 0 — CLOSED 2026-07-24 in **v1A.0.127**
> The compiled Note now carries an Acknowledgments section with all three
> IOP-mandatory declarations. Verified on the served PDF:
> `pdftotext arxiv/paper1a_ech_nogo.pdf -` returns **2** hits for "acknowledg",
> **1** for "competing interests", **1** for "funding", **1** for
> "generative-ai", and **1** for `0009-0008` (ORCID, now in the author block
> too).
>
> **What was wrong:** the entire Acknowledgments block sat inside
> `\begin{comment}…\end{comment}` at `arxiv/paper1a_ech_nogo.tex:4043` onward and
> never compiled, so the Note had no COI, no funding, and no AI statement —
> all three unconditionally mandatory at IOP (quotes in §1).
>
> **What was done:** a **new, Note-scoped** acknowledgments block was written
> and placed immediately before Data and Code Availability (per IOP's own advice
> that the data statement follow the acknowledgements). The old commented block
> was **deliberately not restored** — it thanks the Planck/CMB-S4/LiteBIRD/LSST/
> DESI collaborations and Lior Shamir for galaxy-spin counts and cites frozen
> MCMC chains, none of which this Note uses, and it sits inside a comment region
> that also holds `\subsection{Discrimination Among Bouncing Cosmologies}`,
> tables, and two appendices cut to keep the Note at 8 pages. All of that stays
> commented. **The Note is still 8 pages.**
>
> **Current bytes:** v1A.0.127, md5 `0bc1ee72836c867114118521cf86e1c2`, 8 pages,
> dated "July 24, 2026, 18:35 PDT". Mirrored byte-identical to 8 served paths;
> Convex `paperVersions` row `k571vp9b8j3sby5tb148sxvr218b7j3g`.
>
> **The abstract was not touched** — see §9 item 4 for the verified count.
>
> This kit is ready to execute end to end.

---

## 0. TL;DR

```
1. GATE 0 already closed in v1A.0.127 — re-confirm with §9 item 1 if you like
2. Create a ScholarOne account at mc04.manuscriptcentral.com/cqg-iop        (§2)
3. New submission → article type "Note" → paste §3 metadata
4. Upload ONE PDF: arxiv/paper1a_ech_nogo.pdf                              (§4)
5. Paste the cover letter (§5) and the data-availability statement (§6)
6. Elect the SUBSCRIPTION (free) route — NOT gold OA                        (§7)
7. Suggested referees: §8. Do NOT name anyone from the endorser shortlist.
8. Submit.
```

**Cost: £0.** **arXiv: not required.** **Format conversion: none — revtex4-2
ships as-is.**

---

## 1. The venue's actual requirements — verified live 2026-07-24

Every row was re-fetched this session. Quotes are verbatim.

| Requirement | Verbatim governing sentence | Source URL |
|---|---|---|
| **Portal** | *"Continue to article submission"* → `https://mc04.manuscriptcentral.com/cqg-iop` | https://iopscience.iop.org/journal/0264-9381/page/submission-options |
| **Account** | *"If you are a new author, you will need to set up an account before submitting your first article."* | https://publishingsupport.iopscience.iop.org/questions/how-to-submit-your-journal-article/ |
| **Article type "Note"** | *"brief articles that make a short, interesting point, which would not normally merit publication as a full Paper but still make a useful and novel addition to the literature."* | https://publishingsupport.iopscience.iop.org/journals/classical-and-quantum-gravity/about-classical-quantum-gravity/ |
| **Note length limit** | **None published.** The general guidelines page says only *"Some of our journals have guidelines for the maximum recommended length for each different type of article"* and defers to the About page, which publishes no number for any CQG type. Verified-by-absence on both governing pages. | https://publishingsupport.iopscience.iop.org/journals/classical-and-quantum-gravity/ |
| **arXiv / preprint** | *"authors are permitted to share a Preprint of their article anywhere at any time."* Permitted — never required, and no sentence requires declaring one at submission. | https://publishingsupport.iopscience.iop.org/preprint-pre-publication-policy/ |
| **Initial format** | *"You can format your paper in the way that you choose!"* and *"When submitting a new article, we only require you to upload a single PDF file (and any relevant supplementary data)."* `iopart.cls` is never stated as mandatory at any stage. | https://publishingsupport.iopscience.iop.org/journals/classical-and-quantum-gravity/ |
| **Source files** | Required only **at revision**: *"The latest set of source files, e.g. TeX/LaTeX files or a single Word file (which includes figure/table captions) and individual figure files."* | https://publishingsupport.iopscience.iop.org/questions/what-files-to-submit-at-revision-stage/ |
| **⚠️ Abstract cap — 300 words** | *"The abstract should not normally be more than 300 words. If you submit an article with an abstract longer than 300 words, we may rescind the manuscript and ask you to re-write it."* | https://publishingsupport.iopscience.iop.org/journals/classical-and-quantum-gravity/ |
| **Cost — subscription** | *"Publication on a subscription-access basis is free of charge."* | https://publishingsupport.iopscience.iop.org/journals/classical-and-quantum-gravity/about-classical-quantum-gravity/ |
| **Cost — optional gold OA** | Table reads *"Article publication charge* £2530 €2905 $3490"* (excluding VAT where applicable) | same page |
| **COI — MANDATORY** | *"All authors and co-authors are required to disclose any potential conflicts of interest when submitting their article. Any conflicts of interest should be included in an acknowledgements section."* | https://publishingsupport.iopscience.iop.org/ethical-policy-journals/ |
| **Funding — MANDATORY** | *"IOP Publishing requires all authors to declare any funding they received related to the research article they are submitting for publication."* Portal-side: *"provide information on all funders associated with your work."* | same page + how-to-submit page |
| **Generative AI — MANDATORY when used** | *"If authors use generative AI tools for any of the tasks listed above, they must disclose this usage in the Acknowledgements section of their manuscript. This disclosure should list the model and version of the generative AI tool and how it was used in the work."* | https://publishingsupport.iopscience.iop.org/ethical-policy-journals/ |
| **Data availability — encouraged, not mandatory** | *"Authors are encouraged to share research data and encouraged to provide data availability statements but are not required to."* Placement: *"Authors are advised to place the data availability statement in a dedicated section of the manuscript after the acknowledgements under the heading 'Data availability'."* | https://publishingsupport.iopscience.iop.org/iop-publishing-standard-data-policy/ |
| **ORCID — recommended** | *"During the submission process, we recommend you supply ORCID identifiers for all authors to avoid ambiguity."* | https://publishingsupport.iopscience.iop.org/journals/classical-and-quantum-gravity/ |
| **Suggested / opposed referees — offered, optional** | *"You may also propose preferred (and non-preferred) reviewers on submission."* And: *"Authors are welcome to suggest reviewers for their paper if they wish but this is not required, and we are not obliged to use author suggested reviewers. In the interests of impartiality, if an author-suggested reviewer is used then we will complement this with a review from a second referee chosen by the journal from the general reviwer pool."* (sic — IOP's typo) | how-to-submit page; https://publishingsupport.iopscience.iop.org/questions/how-iop-selects-journal-reviewers/ |
| **Cover letter — optional** | *"Any pertinent information that could affect the way the manuscript is handled may be provided in a cover letter."* No sentence makes it required. | how-to-submit page |
| **Classification** | Free keywords, **no PACS**: *"When you submit an article, you will be asked to supply some keywords relevant to your work."* | CQG guidelines page |
| **Speed** | *"Submission to first decision before peer review: 6 days"*; *"Submission to first decision after peer review: 54 days"*; *"Desk rejection rate: 63%"*; *"Acceptance rate: 21%"* | https://iopscience.iop.org/journal/0264-9381/page/About_the_journal |
| **Independent / unaffiliated author** | No page conditions submission on institutional affiliation. Subscription route is free, so no funding is needed. | absence across all fetched pages |

### Items I could NOT verify — stated plainly

1. **The exact ScholarOne subject-category picker for CQG.** It lives inside the
   logged-in wizard; the public pages publish only the journal's scope areas
   (§3). **UNVERIFIED.** Settled by: log in, Step 1, read the dropdown. §3 gives
   the right answer for every plausible list.
2. **Whether the ScholarOne author-institution box is a required field.**
   **UNVERIFIED.** If it is, type `Independent Researcher` — §3 has the exact
   string. This is not an obstacle, only an unknown.
3. **Whether the £2530 gold-OA figure has a price-year label.** The About page
   prints no effective date. **UNVERIFIED** — irrelevant if you take the free
   subscription route, which is the recommendation.
4. **Which of IOP's data-policy variants CQG applies.** The standard policy says
   *"The 'about the journal' section on each journal's website will confirm which
   research data policy applies"* and five permitted verbatim DAS forms exist that
   I could not extract. **UNVERIFIED.** Settled by: read the "Research data"
   heading on the CQG About page and, if it names a set form, use that form
   verbatim instead of §6's draft. Low risk — the policy is "encouraged, not
   required".
5. **Whether the 6/54-day metrics are current.** A parallel ISSN listing
   (`iopscience.iop.org/journal/1361-6382`) surfaced with 8/63 days and was not
   fetched. **UNVERIFIED at one-day granularity**; the order of magnitude is not
   in doubt.

---

## 2. Portal + account

1. Go to **https://iopscience.iop.org/journal/0264-9381/page/submission-options**
2. Click **"Continue to article submission"** → lands on
   **https://mc04.manuscriptcentral.com/cqg-iop**
3. **Create an account** (first-time authors must — quoted in §1). ScholarOne
   accounts are per-publisher; a ScholarOne account for another publisher will
   not carry over.
4. In the account profile, add ORCID **0009-0008-5616-5994** if it offers ORCID
   linking. This satisfies §1's ORCID recommendation at the portal level even if
   the manuscript itself carries no ORCID line.

---

## 3. Paste-ready metadata

**Article type:** `Note`

**Title** (paste exactly; ScholarOne title fields are plain text — the en-dashes
render fine, but if the field mangles them use hyphens):

```
Algebraic Cartan Elimination in Minimal Einstein-Cartan-Holst Gravity: Spin-Sourced Contact and Zero-Spin Scalar Branches
```

**Author:** `Houston Golden` (sole author, corresponding author)
**Affiliation:** `Independent Researcher, Los Angeles, California, USA`
**Email:** `houston@hubify.com`
**ORCID:** `0009-0008-5616-5994`
 · VERIFIED public 2026-07-24 — `pub.orcid.org/v3.0/0009-0008-5616-5994` returns
 HTTP 200, record name "Houston Golden".

**Subject area / scope selection.** CQG publishes these scope areas: classical
general relativity; applications of relativity; experimental gravitation;
cosmology and the early universe; quantum gravity; supergravity, superstrings and
supersymmetry; mathematical physics relevant to gravitation.
- **Primary: `Classical general relativity`** ✅ recommended. The Note's two
  results are both classical, on-shell statements about the algebraic Cartan
  equation in a first-order gravity action. Neither is a quantum-gravity result.
- **Secondary (if the wizard allows a second): `Quantum gravity`** — the Holst
  term and the Immirzi parameter are the loop-quantum-gravity community's
  furniture, and the two Benedetti–Speziale references are that literature. Pick
  `Mathematical physics relevant to gravitation` instead if the wizard offers
  only one secondary and you would rather signal formal rather than QG audience.
- Do **not** pick `cosmology and the early universe`. The Note explicitly makes
  no cosmological prediction, and the abstract says so ("no ECH dark-energy or
  birefringence prediction is made"). Choosing it invites a referee who expects a
  cosmology result and finds none.

**Keywords** (taken verbatim from the manuscript's own `\keywords` macro,
`arxiv/paper1a_ech_nogo.tex:1335` — six free keywords, no PACS):

```
Einstein-Cartan gravity; Holst action; algebraic torsion; four-fermion interaction; NJL model; perturbation transparency
```

### Abstract — plain text, ready to paste

**⚠️ WORD COUNT: 285 words for this paste block (whitespace tokens). The cap is
300, and IOP says they *"may rescind the manuscript"* above it. Re-verified
2026-07-24 against the v1A.0.127 PDF; the manuscript-native count is 269 words
with each inline math expression counted as one word, and the most pessimistic
convention (naive tokenization of raw `pdftotext`, which splits rendered math)
gives 295. Under the cap on every convention — but with 5 words of headroom in
the worst case, do not add a single sentence to this block.**

**Provenance:** transcribed verbatim from the compiled PDF
`arxiv/paper1a_ech_nogo.pdf`, **v1A.0.127**, md5
`0bc1ee72836c867114118521cf86e1c2`, 8 pages, dated "July 24, 2026, 18:35 PDT".
Math has been ASCII-ified for a web form; no wording changed.

> **The GATE-0 fix landed and did NOT touch the abstract.** The block below was
> re-diffed against the v1A.0.127 PDF on 2026-07-24 and is byte-for-byte the same
> text as under v1A.0.126; only the md5 and the title-block stamp moved.
>
> **RE-VERIFY BEFORE PASTING** if P1A moves again: run
> `md5 -q arxiv/paper1a_ech_nogo.pdf`; if it is no longer
> `0bc1ee72836c867114118521cf86e1c2`, run
> `pdftotext -f 1 -l 1 arxiv/paper1a_ech_nogo.pdf - | head -40` and diff the
> abstract against the block below before submitting.

```
We consolidate two standard consequences of the same algebraic Cartan equation
in minimal Einstein-Cartan-Holst (ECH) gravity. On the spin-sourced branch,
eliminating the non-propagating connection gives the minimal axial-axial contact
interaction -(3 kappa/16)[gamma^2/(1+gamma^2)] J_5^2. A deliberately elevated
homogeneous normalization illustrates only its scale: kappa n_psi^2 / rho_Lambda
= 3.6e-69 (n_psi/100 cm^-3)^2. This coefficient-one dimensional benchmark omits
the actual contact factor 3/16 and the finite-Holst factor gamma^2/(1+gamma^2);
number density also does not fix the state-dependent renormalized composite
<J_5^I J_5I>, a vacuum stress tensor, or an equation of state. In the declared
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
counterparts for matched background and initial data and boundary data with
standard falloff, so the first-order variational surface contribution vanishes.
Equality of right- and left-helicity solutions additionally requires matched
parity-symmetric initial data. This on-connection-shell statement is not an
off-shell equality of the original first-order actions and excludes
quantum/anomaly, non-minimal, propagating-torsion, and nontrivial
global/topological sectors.

The identities used here are standard. The contribution is their
convention-audited consolidation into the two Cartan branches and the sharply
bounded dimensional coefficient benchmark above; no ECH dark-energy or
birefringence prediction is made.
```

> **Judgment call for you:** if ScholarOne's own counter reports >300 (different
> counters treat `-(3 kappa/16)[gamma^2/(1+gamma^2)]` differently), the cheapest
> honest cut is the final paragraph's first sentence — "The identities used here
> are standard." (5 words) — and, if still over, compressing the middle sentence
> of paragraph 1. **Do not cut a caveat.** Every "does not exclude / does not
> fix / is not" clause is load-bearing honesty that survived nine review rounds.

---

## 4. What to upload

**One file. That is all CQG wants at initial submission.**

| Field | Value |
|---|---|
| Path | `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/arxiv/paper1a_ech_nogo.pdf` |
| Version | `v1A.0.127` **(GATE-0 fix landed 2026-07-24)** |
| md5 | `0bc1ee72836c867114118521cf86e1c2` |
| Pages | **8** (unchanged — the Note-scoped declarations block did not add a page) |
| Figures | 0 |
| Size | 362,791 bytes |
| Page size | US Letter (612 × 792 pt) — fine; IOP does not mandate A4 at initial submission |
| Class | `revtex4-2` — **no conversion needed**, format-free per §1 |

Do **not** upload the `.tex`, `.bbl`, or the arXiv tarball. Source files are a
revision-stage requirement (§1). Uploading them now is harmless but adds a step.

**PDF document properties are blank** (`pdfinfo` shows empty Title and Author).
Cosmetic; ScholarOne takes title/author from the form, not the PDF metadata. Not
a blocker.

---

## 5. Cover letter draft

Cover letters are **optional** at IOP (§1) but cheap and useful here, because
three things are worth saying to the editor before the desk-rejection decision:
the article type is deliberate, the author is unaffiliated, and the manuscript is
already publicly archived. CQG's desk-rejection rate is **63%** — this letter is
your one chance to pre-empt the two most likely desk objections (wrong article
type; "what is the new result?").

Paste into the cover-letter field:

```
Dear Editors,

I am submitting the manuscript "Algebraic Cartan Elimination in Minimal
Einstein-Cartan-Holst Gravity: Spin-Sourced Contact and Zero-Spin Scalar
Branches" for consideration as a Note in Classical and Quantum Gravity.

The manuscript makes a deliberately narrow point. Both results follow from the
same algebraic Cartan equation in the minimal Einstein-Cartan-Holst action, and
both identities are individually standard in the literature. What the Note
contributes is their convention-audited consolidation into the two branches of
that one equation: on the spin-sourced branch, the minimal axial-axial contact
interaction with its explicit 3/16 and finite-Holst factors together with a
sharply bounded dimensional benchmark; and on the zero-spin branch, the
statement that the on-connection-shell reduced action is the Einstein-scalar
action, with the conditions under which that equality holds set out explicitly.
I have tried to be exact about what is not claimed: the Note makes no
Einstein-Cartan-Holst dark-energy or birefringence prediction, and the scalar
Fierz sign result is stated as conditional on the declared direct-channel,
hard-cutoff, mean-field convention.

I have chosen the Note article type because the point is short and does not
merit a full Paper, and because the value of the result is in fixing
conventions that are easy to get wrong rather than in opening a new line of
work. If the editors judge the length better suited to a full Paper, I am happy
to be redirected.

I am an independent researcher with no institutional affiliation, no grant
funding, and no collaboration behind this work. The manuscript has not been
submitted elsewhere and is not under consideration at another journal. It has
not been posted to arXiv. A permanent public archive of this manuscript and its
exact source, together with the two algebraic-check scripts, is deposited on
Zenodo under DOI 10.5281/zenodo.21481838 (CC-BY-4.0); I mention this for
transparency, as it is a public record of the same text.

Thank you for your consideration.

Houston Golden
Independent Researcher, Los Angeles, California, USA
ORCID 0009-0008-5616-5994
houston@hubify.com
```

**Do not** add a claimed institution, grant, collaborator, or endorsement. There
is none, and the letter is stronger for saying so plainly.

---

## 6. Data availability answer

IOP's data policy is *encouraged, not required* (§1), and the manuscript already
carries a live **Data and Code Availability** subsection
(`arxiv/paper1a_ech_nogo.tex:4025`) which compiles into the PDF. If the portal
also asks for a DAS in a form field, paste:

```
The algebraic checks reported in this Note are committed as
fierz_lemma_check.py and njl_gap_equation_route1.py in the public repository
https://github.com/Hubify-Projects/bigbounce, frozen at immutable commit
7befce143848b925998a3e6ecc850aa510ab3a94. The manuscript, its exact LaTeX
source, the check scripts, and a provenance manifest are permanently archived
on Zenodo under DOI 10.5281/zenodo.21481838 (CC-BY-4.0, deposited 21 July
2026). No new observational or experimental data were generated or analysed;
all results are analytic, and no companion computation is required for either
action-level result.
```

**DOI verified this session:** `https://doi.org/10.5281/zenodo.21481838` follows
to `https://zenodo.org/records/21481838` with final **HTTP 200**.

**UNVERIFIED:** whether CQG mandates one of IOP's five set DAS wordings (§1
item 4). If the CQG About page's "Research data" heading names a set form, use
that form verbatim instead of the block above.

---

## 7. Cost — what you will actually be charged

| Item | Cost |
|---|---|
| **Submission** | **£0** |
| **Publication, subscription route** | **£0** — *"Publication on a subscription-access basis is free of charge."* |
| Publication, optional gold OA | £2530 / €2905 / $3490 (+VAT where applicable) |
| Colour figures | N/A — the Note has zero figures |

**Recommendation: take the subscription route.** It is free, and it is the
default for a physics Note. Gold OA buys open access you already have by other
means: the same manuscript is permanently and freely readable on Zenodo under
CC-BY-4.0 at DOI 10.5281/zenodo.21481838. **£2530 would buy you nothing you do
not already have.**

**Watch for this at the portal:** IOP's wizard may present the OA election as a
prominent, positively-framed choice. Choosing subscription access is not a
downgrade and carries no penalty in review — editorial decisions at IOP are
independent of the OA election.

---

## 8. Suggested and opposed referees — and the endorser conflict

CQG **offers** both fields and requires neither (§1). Note IOP's own rule: if
they use your suggestion, *"we will complement this with a review from a second
referee chosen by the journal"* — so a suggestion never controls the outcome, it
only speeds up finding someone competent.

### The conflict, stated plainly

`project-context/SSOT/ENDORSER_SHORTLIST_2026-07-22.md` names people being
approached separately for **arXiv endorsement**. Naming the same person as a
suggested referee is a real problem: an endorsement is a personal favour you
asked for; a referee suggestion is a claim of independence. Doing both to the
same person either compromises the referee report or makes the endorsement look
transactional — and both are visible in writing.

**For P1A specifically, there is no conflict, and that is lucky rather than
planned.** The endorser shortlist is entirely cosmology/DESI/bounce people. The
right referees for an Einstein–Cartan–Holst Note are the torsion and
first-order-gravity community, and **none of them is on the shortlist.**

**Hard rule for this submission: no name from `ENDORSER_SHORTLIST_2026-07-22.md`
goes in the suggested-referee box. In particular not Yi-Fu Cai and not Robert
Brandenberger** — both can endorse `gr-qc`, both are on the shortlist, and
Brandenberger is additionally a co-author of the paper whose value P2 corrects.
Keep them in the endorser lane only.

### Suggested referees — candidates drawn from P1A's own reference list

These come from the Note's own bibliography, so their relevance is a matter of
record, not my guess. **I did not verify any individual's current affiliation,
email, or availability** — check each on their institutional page before
entering them.

| Candidate | Why they fit | Basis |
|---|---|---|
| **Ilya L. Shapiro** | Wrote *"Quantum Einstein-Cartan theory with the Holst term"* — **published in CQG itself**, so he is already in this journal's reviewer pool and knows exactly the action P1A works in | P1A ref. [4], *Class. Quantum Grav.* **31**, 185002 (2014) |
| **Simone Speziale** | Two Immirzi-parameter papers in P1A's list; among the most active people on the Holst term and first-order gravity | P1A refs. [5], [6] |
| **Laurent Freidel** | *"Quantum gravity, torsion, parity violation and all that"* — the torsion/parity-sector paper P1A builds on | P1A ref. [3] |
| **Friedrich W. Hehl** | Author of the foundational Einstein–Cartan review the Note leans on. Very senior; may decline or be unavailable — offer as a fourth, not a first | P1A refs. [1], [2] |

**Recommendation:** enter **Shapiro, Speziale, Freidel** — in that order if the
form ranks them. Shapiro first: a CQG-published author on precisely the
Einstein–Cartan-with-Holst action is the single most efficient suggestion you can
make.

### Opposed referees

**Recommendation: leave this blank.** You have no adversary here, and naming one
without cause reads badly. The one case where you would use it — asking to
exclude an author whose number you are correcting — does not apply to P1A; that
situation belongs to P2, not this Note.

---

## 9. Pre-submission checklist

| # | Must be true | Status 2026-07-24 |
|---|---|---|
| 1 | **Compiled PDF contains Acknowledgements + COI + funding + AI disclosure** | ✅ **CLOSED in v1A.0.127, 2026-07-24.** Re-verify any time with:<br>`pdftotext arxiv/paper1a_ech_nogo.pdf - \| grep -ci "acknowledg"` → **2**<br>`… \| grep -ci "competing interests"` → **1**<br>`… \| grep -ci "funding"` → **1**<br>`… \| grep -ci "generative-ai"` → **1**<br>Note-scoped block; the full-paper acknowledgments and the cut cosmology material stay commented. |
| 2 | ORCID `0009-0008-5616-5994` resolves publicly | ✅ **VERIFIED 2026-07-24** — `pub.orcid.org/v3.0/0009-0008-5616-5994` → HTTP 200, name "Houston Golden" |
| 3 | ORCID appears in the manuscript | ✅ **NOW PRESENT** in v1A.0.127 — `\altaffiliation` footnote on the author block, rendering as "ORCID: 0009-0008-5616-5994" beside the email footnote on page 1. Matches how P1B carries it. |
| 4 | Abstract ≤ 300 words | ✅ **UNDER THE CAP ON EVERY COUNTING CONVENTION, and untouched by the v1A.0.127 edit.** Verified from the compiled PDF 2026-07-24: **269 words** counting each inline math expression as one word (the manuscript-native count, and what a human or Word-style counter gives); **285 words** for the ASCII-ified paste block in §3 (whitespace tokens — this is the number to expect if ScholarOne counts what you paste); **295 words** by naive whitespace tokenization of raw `pdftotext` output, where rendered math fragments split into several tokens. Worst case 295 vs a 300 cap — **do not add a sentence.** |
| 5 | Zenodo DOI 10.5281/zenodo.21481838 resolves | ✅ **VERIFIED 2026-07-24** — HTTP 200 at `zenodo.org/records/21481838` |
| 6 | PDF exists, compiles clean, 8 pp | ✅ 8 pages, 0 figures, **v1A.0.127**, md5 `0bc1ee72836c867114118521cf86e1c2`. 0 undefined refs, **0 overfull hboxes**; page 1 and the new page 6 declarations block rendered and visually checked for column overflow (revtex two-column) — clean. |
| 7 | No arXiv placeholder in live text | ✅ verified in the audit; `\preprint{arXiv:XXXX.XXXXX}` at `:1163` is **commented out** |
| 8 | Bibliography self-contained (no "in preparation" companion cites reaching a referee) | ✅ The compiled Note's 11 `\bibitem`s are all third-party literature. The four `Golden2026*` entries in `arxiv/references.bib` are cited only inside `\begin{comment}` blocks. **However** they ship inside any source bundle you upload at revision stage — see item 9. |
| 9 | `arxiv/references.bib` companion entries cleaned | ⚠️ Partially — HEAD `ef9993f2` is *"fix(bib): back-patch the five latent companion entries in arxiv/references.bib"*, so this may already be done. **Not a blocker for initial submission** (PDF-only). Re-check before the revision-stage source upload. |
| 10 | ScholarOne account exists | ⬜ **HOUSTON-ONLY** — not created (this kit creates no accounts) |
| 11 | Subscription-vs-gold-OA decision made | ⬜ **HOUSTON-ONLY** — recommendation: subscription (free), §7 |
| 12 | Referee suggestions chosen, no endorser-list overlap | ✅ candidates in §8; zero overlap with the endorser shortlist by construction |
| 13 | Not under consideration elsewhere | ✅ P1A has been submitted nowhere. The Zenodo deposit is an archive, not a submission, and is disclosed in the cover letter. |

---

## 10. What happens after you click

**Timeline (IOP's own published metrics, §1):**
- **~6 days** to a first decision *before* peer review — i.e. the desk-rejection
  decision. **CQG's desk-rejection rate is 63%.** Expect a real chance of a fast
  no; that is the journal's normal behaviour, not a verdict on the science.
- **~54 days** to a first decision *after* peer review, if it goes out to
  referees.
- Acceptance rate 21%.

So: a week to know if it survived the editor, roughly two months to know if it
survived the referees.

**Realistic risk, named honestly:** the audit flagged that ~3,984 live words over
8 two-column pages is long against CQG's "brief… short interesting point" framing
for a Note. CQG publishes no numeric cap, so this is an **editor-desk risk, not a
rule violation**. The cover letter (§5) addresses it head-on by inviting
redirection to a full Paper. If the desk rejection cites length or article type,
the correct response is to resubmit as a Paper, not to cut science.

**When the decision arrives — what to update in the repo:**

| Outcome | Repo surfaces to update |
|---|---|
| **Any decision** | `project-context/SSOT/paper-1/status.md` (or the P1A status file) — record the venue, submission date, manuscript ID, and decision verbatim. Add a `reviewTimeline.ts` entry in `site/src/data/` **in the same commit** (standing directive: review-round site sync). |
| **Desk reject** | Record the editor's stated reason verbatim — do not paraphrase it into something softer. If it is length/article-type, open a "resubmit as Paper" queue row in `project-context/SSOT/queue.md`. This is a routing outcome, not a science failure; do not let it lower a readiness figure. |
| **Referee reports** | Save the complete raw text of every report under `project-context/peer-reviews/` before recording any verdict — the same integrity rule that governs INT/EXT rounds applies to real human referees, and more so. Truth-audit each finding before closing it. |
| **Accept** | Update Convex (`papers:*` / `activityFeed:add`) so the live site reflects the acceptance — static `papers.ts` alone does not reach the site (standing directive A). Add the journal reference to the Zenodo record's metadata. Update `project-context/SSOT/index.md`. Under directive P, publication readiness is already composed without the venue step, so acceptance does not change a readiness score — it closes the *publishing phase* row. |
| **Accept** | Post-acceptance IOP will request **source files** (§1): `arxiv/paper1a_ech_nogo.tex` + `.bbl`. Clean the `arxiv/references.bib` companion entries first (checklist item 9) — at that point they do reach a copy-editor's eyes. |

---

*Kit prepared 2026-07-24 against git HEAD `ef9993f2`. Every venue requirement
re-fetched live from IOP this session; items that could not be confirmed from an
official page are labelled UNVERIFIED in §1 with the check that would settle
them. Nothing was submitted, no account was created, and no email was sent.*
