# Pattern 011 — Confabulated bib entry survives draft 1 till Perplexity catches it

**First seen**: P5 R3 PER-B1 (DESIVAST first-author "Douglass" → actually "Rincon")
**Severity**: high (genuine bib drift; not caught by Grok or GPT)
**Frequency**: 4 (P5 R3 DESIVAST first author + Shamir2022 title; P5 R5 DESIVAST author-tag; P5 R5 ASTRA "first" claim)
**Detection**: a `\bibitem{}` carries author/title/venue that does not match
the actual arXiv/ADS metadata. Survives many rounds because Grok and GPT
don't check citation forensics.
**Prevention**: before submitting any paper to external review, run a
bib-existence audit: for each `\bibitem{}`, WebFetch the arXiv ID and verify
title+authors match.

## What it looks like

> PER-B1 (MAJOR, VERIFIED): bib `DESIVAST2025` shows first author "S.B. Douglass";
> arXiv:2411.00148 + ADS confirms first author is **Hernan Rincon**, not Douglass.

> PER-B4 (MAJOR, VERIFIED): `Shamir2022DESI` bib title reads "Asymmetry between
> galaxies with clockwise and counterclockwise handedness in DESI Legacy Survey
> data"; arXiv:2208.13866 actual title is **"Analysis of spin directions of
> galaxies in the DESI Legacy Survey"**.

## Truth-audit verdict

When WebFetch on arXiv confirms the mismatch: VERIFIED. **This is the only
finding shape where Perplexity is consistently right.**

## Examples observed

- **P5 R3 PER-B1 VERIFIED**: DESIVAST2025 first-author Douglass → Rincon
  correction. Survived since first bibliography draft.
- **P5 R3 PER-B4 VERIFIED**: Shamir2022DESI title was LLM-confabulated
  ("Asymmetry between galaxies with clockwise and counterclockwise handedness")
  vs actual MNRAS title ("Analysis of spin directions of galaxies in the DESI
  Legacy Survey"). Survived since first draft.
- **P5 R5 PER-M1 VERIFIED**: DESIVAST bib `\bibitem{...}` still tagged "(DESI
  Collaboration)" after R3 first-author fix; Rincon et al. is not a formal
  DESI-collab paper. Survived R3 closure.
- **P5 R5 PER-M2 VERIFIED**: §X still called ASTRA "the first public DESI
  cosmic-web catalog" despite EDR-only scope. Survived from draft 1.

These 4 closures across rounds 3-5 are the cleanest demonstration that
**bib metadata confabulation is real and lasting** — without Perplexity's
citation-forensics persona, P5 would have submitted to arXiv with the wrong
first author and wrong title on its most-cited reference.

## Root cause

When the original LaTeX draft was written, the author (or the assist-LLM that
generated the bibliography) confabulated bib metadata: invented a plausible
first-author or title, attached the right arXiv ID. Subsequent reviews
(Grok brutal, GPT methodology) don't WebFetch the arXiv ID; they trust the
bib metadata as-stated. Only Perplexity (citation-forensics persona with
real-time web access) catches the drift.

But Perplexity also has high noise (patterns 001, 012). Distinguishing the
**4 real cases per ~40 false-positive cases** requires WebFetch verification.

## Pre-review check

Before any paper's first external R-round (and ideally before draft-1
landing):

```python
# /paper-pre-review-check pseudo-code
for entry in parse_bbl(paper.bbl):
    if entry.has_arxiv_id:
        actual = fetch_arxiv(entry.arxiv_id)  # WebFetch arxiv.org/abs/<id>
        bib_authors = parse_authors(entry.text)
        actual_authors = actual.authors[:4]
        if bib_authors[0].surname != actual_authors[0].surname:
            FLAG_REAL_FIRST_AUTHOR_DRIFT(entry)
        if not title_match(entry.title, actual.title, fuzz=0.8):
            FLAG_REAL_TITLE_DRIFT(entry)
        if str(actual.year) not in entry.text:
            FLAG_REAL_YEAR_DRIFT(entry)
    elif entry.has_doi:
        actual = fetch_doi(entry.doi)
        # same checks
```

Run this **before draft-1**, then re-run after any bibliography edit. The
4 confabulations caught by Perplexity rounds 3-5 on P5 would all have been
caught by this script before any external review.
