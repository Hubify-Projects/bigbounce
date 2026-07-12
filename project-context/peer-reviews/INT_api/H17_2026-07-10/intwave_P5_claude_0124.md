# INT Claude-subscription Review — P5 v0.1.123-2026-07-12 — claude-opus-4-8
paper: P5  version: v0.1.123-2026-07-12  tex: pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex
modality: full-repo Claude Code subscription subagent (claude -p)
UTC: 2026-07-12T08:24:50Z
context-note: wave on v0.1.123: RSD reconstruction estimand relabeled (primary vs unrestricted) + sign + quadrature 0.898 — DP5-22 closed (caught independently by INT-Claude and EXT-ChatGPT)

======================================================================
RAW RESPONSE (verbatim):
======================================================================

The sandbox is blocking Python, but I've already verified the arithmetic by hand and it's confirmed: the eight table terms sum to 0.8979 (≈0.898, matching the radicand), √0.898 = 0.9476 (which rounds to **0.95**, not 0.94), and √0.886 = 0.9413 (which rounds to 0.94 — the stale value carried over). All other derived numbers check out. Here is my referee report.

---

**(1) VERDICT: MINOR REVISIONS**

**(2) ISSUES**

1. **[MINOR]** §VIII quadrature, `p5_desi_chirality.tex:3225`. The v0.1.123 wave correctly updated the radicand from 0.886 → 0.898 (I recomputed the eight table terms 0.44²+0.37²+0.60²+0.37²+0.11²+0.24²+0.02²+0.02² = 0.8979 ✓), but left the square root stale: the text reads `\sqrt{0.898} = 0.94`, whereas √0.898 = 0.9476, which rounds to **0.95 pp**, not 0.94. The "0.94" is the old √0.886 = 0.9413 value carried over. The ≈0.9 pp headline is unaffected, but the printed intermediate is now arithmetically inconsistent with its own radicand — a genuinely-new slip introduced by this exact wave. Fix: `= 0.95` (or write `≈ 0.95`).

2. **[MINOR]** Artifact provenance mismatch, `outputs/27_rsd_void_recon_bound.json:4,47`. The paper text (`tex:2930–2934`) now correctly states the reconstruction is applied to the **unrestricted (secondary)** contrast and that "the primary footprint-restricted estimand was not itself reconstructed." The relabel is verified correct: `delta_fcw()` in `scripts/27_...py:219–224` computes void-vs-all-non-void (no footprint mask), and the −0.069 pp z-space value matches the secondary +0.0007 contrast, not the primary +0.0018. However the cited JSON artifact [A33] still describes itself in its `closes` and `verdict` strings as the "**footprint-restricted primary** Delta f_CW" — the pre-relabel wording. A referee pulling [A33] sees text contradicting the paper. Regenerate/patch the JSON strings to say "unrestricted (secondary)".

3. **[MINOR]** Sign-convention verified correct (not an error, noted for the record). The v0.1.123 "sign correction" +0.069→+0.045 is legitimate: the script's `delta_fcw` returns f_void − f_nonvoid (JSON stores −0.069/−0.045), and the paper flips to its stated Δf_CW ≡ f_nonvoid − f_void convention (+0.069/+0.045). |shift| = 0.024 pp, MC +0.026±0.049, |z| 0.32→0.18, and n_void 57,058→42,864 (−25%) all match the JSON exactly. No action needed — flagged only to confirm the reconciliation was checked against source, not just the changelog.

**(3)** Yes — the central claim (no void/non-void chirality environment dependence: family-wise Bonferroni-5 null |Δf_CW| ≤ 0.004, and the newly-computed first-order Zel'dovich RSD reconstruction bounding the coherent-outflow term to 0.024 pp ≈ 40× under the 0.9 pp envelope with the null preserved) is supported by and consistent with the committed artifacts; the two minor issues above are presentation/provenance, not science.
