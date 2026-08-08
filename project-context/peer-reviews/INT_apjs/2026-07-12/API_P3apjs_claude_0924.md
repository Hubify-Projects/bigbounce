# INT Claude-subscription Review (ApJS-framed) — P3APJS v3.1.156-apjs — claude-opus-4-8
paper: P3APJS  version: v3.1.156-apjs  tex: pipelines/p3_anomaly_engine/paper3_apjs.tex
venue-framing: The Astrophysical Journal Supplement Series (ApJS)
modality: full-repo Claude Code subscription subagent (claude -p)
UTC: 2026-07-12T16:24:43Z

======================================================================
RAW RESPONSE (verbatim):
======================================================================

I have now read the full manuscript, independently recomputed the key arithmetic, and verified every headline number against the committed artifacts (via direct file reads and a verification agent). Every checked value matches: the 274,353→268,519 dedup chain, the DESI injection-recovery curve (99–100% at 5σ, ≥15σ narrow-line floor), the k-fold `best_val_mean=1.91`/`all_folds_pass_gate=false`, the Jaccard/OOD numbers, the eROSITA scaler-refit control, the f_NL Fisher chain, and the NANOGrav γ tensions. Nothing is fabricated; the reproducibility-by-construction claim holds.

---

(1) VERDICT: MINOR REVISIONS

(2) ISSUES:

**1. [MINOR] Data Availability (§Data availability; Abstract).** The Zenodo DOI is a placeholder ("minted at submission") and the HuggingFace catalog + weights are committed to be public only "with the arXiv posting." ApJS reviews the *data product*, not just the manuscript: the machine-readable per-object catalog, the `DATA_RELEASE_MANIFEST.md` column/`score_axis`/`membership_only` schema, and the `reproduce_headline_dedup.py`/`held_out_rescore.py` scripts must be accessible to the referee during review. The committed `outputs/*.json` I verified are necessary but not sufficient — provide the released tables and a live DOI. This is the one item that, unaddressed, could push toward major.

**2. [MINOR] Scope — §5 Cosmological Applications.** The multi-tracer f_NL and NANOGrav sections deliver *explicitly null* secondary results (de-biased f_NL returns the single-tracer baseline exactly; γ=2.567 consistent with a matter bounce only at +1.14σ and non-exclusive of environmental SMBHBs). They are honestly labeled "secondary demonstrations," but in an ApJS *catalog* paper they read as scope-creep and dilute the deliverable. Recommend relocating to a companion paper or a single appendix, so the catalog is the unambiguous product.

**3. [MINOR] "Validated catalog-grade" label spans heterogeneous gates (§3 three-tier block; §III.F NEOWISE).** NEOWISE (419 objects) enters the "validated" tier on a masking-geometry QA gate that passes *by construction* — not a detector-sensitivity test. This is disclosed prominently, but applying the word "validated" (even asterisked) to a component with no sensitivity characterization is a usability trap for a catalog consumer. Give NEOWISE its own tier label distinct from the injection-recovery-passing surveys.

**4. [MINOR] DESI validated tier rests on a single production-ensemble sensitivity gate.** The paper candidly states the two Jaccard checks are correlated readings of *short-trained proxy* models (`all_folds_pass_gate=false`), so ~73% of the catalog's detector-sensitivity support is the one re-pulled-SPARCL injection-recovery curve. The disclosure is exemplary, but state explicitly whether the pod-blocked full per-object held-out re-inference with the *production* ensemble can be produced for the data release; if not, the validated-tier claim for DESI should be softened one further notch.

**5. [MINOR] Title/abstract "37.3 million" is a reconciled process-volume figure.** Footnote ⊗ correctly reconciles the 36.76M / 36.93M / 37.29M spread, and no anomaly count depends on it — but a headline scan volume that needs a multi-clause footnote to interpret is friction for a catalog paper. Consider titling with the retained-native scanned pool (36.76M) and relegating the cross-transfer-inclusive figure to the text.

**6. [MINOR] Caveat density / presentation.** The manuscript is extraordinarily disclosure-dense (multi-paragraph table footnotes, deeply nested parentheticals in §II.B, §III, §IV.A). Table 2 (provenance consolidation) is the right model; push more of the tier/threshold/excision bookkeeping into the released documentation and lean the body prose, so a first-time reader reaches the released product without traversing the full audit trail.

(3) The central claim — a released, reproducible, honestly-tiered multi-survey anomaly-candidate catalog (268,519 validated / 377,482 inclusive) — **is supported** (every headline count and validation metric I checked recomputes exactly from the committed artifacts) **and is squarely appropriate for ApJS** as a large, well-documented, reproducibility-by-construction data product, pending the minor accessibility, scope, and presentation revisions above.
