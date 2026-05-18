# P1B_v1B016_R12 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-18_1400pt
**Wall time**: 28.1s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=18112, completion=1944, total=20056

---

## Finding 1 — PAPER-PER-B1 (MAJOR)

Section: Abstract, Secs. 3, 5, 6, Conclusions; citations to Eskilt/Eskilt et al. “joint Planck+ACT” paper.

Issue: The text repeatedly cites a “published joint Planck+ACT value” \(\beta = 0.342^\circ \pm 0.094^\circ\) at \(3.6\sigma\) to “Eskilt2022b” and describes it as a joint Planck+ACT analysis and as the “published Planck/ACT DR6” joint signal, but arXiv:2205.13962 by Eskilt & Komatsu is a WMAP+Planck analysis only (no ACT), albeit with exactly that value and significance. [1] The 0.30°±0.11° Planck value is correctly attributed to Diego-Palazuelos et al. 2022 (arXiv:2201.07682), which is Planck PR4 alone. [0] The text therefore (i) fuses the Eskilt+Komatsu WMAP+Planck result with a “Planck+ACT” label, and (ii) suggests a single “joint Planck+ACT” publication with \(\beta=0.342^\circ\pm 0.094^\circ\) that does not exist.

Fix: Relabel all “joint Planck+ACT” references at \(\beta = 0.342^\circ \pm 0.094^\circ\) as “WMAP+Planck joint analysis” and update the prose accordingly (e.g., “published WMAP+Planck joint value”); reserve “Planck/ACT DR6” phrasing for the separate ACT DR6 analyses and for Diego-Palazuelos et al. / ACT DR6 work, with distinct citations and numbers. [0][1]


## Finding 2 — PAPER-PER-B2 (MAJOR)

Section: Abstract, Sec. 1, Sec. 4, Sec. 6 (birefringence context) — “Planck/ACT DR6 2.4–2.9σ” and ACT DR6 reference.

Issue: The manuscript quotes \(\beta = 0.215^\circ \pm 0.074^\circ\) as an ACT DR6 measurement and describes “published Planck/ACT DR6 \(2.4\)–\(2.9\sigma\)” sky detections, but the cited Diego-Palazuelos 2025 / ACT DR6 paper is not clearly identifiable in current literature: cosmic-birefringence measurements to date with those specific numbers and an ACT DR6 tag do not appear under that author/year combination in arXiv or major journal databases. [0][1] This looks like fused metadata (real Planck PR4 result from Diego-Palazuelos et al. 2022 [0] plus a projected or internal ACT DR6 result) presented as if fully published.

Fix: Either (i) replace the ACT DR6 reference with a real, published ACT birefringence measurement (updating the numeric values, authors, year, and arXiv ID to match exactly), or (ii) if ACT DR6 is still unpublished / in-prep, label it explicitly as such and move any unpublished-number details to a clearly marked “private communication / forecast” context rather than “published Planck/ACT DR6”. [0][1]


## Finding 3 — PAPER-PER-B3 (MAJOR)

Section: Sec. 6, “LiteBIRD forecast” paragraph.

Issue: The paper states that “LiteBIRD is projected to achieve \(\sigma(\beta)\approx 0.03^\circ\)” with a citation “LiteBIRD2023”, but the LiteBIRD cosmic-birefringence forecast papers to date quote constraints on the birefringence angle at the level of a few ×\(10^{-3}\) rad or significantly tighter than 0.03° when expressed as a 1σ error for a monopole rotation, depending on model assumptions. Published LiteBIRD forecasts (e.g., core science goals and polarization performance white papers) do not obviously support the specific \(\sigma(\beta)=0.03^\circ\) number given here, and I cannot match that exact value to a LiteBIRD 2023 paper with that citation key. [0][1]

Fix: Verify the LiteBIRD forecast source directly (title, arXiv ID, journal, and the exact \(\sigma(\beta)\) number); if the correct paper quotes a different uncertainty, update the value and wording to match the published forecast, and correct the bibliography entry so that the arXiv ID, title, and authors correspond to the real LiteBIRD forecasting paper. [0][1]


## Finding 4 — PAPER-PER-B4 (minor)

Section: Sec. 3, “Independent cross-validation” paragraph, reference “ECTorsionDESI2025”.

Issue: The text cites “Liu et al. (ECTorsionDESI2025)” as having constrained an Einstein–Cartan torsion model with DESI DR2 plus standard datasets and quotes AIC improvements \(\Delta\mathrm{AIC}=-5.7\) to \(-6.6\), but an arXiv or journal article matching that combination of author (“Liu”), model (EC torsion), and DESI DR2 analysis cannot be located under a plausible 2024–2025 astro-ph.CO entry. Existing EC/torsion cosmology papers using Planck+BAO+SN typically do not use those exact labels or dataset stacks; this looks like either an in-prep internal note or fused metadata from several torsion-related works. [0][1]

Fix: If this is an unpublished or in-preparation work, clearly label it as such and remove quantitative AIC claims that cannot be checked in a citable paper; otherwise, replace with a verified, published EC/torsion cosmology paper (correct authors, year, and arXiv ID) and ensure that any quoted AIC/Bayesian evidence numbers are actually present in that work. [0][1]


## Finding 5 — PAPER-PER-B5 (minor)

Section: Sec. 6, opening paragraph — Fujita et al. citation.

Issue: The text attributes the spectator-ALP birefringence model class to “Fujita et al. 2021” (key “Fujita2021”) as prior work on this scenario. There are indeed Fujita et al. papers on axion-like fields and cosmic birefringence around 2020–2021, but the current literature includes several closely related but distinct works (different titles and arXiv IDs), and without explicit arXiv numbers in the LaTeX, there is a plausible risk of referencing the wrong Fujita paper (e.g., misaligning a dark energy—ALP paper with a CMB birefringence—ALP paper). [0][1]

Fix: Ensure that “Fujita2021” in the .bib file maps to the specific Fujita et al. paper that actually analyzes an ALP-induced CMB birefringence with a coupling \(C_{a\gamma}\) and parameter ranges comparable to those used here; update the in-text wording if the cited paper’s scope is different (e.g., early dark energy ALPs rather than late-time birefringence) so that the claim “previously studied by Fujita et al.” matches the paper’s actual content. [0][1]


## Finding 6 — PAPER-PER-B6 (nit)

Section: Abstract, Sec. 1, Sec. 4 — phrase “published Planck/ACT DR6 2.4–2.9σ” with dual numeric range.

Issue: The paper describes the “primary sky detection significance” as “published Planck/ACT DR6 2.4–2.9σ” while citing the Planck-only Diego-Palazuelos et al. measurement of \(\beta = 0.30^\circ\pm0.11^\circ\) (which is exactly 2.7σ) and the Eskilt+Komatsu WMAP+Planck joint result of 3.6σ. [0][1] The 2.4–2.9σ range is not directly traceable to a single specific published analysis and appears to be a hand-wavy summary; as written, it blurs distinct datasets (Planck PR4 vs any ACT analysis vs WMAP+Planck) and precise significances.

Fix: Replace “2.4–2.9σ” with explicit, paper-by-paper values and datasets, e.g., “Planck PR4: 2.7σ; WMAP+Planck: 3.6σ”, and make sure the associated citations point to the correct arXiv IDs and titles; avoid blended ranges that are not explicitly given in any one published source. [0][1]
