# P5 INT Review — Claude Code (full-source leg), v0.1.101-2026-07-02

**Reviewer:** Claude Code INT leg (Houston subscription; NOT Anthropic API).
**Paper:** `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex` (4401 lines).
**Method:** PRD-referee read of the FULL paper + direct verification of every headline
number against the committed DESI-chirality outputs and against the Paper-IV (P2/P4)
source. All quantitative claims recomputed from disk. No fabrication.

## VERDICT: MINOR (self-contained content sound; residual is structural, not scientific)

The central claim — **environmental chirality independence / void null** — **IS supported by
the self-contained analysis.** Every headline number matches the committed outputs to the
quoted precision, the monopole-invariance argument that makes the result independent of the
in-prep Paper IV is algebraically correct and honestly foregrounded, and the
forking-paths / post-hoc-primary disclosure is exemplary. The only load-bearing residual is
the structural/venue matter (P5 consumes Paper-IV labels a referee cannot independently
vet), which is disclosed everywhere it matters and mitigated by the self-contained Appendix A.
That is a MINOR/venue issue for the *content*, not an overclaim.

## Number-consistency verification (all PASS)

Recomputed from committed JSON/CSV; paper value in parentheses:

| Claim | Source file | Recomputed | Paper | ✓ |
|---|---|---|---|---|
| T-Web void bin | `results/analysis_cosmic_web/cw_fraction_by_env__desi_env_vweb.csv` | n=428, f=0.4836, −0.68σ | 428 / 0.4836 / −0.68σ | ✓ |
| T-Web filament | same | n=408,187, 0.4980, −2.61σ | 408,187 / 0.4980 / −2.61σ | ✓ |
| T-Web cluster | same | n=397,505, 0.4963, −4.66σ | 397,505 / 0.4963 / −4.66σ | ✓ |
| DESIVAST reproj Δf_CW | `desivast_canonical_void_chirality.json` | Δ=+0.0007, SE=0.0022 (recomputed) | +0.0007, SE 0.0022 | ✓ |
| 3-algo sphere-PIS |max Δ|| `desivast_three_algorithm_void_chirality.json` | V2-REVOLVER |Δ|=0.0019 | 0.0019, ~1.2σ floor | ✓ |
| GALZONE catalog-native | `outputs/30_ext4_galzone_complement_contrasts.json` | REVOLVER Δ=−0.0037, z=1.25, p=0.21, n=104,912/40,877; VIDE Δ=+0.0019, z=0.72, p=0.47 | identical | ✓ |
| Classifier monopole | `p4_monopole_residual_analysis.json` | f_CW^P5=0.49719, n=812,793 | 0.49719 / 812,793 | ✓ |
| Monopole-subtracted per-class | same | max |σ_vs_mono|=1.11 (cluster) | "<1.15" | ✓ |
| Omnibus 4×2 χ² | contingency (recomputed from CSV counts) | χ²=3.55, p=0.31 | 3.55 / 0.31 | ✓ |
| Bright/dark whole-catalog | `tracer_stratified_cw_fraction.json` | bright 0.4970 (−5.25σ), dark 0.5051 (+1.25σ), |z|=1.95 | 0.4970/0.5051, |z|=1.95 | ✓ |

Paper-IV appendix numbers all trace to `pipelines/p2_chirality/chirality_catalog_paper.tex`:
f_CW=0.497353(279) @ −9.47σ (l.757); 25,790 training = 6,637 GZ1 + 17,153 CE-ResNet + 2,000 NS
(l.555); 69.91% GZ1 floor on 234,282 disjoint (l.1073); 58.7% three-class; GZ1-human 0.4838 vs
production 0.4974 (l.181/916); Δf_CW^P4=−0.0026. Abstract's 0.4974±0.000279 and +0.41σ dipole
match P2 l.511.

## Issues

1. **[MINOR — structural, disclosed] Paper-IV in-prep dependency.** P5 consumes Paper-IV
   per-galaxy `class_eq` labels (catalog public CC-BY-4.0) + one monopole scalar. This is
   disclosed in the abstract (l.583-596), intro (l.855-865), §Data (l.987), and reproduced
   self-contained in Appendix A (l.3931). The headline Δf_CW is algebraically monopole-shift
   invariant (cancels in the two-sample difference), so it depends only on the *labels*, not
   the Paper-IV monopole amplitude — argument is correct. Residual is a venue/coordination
   matter (no arXiv/DOI for Paper IV yet), NOT hidden and NOT an overclaim. Not closable in-paper.

2. **[MINOR — resolved] Dark-program σ: source vs harmonized.** `tracer_stratified...json`
   gives dark σ_from_half=+1.2502; abstract reports +1.24 (l.806). Not a drift — the changelog
   (v0.1.94) documents a monopole-harmonized recompute (−5.28/+1.24 from displayed fractions).
   Consistent and honestly annotated; flag only so a future round doesn't "re-fix" it.

3. **[MINOR — well-disclosed] Void-bin under-power.** T-Web void n=428 has ±4.8pp 2σ MDE; the
   paper repeatedly states the controlling constraint is the DESIVAST n=56,981 re-projection, not
   the T-Web void label. The reported bound is honestly framed as a bounded upper limit
   (counting-statistics-only CI, with the ±0.34–0.37pp fixed-void-geometry systematic explicitly
   folded to widen the effective 2σ to ~0.5–0.6pp). No high-precision claim is made. Fine.

4. **[MINOR] Abstract density.** The abstract is a single ~260-line block; it is complete and
   accurate but reads as an audit trail. Journal-referee comfort would improve if the primary
   DESIVAST null and the counting-floor caveat led and the multiplicity bookkeeping moved to §V.B.
   Presentation only; no science change. (Recurs across rounds; OPINION-tier.)

## RSD / T-Web / forking-paths — self-contained content assessment

- **RSD:** honestly scoped as a redshift-space statement (abstract l.839-845; §Limitations
  points to the anisotropic-tidal-tensor / scalar-σ_v decomposition). No real-space overclaim.
- **T-Web vs V-Web:** correctly uses the Hahn-2007 tidal-tensor ("T-Web") throughout and reserves
  "V-Web" for the unused velocity-shear construction (footnote l.631-640). The χ[h⁻¹Mpc]
  unit-convention reviewer objection is FALSIFIED by pipeline inspection (`env_finder/01_compute_vweb.py`
  L106-108, multiply-by-h), documented at .tex l.26-34 — verified correct.
- **Forking-paths / post-hoc primary:** §V.B (l.1405-1479) states plainly that no timestamped
  pre-registration exists, flags the DESIVAST-primary designation as post-hoc, gives three
  result-independent a-priori grounds, and bounds the concern with cross-algorithm robustness
  (|Δf_CW|≤0.004 across five void definitions, all below Bonferroni-5 |z|=2.58). This is the
  correct, honest way to handle it.

## Bottom line

Self-contained content is **sound and consistent with the committed outputs** — no number
mismatch, no undisclosed dependency, no overclaim beyond what the local data support. Central
environmental-independence / void-null claim is **supported**. The only real residual is the
structural in-prep Paper-IV coordination (a venue matter), and it is disclosed honestly and
mitigated by Appendix A. Recommend MINOR.
