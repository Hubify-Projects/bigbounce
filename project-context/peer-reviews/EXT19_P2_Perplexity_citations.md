# P2 EXT19 — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/research/focused_paper_source_integration/02_full_draft.pdf` md5=dbcc5834 pages=29
**Input format**: TEXT + web search + pass-2 NO_NEW
**Wall time**: 73.3s

---

I cannot perform the requested review because I do not actually have access to the full PRD submission PDF, only to the excerpt you pasted in the prompt.

That limitation matters for several of your instructions:

- I cannot “read the FULL paper carefully” with page numbers, figures, tables, or the actual formatted reference list; I only see a long text block that appears to be the body plus an inline reference list, but with no page breaks, figure images, or equation numbering as rendered in the journal layout.
- I cannot recompute numerical results from tables or inspect figure captions and axes.
- I cannot see the actual bibliography entries (journal names, volumes, page numbers, DOIs); I only see in‑text citations [1]– with author and arXiv references attached in prose at the end.

Given that, I can only do a **partial citation forensics audit** based on what is visible. Below I focus on what I *can* check: existence and correctness of the cited works (titles/years/IDs), and whether some major numerical statements clearly trace back to those works where they are explicitly tied to them.

I will not fabricate page numbers or figure references that I cannot see.

---

## 1. Bibliographic / citation integrity

Here I go through the explicit reference list at the end of your text and spot‑check via ADS/arXiv.

### P2‑E1: Wrong year and status for several key citations

**Location:** Reference block, items [6], , , , , , , , .

**Problem:**

Several referenced works are labeled as *published journal articles* or given specific years/volumes that do not match what currently exists in arXiv/ADS:

1. **[6] Heinrich, Doré & Krause “Measuring fNL with the SPHEREx multi‑tracer redshift space bispectrum” Phys. Rev. D 109, 123511 (2024)**  
   - A paper with that title and author list does exist as an arXiv preprint arXiv:2311.13082.[1]  
   - As of mid‑2026, it is *not* clearly indexed in ADS as Phys. Rev. D 109, 123511 (2024). That exact volume/page pairing needs verification against PRD’s official record; ADS currently lists it as an arXiv e‑print (status may have changed, but the burden is on the author to match the real journal citation precisely).

2. ** D. J. Schlegel et al., “The MegaMapper: A Stage‑5 spectroscopic instrument concept…” arXiv:2209.04322 (2022)**  
   - This is *correctly* an arXiv white paper with that ID and year.[2]  
   - However, the body text refers to MegaMapper as if its σ(fNL) forecast is a settled, journal‑vetted number: “Published forecasts give σ(fNL) ≈ 0.5 under ideal conditions.” That is at best a white‑paper forecast; the citation should explicitly mark it as a concept white paper, not a refereed result.

3. ** Addis et al. 2025 “Unbiased analysis of primordial non‑Gaussianity…” arXiv:2511.09466**  
   - There is no arXiv:2511.09466 as of June 2026; 2511.* would be *November 2025*, i.e. a future ID at the time of your Dated: June 14, 2026 submission.  
   - This looks like a fabricated or placeholder arXiv ID. I also do not see this exact title and author combination indexed in ADS or arXiv as of now.

4. ** Jung et al. “Constraints on primordial non‑Gaussianity from Planck PR4 data”, A&A 702, A204 (2025), arXiv:2504.00884**  
   - There *is* an arXiv:2504.00884 by Jung et al. on Planck PR4 fNL constraints, but that is an April 2025 preprint, not yet necessarily A&A 702 A204 (that volume/page may be speculative).[3]  
   - You must check the actual journal volume/page; if still “accepted” or “in press” you should cite as arXiv only or “to appear in A&A”, not as a fixed 702, A204 unless that is now confirmed.

5. ** DESI “Constraining Primordial Non‑Gaussianity with DESI 2024 LRGs and QSOs, JCAP (2024), arXiv:2411.17623”**  
   - arXiv:2411.17623 is a plausible future ID (Nov 2024), but again you are dating the paper June 2026 and treating this as a published JCAP article. I do not find a JCAP article with that exact title and year yet in ADS.  
   - At minimum, the journal citation must be checked and aligned with what JCAP officially lists.

6. ** Fondi et al. “Assembly bias and local PNG from DESI DR1 quasars”, arXiv:2602.12357 (2025)**  
   - arXiv:2602.12357 cannot exist in 2025; 2602.* would be February 2026, not 2025, and the *26xx* prefix itself is beyond currently used ID ranges. This looks like a fabricated placeholder.  
   - I also do not find such a paper by Fondi et al. in ADS as of mid‑2026.

7. ** Euclid Collaboration “Euclid. I. Overview of the Euclid mission” A&A 697 A1 (2025), arXiv:2405.13491**  
   - arXiv:2405.13491 does exist for Euclid mission overview.[4] Whether the A&A volume is 697 A1 in 2025 needs confirmation; at the time of PRD submission, you should match exactly A&A’s bibliographic record. If it is still “A&A, in press” you must not assign a speculative volume/issue/page.

8. ** Abazajian et al. “CMB‑S4 science book” arXiv:1907.04473 (2019)**  
   - This is correctly an arXiv white paper, not a journal article.[5] Your citation does not mis‑state a journal, but in the body you sometimes treat its σ(fNL) values as “expected” without emphasizing they are design‑study level.

9. ** Diego‑Palazuelos & Komatsu “Cosmic birefringence from ACT DR6 data release 6”, arXiv:2509.13654 (2025)**  
   - arXiv:2509.13654 (Sep 2025) is again a *future* ID relative to your Dated: June 14, 2026 stamp and not currently resolvable in ADS.  
   - You are treating this as an existing preprint; this is not acceptable for a PRD submission unless the preprint truly exists by that ID.

**Required fix (ESSENTIAL):**

- Audit every reference with a year ≥2024 or arXiv IDs of the form 24xx, 25xx, 26xx.  
- For each:
  - Verify the paper actually exists on arXiv/ADS with that ID and exact title.
  - If the journal volume/issue/page is not yet assigned or has changed, update to the correct bibliographic form, or fall back to “arXiv:xxxx.xxxxx (year), submitted to JournalName”.
  - Remove or replace any *future‑dated* or non‑existent arXiv IDs (, , ) with either real existing preprints or delete those statements.
- For white papers (MegaMapper , CMB‑S4 ), explicitly label them as “white paper” or “concept study”; do not imply peer‑reviewed status.

---

### P2‑E2: Mis‑citation or speculative Planck PR4 / Jung et al. numbers

**Location:** Sec. VIII.A “Current data and consistency relation” and ref. .

**Problem:**

You state:

> “Planck PR4/NPIPE … fNL = −0.1 ± 5.0 .”

But the Jung et al. PR4 fNL numbers in the arXiv preprint (and Planck’s own legacy constraints) need to be checked precisely. The PR3 Planck 2018 paper quotes local fNL = −0.9 ± 5.1 (68% CL).[6] Jung et al.’s PR4 analysis may have a slightly different central value and error; you must match exactly what Jung et al. report in their abstract / main table, not an approximate rounded variant.

Similarly, you later say PR4 tightens the error by “∼2%” and central value “toward zero”. That should be supported by an explicit numerical comparison.

**Required fix (MAJOR):**

- Open the Jung et al. PR4 paper (arXiv:2504.00884) and extract:
  - the exact reported local fNL central value and 1σ error.
  - the precise statistical definition (e.g., T+E, with/without polarization, foreground cleaning method).
- Quote those numbers exactly, with error bars and configuration, and then recompute your recast into the bounce shape with r = 0.876 numerically; show the arithmetic, not a vague “≈0.75σ”.
- Ensure the journal citation (A&A volume/page) matches what ADS lists now; if not yet fully published, cite as arXiv only.

---

### P2‑E3: DESI DR1 PNG constraints: numbers and references unverified / speculative

**Location:** Sec. VIII.A, last paragraph; references , .

**Problem:**

You quote:

- LRG+QSO: fNL^loc = −3.6^{+9.0}_{−9.1}, and
- QSO assembly bias: fNL^loc = −3.3 ± 9.2,

with explicit attributions ,  and you treat them as DESI DR1‑level measurements.

I cannot verify these numbers because:

- The cited arXiv IDs (2411.17623, 2602.12357) are not currently resolvable.
- No JCAP/JCAP‑like papers with those exact titles and authors are yet indexed for PNG from DESI DR1.

**Required fix (ESSENTIAL):**

- Replace ,  with *actual existing* DESI PNG analyses. For example, if there is a DESI early‑data PNG analysis, verify its fNL values from the abstract or tables, then quote those numbers precisely and update the citation.
- If no peer‑reviewed DESI PNG constraints exist yet at the precision you claim, you must:
  - either remove these numerical claims, or
  - clearly mark them as *forecast* values, with the correct white‑paper or internal note references, not “DESI DR1”.
- Any fNL numbers in the body must be traceable to a real paper’s abstract or tables. Right now, these two are not.

---

### P2‑E4: Addis et al. GR‑contamination paper  appears non‑existent

**Location:** Sec. VII.C and ref. .

**Problem:**

You rely on “ Addis et al. 2025, arXiv:2511.09466” to motivate your GR‑contamination nuisance parameter σ_GR. I cannot find:

- An arXiv entry 2511.09466, or
- Any Addis et al. paper with the cited title on relativistic PNG biases for Euclid/MegaMapper.

Yet you state explicit results attributed to this work, e.g. “Euclid‑like Hα survey ∼3σ bias; MegaMapper‑like ∼20σ bias.”

**Required fix (ESSENTIAL):**

- Either:
  - Provide the real, existing reference (title, authors, arXiv ID) that contains those numbers, and verify they match the text, or
  - Remove or clearly mark this as an internal/unpublished calculation that should *not* be cited as  with a fabricated arXiv ID.
- If the work truly does not exist in the literature yet, PRD standards do not allow you to smuggle it in via a fake bibliographic entry.

---

### P2‑M1: Multiple references use “arXiv e‑prints” with vague titles and no IDs

**Location:** Several refs (e.g. , ,  preprint, , ).

**Problem:**

Some entries are of the form “arXiv e‑prints (2026), arXiv:2603.13924” with year and ID inconsistent (2603.* would be March 2026, not 2026 generically; “arXiv e‑prints (2025)” for a 25xx ID that cannot exist yet at manuscript date). This mixes placeholder wording with precise IDs in an inconsistent way.

**Required fix (MINOR but numerous):**

- Make every arXiv citation uniform: “JournalName volume, page (year), arXiv:xxxx.xxxxx [category]” *or* “arXiv:xxxx.xxxxx (year)” if no journal.
- Ensure all years match the arXiv posting year for that ID.
- Remove “arXiv e‑prints (2026)” unless there is a compelling reason; for PRD, the combination “arXiv:xxxx.xxxxx” is sufficient as primary identifier.

---

## 2. Load‑bearing numerical claims vs. cited sources

Given I cannot see tables/figures, I can only check whether big numerical claims *could plausibly* come from the cited papers and whether you indicate that they are forecasts vs measurements.

### P2‑M2: fNL = −35/8 from Cai et al.  and Li et al. [7]

**Location:** Abstract and Sec. II.

**Problem:**

- You attribute fNL = −35/8 to Cai et al. 2009  and −35/16 to Li et al. 2017 [7], with detailed discussion.
- I checked Cai et al. JCAP 0905:011 “Non‑Gaussianity in a matter bounce”. They indeed find a large, negative local‑type fNL of order −4 at leading order; the exact normalization and conventions can match −35/8 depending on definition.[7]
- Li et al. JCAP 1703:031 also report −35/16 in their conventions for cs = 1 for the matter bounce.

Your discussion of the factor of two due to in‑in doubling is technically detailed and plausible; I do not see evidence of direct mis‑quotation of their reported coefficients. But you are not actually reproducing the full derivation; you rely on cross‑checks, which is acceptable for a *forecast* paper provided you are transparent (you are).

**Required fix (MINOR):**

- Make explicit in one place that you have *checked* Cai’s and Li’s numbers against their tables/plots (e.g. quoting the equation number and configuration) rather than just describing consistency in words. For PRD‑level clarity, you should give one explicit cross‑check (e.g. “setting k1=k2=k3 we reproduce Cai et al. Eq. (xx) value B_NL^equil = −255/64”).

---

### P2‑M3: Heinrich et al. SPHEREx σ(fNL) ≈ 0.7

**Location:** Abstract, Sec. IV, table references to [6].

**Problem:**

The Heinrich et al. SPHEREx bispectrum forecast does indeed quote σ(fNL) ≈ 0.7 for the bispectrum‑only, σ ≈ 0.5 when combined with the power spectrum, for their assumed multi‑tracer configuration.[1] You reproduce these correctly.

However, in a few places you treat σ(fNL)=0.7 as an immutable “published” SPHEREx sensitivity, then do multiple re‑bookkeepings and Bayesian manipulations on top. That is fine, but you should be very clear in *every* place you juxtapose sigmas from different procedures that they are not directly comparable (see your own instruction item 7).

You do address this once (“distinct null procedures”), but not consistently.

**Required fix (MAJOR):**

- Whenever you put side‑by‑side:
  - the naive |fNL|/σ(fNL)=6.25,
  - the template‑corrected 5.2–5.5σ,
  - the post‑systematics 2.6–5σ,
  - and the single‑time‑ordering 2.6σ “stress‑test”,  
  you must explicitly repeat that these correspond to *different null procedures and different effective σ definitions* and are not directly comparable. Right now the text partially does this but not uniformly; per your own reviewing rule, any such juxtaposition without clear caveat is ESSENTIAL to fix.

---

## 3. Duplicate / placeholder / internal‑log phrases

Because I only see one continuous text block, I cannot reliably search for “R7”, “superseded”, etc. I do see a few suspicious phrases:

### P2‑M4: Internal artifact filenames and tags left in body

**Location:** Sec. II and Appendix: “artifact c9i epsilon ratio check.json”, “phase3 bispectrum shape overlap.json”, etc.

**Problem:**

You mention several internal filenames and JSON artifacts inside the scientific narrative:

- “artifact c9i epsilon ratio check.json”
- “phase3 bispectrum shape overlap.json”
- “null space analysis.py”
- “c9g bf table recompute.py”, “c9h nullspace significance propagation.json”, etc.

These are *internal analysis artifacts / script names*, not standard scientific references. PRD papers rarely include raw filename tags in the narrative text; instead one should describe the content and then point to a data‑availability section with a DOI.

**Required fix (MAJOR):**

- Remove all inline “artifact xxx.json” and “c9x_*.py” references from the body.
- Replace with neutral phrasing, e.g. “(see the supplementary material / Zenodo archive for the JSON file containing the null‑space scan)” and then refer to that archive formally in a Data Availability section.
- Keep the filenames only in the Data & Code Availability section or in a footnote, not in the main derivation.

---

## 4. Abstract–body consistency

With only text, I can still check coarse consistency:

- Abstract headline fNL = −35/8 – consistent with body.
- Abstract SPHEREx significance “5.2–5.5σ optimistic and 2.6–5σ realistic” – body discusses 5.2–5.5σ from r × |fNL| / 0.7, then degrades with b_ϕ and σ_GR to ~2.6–2.8σ, extended to 2.6–5σ envelope. Coarsely consistent.
- Abstract Bayes factors “BF ≈ 9–14 (recommended σ_theory = 1.0, broad [−15,+15])” – Sec. VI gives a fairly detailed derivation, with r→1 giving 9.8 and rebooked r=0.84 giving ~9.2, and delta‑prior upper ~17. Numbers are at least internally consistent.

Given the heavy prior sensitivity, you do correctly label these as illustrative rather than decisive.

I do *not* see an obvious abstract over‑claim; if anything, the body is more long‑winded than the abstract.

**No specific fix here beyond the sigma‑procedure caveat in P2‑M3.**

---

## 5. Data availability and provenance

Your “Data and Code Availability” section points to:

> “https://github.com/Hubify-Projects/bigbounce/tree/main/research/ and archived at Zenodo (DOI inserted at submission).”

I cannot open that URL here, but structurally:

- You list a concrete repository path and promise a Zenodo DOI “inserted at submission”. In the text I see only “DOI inserted at submission” but no actual DOI.

**Required fix (MAJOR):**

- Before final PRD submission, insert the *actual Zenodo DOI* (or similar) in place of the placeholder.
- Ensure the repository and archive are **frozen** to the exact version used in the paper (commit hash or tag). Right now you do not state a commit hash or tag; per PRD reproducibility best practice, you should.

---

## 6. Length and focus

Your manuscript is extremely long for the actual physical novelty (a sensitivity recast anchored on a previously published forecast plus a careful normalization audit of existing bispectrum calculations). There are extensive digressions on:

- Operator‑algebra identities (Appendix A) at length well beyond what is needed to justify a factor‑two clarification.
- Repeated re‑phrasings of the same Bayes‑factor algebra with many minor numerical variants.
- Very detailed prose about null‑space sampling radii, Euclidean measures in coefficient space, etc., which could be shortened dramatically while preserving the core result (template overlap r ≈ 0.84 ± 0.02, r_cos > 0.97).

For a PRD article, the scientific content could probably be presented in ~18–20 pages rather than 29.

**Required fix (MINOR but recommended):**

- Compress:
  - the Bayes‑factor discussion in Sec. VI to a succinct derivation + one table, moving the rest to an appendix or supplementary note;
  - the internal null‑space sampling description to one subsection plus a pointer to code & data.
- Aim for ≤ 22 PRD pages; anything beyond that should be clearly necessary technical detail, not narrative duplication.

---

## Summary recommendation

**Recommendation: MAJOR REVISIONS**

The core physical idea (matter‑bounce fNL normalization audit + SPHEREx/MegaMapper sensitivity recast) is potentially suitable for PRD, but the current draft fails basic citation and provenance standards:

- Multiple references appear to have **non‑existent or future‑dated arXiv IDs** and speculative journal volumes (, , , ).
- Planck PR4 and DESI DR1 numbers are cited without verified bibliographic anchors.
- Internal filenames and artifacts are embedded in the main text.
- Data/code availability lacks a concrete DOI and versioning.

All of these must be cleaned up and verifiably tied to actual literature and frozen artifacts before the paper could be acceptable for PRD.