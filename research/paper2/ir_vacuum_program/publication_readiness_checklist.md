# Closure Paper — Publication Readiness Checklist

**Paper:** "Systematic Closure of Minimal First-Principles Routes to Dark Energy in Einstein-Cartan-Holst Gravity"
**Author:** Houston Golden
**Date assessed:** 2026-03-13
**PDF size:** 277 KiB (~15 pages + figures + repo tables)

---

## Strengths (ready)

- [x] Title accurately describes content
- [x] Abstract is self-contained and standalone
- [x] Introduction motivates the problem without dependency on companion paper
- [x] Four routes clearly presented with setup, gates, results, closure
- [x] Combined interpretation synthesizes structural lesson
- [x] Requirements for future work (R1–R4) are concrete and useful
- [x] Three candidate next-generation directions identified
- [x] Conclusion is strong and honest
- [x] Figures present (G_SP vs gamma, V_eff comparison)
- [x] Reproducibility section with full script inventory
- [x] All closure arguments are sharp, not vague
- [x] Compiles without errors

## Remaining weak spots

- [ ] **Overfull hbox warnings in longtable file paths** — cosmetic only, but should be fixed for final submission (reduce \texttt{} path lengths or adjust column widths)
- [ ] **Diego-Palazuelos arXiv ID** — used 2501.10850; verify this is the correct ACT DR6 birefringence paper
- [ ] **Repository references** — the \texttt{comp1}, \texttt{comp2}, etc. citations point to repo files, not published references. For arXiv submission this is acceptable (repo ships alongside). For journal, may need to describe methodology inline instead.
- [ ] **No ORCID** — add author ORCID for journal submission
- [ ] **No MSC/PACS codes** — consider adding for journal compatibility
- [ ] **Section 2 ("Context and Motivation")** — still references \cite{Golden2026} which is itself unpublished. For standalone submission, this is fine as a preprint cross-reference but should be noted.
- [ ] **Figures are PNG** — journals may prefer PDF/EPS vector figures. The generation scripts exist; re-run to produce PDF versions if needed.

## Assessment: PUBLICATION-READY with minor cosmetic fixes

The paper is scientifically complete and self-contained. The remaining issues are cosmetic or logistical, not scientific. It can be posted to arXiv immediately.

---

## Recommended journal / arXiv positioning

### arXiv categories
- **Primary:** gr-qc
- **Cross-list:** hep-th, astro-ph.CO

### Journal options (ranked)

1. **Physical Review D** — Letter or Regular Article
   - Best fit: systematic negative results in quantum gravity / dark energy
   - Format: the paper is ~15 pages, appropriate for a Regular Article
   - Precedent: PRD publishes systematic no-go results regularly

2. **Classical and Quantum Gravity** — Paper or Topical Review
   - Good fit for Einstein-Cartan / LQG community
   - May reach the most relevant audience

3. **Physics Letters B** — if shortened to letter format (~6 pages)
   - Would need to cut reproducibility tables and compress T1/S1 sections
   - Stronger impact factor but requires significant compression

4. **JCAP** — if expanded with more cosmological context
   - Would need to add more observational discussion
   - Less natural fit for a negative-results paper

### Recommendation
**PRD Regular Article** or **arXiv-first with PRD submission to follow.** The paper's length and technical depth are appropriate for PRD. arXiv posting can happen immediately.
