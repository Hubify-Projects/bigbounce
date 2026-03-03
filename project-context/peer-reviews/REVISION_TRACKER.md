# BigBounce Manuscript Revision Tracker

**Paper:** Geometric Dark Energy from Spin-Torsion Cosmology
**Author:** Houston Golden
**Current version:** v0.8.0
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
**Status:** ALL PHASES COMPLETE

| # | Issue | Severity | Status | Resolved In |
|---|-------|----------|--------|-------------|
| 1 | Inflationary dilution vs bounce relic contradiction | FATAL | **DONE** | Phase 2 commit (Option A: keep dilution, drop bounce relic Ω_k/ΔN_eff claims) |
| 2 | $w=-1$ freezing logic not derived | FATAL | **DONE** | Phase 2 commit (downgraded to assumption, logical gap acknowledged) |
| 3 | Parity-odd action dimensional inconsistency | FATAL | **DONE** | Phase 2 commit (abstract formula fixed, Appendix E.4 reconciled) |
| 4 | CMB birefringence: no photon-sector coupling | FATAL | **DONE** | Phase 3 commit (reframed as consistency, not prediction; f(τ_rec) removed) |
| 5 | $f(\tau_{\rm rec})$ undefined / hides 10^120 enhancement | FATAL/MAJOR | **DONE** | Phase 3 commit (formula removed, honest statement about missing coupling) |
| 6 | H0 tension sigma arithmetic wrong (1.4sigma vs 2.9sigma) | MAJOR | **DONE** | `cfeba36` |
| 7 | Fits labeled as "predictions" | MAJOR | **DONE** | Phase 3 commit (all Tables, captions, body text relabeled) |
| 8 | Bayes factor table/equation inconsistency | MAJOR | **DONE** | `cfeba36` |
| 9 | JWST JADES on global dipole plot | MAJOR | **DONE** | `cfeba36` |
| 10 | Marketing tone (Detection Timeline, Discovery Era, fine-tuning scoreboards) | MAJOR | **DONE** | Phase 4 commit (Sec renamed "Observational Forecast", all captions softened, reproducibility honest) |

**Revision phases:**
- [x] Phase 1: Arithmetic / internal consistency (Issues 6, 8, 9, ref [37]) — commit `cfeba36`
- [x] Phase 2: Theory coherence (Issues 1, 2, 3 — Option A adopted)
- [x] Phase 3: Remove unsupported predictions (Issues 4, 5, 7)
- [x] Phase 4: Reproducibility and tone (Issue 10, code release honesty)

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

### Phases 2-4 Changes Summary (2026-03-02)

**Phase 2A — Inflation vs bounce relic (Issue 1, Option A):**
- Sec I.B: "values follow from bounce physics" → "motivated by—but not uniquely predicted by—the bounce scenario"
- Sec III.C: Three mechanisms rewritten — ΔN_eff and Ω_k explicitly labeled as phenomenological parameters fit to data; added note that Ω_k~10^{-3} cannot survive 92 e-folds as a direct bounce relic
- Sec VII.D: "not phenomenological degrees of freedom" → honest statement about phenomenological extensions
- Sec X (Falsification): Removed "closed bounce geometry" language for Ω_k
- Table params (Appendix B): "Closed bounce geometry" → "Phenomenological"; "Bounce production" → "Phenomenological"
- Sec IV.A: "from bounce physics" → "phenomenological parameters"

**Phase 2B — w=-1 freezing (Issue 2):**
- Sec II.C.2: Rewrote "Why w=-1" paragraph — now explicitly labeled as assumption, not derivation; logical gap acknowledged (if K_{ab}→0, why doesn't operator vanish?); flagged IR effective action derivation as open problem

**Phase 2C — Dimensional inconsistency (Issue 3):**
- Abstract: Λ_const = (α/M)D_inf → Λ_eff = Ξ M_Pl^2 with Ξ = [(α/M) M_Pl] D_inf (dimensionally correct)
- Sec I.B: Same formula fix
- Sec I.B item 6: Ξ definition corrected with M_Pl factor
- Appendix E.4: Reconciled with main text convention — clarified that M_Pl appears in energy density extraction, not in action coefficient

**Phase 3A — Birefringence coupling + f(τ_rec) (Issues 4, 5):**
- Sec III.A: Removed β = (α/M) D_inf × f(τ_rec) ≈ 0.30° formula entirely; replaced with honest statement that deriving β requires an explicit photon-torsion coupling not yet available; β treated as consistency with Planck, not a prediction
- Conclusions: Updated observational signatures paragraph to match

**Phase 3B — Fits vs predictions (Issue 7):**
- "predicted dipole amplitude" → "fitted dipole amplitude" (JWST paragraph)
- "predicted signal" → "observed/expected signal" (2× instances)
- "our model's predictions" → "our model's MCMC fits" (Fig 3b caption)
- "compared with our prediction" → "compared with our MCMC fit" (Table H0data caption)
- "Method: Theory" → "Method: MCMC fit" (Tables H0data, S8data)
- "predicted signatures" → "parity-odd signatures" (Discussion)
- "falsifiable predictions" → "testable outputs" (Related Work)
- "consistent with predictions" → "consistent with the framework" (Forecast Sec)

**Phase 4A — Timeline/scoreboards (Issue 10):**
- Sec IX title: "Detection Timeline" → "Observational Forecast"
- Fig 7 caption: Added "assuming signals exist at expected levels" + "illustrative" caveat
- Table X caption: Added "(illustrative; assumes signal exists at expected amplitudes)"
- Fig 8 caption: Added "conditional on assumed signal amplitudes" caveat
- Closing sentence: "decisively testable" → "within reach of planned experiments...not that detection is guaranteed"
- Fig 5 caption: "reduces fine-tuning by 115 orders" → "reparameterizes the fine-tuning...not a complete resolution"
- Reproducibility: "bundle in preparation and will be released" → "not yet available but is planned"
- Conclusions Known Limitations: Expanded to include Ω_k/ΔN_eff phenomenological status + code not available

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

### Round 2: arXiv-Readiness Audit (2026-03-03)

**Reviewer:** Houston Golden (manual PDF audit)
**Manuscript version:** v0.7.0 post-Phase 4
**Overall score:** Borderline → addressed in commit `1e97f96`

**Issues Identified:** 5 structural issues
**Status:** ALL ADDRESSED

| # | Issue | Status | Resolved In |
|---|-------|--------|-------------|
| R2-1 | Title "Comprehensive Framework with Observational Validation" too strong | **DONE** | → "Phenomenological Constraints and Correlated Signatures" |
| R2-2 | Dimensional appendix needed (action → ρΛ chain not shown) | **DONE** | New Appendix I with full dimensional audit |
| R2-3 | "emerges" language overreaches for assumed mechanism | **DONE** | → "is modeled as emerging" throughout |
| R2-4 | Reproducibility package missing | **DONE** | New Appendix J + arxiv/reproducibility/ skeleton |
| R2-5 | Forecast section (Sec IX) high-risk for skepticism | **DONE** | Moved to Appendix H; main text is 1-paragraph summary |

**Additional fixes:**
- "natural consequence of the effective action" → "consistent with a possible photon-sector extension"
- Explicit IR vacuum disclaimer: "This work does not derive the IR effective vacuum term from first principles"
- Table V: added compressed vs full-multipole χ² clarification
- "comprehensive framework" → "phenomenological framework" in Conclusions

**PDF:** 29 pages (up from 28 due to new appendices), 0 undefined references

---

### Round 3: Nuclear Option — Harsh Reviewer #2 Response (2026-03-03)

**Reviewer:** Simulated aggressive Reviewer #2 + Houston's directives
**Manuscript version:** v0.7.0 post-Round 2
**Approach:** Full nuclear option — maximum credibility, no overclaims

**Issues Addressed:** 10 critical issues (from two overlapping audits)

| # | Issue | Status | Resolution |
|---|-------|--------|------------|
| R3-1 | Abstract "deriving dark energy" oversells | **DONE** | → "modeling dark energy as arising from"; w=-1 assumption noted inline |
| R3-2 | Ω_k self-falsifying (92 e-folds kills it) | **DONE** | Ω_k REMOVED from MCMC; fixed to 0; caveat on existing fit values |
| R3-3 | w=-1 by fiat (already labeled assumption) | **DONE** | Already fixed Round 1; verified still in place |
| R3-4 | Galaxy spin 37-order gap | **DONE** | Explicit order-of-magnitude estimate added to Sec II.C.3 |
| R3-5 | β=0.30° in abstract without photon coupling | **DONE** | Numerical value removed from abstract; body text retains as Planck measurement |
| R3-6 | JWST on Figure 2 | **DONE** | Already excluded from fit Round 1; caption caveated |
| R3-7 | Forecast section (pseudoscience risk) | **DONE** | Section IX DELETED entirely; Appendix H DELETED entirely |
| R3-8 | CAMB diff is description not patch | **NOTED** | Disclosed in text; actual patch requires CAMB development |
| R3-9 | A(z) functional form arbitrary | **DONE** | Called "phenomenological" in abstract, body, conclusions |
| R3-10 | Abstract oversells vs body text | **DONE** | Rewrote abstract to match body text honesty |

**Additional changes:**
- Parameter count: 8 → 7 (Ω_k removed); effective 8 → 7
- Model comparison table: footnote explaining values need re-evaluation with Ω_k=0
- Falsification criteria: "Prediction" → "Expected signature" for CMB and galaxy spin
- Triple signature claim: softened to "if they can be connected to the theory quantitatively"
- Conclusions closing: now lists gaps (photon coupling, A_0, w=-1) as blocking issues
- All "resolves" → "partially reduces" for tensions
- "quantitative predictions" → "testable outputs" in intro
- Figure 5 caption: removed Ω_k reference
- Comprehensive comparison table: 8 → 7 parameters
- cobaya_config.yaml: Ω_k removed
- params_bestfit.ini: Ω_k removed

**PDF:** 28 pages (down from 29 — forecast section removed), 0 undefined references

---

## Future Rounds

*Add new sections here as additional reviews are conducted.*
