# Claude INT Referee Report — Paper P1A (EXACT-PDF)

**Journal target:** Classical and Quantum Gravity (Note format)
**Paper:** *Algebraic Cartan Elimination in Minimal Einstein–Cartan–Holst Gravity: Spin-Sourced Contact and Zero-Spin Scalar Branches*, Houston Golden.
**Version:** v1A.0.125 (Dated July 21, 2026, 19:58 PDT), 7 pp.
**PDF:** `arxiv/paper1a_ech_nogo.pdf`
**Referee:** Claude INT leg, 2026-07-22.

## EXACT-PDF BINDING — PASS
- Recorded sha256 (P1A in `intwave_bindings.json`): `88760604b96bf3c0b726de29363ab9f754b20d387c0696d7806d0b551cea1412`
- Computed `shasum -a 256 arxiv/paper1a_ech_nogo.pdf`: `88760604b96bf3c0b726de29363ab9f754b20d387c0696d7806d0b551cea1412`
- **MATCH.** Reviewed the exact bound PDF. `pdfinfo`: 7 pages, letter, pdfTeX-1.40.29, CreationDate Tue Jul 21 20:46:17 2026 PDT.

## Verification performed
- Full text extraction (`pdftotext -layout`) read end-to-end.
- All 7 pages rendered at 130 dpi (`pdftoppm`) and visually inspected for overflow/layout.
- LaTeX log (`arxiv/paper1a_ech_nogo.log`, same 20:46 compile): **zero** Overfull hboxes, **zero** undefined references / undefined citations / multiply-defined labels. Only six benign Underfull hboxes (justification-only).
- Numerical claims re-derived by running the paper's own machine-checkable script `arxiv/scripts/njl_gap_equation_route1.py`.
- DOI + git-commit + code-file existence checks (below).

## Numbers — ALL VERIFIED
Script `njl_gap_equation_route1.py` output reproduces every displayed figure:
- Max scalar ratio R_S = 2.14859 → paper "2.15" (Table I, Eq. B4). ✓
- Max axial benchmark R_A = 1.07430 → paper "1.07" (Table I). ✓  R_A rows 0.119/0.358/1.07 = R_S/2 rows 0.239/0.716/2.15. ✓
- ρ_4f benchmark κn²_ψ = 9.954×10⁻⁸⁰ eV⁴ → paper "1.0×10⁻⁷⁹ eV⁴" (Eq. 10). ✓
- κn²_ψ/ρ_Λ = 3.5571×10⁻⁶⁹ → paper "3.6×10⁻⁶⁹" (abstract, Eq. 10, conclusions). ✓
- orders_below = 68.449 → paper "about 68.4 orders below" (p. 3). ✓
- With 3/16 contact factor: 1.866×10⁻⁸⁰ eV⁴ → paper "1.9×10⁻⁸⁰ eV⁴"; ratio 6.670×10⁻⁷⁰ → paper "6.7×10⁻⁷⁰ ρ_Λ". ✓
- Hand-check of κn²_ψ from ℏc=1.9733×10⁻⁵ eV·cm, M_Pl=1.2209×10²⁸ eV independently gives 9.96×10⁻⁸⁰ eV⁴. ✓

Algebra spot-checks (independent): Q_γ Q⁻¹_γ = 1 with Q_γ=⋆+γ⁻¹, Q⁻¹_γ=[γ²/(1+γ²)](γ⁻¹−⋆), ⋆²=−1 → identity holds (Eq. 2). ✓ Eq. (6) 4πG=κ/2 and −(3/2)πG=−3κ/16 correct. ✓ ε⁰¹²³=−1 from ε_0123=+1 in mostly-plus signature correct. ✓ R_S = 3N_fN_c/(4π) → 0.239/0.716/2.148 for N_fN_c=1/3/9. ✓

## Availability / archive / commit — CHECKED
- Data-and-Code-Availability section (pp. 6–7) names `fierz_lemma_check.py`, `njl_gap_equation_route1.py`, `njl_gap_equation_route1_results.json`, "frozen at immutable repository commit 7befce143848."
- Commit resolves: full hash `7befce143848b925998a3e6ecc850aa510ab3a94`, subject "fix(p1a): align NJL artifact with cutoff scope"; 12-char stub in paper matches. ✓
- All three named files exist at `arxiv/scripts/`. ✓
- Task-supplied DOI https://doi.org/10.5281/zenodo.21481838 resolves 302 → `https://zenodo.org/records/21481838` (HTTP 200). ✓  **However, the PDF contains no Zenodo/DOI/arXiv-id/URL string anywhere** (grep of full text confirms — only reference-list arXiv IDs of cited works appear).

## Scope honesty — STRONG
The Note is exemplary in claim discipline: it repeatedly and explicitly disavows a dark-energy prediction, birefringence, and any operator-complete/unrestricted no-go (abstract; p. 2 "No operator-complete or unrestricted no-go is claimed"; Sec. V; Conclusions). The NJL result is flagged conditional (regulator/channel/species-bound) in every place it appears. The finite-density number is explicitly labeled an illustrative scale, not an EoS/vacuum-stress claim. Title claims match content. No overclaim detected.

---

## FINDINGS

### BLOCKER
None.

### MAJOR
**M1 — Data-availability statement is not reader-resolvable (journal-policy gap).**
Evidence: p. 6 (col. 2) "These exact files are frozen at immutable repository commit 7befce143848"; p. 6 (col. 1, Data and Code Availability) lists bare filenames. The statement gives no repository name, no public URL, and no persistent-archive DOI. A CQG reader cannot locate the artifacts from the paper alone. A Zenodo DOI (10.5281/zenodo.21481838) exists and resolves, but it is *not cited anywhere in the PDF* (full-text grep negative). Fix is trivial and non-scientific: cite the existing resolving DOI and/or a public repo URL in the availability statement. Severity is MAJOR on journal data-availability policy compliance, but note it requires no scientific rework — hence the overall verdict remains MINOR-REVISIONS.

### MINOR
**m1 — Citation attribution of the Fierz convention.** p. 2 (col. 2) "map the ordering (12)(34) to (14)(32) ... minus sign relative to the Nieves–Pal c-number identity"; Appendix A (p. 6) "the normalized convention of Nieves and Pal [7, 8]." Reference [7] is Itzykson & Zuber (a general QFT text), [8] is Nieves & Pal. Attributing the pair "[7, 8]" to "Nieves and Pal" is loose; either split the attribution or phrase as "[7, 8]" without naming only Nieves–Pal.

**m2 — Same operator carries two equation numbers with an internal forward reference.** L^NJL_tor appears as Eq. (8) (p. 3, J₅-form, asserted in Sec. II as "the maximal Einstein–Cartan magnitude") and again as Eq. (9) (p. 3, ψ̄γᵃγ⁵ψ-form, derived in Sec. III via Hehl–Datta). Sec. III opens "The contact operator in Eq. (9)" while Eq. (8) — the same object — was stated earlier. Harmless but a reader-facing redundancy/forward-reference; consider unifying or cross-noting that (8) and (9) are the identical operator in two notations.

**m3 — Filename vs. claim (observational, outside the PDF).** The file is `paper1a_ech_nogo.pdf` yet the paper explicitly disclaims any no-go ("No operator-complete or unrestricted no-go is claimed"). Not a defect in the document itself; flagged only so the submission filename/arXiv title metadata are not read as a no-go claim. No action required inside the PDF.

## Presentation / layout
Clean throughout. Fc matrix (Eq. A1), Table I, the two-column-spanning Eq. (13), and all inline density expressions render without column overflow or collision. Contents list matches section/subsection/appendix structure and page numbers. Version stamp v1A.0.125 in \date matches the binding. No stale version/date artifacts.

## Summary
A tightly-scoped, convention-audited consolidation Note whose every quantitative claim reproduces from its own committed script, with clean typesetting, resolvable commit, and unusually honest claim boundaries. The lone substantive referee ask is to make the data-availability pointer resolvable (add the already-existing Zenodo DOI / repo URL); the remaining items are cosmetic. No scientific rework indicated.

VERDICT: MINOR-REVISIONS
