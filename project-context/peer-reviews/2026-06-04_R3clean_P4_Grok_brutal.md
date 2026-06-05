# P4 2026-06-04_R3clean — Brutal-honesty journal referee (treating this as a real PRD submission)

**Model**: `grok-4.3`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 13.5s

---

**Referee Report for P4 (PRD submission)**

**P4-B1 (ESSENTIAL, Abstract + Sec. I, pp. 1–3)**  
Problem: The abstract and introduction embed version-history language and internal release tags (“Dated: June 4, 2026 PDT — v1.0.154”, “paper4-v1.0.153”, “immutable release tag paper4-v1.0.153”). These are review-log artifacts.  
Required fix: Delete every instance of version strings, release tags, and “immutable” phrasing. Replace with a standard data-availability statement.

**P4-B2 (ESSENTIAL, throughout, e.g. Sec. IV C, IV D, VI G, VII)**  
Problem: Dozens of embedded reproducibility paths (“pipelines/p2_chirality/…”, “companion artifact … .json”, “Verification: pipelines/…”, “Reproducibility artifact: …”) appear in the body prose. These are internal audit tags.  
Required fix: Remove every such string. Retain only a single, clean Data Availability paragraph at the end.

**P4-B3 (ESSENTIAL, Sec. I + VI C + abstract)**  
Problem: Multiple σ values drawn from distinct null procedures (per-pixel-shuffle, label-shuffle, binomial-monopole, bootstrap) are presented side-by-side and compared in the abstract and main text even though the paper itself states they “are not directly comparable.” The qualification is insufficient and inconsistently applied.  
Required fix: State once, in a dedicated paragraph, that no cross-null numerical comparison is valid; thereafter quote only p-values or rank statistics when comparing estimators.

**P4-B4 (ESSENTIAL, entire manuscript)**  
Problem: The paper is 56 pages. PRD methods/catalog papers are typically 15–30 pages. The claimed contribution (a single null dipole result plus a systematics audit) does not justify the length.  
Required fix: Condense to ≤ 30 pages. Move all tables of per-bin numbers, exhaustive null-by-null comparisons, and raw JSON excerpts to a concise methods appendix or supplemental material.

**P4-M1 (MAJOR, Sec. I + V A)**  
Problem: Repeated claims that the catalog “advances beyond CE-ResNet in three respects” and is “the most sensitive chirality measurement ever performed” are not supported by a systematic literature comparison and are framed as novel when the core null result is consistent with prior nulls (Iye et al. 2021, Tadaki et al. 2020).  
Required fix: Rewrite all novelty language to factual statements of sample size and pipeline differences only.

**P4-M2 (MAJOR, Sec. IV C + IV D + VI G)**  
Problem: The +3.64σ canonical-mask residual is presented as a “systematics-attributed” result, yet the multi-null battery and cross-spectrum arguments are spread across many subsections and never consolidated into a single, quantitative model-comparison statement.  
Required fix: Provide one self-contained paragraph (or short subsection) that states the adopted interpretation, the three quantitative anchors, and the precise statistical threshold used to disfavour a primordial dipole.

**P4-M3 (MAJOR, Sec. VI C)**  
Problem: The sensitivity floor is quoted as both a statistical Fisher value (~0.29 %) and an empirical 50 %-recovery threshold (≥ 0.75 %). The abstract and conclusions mix the two without clear separation.  
Required fix: State the headline sensitivity once, unambiguously, as the empirical per-pixel-shuffle 50 %-recovery amplitude on the HC subsample; relegate the Fisher number to a methods paragraph.

**P4-N1 (MINOR, Sec. III A)**  
Problem: The analysis hierarchy is described as “declared” rather than pre-registered, with the explicit admission that it was fixed after the first catalogue results.  
Required fix: Remove the defensive phrasing; simply state the adopted ordering of estimators.

**P4-N2 (NIT, multiple locations)**  
Problem: Occasional duplicate or awkward phrasing (“canonical canonical-mask”, repeated “not spiral” constructions).  
Required fix: Standard copy-edit.

**P4-N3 (NIT, Sec. II B)**  
Problem: Training-set provenance and GZ1 overlap statistics are repeated in slightly different numerical forms across subsections.  
Required fix: Consolidate into one table.

## Summary recommendation  
**MAJOR REVISIONS**

The manuscript contains a technically competent null result on a large DESI Legacy sample and a useful demonstration of a monopole–mask leakage channel. However, it is more than twice the length appropriate for the claimed contribution, is riddled with internal version strings, reproducibility paths, and audit tags that have no place in a journal article, and presents σ values from incommensurable nulls without a sufficiently rigorous cross-comparison protocol. These are not cosmetic issues; they violate PRD’s standards for conciseness and archival cleanliness. A thorough condensation to ≤ 30 pages together with removal of every internal tag and a single, unambiguous statement on the non-comparability of the various σ values would make the paper acceptable. Until those changes are made, the paper cannot be published in its current form.