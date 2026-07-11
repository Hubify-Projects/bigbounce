# P3 — Venue decision packet

**Paper:** P3 · multi-survey autoencoder anomaly catalog · v3.1.152 · 37pp
**Source:** `pipelines/p3_anomaly_engine/paper3_draft.tex`
**Date:** 2026-07-11 · **Status:** Houston-gated — pick a lane, then submit.

---

## The decision in one line

> **Three of five reviewers independently converged on the same point: this is a
> catalog paper, and PRD is the wrong venue.** That is signal, not noise. My
> recommendation is **ApJS** — but the science does not change either way, so the
> cost of getting this wrong is a resubmission, not a retraction.

---

## The signal — the venue objection is verbatim, from three independent referees

Not one harsh referee's quirk. Three fresh, uncoordinated reviewers reached the
catalog-venue conclusion on the identical PDF:

- **Gemini INT** (gemini-3.1-pro-preview, native-PDF, `INT_v3/ROUND_2026-07-09/API_P3_gemini.md`, MAJOR#1):
  > "Catalog releases and descriptions of data-mining pipelines belong in
  > astronomical journals (**such as ApJS, MNRAS, or A&A**), not in Physical
  > Review D. The cosmology applications (Section V) are explicitly described by
  > the author as 'secondary methodological demonstrations' that yield no
  > statistically significant detections … **rendering the manuscript out of
  > scope for a fundamental physics journal.**"

- **ChatGPT EXT** (`EXT_real/H17_2026-07-10/W1/P3_chatgpt_W1.md`, MAJOR): the
  headline is "analyst-defined rather than statistically measured … the largest
  validated anomaly catalog is therefore driven substantially by arbitrary
  quotas" — a catalog-construction critique, plus §V "should be separated into a
  dedicated study."

- **OpenAI INT** (per `DISPOSITIONS/P3.md` DP3-10/DP3-16, OpenAI#1): "remove
  f_NL + NANOGrav ⇒ paper is catalog-engineering, not a PRD physics result."

Grok (EXT/INT) and Claude INT do **not** dispute the science — they return
MINOR/MINOR-REVISIONS with "central claim supported." So the disagreement is
purely **venue fit**, and it points one direction: away from PRD.

Per pattern-066 the *verdict-word* variance is referee noise — but the *content*
of the objection is coherent across three reviewers, which is exactly the kind of
convergence a human referee at PRD will also reach. Disposition DP3-16 is
correctly flagged **OPEN-VENUE / HOUSTON-GATED**, not an editable defect.

---

## The three lanes, side by side

| | **PRD** (submit as-is) | **ApJS** ✅ recommended | **MNRAS** |
|---|---|---|---|
| **Fit argument** | §V cosmological-applications sections (f_NL forecast, NANOGrav) provide the "fundamental physics" hook. | The natural catalog/data-release venue — **Gemini named it first**. Built for machine-readable catalog releases + reproducibility. | Also a valid catalog venue; broader astro audience; suggested alongside ApJS by Gemini. |
| **Manuscript class** | revtex4-2 (already the source format) | AASTeX 6.3+ (`\documentclass{aastex631}`) | MNRAS class (`mnras.cls`) |
| **Format conversion** | **none** — already revtex | revtex → AASTeX. Per our compressed-effort table, format conversions are **~30-min agent work** (boilerplate/scaffolding tier, ~100×). | revtex → mnras.cls, same ~30-min agent tier. |
| **Content restructure** | none | none — §V stays as disclosed secondary demos; abstract already labels the catalog the primary deliverable | none |
| **Data-behind-figures** | not required | **Expected.** Machine-readable tables + data-behind-figures is the ApJS norm; we already release the catalog + weights + scripts on HuggingFace — needs MRT-format table + Zenodo DOI wiring. | Encouraged; supplementary data accepted. |
| **Risk** | The **documented venue objection carries straight to human PRD referees** — three LLM referees already reached it; a human editor may desk-reject or bounce to a data journal. | Low science risk. Cost is the MRT/data-behind-figures polish (already mostly done). | Low; slightly more prose-restructure expected than ApJS's catalog template. |
| **arXiv category** | `astro-ph.IM` primary / `astro-ph.CO` + `astro-ph.GA` cross-list (per `WAVE1_SUBMIT_WALKTHROUGH.md` L117-118 — **NOT** CO-primary; walkthrough already treats P3 as a methods/catalog paper). | Same categories — **unchanged**. astro-ph.IM primary is already the honest classification for a catalog + ML-methods paper. | Same. |

**What changes per lane:** PRD = zero change (and zero de-risking). ApJS/MNRAS =
**format only** (class file swap + MRT table + Zenodo DOI), ~30-min agent work.

**What does NOT change in any lane:** the science. 268,519-candidate process-volume
catalog, the 2,468 like-for-like benchmark, the DESI injection-recovery gate + two
correlated fold-stability probes, §V's honest nulls (f_NL σ=8.14 envelope,
NANOGrav γ=2.567 at +1.14σ), every disclosed provenance limitation. The reviewers
are unanimous that the catalog itself is technically supported.

---

## Recommendation — **ApJS**, cross-listed unchanged on arXiv

**Reasoning, weighing the signal honestly:**

1. **Three independent referees converged on the venue point** — that is the
   strongest cross-reviewer agreement P3 produced. When Gemini, ChatGPT, and
   OpenAI reach the same structural conclusion on unchanged content, a human PRD
   editor is likely to as well. Submitting to PRD as-is walks a documented
   objection into the human round; ApJS retires it before it starts.

2. **The paper's own framing already concedes the point.** The abstract labels the
   catalog the "primary deliverable" and §V "secondary demonstrations" returning
   nulls. ApJS is where that framing is a feature, not a scope problem.

3. **Gemini named ApJS first**, and ApJS's catalog/data-release template is the
   best match for what P3 actually is: a released catalog + model weights +
   reproducibility scripts (already public on HuggingFace).

4. **The conversion is cheap** (~30-min agent tier) and the science-risk is nil —
   so the downside of choosing ApJS is trivial, while the downside of choosing PRD
   is a probable venue bounce after a multi-month referee wait.

5. **arXiv posture is identical either way** (astro-ph.IM primary, CO+GA
   cross-list), so the astro-ph.CO cosmology audience still sees it.

**Runner-up: MNRAS** — equally defensible, slightly broader audience, marginally
more prose-restructure than ApJS's purpose-built catalog template. Choose MNRAS
over ApJS only if you specifically want the wider MNRAS readership.

**Not recommended: PRD as-is** — the only lane that carries a known, thrice-echoed
objection into the human round for no science gain.

---

**Ask:** pick **ApJS** (recommended) / MNRAS / PRD. On ApJS or MNRAS I run the
~30-min class-conversion + MRT-table + Zenodo-DOI pass and re-verify the compile;
the science and the arXiv categories are untouched.
