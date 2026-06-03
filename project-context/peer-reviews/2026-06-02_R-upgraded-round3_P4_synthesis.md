# P4 R-upgraded-round3 — Synthesis & Truth-Audit

**Date**: 2026-06-02
**Paper version reviewed**: v1.0.147
**Paper version after closures**: v1.0.148
**Vendors**: Grok-4 brutal, GPT-5 (fallback gpt-4o) methodology, Perplexity sonar-pro citation, Gemini-2.5-pro cosmology
**Reports parsed**: 4
**Findings raised**: ~18 (3 explicit MAJOR-class, rest minor/nit, plus 6 GPT-Bx items)

---

## Per-finding truth-audit

| ID | Class | Verdict | Evidence | Closure |
|----|-------|---------|----------|---------|
| PAPER-PER-B1 | MAJOR | **VERIFIED + reviewer underreported** | Bibitem (line 4458) had arXiv:**2003.04325** which is a chiral plasma paper, not Motloch. Correct ID = **2003.04800**. Author list was "Motloch & Pen" — actual paper is Motloch, Yu, Pen, Xie. Description fused BOSS/2MRS (incorrect — actual paper uses SDSS-only initial-condition reconstruction). | Fixed in v1.0.148: arXiv ID corrected, full author list, description rewritten to "initial density field reconstructed from SDSS galaxy positions". closed-by-real-action |
| PAPER-PER-B2 | MAJOR | **VERIFIED** | Table row "Training labels: GZ1 + bot-validated" not supported by Jia et al. 2023 (arXiv:2210.04168), which describes training on **GZ1 labels only**. "bot-validated" was bigbounce-paper over-specification. | Fixed in v1.0.148: changed to "GZ1 (per Jia et al. 2023)". closed-by-real-action |
| PAPER-PER-b4 | minor | **VERIFIED** | Motloch et al. report ~2.7σ (Nature Astronomy abstract); paper said ~2σ. Defensible as "marginal" but reviewer-tightenable. | Fixed in v1.0.148: ~2σ → ~2.7σ. closed-by-real-action |
| PAPER-PER-b3 | minor | VERIFIED — minor framing | Walmsley "featured" ≠ "spiral" strictly. | DEFERRED — already qualified in surrounding text; cosmetic only. |
| PAPER-PER-n1 | nit | STALE | Bib already disambiguates Shamir:2022 (methodology) vs Shamir:2022DESI (data) with explicit comment block at lines 4372–4373. | closed-by-truth-audit-falsification |
| PAPER-PER-n2 | nit | OPINION | "Not separately reported" already accurate phrasing. | declined |
| PAPER-GPT-B1 | "B" | **STALE** | .tex already labels 0.29% as "(statistical)" theoretical Fisher floor vs 0.75% as "empirical 50%-recovery-3σ injection threshold" (lines 88, 202–203). | closed-by-truth-audit-falsification |
| PAPER-GPT-B2 | "B" | OPINION | Single ℓ=1 bin justified by isotropy observable; not a blocker. | declined |
| PAPER-GPT-B3 | "B" | DUPLICATE of GEM-M1 | Treated under M1. | merged |
| PAPER-GPT-B4 | "B" | STALE | Half-mod vs full-amplitude convention already disambiguated in v1.0.14x rounds. | closed-by-artifact-verification |
| PAPER-GPT-B5 | "B" | OUT-OF-SCOPE | Like-for-like Shamir reanalysis explicitly scoped-out in abstract + §9.1; reviewer overlooked the scope statement. | declined |
| PAPER-GPT-B6 | "B" | STALE | Falsification criterion already stated (line 88) at 5σ + ≥0.75%. | closed-by-truth-audit-falsification |
| PAPER-GEM-M1 | MAJOR | OPINION (defensible interpretation) | Reviewer asks for a positive generative-template regression of the +3.64σ residual. Paper argues elimination + decomposition; this is a legitimate methodological preference, not an error. | deferred-genuine — depth/PSF template regression is a follow-up work, not in-scope for this paper. |
| PAPER-GEM-M2 | MAJOR | OPINION | Multi-σ values reflect different estimators × different nulls on same data; paper's footnote 15 + Table XI already reconcile. A unified null-definitions table would improve clarity but absence is not a defect. | deferred-genuine — clarity improvement queued for v1.0.149+ if Houston greenlights. |
| PAPER-GEM-m1 | minor | OPINION | TTT transfer-function uncertainty already flagged. | declined |
| PAPER-GEM-m2 | minor | VERIFIED — already disclosed | Hold-out size limitation already acknowledged in §3.E. | declined |
| PAPER-GEM-m3 | minor | OPINION | Term "parity analyses" used in legacy literature context; rewriting throughout is cosmetic. | declined |
| PAPER-GEM-m4 | minor | OPINION | Two analyses present complementary evidence, not redundant. | declined |
| PAPER-GRO-M1..N3 | minor/nit | OPINION | All stylistic. | declined |

---

## Closures applied to v1.0.148

1. **arXiv ID 2003.04325 → 2003.04800** (Motloch bibitem) — critical metadata fix
2. **Author list** Motloch & Pen → Motloch, Yu, Pen, Xie — completeness fix
3. **Motloch description rewrite** — removed incorrect BOSS/2MRS attribution; replaced with accurate SDSS-only + initial-density-field reconstruction phrasing
4. **Significance 2σ → 2.7σ** (Motloch correlation) — accuracy
5. **CE-ResNet training labels** "GZ1 + bot-validated" → "GZ1 (per Jia et al. 2023)" — Jia attribution fix
6. **Author macro** "Motloch & Pen" → "Motloch et al." in §4.K.4 — author-count fix

PDF: 26.3 MB, 4-pass pdflatex, 0 undef refs.
Mirrored to: site/public/p4-chirality.pdf, site/public/papers/chirality_catalog_paper.pdf, paper4_chirality_catalog.pdf (3 paths), arxiv/, public/papers/, site/out/papers/, plus versioned chirality_catalog_paper_v148.pdf.

---

## Counter

**3 VERIFIED on v1.0.147** (all citation/metadata-class, all closed-by-real-action in v1.0.148).
**Prior round** (R-upgraded-postretro v1.0.146): 3 VERIFIED (Motloch attribution + Ivezic + reading-direction overstatement) — those addressed the surface-level Motloch attribution; this round caught the deeper metadata errors (wrong arXiv ID, wrong dataset attribution, missing co-authors) that survived.

Cumulative cascade depth across last 2 rounds: 6 VERIFIED citation-class findings → strong signal that **citation-forensics layer caught real errors prior R-rounds missed**. v1.0.148 should now be citation-clean enough to pass another Perplexity sonar-pro pass.

Pattern hits (catalog):
- **pattern-016-arxiv-id-fusion** (NEW candidate — arXiv ID swapped to unrelated paper) — eligible for catalog promotion
- **pattern-001-citation-attribution-fusion** (recurring; 3rd P4 hit)
- **pattern-002-bibitem-author-incomplete** (recurring)

No BLOCKERs. No MAJORs survive on v1.0.148 (3 closed, 2 deferred-genuine as OPINION/follow-up).
