# EXT22 P1B gemini — chat: https://gemini.google.com/u/0/app/d8b938d5a1fda614

Recommendation: MINOR REVISIONS

Overview of the Manuscript
This manuscript serves as a technical verification companion to the Einstein-Cartan-Holst (ECH) spin-torsion cosmology program outlined in "Paper I(a)". It presents three distinct numerical validation layers: a stock-CAMB ΛCDM+ΔNeff MCMC proxy run, a NaMaster pseudo-Cl polarization pipeline validation on synthetic skies, and a spectator axion-like particle (ALP) cosmic birefringence consistency check.
The paper is exceptionally well-scoped, explicitly framing its analyses as null-consistency and compatibility checks rather than outright claims of model preference or new sky detections. Given the methodological rigor and the outstanding commitment to open science, the paper is well-suited for publication after addressing a few pervasive rendering and typographic anomalies.

Strengths

Exemplary Commitment to Open Science and Reproducibility: The author provides an incredibly thorough reproducibility manifest. Providing public GitHub repositories, precise configuration YAML filenames, deterministic random seeds, and active Hugging Face repository URLs for the raw frozen MCMC chains sets a benchmark for cosmological data publications.

Methodological Candor and Scientific Honesty: Rather than hiding the fine-tuning or data limitations under the rug, the author is refreshingly transparent. For example, the text openly acknowledges that the spectator ALP model requires a ∼25× fine-tuning of the misalignment initial condition to remain safely sub-dominant (Ωa < 0.01), and explicitly notes that the stock-CAMB run is a phenomenological proxy rather than a bespoke spin-torsion theory module.

Rigorous Pipeline Calibration: The NaMaster pseudo-Cl validation effectively isolates algebraic deconvolution and mask-coupling biases on foreground-free synthetic skies. The multi-configuration robustness battery successfully pins down the source of the ∼12% multiplicative under-recovery to the unweighted estimator's treatment of noise-dominated high-l bins and the injected B-mode template shape.

Blockers
None. There are no severe scientific gaps or missing control frameworks that undermine the core utility of this technical verification companion.

Major Comments

1. Supernova Catalog Overlap Systematic
The author notes that the iter2 w0wa chain combines the DES-SN5YR and Pantheon+ datasets via a simple product likelihood without an explicit joint covariance matrix to account for the ∼20% shared supernova events. While the text accurately characterizes this as a known limitation and an uncorrected systematic that introduces an artificial inward pull, it would strengthen the paper to comment briefly on how much the upcoming joint-covariance treatments (e.g., standard cross-collaboration frameworks) are anticipated to shift the marginal tail distances (+4.3σ in w0 and −3.6σ in wa). This is a diagnostic cross-check, but a sentence clarifying if this systematic could plausibly eliminate the phantom-crossing signature entirely would benefit the community.

Minor Comments and Typographic Fixes

1. Systematic Sign Glitch (σ→0)
There appears to be a pervasive character encoding or rendering glitch where the Greek letter σ (sigma) has been converted into the digit 0 across the entire document text and several table headers. Examples include:
Page 1: "~3.60 tension" should be "~3.6σ tension".
Page 1: "2.7-2.90" should be "2.7–2.9σ".
Page 1: "3.60 headline" should be "3.6σ headline".
Page 4: "tail-distances +4.30 in wo, -3.60 in wa" should be "+4.3σ in w0, −3.6σ in wa".
Page 5, Table I note: "2.60 two-Gaussian tension" and "2.00 from the DES-Y3 prior" should be "2.6σ" and "2.0σ" respectively.
Page 6, Table II: The heading column "vs ACDM" renders errors like "(marg.-tail, +4.30)" and "-3.60 from 0".
Please run a global find-and-replace sweep on the final PDF compilation to restore the proper σ notation.

2. Physical Impossibility in Scalar Spectral Index (ns) Values
In Table I and Table II, some values recorded for the primordial scalar spectral index (ns) are unphysical and appear to suffer from a typographic or column-shifting layout bug:
In Table I, the row labeled "71" (likely a mangled rendering of ns) lists a value of 3.965±0.006 for the Full-tension column, while correctly listing 0.967±0.006 for the Planck+BAO+SN column.
In Table II, the ns row lists a value of 3.9655±0.0036.
Cosmologically, ns must be close to 0.965. It looks like a leading 0 was mistakenly replaced by a 3 (perhaps bleeding over from an adjacent parameter or an aggregation script artifact). Please correct these table entries to reflect the true chain outputs.

3. Chronological Consistency
On Page 1, the text states a manuscript date of June 20, 2026, while the NaMaster production run is noted as being performed in April 2026, and the iter2 chain is dated May 18, 2026. This timeline is completely logical and consistent for a submission tracking chain history. No action needed, just noting that the data asset tracking matches perfectly.
