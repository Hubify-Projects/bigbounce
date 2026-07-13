# INT Claude-subscription Review — P5 v0.1.126-2026-07-12 — claude-opus-4-8
paper: P5  version: v0.1.126-2026-07-12  tex: pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex
modality: full-repo Claude Code subscription subagent (claude -p)
UTC: 2026-07-13T12:43:34Z
context-note: M28

======================================================================
RAW RESPONSE (verbatim):
======================================================================

I have verified the load-bearing numbers against the committed artifacts (RSD reconstruction, GZ1 void-stratum confusion, primary Δf_CW arithmetic, systematic-budget quadrature) and they all match. I found one genuinely-new reader-visible bookkeeping defect. Here is my review.

---

**(1) VERDICT: MINOR REVISIONS**

**(2) ISSUES:**

1. **[MINOR] Artifact-ID range statement contradicts the artifact table it introduces.** In four places the manuscript asserts the artifact index runs `[A1]--[A32]`: the acknowledgments (`p5_desi_chirality.tex:4541`, "the [A1]--[A32] artifact links"), and the Appendix C note (`:5043` "the bracketed artifact IDs [A1]--[A32] in this appendix" and `:5047` "Artifact IDs [A1]--[A32] used throughout"). But the artifact-map table in that same appendix now runs through `[A34]` — rows `[A33]` (`outputs/27_rsd_void_recon_bound.json`, `:5098`) and `[A34]` (`scripts/27_rsd_void_recon_bound.py`, `:5099`), both cited in the body at `:2590–2591` and `:4406`. The table caption (`:5056`) compounds it: "Paths A2--A30 are within `pipelines/p5_desi_chirality/`; ... A1, A31, and A32 point to the companion catalog pipeline" omits A33/A34 entirely (both are in-`p5`). This is a genuinely-new defect introduced when the RSD artifacts were appended in v0.1.122 without updating the range descriptors; fix the four "[A1]--[A32]" strings to "[A1]--[A34]" and extend the caption's path-location enumeration to A34.

2. **[MINOR] Central input (Paper IV catalog) is an unpublished companion with an unresolved arXiv placeholder.** The abstract (`:793`) and macro (`:24`) still carry `arXiv:XXXX.XXXXX`, and the per-galaxy `class_eq` labels that the headline contrast consumes come from a paper "posted concurrently under coordinated submission." The manuscript handles this correctly and honestly — §Limitations (`:4261–4319`) makes acceptance "strictly conditional" on Paper IV's publication/co-review, and demonstrates the headline is monopole-invariant and model-independently corroborated (GZ1 human-vote null z=−0.54σ; void-stratum confusion null z=−0.89, p=0.37, which I verified against `gz1_stratified_confusion.json`). No new action beyond flagging for editorial attention: this is the one genuinely load-bearing external dependency and it is already dispositioned; I note it only because a referee cannot fully vet the label provenance until the placeholder resolves.

3. **[MINOR] "2σ systematic envelope" mixes a 2σ statistical half-width with peak systematic excursions in quadrature.** The `≈0.9pp` envelope (abstract `:810`; `tab:systematic_budget`, `:2870–2874`) combines a 2σ counting CI (0.44pp) with per-channel *peak* systematic magnitudes (geometry 0.60, membership 0.37, …) via √0.898 = 0.94pp. The arithmetic is correct and the construction is conservative (peaks, not 1σ), and it is disclosed as an "honest quadrature envelope," but labeling the counting term "2σ" while the systematic terms are peak-excursions is a slight category mix that one sentence in the caption should make explicit. Not blocking.

*Verified clean (no issue):* primary Δf_CW = +0.0018, SE 0.0023, z=0.78, CI [−0.0027,+0.0064] all reproduce from the integer counts (28,339/57,081 vs 126,202/253,276); σ_from_half −1.69/−1.73 self-consistent; RSD shift 0.024pp (MC +0.026±0.049), |z| 0.32→0.18, n_void 57,058 all match `outputs/27_rsd_void_recon_bound.json`; de-attenuation 0.9/0.3982=2.26pp correct; eight-term multline names eight terms (the v0.1.126 seven→eight fix holds).

**(3)** Yes — the central claim (no detectable void/non-void environmental chirality dependence, Δf_CW = +0.0018, p=0.43, with a family-wise Bonferroni-5 null across all five DESIVAST definitions) is supported by the data and every checked number reproduces from the committed artifacts; the remaining items are presentation bookkeeping and the disclosed, correctly-handled Paper IV citation-timing dependency.
