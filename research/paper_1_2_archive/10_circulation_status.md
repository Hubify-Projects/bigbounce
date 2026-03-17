# Paper 1.2 — Circulation Status

**Date:** 2026-03-14
**After:** Final pre-circulation patch (three referee-simulation fixes)

---

## Verdict: READY_FOR_CIRCULATION

---

## Fixes Implemented

| Fix | Location | What was added |
|-----|----------|----------------|
| MCL novelty clarification | Section 6.6 (line ~649) | Two sentences stating that canonical normalization is standard but its application as a constraint on geometric DE mechanisms in PGT is new |
| H₀ discrepancy explanation | Section 3.2.4 (after Table II discussion) | Three-line clarification attributing the difference (69.2 vs 67.68) to different Planck likelihood implementations and dataset vintages; values agree at 1.1σ |
| Fine-tuning table footnote | Table IV | Dagger footnote stating the ECH natural scale is a parametric estimate, not an independently derived scale |

All three fixes verified in `paper_1_2_draft.tex` and propagated to `paper_1_2_circulation.tex`.

---

## Circulation PDF

**Path:** `research/paper_1_2/paper_1_2_circulation.pdf`
**Size:** 187.01 KiB
**Compilation:** tectonic, 0 errors, cosmetic warnings only (underfull hbox, duplicate table labels from multi-pass)
**Version:** v1.2.0

---

## Circulation Package Contents

| File | Purpose |
|------|---------|
| `paper_1_2_circulation.pdf` | The paper |
| `paper_1_2_circulation.tex` | Source (if requested) |
| `circulation_email_template.md` | Email template for sending |
| `circulation_cover_note.md` | Longer cover note with feedback questions |

---

## Confirmation

- No TODO markers remain
- No editorial comments remain
- No draft version strings remain
- Acknowledgments section written (placeholder for referee names)
- DiegoPalazuelos2025 citation still missing arXiv ID (flagged, not blocking for circulation)
- Legner2025 arXiv ID (2507.09228) flagged for verification before submission

---

## Recommended First Readers

### Theory-focused
- Someone working in Poincare gauge theory or metric-affine gravity — they can assess whether the mass-coupling lock is genuinely new in the PGT literature and whether Foundation B (metric-affine Nieh-Yan) is distinct from Route T1
- Someone in quantum gravity phenomenology — they can assess whether the DR1-DR5 framework is useful beyond this specific program

### Cosmology-focused
- Someone working on MCMC dark-energy constraints — they can assess whether Part I is sufficiently distinct from standard ΔNeff analyses and whether the verification discussion is clear
- Someone in the EC/torsion cosmology community (e.g., connected to Liu et al. 2025 or Legner et al. 2025) — they can assess whether the related work section is fair and complete

### Ideal profile
A reader who works at the intersection of modified gravity theory and cosmological data analysis. They will be able to assess both the structural arguments (Parts II-III) and the phenomenological claims (Part I) in a single reading.

---

## Next Steps After Circulation

1. Collect feedback (1-2 weeks)
2. Incorporate revisions (if any)
3. Fix DiegoPalazuelos2025 citation
4. Verify Legner2025 arXiv ID
5. Finalize acknowledgments with reader names
6. Upload companion technical note to arXiv
7. Submit to JCAP (primary) or CQG (backup)
