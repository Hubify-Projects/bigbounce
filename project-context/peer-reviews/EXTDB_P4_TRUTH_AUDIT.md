# EXTDB P4 — Truth Audit (ChatGPT MAJOR vs source)

Round: EXTDB (DE-BIASED) | Paper: P4 chirality catalog v1.0.191
Source: `pipelines/p2_chirality/chirality_catalog_paper.tex`
Auditor verdict: **ChatGPT MAJOR = FALSE-POSITIVE** (both load-bearing concerns already handled in text). Consistent with Grok MINOR + Gemini MINOR. Patterns 061/063 (referee raises valid-sounding concern the paper already closes).

---

## Claim B2 — HC threshold p_eq>0.6 is post-hoc ("garden of forking paths")

**VERDICT: FALSIFIED.** The threshold is (a) a pre-specified operational definition and (b) accompanied by an explicit robustness sweep showing the null is invariant across the plausible threshold range. ChatGPT's own B2 says a sweep "would defuse" the concern — the paper HAS the sweep.

Strongest evidence (§Pre-registration, `sec:prereg`, line 613):

> "The primary fit uses the high-confidence Catalog~C selection of the generator script (`run_dipole_catalog_c.py`: ... confidence $>0.6$)... **the primary is defined at the threshold the generator script has used throughout.**"

> "**A full confidence-cut sweep** ($p_{\rm eq}\in\{0,0.4,0.5,0.6,0.7,0.8\}$; 2000-permutation pixel nulls each) localizes the transition: $z=+4.3,+4.1,+4.0$ at cuts $0,0.4,0.5$, **collapsing to $z=+0.41,+1.14,+0.51$ at $0.6,0.7,0.8$** ... (artifact `c12_r24conf_local_batch.json`)."

Decisive point: 0.6 is **not** a cherry-picked minimum. The null holds across the entire high-confidence regime — 0.6→0.41σ, 0.7→1.14σ, 0.8→0.51σ — all |z|<1.2. The transition (≤0.5 gives z≈4, ≥0.6 gives z<1.2) is sharp and physically attributed to the low-confidence tail. A robustness sweep showing the conclusion is invariant across the threshold range **eliminates the researcher degree of freedom** that forking-paths exploits.

Corroborating in-paper defenses:
- HC-strict parallel cut p_eq>0.8 (N=624,660) reported alongside HC-broad-0.6 (line 1002) — a second pre-declared cut, same null.
- 2×3 robustness panel crossing fit-weighting × mask threshold, every cell |z|≤0.8 (line 613, artifact `c12`).
- Quartile washout (line 934): per-p_eq-quartile ℓ=1 significances +0.20,−0.42,+0.44,+0.43, **no monotonic trend in label quality** — a real dipole carried by well-measured spirals would strengthen with quality; it doesn't.
- Calibration caveat (line 528): p_eq cuts explicitly framed as "monotone sample-selection thresholds (rankings by classifier confidence), not statements that a label is correct with probability p_eq."

No fix required. (Grok m1 / ChatGPT could be partially honored by adding a one-line Spearman(p_eq, local depth) check — optional polish, not a blocker.)

---

## Claim B3 — GZ1 chirality accuracy 69.91% (κ=0.40) too weak for "sub-percent" claims

**VERDICT: FALSIFIED (largely); accuracy is disclosed, propagated, and conservative for a NULL headline.**

Evidence:
- Disclosed prominently (§II, line 417; Appendix B, line 887; §release, line 1023): "spiral-chirality accuracy $69.91\%$ (Cohen's $\kappa=0.40$)... We treat $69.91\%$ as the **conservative accuracy floor and propagate it to all downstream isotropy bounds**."
- Propagation is empirical, through the real pipeline: injection-recovery floors A50≈0.75%, A95∈[1.0,1.5]% (HC-broad) and full-sample A50≈0.36%, A95≈0.63% (line 613) — label noise is baked into the recovered floor, not assumed away. The 1.7% reference dipole the paper excludes sits **above** these floors, so power is adequate for the exclusion claim.
- Dilution arithmetic explicit: g=2a−1 (line 744); Neff reduction ~10–15% → ~5–8% sensitivity penalty, σ(A)∝Neff^{−1/2} (line 999).
- Per-class confusion already reported (line 887): CW 0.539/0.545, CCW 0.527/0.588 — ChatGPT's "asymmetric CW/CCW confusion" data is in the paper.

Conceptual point P4's headline is a **NULL** (no chirality dipole) + a template exclusion. A moderate-accuracy classifier **dilutes any real signal toward null** — this makes a false null-detection conservative, not a defect, and the exclusion's power is set by empirically-measured injection floors that already include the dilution. ChatGPT's ask for "fuller asymmetric confusion propagation beyond symmetric dilution" is a refinement (the symmetric g=2a−1 mapping is leading-order, justified by equivariant TTA enforcing flip-symmetric soft probabilities, and is superseded anyway by the empirical injection floors). MINOR-tier, not MAJOR.

---

## Disposition

| ChatGPT item | Verdict | Reason |
|---|---|---|
| B2 (threshold post-hoc) | FALSIFIED | Full confidence-cut sweep present; null robust across 0.6–0.8; threshold = generator's pre-used operational definition |
| B3 (GZ1 69.91% too weak) | FALSIFIED | Disclosed as conservative floor; propagated via empirical injection floors; dilution toward null is conservative for a null headline |
| B1 (overqualified null / decision tree) | OPINION→addressed | Estimator hierarchy + monopole-mask leakage + 8-anchor systematics battery already give the decision tree (§monopole_mask_null, App D) |
| M1–M4, m1–m5 | OPINION/polish | Same polish-tier as Grok/Gemini MINORs |

**Net: ChatGPT MAJOR does not survive contact with the source. P4 stays ACCEPT-class (MINOR), matching Grok + Gemini.** The post-hoc-threshold concern was genuinely new under the de-biased bar and was audited on its merits — the paper pre-empts it with an explicit robustness sweep. No .tex fix required to close the MAJOR; optional one-line Spearman(p_eq, depth) panel would convert Grok m1 to closed.
