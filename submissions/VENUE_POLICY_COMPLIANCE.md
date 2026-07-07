# Venue-Policy Compliance — bigbounce 6-paper wave

**Date:** 2026-07-07 · **Author:** Houston Golden (sole author, all six)
**Scope:** pre-submission AI-methods / authorship / data-availability / moderation compliance for P1A, P1B, P2, P3, P4, P5.
**Routing:** arXiv first (astro-ph.CO / astro-ph.GA / gr-qc), then journals per map — P4→PRD or MNRAS · P3→ApJS or AJ · P2→PRD/JCAP · P5→MNRAS/PRD · P1A→JCAP/PRD · P1B→companion/pair.

> **Method note:** every policy below was fetched/searched from the venue's official pages on 2026-07-07. Nothing is guessed. Where a page bot-blocked automated fetch (APS 403, AAS BAAS-DOI 403), quotes were harvested verbatim via search of the live official page and the source URL is recorded; open those in a logged-in browser for byte-exact confirmation before final submission.

---

## 0. Snapshot: what each paper's disclosure currently says

All six carry an "AI-assisted methods/methodology" paragraph in the acknowledgments. Two tiers:

| Paper | "verified by author against committed artifacts" | Explicit author-responsibility clause | Explicit "AI is not an author" | Names model/version |
|-------|:--:|:--:|:--:|:--:|
| **P1A** | ✓ | ✓ "author takes **sole responsibility** for all scientific claims, derivations, numerical results, and bibliographic attributions" | ✗ (implied by "under the author's direction") | Partial — "Anthropic's Claude", no version |
| **P1B** | ✓ | ✓ "author takes **sole responsibility** for all…" | ✗ (implied) | Partial — "Anthropic's Claude", no version |
| **P2**  | ✓ | ✓ "takes **full responsibility** for the content" | ✓ "the AI pipeline is … **not an author**" | ✗ "agentic AI pipeline / multi-model" |
| **P3**  | ✓ | ✗ **MISSING** | ✗ **MISSING** | ✗ |
| **P4**  | ✓ | ✓ "takes **full responsibility** for the content" | ✓ "the AI pipeline is … **not an author**" | ✗ |
| **P5**  | ✓ | ✗ **MISSING** | ✗ **MISSING** | ✗ |

**P2 and P4 are the gold-standard wording** (responsibility + not-an-author, both explicit). **P3 and P5 are the two gaps** — they assert verification and "reproducibility as a strength" but never state author responsibility or that the AI is not an author. Fix proposed in §6.

Data-availability: P3, P4, P5 have explicit Data-Availability / Data-and-Code sections (HuggingFace CC-BY-4.0 + GitHub + Zenodo-DOI-at-submission). P1A/P1B point to the public reproducibility tree / manifest. No AI-generated figures anywhere (all matplotlib/data plots). No residual reviewer-log / LLM-prompt text leaks into any compiled body (scanned 2026-07-07 — clean). No ORCID in any packet (see §5).

---

## 1. arXiv (all six — gate 1)

**Policy — AI use & authorship** (https://blog.arxiv.org/2023/01/31/arxiv-announces-new-policy-on-chatgpt-and-similar-tools/):
> "generative AI language tools **should not be listed as an author**".
> "continue to require authors to **report in their work any significant use of sophisticated tools** … we now include in particular text-to-text generative AI among those that should be reported consistent with subject standards for methodology."
> "by signing their name as an author of a paper, they each individually **take full responsibility for all its contents, irrespective of how the contents were generated**."

**Policy — moderation** (https://info.arxiv.org/help/moderation/index.html): submissions "must comply with appropriate standards of scholarly communication"; may be declined if they lack "originality, novelty, significance," or contain "falsified, plagiarized content or serious misrepresentations." 2026 enforcement (Research Information / Inside Higher Ed, 2026): arXiv now penalizes (up to a 1-year ban) "incontrovertible evidence" of **unchecked** LLM output — hallucinated citations, fabricated references, or **residual chatbot prompts left in the text**. The policy does *not* ban AI use; it enforces author accountability.

**Policy — endorsement** (https://info.arxiv.org/help/endorsement.html): "arXiv requires that users be endorsed before submitting their first paper to arXiv or a new category." astro-ph and gr-qc are endorsement domains; a single-author first-time submitter **does need endorsement**.

**Our status — COMPLIANT (with one operational item):**
- AI never listed as author ✓ (Houston sole author, all six).
- Significant AI use reported in each paper's methods/acks ✓.
- Author responsibility: explicit in P1A/P1B/P2/P4; **missing in P3/P5** (§6) — arXiv's "sign = full responsibility" is satisfied by the signature itself, so this is *not* an arXiv blocker, but closing the P3/P5 gap removes any moderation ambiguity.
- No fabricated references / residual prompts: body scan clean ✓; the P2 Cai–Li factor-of-2 is *disclosed as unresolved* (not overclaimed) ✓; P1A previously stripped embedded R-round logs ✓.

**arXiv moderation risk assessment — LOW, with two flags:**
1. **Endorsement (operational, not content):** first-time single-author submitter in gr-qc/astro-ph.CO/astro-ph.GA **needs an endorser**. This is the single most likely cause of a first-submission hold. Line up an endorser before wave 1. Not a content risk.
2. **AI-heavy single-author profile:** the honest, prominent AI-methods disclosure is an *asset* here, not a liability — it is exactly what arXiv's policy asks for. The residual risk is *tone*: any sentence that reads as overclaiming a discovery invites "lacks significance" scrutiny. Our papers headline **null results and disclosed limitations** (P4/P5 null dipole; P1A no-go; P2 factor-of-2 explicitly unresolved), which is the opposite of overclaiming — good. Keep the "reproducibility-by-construction as a strength" framing (P3/P5) but pair it with the responsibility clause so it doesn't read as AI-cheerleading.

**Verdict: COMPLIANT.** Pre-wave-1 action = secure an arXiv endorser (operational). Disclosure edits (§6) recommended but not blocking for arXiv.

---

## 2. APS / Physical Review D — P4, P2, P5, P1A candidates

**Policy — AI/LLM** (https://journals.aps.org/authors/ai-based-writing-tools):
> "AI writing tools **cannot be listed as an author** but can be added in the Acknowledgments."
> "An AI-based writing tool **does not meet the criteria for authorship because it is neither accountable nor can it take responsibility** for a research paper's contents."
> "Authors should **disclose the use of AI tools to editors in their Cover Letter** and (if desired) within the paper itself."
> "Authors must **take full responsibility for the contents of their manuscripts**."
> "The Physical Review journals **do not allow submissions containing images generated or modified by generative AI** … " (exception: AI-assisted tools that are part of the research design, described in methods).

**Policy — Data Availability** (https://journals.aps.org/authors/data-availability-statements): a **Data Availability Statement is required** for PRD submissions on/after **Sept 4 2024**; authors "must select one of several pre-scripted data availability statements"; supplemental-material files must **not** be used in place of a citable data repository.

**Policy — format:** RevTeX 4-2 (APS standard); PRD Regular Articles have **no hard page limit**.

**Our status — NEEDS-TWEAK (minor) + operational:**
- AI not an author ✓; disclosure in acknowledgments ✓ (APS permits acks placement).
- **Cover-letter disclosure (operational, required):** APS wants LLM use disclosed *to editors in the cover letter*. Our `REFEREE_COVER_LETTER.md` files must carry one explicit sentence disclosing the agentic-AI pipeline. **Add it to every PRD-routed cover letter** (P4, P2, P5, P1A) — this is an APS hard requirement not satisfied by the in-paper acknowledgment alone.
- Author responsibility: P4/P2/P1A ✓; **P5 missing** → close §6.
- AI-generated images: none (all data/matplotlib figures) ✓ — compliant.
- Data Availability Statement: pick and paste the APS pre-scripted statement matching our HuggingFace-CC-BY + GitHub + Zenodo deposit at submission; do **not** rely on supplemental files. P4/P5 already have data sections that map cleanly onto the "data available in a public repository" pre-scripted option.
- RevTeX 4-2 ✓ (all papers).

**Verdict: NEEDS-TWEAK-COVER-LETTER** (add AI-disclosure sentence to PRD cover letters) + **P5 responsibility clause** (§6). Content otherwise compliant.

---

## 3. AAS journals — ApJS/AJ (P3), AJ (P4 alt)

**Policy — AI/LLM** (https://journals.aas.org/manuscript-preparation/):
> "Authors are expected to **acknowledge and cite the use of any LLM** used in manuscript preparation. **Responsibility for the accuracy of the submission remains with the authors**."
Authorship is human-contribution-governed (Professional & Ethical Standards page); no clause permits AI authorship.

**Policy — software/data** (https://journals.aas.org/policy-statement-on-software/ · https://journals.aas.org/data-guide/): software should be cited **both** by describing-article and by a **DOI (Zenodo/FigShare)**; authors "archive the published version of their code using … Zenodo or FigShare"; tables >~200 rows delivered machine-readable at submission; deposits require a summary of files, formats, file↔article relationship, and units; datasets need an explicit **open license (CC-BY for data / MIT for software)**.

**Scope:** ApJS = "extensive papers … catalogs and large compilations of data"; AJ = "significant scientific results derived from observations." → **P3 (377,780-object multi-survey anomaly catalog) and P4 (8.47M-galaxy chirality catalog) are natural ApJS fits.**

**Our status — NEEDS-TWEAK (P3) / mostly-compliant (P4):**
- **P3 disclosure gap (§6):** AAS wants the LLM use acknowledged **and** author accountability stated. P3's paragraph acknowledges the pipeline but **omits the responsibility clause** → close §6. AAS explicitly requires "responsibility … remains with the authors."
- Software DOI: AAS wants a Zenodo/FigShare **software DOI**, not only a GitHub URL. P3/P4 currently cite GitHub + "Zenodo DOI at submission." **Mint the Zenodo DOI for the code/catalog and cite it** at submission (already flagged as a to-do in the papers — make it hard-required for AAS routing).
- Machine-readable tables + license: P3/P4 catalogs are Parquet on HuggingFace under **CC-BY-4.0** ✓ (satisfies open-license requirement); ensure the >200-row headline tables have an MRT/machine-readable deposit at submission.

**Verdict: NEEDS-TWEAK** — P3 responsibility clause (§6) + Zenodo software/data DOI minted at submission + MRT tables. Content compliant.

---

## 4. MNRAS/OUP (P4, P5) · JCAP/IOP-SISSA (P1A, P2)

### MNRAS / OUP
**Policy — AI** (https://academic.oup.com/mnras/pages/General_Instructions):
> "Natural language processing tools driven by artificial intelligence (AI) **do not qualify as authors** as they cannot take responsibility for the submitted work, and the journal will **screen for them in author lists**."
> "The use of AI … **should be disclosed both in cover letters to Editors and in the Methods or Acknowledgements section** of manuscripts."
> "Per COPE, **authors are fully responsible for the content** of their manuscript, even those parts produced by an AI tool."

**Policy — Data Availability** (same page): "The inclusion of a **Data Availability Statement is a requirement**"; placed in the endmatter **after the Acknowledgements** under the heading "Data availability."

**Our status — NEEDS-TWEAK (minor):**
- AI not an author ✓; disclosed in acks ✓; **add the same disclosure sentence to the MNRAS cover letter** (P4, P5) — MNRAS requires both cover-letter *and* paper.
- Author responsibility: P4 ✓; **P5 missing** → §6.
- Data Availability Statement present ✓ (P4 "Data Availability" §; P5 "Data and code availability" §) — confirm the heading/placement is "Data availability" in the endmatter after acks for MNRAS house style.

**Verdict: NEEDS-TWEAK-COVER-LETTER** + P5 clause. Content compliant.

### JCAP / IOP-SISSA
**Policy — AI** (https://publishingsupport.iopscience.iop.org/questions/generative-ai-tools/ · .../ethical-policy-journals/):
> "AI tools **cannot meet the requirements for authorship** as they cannot take responsibility for the submitted work."
> authors "must **disclose this usage in the Acknowledgements section** … including **the model and version of the generative AI tool and how it was used** in the work."
> "All authors **remain fully responsible for all material** presented in their manuscript, and for ensuring its accuracy, integrity and originality."
> Prohibited: "Fabricate … data or results," "Generate reference lists," and — "**concealing prompts for GenAI tools within a manuscript … will result in immediate rejection**."

**Our status — NEEDS-TWEAK (IOP model/version naming):**
- AI not an author ✓; disclosed in acknowledgments ✓ (IOP's required placement).
- **IOP-specific gap:** IOP requires the disclosure to **name the model + version + how used**. P1A/P1B name "Anthropic's Claude" but **no version**; P2 says "agentic AI pipeline / multi-model" with **no model named**. For JCAP-routed papers (P1A, P2), **add model + version** (e.g. "Anthropic Claude (Opus/Sonnet family, 2026), used for … under the author's direction"). This is the one IOP-specific wording change.
- No concealed prompts: body scan clean ✓ — critical for IOP (immediate-rejection trigger). Reference lists are human-curated/verified, not AI-generated ✓.
- Author responsibility: P1A/P2 ✓ (both have it) — good.

**Verdict: NEEDS-TWEAK-MODEL-VERSION** for JCAP routing (P1A, P2). Content compliant.

---

## 5. Cross-cutting operational items (all venues)

1. **arXiv endorsement** — secure an endorser for gr-qc / astro-ph.CO / astro-ph.GA before wave 1 (most likely first-submission hold cause; not a content issue).
2. **ORCID** — no ORCID in any packet. arXiv, APS, AAS, OUP, IOP all support/encourage ORCID; APS and OUP increasingly expect it. **Register + add ORCID iD to the arXiv account and each submission's author metadata.** Low effort, removes friction.
3. **Cover-letter AI disclosure** — APS *and* MNRAS require AI use disclosed to editors *in the cover letter*, not only in the paper. Add one sentence to every `REFEREE_COVER_LETTER.md` in the PRD/MNRAS lanes.
4. **Zenodo DOI at submission** — AAS wants a software/data DOI (Zenodo/FigShare); APS/MNRAS/IOP prefer a citable archival deposit over a bare GitHub URL. Mint at submission and replace the "DOI inserted at submission" placeholders (P3, P4, P5).
5. **No AI-generated figures** — confirmed none; keep it that way (APS hard rule).

---

## 6. Proposed disclosure edits (directive-G pass — LIST ONLY, do not apply here)

Two content edits close every content-level gap. Both are single-sentence additions to the acknowledgments AI-methods paragraph. **P1A/P1B/P2/P4 need no content edit** (responsibility + not-an-author already present; P1A/P1B/P2 only need the JCAP model-version tweak *if* JCAP-routed — see below).

### Edit A — **P3** (`pipelines/p3_anomaly_engine/paper3_draft.tex`, acknowledgments AI-methods paragraph, ~line 1489)
Append to the end of the "AI-assisted methodology" paragraph (after "…the same pipeline a reader runs to verify it."):
> `The author designed the study, made all scientific judgments, and takes full responsibility for the content, including any material produced with AI assistance; the AI pipeline is a reproducibility and verification instrument, not an author.`
*Satisfies:* AAS "responsibility remains with the authors," APS/MNRAS/IOP "fully responsible," arXiv "full responsibility."

### Edit B — **P5** (`pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex`, acknowledgments AI-methods paragraph, ~line 3985)
Append to the end of the "AI-assisted methodology" paragraph (after "…the same one a reader runs to verify it."):
> `The author designed the study, made all scientific judgments, and takes full responsibility for the content, including any material produced with AI assistance; the AI pipeline is a reproducibility and verification instrument, not an author.`
*Satisfies:* MNRAS/APS "fully responsible," arXiv "full responsibility," and the "not an author" clause.

### Edit C — **P1A + P2, JCAP-routing only** (model + version naming, IOP requirement)
Only if P1A / P2 are routed to JCAP. In the AI-methods paragraph, name the model and version:
- **P1A** (`arxiv/paper1a_ech_nogo.tex` ~line 4036): change "an agentic AI research pipeline (Anthropic's Claude, operated under the author's direction)" → `an agentic AI research pipeline (Anthropic Claude, Opus/Sonnet 2026 releases, operated under the author's direction)`.
- **P2** (`research/focused_paper_source_integration/02_full_draft.tex` ~line 1380): change "an agentic AI pipeline --- a multi-model system for …" → `an agentic AI pipeline built on Anthropic Claude (Opus/Sonnet, 2026) with OpenAI and Google models for cross-checking --- a multi-model system for …`.
*Satisfies:* IOP "model and version … and how it was used." **Not needed for PRD routing** (APS does not require model/version). Fill in the exact model IDs actually used before applying.

> All three edits are additive, non-load-bearing, and can ship as one directive-G bundle (bump `\paperVersion` patch + `\date` + recompile 0-undef-refs + re-mirror PDFs + Convex `paperVersions:bump` per directive-G) if/when Houston greenlights. **Not applied by this audit — listed only.**

---

## 7. Per-venue verdict table

| Venue | Papers | Verdict | Blocking? |
|-------|--------|---------|-----------|
| **arXiv** | all 6 | **COMPLIANT** | No content blocker. Operational: secure endorser + add ORCID. |
| **APS / PRD** | P4, P2, P5, P1A | **NEEDS-TWEAK** | Add AI-disclosure sentence to cover letter (op) + P5 responsibility clause (Edit B). No AI figures ✓. DA-statement required. |
| **AAS ApJS/AJ** | P3, P4 | **NEEDS-TWEAK** | P3 responsibility clause (Edit A) + Zenodo software/data DOI + MRT tables. |
| **MNRAS / OUP** | P4, P5 | **NEEDS-TWEAK** | Cover-letter AI disclosure (op) + P5 responsibility clause (Edit B). DA-statement heading/placement ✓. |
| **JCAP / IOP** | P1A, P2 | **NEEDS-TWEAK** | Name model+version in disclosure (Edit C). Concealed-prompt scan clean ✓ (rejection-trigger avoided). |

**Bottom line:** No content blocker anywhere. Only two in-paper content edits needed (P3 + P5 responsibility clause, Edit A/B) — a single directive-G bundle. Everything else is per-venue operational (cover-letter sentence, Zenodo DOI, ORCID, endorser) done at submission time. P2/P4 disclosures are the gold-standard template; P1A/P1B are strong (sole-responsibility clause). The AI-methods disclosures are an arXiv-moderation *asset*, not a risk — honest, prominent, and paired with null/disclosed-limitation headlines rather than overclaims.

---

### Sources (fetched/searched 2026-07-07)
- arXiv AI policy — https://blog.arxiv.org/2023/01/31/arxiv-announces-new-policy-on-chatgpt-and-similar-tools/
- arXiv moderation — https://info.arxiv.org/help/moderation/index.html
- arXiv endorsement — https://info.arxiv.org/help/endorsement.html
- arXiv submission agreement — https://info.arxiv.org/help/policies/submission_agreement.html
- APS AI tools — https://journals.aps.org/authors/ai-based-writing-tools
- APS data availability — https://journals.aps.org/authors/data-availability-statements
- APS editorial policies — https://journals.aps.org/authors/editorial-policies · PRD authors — https://journals.aps.org/prd/authors
- AAS manuscript prep / LLM — https://journals.aas.org/manuscript-preparation/
- AAS software policy — https://journals.aas.org/policy-statement-on-software/ · data guide — https://journals.aas.org/data-guide/
- AAS ethical standards — https://journals.aas.org/professional-and-ethical-standards-for-the-aas-journals/
- MNRAS general instructions — https://academic.oup.com/mnras/pages/General_Instructions
- OUP author AI use — https://academic.oup.com/pages/for-authors/books/author-use-of-artificial-intelligence
- IOP generative AI — https://publishingsupport.iopscience.iop.org/questions/generative-ai-tools/ · ethical policy — https://publishingsupport.iopscience.iop.org/ethical-policy-journals/
