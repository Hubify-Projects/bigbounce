# INT Claude-subscription Review — P5 v0.1.119-2026-07-10 — claude-opus-4-8
paper: P5  version: v0.1.119-2026-07-10  tex: pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex
modality: full-repo Claude Code subscription subagent (claude -p)
UTC: 2026-07-11T06:48:50Z
context-note: confirm wave 1/2 on v0.1.119 (§XII-B de-attenuation site now cites the void measurement); no other changes

======================================================================
RAW RESPONSE (verbatim):
======================================================================

I have everything I need. I verified the flagged v0.1.119 §XII-B change and the numbers it introduces against the committed artifact (`gz1_stratified_confusion.json`), plus the primary headline and the changelog trail.

**Verification results (recomputed/cross-checked against committed artifacts, not just read):**

| Claim in paper | Paper value | Artifact value | Match |
|---|---|---|---|
| §XII-B void arm N | 933 | 933 (line 285) | ✓ |
| void error-asym | −0.023 [−0.060,+0.014] | −0.022906, CI [−0.05947,+0.01366] | ✓ (CI upper rounds −0.059) |
| non-void N | 5,778 | 5,778 (line 320) | ✓ |
| non-void error-asym | −0.005 [−0.020,+0.010] | −0.005058 [−0.01962,+0.00950] | ✓ |
| two-prop diff / z / p | −0.018, −0.89, 0.37 [−0.057,+0.022] | −0.017848, −0.8888, 0.3741 [−0.0572,+0.0215] | ✓ |
| 3-void-def nulls | all-lowz 0.25 / REVOLVER 0.66 / VIDE 0.19 | 0.2453 / 0.6575 / 0.1870 | ✓ |
| de-attenuation | 2a−1=0.3982; 0.9/0.3982≈2.26 | 2(0.6991)−1=0.3982; =2.260 | ✓ |
| primary Δf_CW | +0.0018, z=+0.78, p=0.43, n=57,081/253,276 | 0.001809, 0.781, 0.4349, 57081/253276 | ✓ |

The §XII-B de-attenuation site (`p5_desi_chirality.tex:4452-4467`) now cites the directly-measured void axis; every number resolves to the committed artifact to rounding. Wave 1/2 confirmed — no genuinely-new real finding.

---

**(1) VERDICT: MINOR REVISIONS**

**(2) ISSUES:**

1. **[MINOR]** `p5_desi_chirality.tex:44-73` — Changelog bookkeeping gap. `\paperVersion` is `v0.1.119` but the preamble changelog jumps from a `v0.1.117` block (l.45) to a `v0.1.116` block (l.60) that was retro-annotated `[SUPERSEDED v0.1.119]` (l.70); there is no dedicated `v0.1.118`/`v0.1.119` entry documenting the void-stratum integration that this bump actually performs. Add a `v0.1.119` block stating the §XII-B/abstract/Limitations void-axis citation as the change of record. (Comment-only; not reader-visible in the PDF.)

2. **[MINOR]** `p5_desi_chirality.tex:4452-4473` — §XII-B asserts "direct empirical support ... including the void axis this paper constrains" and reports the void-arm null, but the inline text does not restate that the void arm is under-powered (±3.7 pp), deferring it only via `\S\ref{sec:limitations}`. The abstract (l.789-792) and Limitations (l.4942) both state the underpowering explicitly ("corroborates but cannot by itself exclude a headline-scale environment-dependent label bias"). To hold the paper's own disclosure standard uniformly, add the ±3.7 pp / cannot-exclude qualifier inline at the §XII-B claim so the void-axis "support" is not read as stronger than the ±3.7 pp measurement licenses.

3. **[MINOR]** `p5_desi_chirality.tex:4461,4933` — Rounding direction: the void error-asymmetry CI lower bound is written `-0.060`, but the artifact value is `-0.05947`, which rounds to `-0.059` at the 3-decimal precision used for the adjacent figures (`-0.023`, `+0.014`). Trivial, but a referee recomputing will notice the inconsistent rounding; use `-0.059`.

**(3)** Yes — the central claim (a bounded, family-wise Bonferroni-5 void/non-void chirality null in DESI DR1, with an honestly de-attenuated ≈2.26 pp physical-chirality bound now backed by a directly-measured, parity-symmetric void-axis confusion matrix) is fully supported by the committed artifacts; the remaining items are disclosure-uniformity and bookkeeping polish, not defects in the result.
