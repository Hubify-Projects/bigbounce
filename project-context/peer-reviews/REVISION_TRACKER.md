# BigBounce Manuscript Revision Tracker

**Paper:** Geometric Dark Energy from Spin-Torsion Cosmology
**Author:** Houston Golden
**Current version:** v0.7.0
**Target:** arXiv-ready manuscript

---

## How This Works

Every peer review / audit gets saved in `project-context/peer-reviews/` with the naming convention:
```
YYYY-MM-DD_HHMMtz_description.md
```

This tracker logs each revision round and which issues have been addressed.

---

## Revision Rounds

### Round 1: Comprehensive Audit (2026-03-02 19:17 PST)

**Files:**
- `2026-03-02_1917PST_comprehensive-audit.md` — Full 10-issue audit with severity ranking
- `2026-03-02_1917PST_claims-table.md` — Derived vs Assumed vs Fit classification

**Issues Identified:** 10 critical/major issues
**Status:** Phase 1 COMPLETE

| # | Issue | Severity | Status | Resolved In |
|---|-------|----------|--------|-------------|
| 1 | Inflationary dilution vs bounce relic contradiction | FATAL | PENDING | — |
| 2 | $w=-1$ freezing logic not derived | FATAL | PENDING | — |
| 3 | Parity-odd action dimensional inconsistency | FATAL | PENDING | — |
| 4 | CMB birefringence: no photon-sector coupling | FATAL | PENDING | — |
| 5 | $f(\tau_{\rm rec})$ undefined / hides 10^120 enhancement | FATAL/MAJOR | PENDING | — |
| 6 | H0 tension sigma arithmetic wrong (1.4sigma vs 2.9sigma) | MAJOR | **DONE** | `cfeba36` |
| 7 | Fits labeled as "predictions" | MAJOR | **PARTIAL** | `cfeba36` (Abstract, Table I, Sec I.B, Conclusions) |
| 8 | Bayes factor table/equation inconsistency | MAJOR | **DONE** | `cfeba36` |
| 9 | JWST JADES on global dipole plot | MAJOR | **DONE** | `cfeba36` |
| 10 | Marketing tone (Detection Timeline, Discovery Era, fine-tuning scoreboards) | MAJOR | **PARTIAL** | `cfeba36` (Discovery Era removed, Conclusions rewritten; timeline table/Fig 5 scoreboards still present) |

**Revision phases:**
- [x] Phase 1: Arithmetic / internal consistency (Issues 6, 8, 9, ref [37]) — commit `cfeba36`
- [ ] Phase 2: Theory coherence (Issues 1, 2, 3 — pick Option A)
- [ ] Phase 3: Remove unsupported predictions (Issues 4, 5, 7)
- [ ] Phase 4: Reproducibility and tone (Issue 10, code release)

### Phase 1 Changes Summary (commit `cfeba36`, 2026-03-02)

**1A — H0 tension sigma arithmetic:**
- 1.4σ → 2.9σ (vs SH0ES) in Abstract, Table I, Table fullcomp, Conclusions
- σ8: 0.8σ → 1.5σ (vs Planck)
- Table I: "Our Solution" → "MCMC Fit", added calculation footnotes
- Sec I.B: "End-to-end derivation" → "Dark energy scale motivation"
- Abstract: "Key predictions" → "accommodates three correlated observational signatures"

**1B — Model-comparison bookkeeping:**
- Table V: clarified as "full tension dataset", defined χ²_eff
- Eq.(38): explicit dataset names
- Table VI: explains χ² magnitude difference vs Table V
- Table fullcomp: ln B footnoted with Planck+BAO caveat

**1C — JWST JADES:**
- Table II: JWST separated below rule, "Not included in dipole fit"
- Fig 2 caption: explicitly excludes JWST
- Conclusions: JWST removed from evidence list

**1D — Stouffer citation:**
- Stouffer 1949 → PDG Statistics Review 2024
- "Discovery Era" → "Full Operations"
- Conclusions: "Detection timeline" paragraph removed, "Known limitations" added

---

## Verification Protocol

After each revision round:
1. Recompile PDF (3-pass + bibtex)
2. Verify 0 undefined references
3. Run dimensional consistency check on all equations
4. Grep for removed language patterns (e.g., "Discovery Era", "uniquely", "no other model")
5. Verify claims table accuracy against revised text
6. Sync website if applicable
7. Update this tracker with resolution status

---

## Future Rounds

*Add new sections here as additional reviews are conducted.*
